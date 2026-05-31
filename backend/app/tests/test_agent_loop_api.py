from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app
from app.schemas.agent_memory import EpisodicMemoryRecord, WorkingMemoryRecord
from app.schemas.event import Event


def _event_items(response) -> list[dict]:
    return response.json()["data"]["items"]


def _working_memory(memory_id: str) -> WorkingMemoryRecord:
    return WorkingMemoryRecord(
        memory_id=memory_id,
        agent_id="agent.default",
        world_id="world.default",
        content="remember the stable preference",
        source="test",
        priority=5,
        created_at="2026-05-30T00:00:00+00:00",
        updated_at="2026-05-30T00:01:00+00:00",
    )


def _episodic_memory(memory_id: str) -> EpisodicMemoryRecord:
    return EpisodicMemoryRecord(
        memory_id=memory_id,
        agent_id="agent.default",
        world_id="world.default",
        summary="agent observed a prior event",
        tick=2,
        world_time_seconds=1200,
        source="test",
        created_at="2026-05-30T00:02:00+00:00",
    )


def test_loop_step_endpoint_returns_noop_response_by_default() -> None:
    app = create_app()
    app.state.event_log.append(
        Event(
            id="event-1",
            tick_id=1,
            world_time_seconds=600,
            type="test.event",
            source="test",
            payload={"value": 1},
            created_at="2026-05-30T00:01:00+00:00",
        )
    )
    client = TestClient(app)

    response = client.post("/world/agent/loop/step", json={"event_limit": 1})

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == 0
    data = body["data"]
    assert data["intent"]["type"] == "noop"
    assert data["result"]["status"] == "noop"
    assert data["result"]["applied"] is False
    assert [event["id"] for event in data["perception"]["recent_events"]] == ["event-1"]


def test_loop_step_endpoint_includes_read_only_memory_context() -> None:
    app = create_app()
    app.state.agent_memory_store.add_working_memory(_working_memory("working-1"))
    app.state.agent_memory_store.add_episodic_memory(_episodic_memory("episodic-1"))
    client = TestClient(app)

    response = client.post("/world/agent/loop/step", json={"event_limit": 1})

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["result"]["status"] == "noop"
    assert data["result"]["applied"] is False

    memory_context = data["perception"]["memory_context"]
    assert [item["memory_id"] for item in memory_context["working_memory"]] == [
        "working-1"
    ]
    assert [item["memory_id"] for item in memory_context["episodic_memory"]] == [
        "episodic-1"
    ]


def test_loop_step_endpoint_applies_params_patch_with_agent_loop_source() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.post(
        "/world/agent/loop/step",
        json={
            "intent": {
                "type": "params.patch",
                "reason": "increase counter",
                "patches": [
                    {
                        "op": "set",
                        "path": "counter.increment",
                        "value": {"value": 4, "type": "number"},
                    }
                ],
            }
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["result"]["status"] == "accepted"
    assert data["result"]["applied"] is True
    assert data["result"]["params"]["counter"]["increment"] == {
        "value": 4,
        "type": "number",
    }

    events_response = client.get("/world/events?limit=20")
    events = _event_items(events_response)
    applied_events = [event for event in events if event["type"] == "params.applied"]
    assert len(applied_events) == 1
    assert applied_events[0]["id"] == data["result"]["event_id"]
    assert applied_events[0]["source"] == "agent.loop"


def test_loop_step_endpoint_rejects_unknown_loop_request_fields() -> None:
    app = create_app()
    client = TestClient(app)

    before_params = client.get("/world/params").json()["data"]
    response = client.post(
        "/world/agent/loop/step",
        json={
            "event_limit": 1,
            "unexpected": "drop-me",
            "intent": {
                "type": "params.patch",
                "patches": [
                    {
                        "op": "set",
                        "path": "counter.increment",
                        "value": 5,
                    }
                ],
            },
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "extra_forbidden"
    assert client.get("/world/params").json()["data"] == before_params


def test_loop_step_endpoint_rejects_unknown_action_intent_fields() -> None:
    app = create_app()
    client = TestClient(app)

    before_params = client.get("/world/params").json()["data"]
    response = client.post(
        "/world/agent/loop/step",
        json={
            "intent": {
                "type": "params.patch",
                "requires_confirmation": True,
                "patches": [
                    {
                        "op": "set",
                        "path": "counter.increment",
                        "value": 5,
                    }
                ],
            },
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "extra_forbidden"
    assert client.get("/world/params").json()["data"] == before_params


def test_loop_step_endpoint_rejects_unknown_patch_item_fields() -> None:
    app = create_app()
    client = TestClient(app)

    before_params = client.get("/world/params").json()["data"]
    response = client.post(
        "/world/agent/loop/step",
        json={
            "intent": {
                "type": "params.patch",
                "patches": [
                    {
                        "op": "set",
                        "path": "counter.increment",
                        "value": 5,
                        "unexpected_patch_field": True,
                    }
                ],
            },
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "extra_forbidden"
    assert client.get("/world/params").json()["data"] == before_params

    events_response = client.get("/world/events?limit=20")
    events = _event_items(events_response)
    assert [event for event in events if event["type"] == "params.applied"] == []


def test_loop_step_endpoint_returns_rejected_action_as_200_result() -> None:
    app = create_app()
    client = TestClient(app)

    before_params = client.get("/world/params").json()["data"]
    response = client.post(
        "/world/agent/loop/step",
        json={"intent": {"type": "world.spawn", "metadata": {"source": "test"}}},
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["result"]["status"] == "rejected"
    assert data["result"]["applied"] is False
    assert data["result"]["errors"][0]["reason"] == "unsupported_action"
    assert client.get("/world/params").json()["data"] == before_params


def test_loop_step_endpoint_rejects_noop_patches_without_event() -> None:
    app = create_app()
    client = TestClient(app)

    before_params = client.get("/world/params").json()["data"]
    response = client.post(
        "/world/agent/loop/step",
        json={
            "intent": {
                "type": "noop",
                "patches": [
                    {
                        "op": "set",
                        "path": "counter.increment",
                        "value": 5,
                    }
                ],
            }
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["result"]["status"] == "rejected"
    assert data["result"]["applied"] is False
    assert data["result"]["errors"][0]["reason"] == "unexpected_payload"
    assert client.get("/world/params").json()["data"] == before_params

    events_response = client.get("/world/events?limit=20")
    events = _event_items(events_response)
    assert [event for event in events if event["type"] == "params.applied"] == []


def test_loop_step_endpoint_returns_invalid_params_patch_as_200_result() -> None:
    app = create_app()
    client = TestClient(app)

    before_params = client.get("/world/params").json()["data"]
    response = client.post(
        "/world/agent/loop/step",
        json={
            "intent": {
                "type": "params.patch",
                "patches": [
                    {
                        "op": "set",
                        "path": "runtime.secret",
                        "value": 3,
                    }
                ],
            }
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["result"]["status"] == "rejected"
    assert data["result"]["applied"] is False
    assert data["result"]["errors"][0]["reason"] == "reserved_prefix"
    assert client.get("/world/params").json()["data"] == before_params

    events_response = client.get("/world/events?limit=20")
    events = _event_items(events_response)
    assert [event for event in events if event["type"] == "params.applied"] == []


def test_loop_step_endpoint_keeps_request_schema_errors_as_422() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.post(
        "/world/agent/loop/step",
        json={"event_limit": 0},
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"]


def test_existing_params_agent_route_still_applies_patch() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.post("/world/agent/params/propose-and-apply")

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["applied"] is True
    assert data["patches"]
