"""Tests for ParamsAgent propose-and-apply loop."""

import pytest
from fastapi.testclient import TestClient

from app.agent.llm_provider import MockLLMProvider
from app.agent.params_agent import ParamsAgent
from app.api.app_factory import create_app


def _event_items(response) -> list[dict]:
    return response.json()["data"]["items"]


def _make_app_with_mock(responses: list[dict], max_attempts: int = 3):
    """Create app and override params_agent with a custom MockLLMProvider."""
    app = create_app()
    from app.world.validation import ParamRegistry

    registry = ParamRegistry.default()
    llm = MockLLMProvider(responses=responses)
    app.state.params_agent = ParamsAgent(
        llm=llm,
        param_validator=app.state.param_validator,
        param_dry_run_validator=app.state.param_dry_run_validator,
        world_state=app.state.world_state,
        event_log=app.state.event_log,
        runtime_engine=app.state.runtime_engine,
        registry=registry,
        max_attempts=max_attempts,
    )
    return app


def test_agent_applies_patch_when_valid() -> None:
    app = _make_app_with_mock(
        responses=[
            {"patches": [{"op": "set", "path": "counter.increment", "value": {"value": 2, "type": "number"}}]}
        ]
    )
    client = TestClient(app)

    response = client.post("/world/agent/params/propose-and-apply", json={"goal": "increase counter speed"})
    assert response.status_code == 200

    data = response.json()["data"]
    assert data["applied"] is True
    assert data["attempts"] == 1
    assert len(data["patches"]) == 1

    # Step twice and verify counter increments by 2
    client.post("/runtime/step")
    client.post("/runtime/step")

    events_response = client.get("/world/events?limit=200")
    assert events_response.status_code == 200

    counter_events = [e for e in _event_items(events_response) if e["type"] == "module.counter"]
    counter_events.sort(key=lambda e: e["tick_id"])

    assert [e["payload"]["increment"] for e in counter_events] == [2, 2]
    assert [e["payload"]["counter"] for e in counter_events] == [2, 4]


def test_agent_retries_on_failure_and_then_succeeds() -> None:
    app = _make_app_with_mock(
        responses=[
            # First attempt: value too large → triggers numeric_divergence in dry-run (20 steps * 5001 = 100020 > 100000)
            {"patches": [{"op": "set", "path": "counter.increment", "value": 5001}]},
            # Second attempt: valid value
            {"patches": [{"op": "set", "path": "counter.increment", "value": {"value": 2, "type": "number"}}]},
        ],
        max_attempts=3,
    )
    client = TestClient(app)

    response = client.post("/world/agent/params/propose-and-apply", json={"goal": "test retry"})
    assert response.status_code == 200

    data = response.json()["data"]
    assert data["applied"] is True
    assert data["attempts"] == 2


def test_agent_rejects_after_max_attempts() -> None:
    app = _make_app_with_mock(
        responses=[
            # Every attempt returns an unknown path → static validation fails
            {"patches": [{"op": "set", "path": "nonexistent.param", "value": 42}]},
            {"patches": [{"op": "set", "path": "nonexistent.param", "value": 42}]},
        ],
        max_attempts=2,
    )
    client = TestClient(app)

    # Save params before
    params_before = client.get("/world/params").json()["data"]

    response = client.post("/world/agent/params/propose-and-apply", json={"goal": "fail test"})
    assert response.status_code == 422

    body = response.json()
    assert body["code"] == 30

    # Verify error data is present
    assert body["data"] is not None
    assert "errors" in body["data"]
    assert body["data"]["attempts"] == 2

    # Verify world_state was NOT modified
    params_after = client.get("/world/params").json()["data"]
    assert params_after == params_before

    # Verify proposal_rejected event was emitted
    events_response = client.get("/world/events?limit=200")
    rejected_events = [e for e in _event_items(events_response) if e["type"] == "params.proposal_rejected"]
    assert len(rejected_events) == 1
    assert rejected_events[0]["payload"]["attempts"] == 2


def test_agent_handles_invalid_llm_json() -> None:
    app = _make_app_with_mock(
        responses=[
            # First: missing 'patches' key
            {"wrong_key": "bad"},
            # Second: valid
            {"patches": [{"op": "set", "path": "counter.increment", "value": 3}]},
        ],
        max_attempts=3,
    )
    client = TestClient(app)

    response = client.post("/world/agent/params/propose-and-apply")
    assert response.status_code == 200

    data = response.json()["data"]
    assert data["applied"] is True
    assert data["attempts"] == 2
