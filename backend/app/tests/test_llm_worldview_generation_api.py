from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _client() -> TestClient:
    return TestClient(create_app())


def _request(**overrides):
    payload = {
        "request_id": "worldview-request-1",
        "worldview_premise": "A coastal research world with careful robots and changing weather",
        "public_constraints": {"tone": "calm"},
    }
    payload.update(overrides)
    return payload


def _public_value_text(value) -> str:
    if isinstance(value, dict):
        return " ".join(_public_value_text(item) for item in value.values())
    if isinstance(value, list):
        return " ".join(_public_value_text(item) for item in value)
    return str(value).lower()


def test_worldview_generation_returns_labeled_deterministic_fallback_when_provider_missing(
    monkeypatch,
) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    client = _client()

    response = client.post("/world/generation/worldview", json=_request())

    assert response.status_code == 200
    payload = response.json()["data"]
    serialized_values = _public_value_text(payload)
    assert payload["schema_version"] == "0.9.2"
    assert payload["generation_status"] == "fallback"
    assert payload["generation_mode"] == "deterministic_fallback"
    assert payload["creation_mode"] == "deterministic_generic_fallback"
    assert payload["llm_backed"] is False
    assert payload["provider_backed"] is False
    assert payload["deterministic_generic_fallback_detected"] is True
    assert payload["provider_class"] == "unconfigured"
    assert payload["validation_metadata"]["premise_specific"] == "true"
    assert payload["validation_metadata"]["system_digestible"] is True
    assert payload["public_world_model"]["agents_outline"][0]["agent_id"] != "agent.observer"
    assert payload["world_creation_summary"]["distinct_from_deterministic_generic_response"] is True
    assert all(value is False for value in payload["redaction"].values())
    assert "raw_prompt" not in serialized_values
    assert "raw_response" not in serialized_values
    assert "provider_trace" not in serialized_values


def test_worldview_generation_can_report_not_configured_without_fallback(monkeypatch) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    client = _client()

    response = client.post(
        "/world/generation/worldview",
        json=_request(allow_deterministic_fallback=False),
    )

    assert response.status_code == 200
    payload = response.json()["data"]
    assert payload["generation_status"] == "not_configured"
    assert payload["generation_mode"] == "not_configured"
    assert payload["creation_mode"] == "provider_not_configured"
    assert payload["blockers"] == ["provider_not_configured"]
    assert payload["validation_metadata"]["runtime_ready"] == "blocked"
    assert payload["diagnostics"][0]["code"] == "provider_not_configured"


def test_worldview_generation_mock_is_non_live_and_not_provider_backed(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "mock")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "mock-public")
    client = _client()

    response = client.post("/world/generation/worldview", json=_request())

    assert response.status_code == 200
    payload = response.json()["data"]
    assert payload["generation_status"] == "fallback"
    assert payload["generation_mode"] == "safe_mock"
    assert payload["creation_mode"] == "safe_mock_non_live"
    assert payload["llm_backed"] is False
    assert payload["provider_backed"] is False
    assert payload["model_label"] == "mock-public"
    assert "safe mock generation is non-live" in payload["warnings"][0]


def test_worldview_generation_configured_provider_is_blocked_without_live_authorization(
    monkeypatch,
) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "deepseek")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "deepseek-public")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "sk-live-secret-key")
    client = _client()

    response = client.post("/world/generation/worldview", json=_request())

    assert response.status_code == 200
    payload = response.json()["data"]
    serialized = str(payload).lower()
    assert payload["generation_status"] == "blocked"
    assert payload["generation_mode"] == "blocked"
    assert payload["creation_mode"] == "blocked"
    assert payload["llm_backed"] is False
    assert payload["provider_backed"] is False
    assert payload["blockers"] == ["live_provider_call_not_authorized"]
    assert payload["diagnostics"][0]["code"] == "live_provider_call_not_authorized"
    assert "sk-live-secret-key" not in serialized


def test_worldview_generation_rejects_private_request_markers_without_echo() -> None:
    client = _client()

    response = client.post(
        "/world/generation/worldview",
        json=_request(worldview_premise="public world raw_prompt sk-live-secret"),
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["code"] == 30
    assert "sk-live-secret" not in serialized
    assert "raw_prompt" not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_worldview_generation_rejects_contract_forbidden_marker_variants() -> None:
    client = _client()

    for marker in (
        "api key",
        "raw provider request",
        "raw_provider_request",
        "raw provider response",
        "raw_provider_response",
        "provider trace",
        "private evaluator data",
    ):
        response = client.post(
            "/world/generation/worldview",
            json=_request(worldview_premise=f"public world {marker}"),
        )

        assert response.status_code == 422
        payload = response.json()
        serialized = str(payload).lower()
        assert payload["code"] == 30
        assert marker not in serialized
        assert "input" not in payload["data"]["errors"][0]


def test_worldview_generation_rejects_private_extra_fields_without_echo() -> None:
    client = _client()

    for private_field in (
        "hidden context",
        "private goal",
        "private memory",
        "raw request",
        "raw response",
        "raw thought",
        "provider_trace",
    ):
        response = client.post(
            "/world/generation/worldview",
            json={**_request(), private_field: "raw response sk-live-secret"},
        )

        assert response.status_code == 422
        payload = response.json()
        serialized = str(payload).lower()
        assert payload["code"] == 30
        assert "raw response sk-live-secret" not in serialized
        assert private_field not in serialized
        assert "input" not in payload["data"]["errors"][0]


def test_worldview_generation_non_ascii_premise_gets_digest_tags(monkeypatch) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    client = _client()

    response = client.post(
        "/world/generation/worldview",
        json=_request(worldview_premise="一个海边研究世界，有谨慎的机器人和变化的天气"),
    )

    assert response.status_code == 200
    payload = response.json()["data"]
    tags = payload["public_world_model"]["world_parameters_outline"]["public_tags"]
    assert tags
    assert any(tag.startswith("cjk_") for tag in tags)
    assert all(not tag.startswith("unicode_len_") for tag in tags)


def test_manifest_and_openapi_expose_worldview_generation_surface() -> None:
    client = _client()

    manifest = client.get("/manifest").json()
    surfaces = {
        (surface["path"], surface["operation_id"])
        for surface in manifest["public_surfaces"]
    }
    assert (
        "/world/generation/worldview",
        "generate_world_from_worldview",
    ) in surfaces

    openapi = client.get("/openapi.json").json()
    route = openapi["paths"]["/world/generation/worldview"]["post"]
    assert route["operationId"] == "generate_world_from_worldview"


def test_existing_public_world_creation_remains_deterministic_generic() -> None:
    client = _client()

    response = client.post(
        "/worlds",
        json={"world_prompt": "A coastal research world with careful robots"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "created"
    assert payload["public_initial_state"]["public_agents"][0]["agent_id"] == "agent.observer"
    assert "generation_mode" not in payload
