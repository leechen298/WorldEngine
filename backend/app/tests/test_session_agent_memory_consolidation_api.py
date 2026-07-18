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


def _create_session(client: TestClient, world_id: str = "world-memory") -> str:
    response = client.post("/sessions", json={"world_id": world_id})
    assert response.status_code == 200
    return response.json()["data"]["session_id"]


def _serialized(value: object) -> str:
    return str(value).lower()


def test_session_agent_memory_read_starts_empty_and_public() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.get(f"/sessions/{session_id}/agents/agent.observer/memory")

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["world_id"] == "world-memory"
    assert data["agent_id"] == "agent.observer"
    assert data["working_memory"] == []
    assert data["episodic_memory"] == []
    assert data["consolidation_status"] == "not_consolidated"
    assert data["redaction_status"] == "passed"
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)


def test_rest_consolidation_records_public_working_and_episodic_memory() -> None:
    client = _client()
    session_id = _create_session(client)
    client.post("/runtime/step")
    step = client.post(
        f"/sessions/{session_id}/agents/agent.observer/step",
        json={"mode_hint": "rest"},
    )
    assert step.status_code == 200

    response = client.post(
        f"/sessions/{session_id}/agents/agent.observer/memory/consolidate",
        json={"mode": "rest", "event_limit": 10},
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["agent_id"] == "agent.observer"
    assert data["consolidation_status"] == "consolidated"
    assert data["working_memory"]["source"] == "session_agent_public_summary"
    assert data["episodic_memory"]["source"] == "session_agent_rest_consolidation"
    assert data["personality_mutation_applied"] is False
    assert data["skill_mutation_applied"] is False
    assert data["private_memory_payload_included"] is False
    assert data["event_evidence"]["event_delta_count"] == 2
    assert data["redaction_status"] == "passed"
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    memory = client.get(f"/sessions/{session_id}/agents/agent.observer/memory").json()["data"]
    assert len(memory["working_memory"]) == 1
    assert len(memory["episodic_memory"]) == 1
    assert memory["consolidation_status"] == "consolidated"
    assert memory["episodic_memory"][0]["event_refs"]

    events = client.get("/world/events?limit=200").json()["data"]["items"]
    memory_events = [
        event for event in events if event["type"] == "world.agent.memory.recorded"
    ]
    consolidation_events = [
        event for event in events if event["type"] == "world.agent.consolidation.recorded"
    ]
    assert len(memory_events) == 1
    assert len(consolidation_events) == 1
    assert memory_events[0]["payload"]["private_memory_payload_included"] is False
    assert consolidation_events[0]["payload"]["personality_mutation_applied"] is False
    assert consolidation_events[0]["payload"]["skill_mutation_applied"] is False


def test_non_rest_ticks_do_not_create_episodic_or_consolidation_records() -> None:
    client = _client()
    session_id = _create_session(client)

    client.post("/runtime/step")
    client.post("/runtime/step")
    step = client.post(
        f"/sessions/{session_id}/agents/agent.observer/step",
        json={"event_limit": 5},
    )
    assert step.status_code == 200

    memory = client.get(f"/sessions/{session_id}/agents/agent.observer/memory")

    assert memory.status_code == 200
    data = memory.json()["data"]
    assert data["working_memory"] == []
    assert data["episodic_memory"] == []
    assert data["consolidation_status"] == "not_consolidated"

    events = client.get("/world/events?limit=200").json()["data"]["items"]
    assert not [
        event for event in events if event["type"] == "world.agent.consolidation.recorded"
    ]


def test_memory_consolidation_rejects_private_payload_without_echo() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.post(
        f"/sessions/{session_id}/agents/agent.observer/memory/consolidate",
        json={
            "mode": "rest",
            "private_memory": "raw_prompt provider_trace sk-live-secret",
        },
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["code"] == 30
    assert "private_memory" not in serialized
    assert "raw_prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "sk-live-secret" not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_session_agent_memory_manifest_surface_is_discoverable() -> None:
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    surfaces = response.json()["public_surfaces"]
    assert {
        "path": "/sessions/{session_id}/agents/{agent_id}/memory",
        "method": "GET",
        "operation_id": "get_session_agent_memory",
        "status": "available",
        "maturity": "implemented",
        "validation_status": "pass",
        "required_for_mvp": False,
        "notes": ["session-scoped public Agent memory summary surface"],
    } in surfaces
    assert {
        "path": "/sessions/{session_id}/agents/{agent_id}/memory/consolidate",
        "method": "POST",
        "operation_id": "consolidate_session_agent_memory",
        "status": "available",
        "maturity": "implemented",
        "validation_status": "pass",
        "required_for_mvp": False,
        "notes": ["session-scoped public Agent rest consolidation surface"],
    } in surfaces
