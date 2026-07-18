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


def _serialized(value: object) -> str:
    return str(value).lower()


def _create_session(client: TestClient, world_id: str = "world-session") -> str:
    response = client.post("/sessions", json={"world_id": world_id})
    assert response.status_code == 200
    return response.json()["data"]["session_id"]


def test_session_direction_queues_lightning_risk_as_external_pressure_only() -> None:
    client = _client()
    session_id = _create_session(client, "world-lightning")

    response = client.post(
        f"/sessions/{session_id}/directions",
        json={
            "instruction_text": "The observer may face lightning-strike risk as external pressure.",
            "apply_after_tick": 1,
            "expires_after_tick": 4,
            "public_context": {"visible_weather": "storm clouds"},
        },
    )

    assert response.status_code == 200
    payload = response.json()
    data = payload["data"]
    serialized = _serialized(payload)
    assert payload["code"] == 0
    assert data["world_id"] == "world-lightning"
    assert data["status"] == "queued"
    assert data["classification"]["allowed"] is True
    assert data["classification"]["category"] == "external_pressure"
    assert data["queue_item"]["world_id"] == "world-lightning"
    assert data["queue_item"]["status"] == "queued"
    assert data["queue_item"]["public_context_keys"] == ["visible_weather"]
    assert data["direct_state_mutation_applied"] is False
    assert "lightning-strike risk" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    summary = client.get(f"/sessions/{session_id}/directions").json()["data"]
    assert summary["session_id"] == session_id
    assert summary["world_id"] == "world-lightning"
    assert summary["queue_status"] == "available"
    assert summary["rejected_count"] == 0
    assert [item["direction_id"] for item in summary["queued_items"]] == [
        data["queue_item"]["direction_id"]
    ]

    events = client.get("/world/events?limit=200").json()["data"]["items"]
    queued_events = [
        event for event in events if event["type"] == "world.session_direction.queued"
    ]
    assert len(queued_events) == 1
    event_payload = queued_events[0]["payload"]
    assert event_payload["session_id"] == session_id
    assert event_payload["world_id"] == "world-lightning"
    assert event_payload["status"] == "queued"
    assert event_payload["direction_id"] == data["queue_item"]["direction_id"]
    assert event_payload["classification"]["category"] == "external_pressure"
    assert event_payload["instruction_text_length"] == len(
        "The observer may face lightning-strike risk as external pressure."
    )
    assert event_payload["public_context_keys"] == ["visible_weather"]
    assert event_payload["direct_state_mutation_applied"] is False
    assert "lightning-strike risk" not in _serialized(event_payload)


def test_session_direction_rejects_direct_final_fact_without_queueing() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.post(
        f"/sessions/{session_id}/directions",
        json={"instruction_text": "Kill this Agent now and force the outcome"},
    )

    assert response.status_code == 200
    payload = response.json()
    data = payload["data"]
    serialized = _serialized(payload)
    assert data["status"] == "rejected"
    assert data["classification"]["allowed"] is False
    assert data["classification"]["category"] == "direct_final_fact"
    assert data["rejection_reason"] == "direct_final_fact"
    assert data["queue_item"] is None
    assert data["direct_state_mutation_applied"] is False
    assert "kill this agent" not in serialized

    summary = client.get(f"/sessions/{session_id}/directions").json()["data"]
    assert summary["queue_status"] == "empty"
    assert summary["queued_items"] == []
    assert summary["rejected_count"] == 1

    events = client.get("/world/events?limit=200").json()["data"]["items"]
    assert not [
        event for event in events if event["type"] == "world.session_direction.queued"
    ]
    rejected_events = [
        event for event in events if event["type"] == "world.session_direction.rejected"
    ]
    assert len(rejected_events) == 1
    event_payload = rejected_events[0]["payload"]
    assert event_payload["session_id"] == session_id
    assert event_payload["status"] == "rejected"
    assert event_payload["classification"]["category"] == "direct_final_fact"
    assert event_payload["direct_state_mutation_applied"] is False
    assert "kill this agent" not in _serialized(event_payload)


def test_session_direction_rejects_private_marker_without_public_echo() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.post(
        f"/sessions/{session_id}/directions",
        json={
            "instruction_text": "Increase storm risk",
            "branch_id": "raw_provider_response",
            "public_context": {"visible": "sk-live-secret"},
        },
    )

    assert response.status_code == 200
    payload = response.json()
    data = payload["data"]
    serialized = _serialized(payload)
    assert data["status"] == "rejected"
    assert data["classification"]["category"] == "private_marker_detected"
    assert data["classification"]["redaction_status"] == "redacted"
    assert data["queue_item"] is None
    assert data["direct_state_mutation_applied"] is False
    assert "raw_provider_response" not in serialized
    assert "sk-live-secret" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    events = client.get("/world/events?limit=200").json()["data"]["items"]
    rejected_events = [
        event for event in events if event["type"] == "world.session_direction.rejected"
    ]
    assert len(rejected_events) == 1
    event_payload = rejected_events[0]["payload"]
    assert event_payload["branch_id"] is None
    assert event_payload["public_context_keys"] == []
    assert event_payload["classification"]["redaction_status"] == "redacted"
    assert "raw_provider_response" not in _serialized(event_payload)
    assert "sk-live-secret" not in _serialized(event_payload)


def test_unknown_session_direction_returns_existing_error_envelope() -> None:
    client = _client()

    response = client.post(
        "/sessions/session-missing/directions",
        json={"instruction_text": "Increase rain risk"},
    )

    assert response.status_code == 404
    payload = response.json()
    assert payload["code"] == 24
    assert payload["msg"] == "Unknown session_id"


def test_session_direction_manifest_surfaces_are_discoverable() -> None:
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    surfaces = response.json()["public_surfaces"]
    operation_ids = {surface["operation_id"] for surface in surfaces}
    assert "submit_world_session_direction" in operation_ids
    assert "get_world_session_directions" in operation_ids
