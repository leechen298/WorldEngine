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


def _rule_set(world_id: str = "world-1") -> dict:
    return {
        "world_id": world_id,
        "generation_id": "generation-session-evolution",
        "premise_digest": "abcdef123456",
        "parameters": [
            {
                "parameter_id": "param.weather_intensity",
                "path": "environment.weather_intensity",
                "value_type": "int",
                "initial_value": 2,
                "visibility": "public",
                "description": "public weather intensity",
                "constraints": {"min": 0, "max": 10},
                "source": {"kind": "generated", "ref": "0.11.4-test"},
                "rule_refs": ["rule.weather_drift"],
            }
        ],
        "rules": [
            {
                "rule_id": "rule.weather_drift",
                "rule_kind": "environment_trend",
                "trigger": {"type": "direction_or_tick"},
                "conditions": [{"type": "public_weather_state"}],
                "effects": [
                    {
                        "op": "set",
                        "parameter_ref": "param.weather_intensity",
                        "value_expression": {
                            "type": "bounded_value",
                            "min": 0,
                            "max": 10,
                        },
                    }
                ],
                "target_parameter_refs": ["param.weather_intensity"],
                "allowed_ops": ["set"],
                "priority": 10,
                "cooldown": {"ticks": 1},
                "evidence": {
                    "public_explanation": "weather intensity can change within bounds"
                },
            }
        ],
        "constraints": [
            {
                "constraint_id": "constraint.weather_bounds",
                "scope": "parameter",
                "target_refs": ["param.weather_intensity"],
                "rule_refs": ["rule.weather_drift"],
                "expression": {"type": "range", "min": 0, "max": 10},
                "public_explanation": "weather intensity remains bounded",
            }
        ],
        "boundaries": [],
    }


def _create_session(client: TestClient, world_id: str = "world-1") -> str:
    response = client.post("/sessions", json={"world_id": world_id})
    assert response.status_code == 200
    return response.json()["data"]["session_id"]


def _attach_rules(client: TestClient, session_id: str, world_id: str = "world-1") -> None:
    response = client.post(f"/sessions/{session_id}/rules", json=_rule_set(world_id))
    assert response.status_code == 200
    assert response.json()["data"]["attachment_status"] == "attached"


def test_session_evolution_step_applies_legal_public_diff_with_direction_ref() -> None:
    client = _client()
    session_id = _create_session(client)
    _attach_rules(client, session_id)
    direction_response = client.post(
        f"/sessions/{session_id}/directions",
        json={
            "instruction_text": "The observer may face lightning-strike risk as external pressure.",
            "apply_after_tick": 0,
            "expires_after_tick": 2,
        },
    )
    assert direction_response.status_code == 200
    direction_id = direction_response.json()["data"]["queue_item"]["direction_id"]

    response = client.post(f"/sessions/{session_id}/evolution/step", json={"apply": True})

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["world_id"] == "world-1"
    assert data["status"] == "accepted"
    assert data["candidate"]["direction_refs"] == [direction_id]
    assert data["candidate"]["rule_refs"] == ["rule.weather_drift"]
    assert data["result"]["status"] == "accepted"
    assert data["result"]["state_diff"]["changed_parameter_ids"] == [
        "param.weather_intensity"
    ]
    assert data["result"]["direct_state_mutation_applied"] is False
    assert data["direct_state_mutation_applied"] is False
    assert data["replay_event_id"]
    assert "lightning-strike risk" not in serialized
    assert "injury" not in serialized
    assert "death" not in serialized
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)

    params = client.get("/world/params").json()["data"]
    assert params == {"environment": {"weather_intensity": 3}}

    events = client.get("/world/events?limit=200").json()["data"]["items"]
    accepted_events = [
        event for event in events if event["type"] == "world.session_evolution.accepted"
    ]
    assert len(accepted_events) == 1
    event_payload = accepted_events[0]["payload"]
    assert event_payload["session_id"] == session_id
    assert event_payload["candidate_id"] == data["candidate"]["candidate_id"]
    assert event_payload["direction_refs"] == [direction_id]
    assert event_payload["state_diff"]["items"][0]["old_public_value"] == 2
    assert event_payload["state_diff"]["items"][0]["new_public_value"] == 3
    assert event_payload["direct_state_mutation_applied"] is False
    assert "lightning-strike risk" not in _serialized(event_payload)


def test_session_evolution_step_blocks_without_attached_rules() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.post(f"/sessions/{session_id}/evolution/step", json={"apply": True})

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["status"] == "blocked"
    assert data["candidate"] is None
    assert data["result"]["status"] == "blocked"
    assert data["result"]["diagnostics"][0]["code"] == "session_rules_not_attached"
    assert data["direct_state_mutation_applied"] is False
    assert client.get("/world/params").json()["data"] == {}

    events = client.get("/world/events?limit=200").json()["data"]["items"]
    blocked_events = [
        event for event in events if event["type"] == "world.session_evolution.blocked"
    ]
    assert len(blocked_events) == 1
    assert blocked_events[0]["payload"]["direct_state_mutation_applied"] is False


def test_session_evolution_step_is_additive_to_manual_world_evaluation() -> None:
    client = _client()
    session_id = _create_session(client)
    _attach_rules(client, session_id)

    session_response = client.post(
        f"/sessions/{session_id}/evolution/step",
        json={"apply": False},
    )

    assert session_response.status_code == 200
    assert session_response.json()["data"]["status"] == "accepted"
    assert client.get("/world/params").json()["data"] == {}

    candidate = session_response.json()["data"]["candidate"]
    manual_response = client.post(
        "/worlds/world-1/evolution/evaluate-event",
        json={"candidate": candidate, "rule_set": _rule_set(), "apply": True},
    )

    assert manual_response.status_code == 200
    assert manual_response.json()["result"]["status"] == "accepted"
    assert client.get("/world/params").json()["data"] == {
        "environment": {"weather_intensity": 3}
    }


def test_session_evolution_manifest_surface_is_discoverable() -> None:
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    surfaces = response.json()["public_surfaces"]
    assert {
        "path": "/sessions/{session_id}/evolution/step",
        "method": "POST",
        "operation_id": "run_world_session_evolution_step",
        "status": "available",
        "maturity": "implemented",
        "validation_status": "pass",
        "required_for_mvp": False,
        "notes": ["session-scoped rule-bound event generation and diff surface"],
    } in surfaces
