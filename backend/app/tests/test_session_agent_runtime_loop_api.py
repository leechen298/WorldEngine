from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


PRIVATE_PUBLIC_MARKERS = (
    "api_key",
    "authorization",
    "hidden context",
    "private memory",
    "provider_trace",
    "raw_prompt",
    "raw provider response",
    "sk-live-secret",
)


def _client() -> TestClient:
    return TestClient(create_app())


def _create_session(client: TestClient, world_id: str = "world-agent") -> str:
    response = client.post("/sessions", json={"world_id": world_id})
    assert response.status_code == 200
    return response.json()["data"]["session_id"]


def _serialized(value: object) -> str:
    return str(value).lower()


def test_session_agent_list_and_read_return_public_default_state() -> None:
    client = _client()
    session_id = _create_session(client)

    listed = client.get(f"/sessions/{session_id}/agents")

    assert listed.status_code == 200
    payload = listed.json()
    serialized = _serialized(payload)
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["world_id"] == "world-agent"
    assert data["total"] == 1
    agent = data["items"][0]
    assert agent["agent_id"] == "agent.observer"
    assert agent["state"] == "observing"
    assert agent["public_status"] == "ready"
    assert agent["runtime_ref"]["tick_id"] == 0
    assert agent["redaction_status"] == "passed"
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    read = client.get(f"/sessions/{session_id}/agents/agent.observer")

    assert read.status_code == 200
    assert read.json()["data"]["agent_id"] == "agent.observer"


def test_session_agent_step_records_worldengine_owned_public_evidence() -> None:
    client = _client()
    session_id = _create_session(client)
    client.post("/runtime/step")

    response = client.post(
        f"/sessions/{session_id}/agents/agent.observer/step",
        json={"event_limit": 5},
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["agent_id"] == "agent.observer"
    assert data["previous_state"]["state"] == "observing"
    assert data["updated_state"]["state"] in {"no_intent", "waiting", "acting"}
    assert data["updated_state"]["runtime_ref"]["tick_id"] == 1
    assert data["public_intent"] in {
        "acknowledge_public_event",
        "maintain_observation",
    }
    assert data["client_scripted_action"] is False
    assert data["redaction_status"] == "passed"
    assert data["event_evidence"]["event_delta_count"] >= 2
    assert data["event_evidence"]["event_ids"]
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    events = client.get("/world/events?limit=200").json()["data"]["items"]
    agent_events = [event for event in events if event["source"] == "session.agent"]
    assert {event["type"] for event in agent_events} >= {
        "world.agent.observed",
        "world.agent.intent.recorded",
    }
    for event in agent_events:
        assert event["payload"]["session_id"] == session_id
        assert event["payload"]["agent_id"] == "agent.observer"
        assert event["payload"]["client_scripted_action"] is False
        assert not any(marker in _serialized(event["payload"]) for marker in PRIVATE_PUBLIC_MARKERS)


def test_session_agent_step_rejects_client_scripted_action_payload() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.post(
        f"/sessions/{session_id}/agents/agent.observer/step",
        json={
            "event_limit": 5,
            "intent": {
                "type": "params.patch",
                "patches": [
                    {
                        "op": "set",
                        "path": "counter.increment",
                        "value": {"value": 99, "type": "number"},
                    }
                ],
            },
        },
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["code"] == 30
    assert "params.patch" not in serialized
    assert "counter.increment" not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_session_agent_runtime_loop_manifest_surface_is_discoverable() -> None:
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    surfaces = response.json()["public_surfaces"]
    assert {
        "path": "/sessions/{session_id}/agents",
        "method": "GET",
        "operation_id": "list_session_agents",
        "status": "available",
        "maturity": "implemented",
        "validation_status": "pass",
        "required_for_mvp": False,
        "notes": ["session-scoped public Agent state list surface"],
    } in surfaces
    assert {
        "path": "/sessions/{session_id}/agents/{agent_id}/step",
        "method": "POST",
        "operation_id": "run_session_agent_step",
        "status": "available",
        "maturity": "implemented",
        "validation_status": "pass",
        "required_for_mvp": False,
        "notes": ["session-scoped WorldEngine-owned public Agent runtime step"],
    } in surfaces
