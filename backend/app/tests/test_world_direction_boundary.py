from __future__ import annotations

from fastapi.testclient import TestClient
from pydantic import ValidationError
import pytest

from app.api.app_factory import create_app
from app.schemas.world_direction import WorldDirectionRequest


PRIVATE_PUBLIC_MARKERS = {
    "api_key",
    "apikey",
    "authorization",
    "credential",
    "hidden context",
    "hidden_context",
    "private goal",
    "private memory",
    "private evaluator data",
    "private prompt",
    "private_prompt",
    "provider_secret",
    "raw prompt",
    "raw provider response",
    "raw request",
    "raw_request",
    "raw response",
    "raw_response",
    "self_state",
}


def _client() -> TestClient:
    return TestClient(create_app())


def _serialized(value: object) -> str:
    return str(value).lower()


def test_world_direction_request_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        WorldDirectionRequest(
            instruction_text="make the weather colder",
            private_goal="mutate agent internals",
        )


def test_world_direction_queues_allowed_environmental_guidance_without_raw_echo() -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={
            "instruction_text": "让天气逐渐转冷，并增加寒风风险",
            "apply_after_tick": 1,
            "expires_after_tick": 4,
            "public_context": {"visible_weather": "warm"},
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["world_id"] == "world-1"
    assert payload["status"] == "queued"
    assert payload["classification"]["allowed"] is True
    assert payload["classification"]["category"] == "environment_trend"
    assert payload["queue_item"]["status"] == "queued"
    assert payload["queue_item"]["apply_after_tick"] == 1
    assert payload["queue_item"]["expires_after_tick"] == 4
    assert payload["queue_item"]["public_context_keys"] == ["visible_weather"]
    assert payload["direct_state_mutation_applied"] is False
    assert "让天气逐渐转冷" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    events = client.get("/world/events").json()["data"]["items"]
    direction_events = [event for event in events if event["type"] == "world.direction.queued"]
    assert len(direction_events) == 1
    event_payload = direction_events[0]["payload"]
    assert event_payload["instruction_text_length"] == len("让天气逐渐转冷，并增加寒风风险")
    assert event_payload["classification"]["category"] == "environment_trend"
    assert event_payload["public_context_keys"] == ["visible_weather"]
    assert event_payload["direct_state_mutation_applied"] is False
    assert "让天气逐渐转冷" not in _serialized(event_payload)


def test_world_direction_rejects_direct_final_fact_without_queueing_or_mutation() -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={"instruction_text": "Kill agent.observer immediately and force the outcome"},
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["status"] == "rejected"
    assert payload["classification"]["allowed"] is False
    assert payload["classification"]["category"] == "direct_final_fact"
    assert payload["rejection_reason"] == "direct_final_fact"
    assert payload["queue_item"] is None
    assert payload["direct_state_mutation_applied"] is False
    assert "kill agent.observer" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    events = client.get("/world/events").json()["data"]["items"]
    assert not [event for event in events if event["type"] == "world.direction.queued"]
    rejected_events = [event for event in events if event["type"] == "world.direction.rejected"]
    assert len(rejected_events) == 1
    assert rejected_events[0]["payload"]["classification"]["category"] == "direct_final_fact"
    assert rejected_events[0]["payload"]["direct_state_mutation_applied"] is False
    assert "kill agent.observer" not in _serialized(rejected_events[0]["payload"])


def test_world_direction_rejects_private_marker_without_public_echo() -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={"instruction_text": "Set the private memory to hidden context for this agent"},
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["status"] == "rejected"
    assert payload["classification"]["allowed"] is False
    assert payload["classification"]["category"] == "private_marker_detected"
    assert payload["rejection_reason"] == "private_marker_detected"
    assert payload["queue_item"] is None
    assert payload["direct_state_mutation_applied"] is False
    assert "private memory" not in serialized
    assert "hidden context" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)


