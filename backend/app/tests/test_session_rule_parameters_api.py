from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _client() -> TestClient:
    return TestClient(create_app())


def _create_session(client: TestClient) -> str:
    response = client.post("/sessions", json={"world_id": "world-rules-1"})
    assert response.status_code == 200
    return response.json()["data"]["session_id"]


def _valid_rule_set(world_id: str = "world-rules-1") -> dict:
    return {
        "world_id": world_id,
        "generation_id": "generation-rules-1",
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
                "source": {"kind": "generated", "ref": "0.11.2-test"},
                "rule_refs": ["rule.weather_drift"],
            }
        ],
        "rules": [
            {
                "rule_id": "rule.weather_drift",
                "rule_kind": "environment_trend",
                "trigger": {"type": "tick_interval", "interval": 3},
                "conditions": [
                    {
                        "type": "parameter_min",
                        "parameter_ref": "param.weather_intensity",
                        "min": 0,
                    }
                ],
                "effects": [
                    {
                        "op": "set",
                        "parameter_ref": "param.weather_intensity",
                        "value_expression": {
                            "type": "bounded_delta",
                            "delta": 1,
                            "min": 0,
                            "max": 10,
                        },
                    }
                ],
                "target_parameter_refs": ["param.weather_intensity"],
                "allowed_ops": ["set"],
                "priority": 10,
                "cooldown": {"ticks": 1},
                "evidence": {"public_explanation": "weather may intensify within bounds"},
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
        "boundaries": [
            {
                "boundary_id": "boundary.no_private_state",
                "category": "private_state",
                "target_refs": ["param.weather_intensity"],
                "public_explanation": "rules cannot mutate private agent memory",
            }
        ],
    }


def test_valid_rule_set_attaches_to_session_and_can_be_read_back() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.post(f"/sessions/{session_id}/rules", json=_valid_rule_set())

    assert response.status_code == 200
    payload = response.json()["data"]
    assert payload["attachment_status"] == "attached"
    assert payload["validation"]["validation_status"] == "accepted"
    assert payload["summary"]["parameter_paths"] == ["environment.weather_intensity"]
    assert payload["summary"]["rule_ids"] == ["rule.weather_drift"]
    assert payload["summary"]["boundary_ids"] == ["boundary.no_private_state"]

    read_response = client.get(f"/sessions/{session_id}/rules")
    assert read_response.status_code == 200
    read_payload = read_response.json()["data"]
    assert read_payload["attachment_status"] == "attached"
    assert read_payload["summary"] == payload["summary"]
    assert read_payload["validation"]["validation_status"] == "accepted"


def test_get_rules_before_attach_reports_not_attached() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.get(f"/sessions/{session_id}/rules")

    assert response.status_code == 200
    payload = response.json()["data"]
    assert payload["attachment_status"] == "not_attached"
    assert payload["summary"] is None
    assert payload["validation"] is None
    assert payload["redaction_status"] == "not_run"


def test_invalid_rule_set_is_rejected_without_replacing_last_summary() -> None:
    client = _client()
    session_id = _create_session(client)
    valid = _valid_rule_set()
    assert client.post(f"/sessions/{session_id}/rules", json=valid).status_code == 200

    invalid = _valid_rule_set()
    invalid["rules"][0]["target_parameter_refs"] = ["param.missing"]
    invalid["rules"][0]["effects"][0]["parameter_ref"] = "param.missing"
    response = client.post(f"/sessions/{session_id}/rules", json=invalid)

    assert response.status_code == 200
    payload = response.json()["data"]
    assert payload["attachment_status"] == "rejected"
    assert payload["validation"]["validation_status"] == "rejected"
    assert any(
        diagnostic["code"] == "unresolved_parameter_ref"
        for diagnostic in payload["validation"]["diagnostics"]
    )

    read_payload = client.get(f"/sessions/{session_id}/rules").json()["data"]
    assert read_payload["attachment_status"] == "attached"
    assert read_payload["summary"]["rule_ids"] == ["rule.weather_drift"]
    assert read_payload["validation"]["validation_status"] == "accepted"


def test_private_marker_rule_set_is_rejected_without_echo() -> None:
    client = _client()
    session_id = _create_session(client)
    private = _valid_rule_set()
    private["parameters"][0]["description"] = "raw prompt sk-live-secret"
    private["rules"][0]["evidence"]["public_explanation"] = "provider_trace hidden context"

    response = client.post(f"/sessions/{session_id}/rules", json=private)

    assert response.status_code == 200
    payload = response.json()["data"]
    serialized = str(payload).lower()
    assert payload["attachment_status"] == "rejected"
    assert payload["validation"]["redaction_status"] == "failed"
    assert payload["summary"]["world_id"] == "redacted"
    assert payload["summary"]["generation_id"] == "redacted"
    assert payload["summary"]["premise_digest"] == "redacted"
    assert payload["summary"]["parameter_paths"] == []
    assert payload["summary"]["rule_ids"] == []
    assert "sk-live-secret" not in serialized
    assert "raw prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "hidden context" not in serialized


def test_private_marker_top_level_rule_fields_are_redacted_from_summary() -> None:
    client = _client()
    session_id = _create_session(client)
    private = _valid_rule_set(world_id="raw_prompt.sk-live-secret")

    response = client.post(f"/sessions/{session_id}/rules", json=private)

    assert response.status_code == 200
    payload = response.json()["data"]
    serialized = str(payload).lower()
    assert payload["attachment_status"] == "rejected"
    assert payload["summary"]["world_id"] == "redacted"
    assert payload["summary"]["generation_id"] == "redacted"
    assert payload["summary"]["premise_digest"] == "redacted"
    assert "sk-live-secret" not in serialized
    assert "raw_prompt" not in serialized


def test_cross_world_rule_set_is_rejected_without_replacing_summary() -> None:
    client = _client()
    session_id = _create_session(client)
    valid = _valid_rule_set()
    assert client.post(f"/sessions/{session_id}/rules", json=valid).status_code == 200

    response = client.post(
        f"/sessions/{session_id}/rules",
        json=_valid_rule_set(world_id="world-other"),
    )

    assert response.status_code == 200
    payload = response.json()["data"]
    assert payload["attachment_status"] == "rejected"
    assert payload["validation"]["validation_status"] == "rejected"
    assert any(
        diagnostic["code"] == "session_world_mismatch"
        for diagnostic in payload["validation"]["diagnostics"]
    )

    read_payload = client.get(f"/sessions/{session_id}/rules").json()["data"]
    assert read_payload["attachment_status"] == "attached"
    assert read_payload["summary"]["world_id"] == "world-rules-1"


def test_unknown_session_rules_return_404() -> None:
    client = _client()

    read_response = client.get("/sessions/session-missing/rules")
    write_response = client.post("/sessions/session-missing/rules", json=_valid_rule_set())

    assert read_response.status_code == 404
    assert write_response.status_code == 404


def test_manifest_and_openapi_expose_session_rule_surfaces() -> None:
    client = _client()

    manifest = client.get("/manifest").json()
    surfaces = {
        (surface["method"], surface["path"]): surface
        for surface in manifest["public_surfaces"]
    }
    assert surfaces[("POST", "/sessions/{session_id}/rules")]["validation_status"] == "pass"
    assert surfaces[("GET", "/sessions/{session_id}/rules")]["validation_status"] == "pass"

    openapi = client.get("/openapi.json").json()
    assert openapi["paths"]["/sessions/{session_id}/rules"]["post"]["operationId"] == (
        "attach_world_session_rules"
    )
    assert openapi["paths"]["/sessions/{session_id}/rules"]["get"]["operationId"] == (
        "get_world_session_rules"
    )