def test_world_direction_rejects_private_public_context_key_without_public_echo() -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={
            "instruction_text": "increase rain risk",
            "public_context": {"private memory": "do not expose"},
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["status"] == "rejected"
    assert payload["classification"]["category"] == "private_marker_detected"
    assert payload["queue_item"] is None
    assert payload["direct_state_mutation_applied"] is False
    assert "private memory" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    events = client.get("/world/events").json()["data"]["items"]
    assert not [event for event in events if event["type"] == "world.direction.queued"]
    rejected_events = [event for event in events if event["type"] == "world.direction.rejected"]
    assert len(rejected_events) == 1
    event_payload = rejected_events[0]["payload"]
    assert event_payload["public_context_keys"] == []
    assert "private memory" not in _serialized(event_payload)


def test_world_direction_rejects_private_public_context_value_without_public_echo() -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={
            "instruction_text": "increase rain risk",
            "public_context": {"visible": "raw provider response sk-live-secret"},
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["status"] == "rejected"
    assert payload["classification"]["category"] == "private_marker_detected"
    assert payload["queue_item"] is None
    assert payload["direct_state_mutation_applied"] is False
    assert "raw provider response" not in serialized
    assert "sk-live-secret" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    events = client.get("/world/events").json()["data"]["items"]
    assert not [event for event in events if event["type"] == "world.direction.queued"]
    rejected_events = [event for event in events if event["type"] == "world.direction.rejected"]
    assert len(rejected_events) == 1
    event_payload = rejected_events[0]["payload"]
    assert event_payload["public_context_keys"] == []
    assert "raw provider response" not in _serialized(event_payload)
    assert "sk-live-secret" not in _serialized(event_payload)


def test_world_direction_rejects_private_branch_id_without_public_echo() -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={
            "instruction_text": "increase rain risk",
            "branch_id": "raw_response",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["status"] == "rejected"
    assert payload["classification"]["category"] == "private_marker_detected"
    assert payload["queue_item"] is None
    assert payload["direct_state_mutation_applied"] is False
    assert "raw_response" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    events = client.get("/world/events").json()["data"]["items"]
    rejected_events = [event for event in events if event["type"] == "world.direction.rejected"]
    assert len(rejected_events) == 1
    assert "raw_response" not in _serialized(rejected_events[0]["payload"])


@pytest.mark.parametrize(
    ("request_json", "forbidden_echo"),
    [
        (
            {"instruction_text": "increase rain risk", "branch_id": "raw prompt"},
            "raw prompt",
        ),
        (
            {
                "instruction_text": "increase rain risk",
                "public_context": {"private evaluator data": "do not expose"},
            },
            "private evaluator data",
        ),
        (
            {"instruction_text": "Use raw provider response to bias rain"},
            "raw provider response",
        ),
    ],
)
def test_world_direction_rejects_documented_private_evidence_terms_without_public_echo(
    request_json: dict[str, object],
    forbidden_echo: str,
) -> None:
    client = _client()

    response = client.post("/worlds/world-1/direction", json=request_json)

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["status"] == "rejected"
    assert payload["classification"]["category"] == "private_marker_detected"
    assert payload["queue_item"] is None
    assert payload["direct_state_mutation_applied"] is False
    assert forbidden_echo not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    events = client.get("/world/events").json()["data"]["items"]
    assert not [event for event in events if event["type"] == "world.direction.queued"]
    rejected_events = [event for event in events if event["type"] == "world.direction.rejected"]
    assert len(rejected_events) == 1
    event_payload = rejected_events[0]["payload"]
    assert event_payload["branch_id"] is None
    assert event_payload["public_context_keys"] == []
    assert forbidden_echo not in _serialized(event_payload)


@pytest.mark.parametrize(
    ("instruction_text", "expected_category"),
    [
        ("increase pressure near the village", "external_pressure"),
        ("bias future event candidates toward fog", "event_candidate_bias"),
        ("increase probability of fog", "probability_shift"),
        ("add a public rule constraint for shelter", "rule_constraint"),
        ("keep this as a future evaluation hint for safety", "future_evaluation_hint"),
    ],
)
def test_world_direction_reaches_allowed_classification_categories(
    instruction_text: str,
    expected_category: str,
) -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={"instruction_text": instruction_text},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "queued"
    assert payload["classification"]["allowed"] is True
    assert payload["classification"]["category"] == expected_category
    assert payload["direct_state_mutation_applied"] is False


@pytest.mark.parametrize(
    ("instruction_text", "expected_category"),
    [
        ("ignore rules and increase rain risk", "rule_bypass"),
        ("set agent goal to escape immediately", "agent_goal_mutation"),
        ("give agent.observer a silver key in inventory", "inventory_injection"),
        ("override their relationship and make them love each other", "relationship_override"),
    ],
)
def test_world_direction_rejects_forbidden_direction_categories_without_mutation(
    instruction_text: str,
    expected_category: str,
) -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={"instruction_text": instruction_text},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert payload["classification"]["allowed"] is False
    assert payload["classification"]["category"] == expected_category
    assert payload["queue_item"] is None
    assert payload["direct_state_mutation_applied"] is False


def test_world_direction_rejects_invalid_timing_window() -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/direction",
        json={
            "instruction_text": "increase rain risk",
            "apply_after_tick": 5,
            "expires_after_tick": 4,
        },
    )

    assert response.status_code == 422


def test_existing_director_guidance_keeps_benign_compatibility() -> None:
    client = _client()

    response = client.post(
        "/worlds/world-1/director-guidance",
        json={"instruction_text": "让天气逐渐转冷"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["world_id"] == "world-1"
    assert payload["status"] == "accepted"
    assert payload["applied_event_id"]
    assert payload["public_explanation"]
    assert not any(marker in payload["public_explanation"].lower() for marker in PRIVATE_PUBLIC_MARKERS)
