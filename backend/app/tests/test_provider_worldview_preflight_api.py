from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _client() -> TestClient:
    return TestClient(create_app())


def _request(**overrides):
    payload = {
        "request_id": "preflight-1",
        "worldview_premise": "A coastal research world with careful robots",
    }
    payload.update(overrides)
    return payload


def test_preflight_reports_not_configured_without_worldview(monkeypatch) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    monkeypatch.delenv("WORLDENGINE_LLM_MODEL", raising=False)
    client = _client()

    response = client.post("/provider/worldview-preflight", json={"request_id": "readiness-only"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["schema_version"] == "0.11.1"
    assert payload["preflight_status"] == "no_worldview_request"
    assert payload["provider"]["provider_readiness"] == "not_configured"
    assert payload["live_call_authorized"] is False
    assert payload["call_attempted"] is False
    assert payload["worldview"] is None


def test_preflight_reports_deterministic_fallback_when_provider_missing(monkeypatch) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    client = _client()

    response = client.post("/provider/worldview-preflight", json=_request())

    assert response.status_code == 200
    payload = response.json()
    worldview = payload["worldview"]
    assert payload["preflight_status"] == "deterministic_fallback_available"
    assert payload["provider"]["provider_class"] == "unconfigured"
    assert worldview["generation_status"] == "fallback"
    assert worldview["generation_mode"] == "deterministic_fallback"
    assert worldview["creation_mode"] == "deterministic_generic_fallback"
    assert worldview["llm_backed"] is False
    assert worldview["provider_backed"] is False
    assert worldview["deterministic_generic_fallback_detected"] is True


def test_preflight_reports_not_configured_when_fallback_disabled(monkeypatch) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    client = _client()

    response = client.post(
        "/provider/worldview-preflight",
        json=_request(allow_deterministic_fallback=False),
    )

    assert response.status_code == 200
    payload = response.json()
    worldview = payload["worldview"]
    assert payload["preflight_status"] == "not_configured"
    assert worldview["generation_status"] == "not_configured"
    assert worldview["generation_mode"] == "not_configured"
    assert worldview["blockers"] == ["provider_not_configured"]


def test_preflight_blocks_configured_provider_without_live_call(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "deepseek")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "sk-live-secret-model")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "sk-live-secret-key")
    client = _client()

    response = client.post("/provider/worldview-preflight", json=_request())

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    worldview = payload["worldview"]
    assert payload["preflight_status"] == "provider_ready_blocked_without_live_authorization"
    assert payload["provider"]["provider_readiness"] == "configured"
    assert payload["provider"]["model_label"] == "redacted"
    assert payload["live_call_authorized"] is False
    assert payload["call_attempted"] is False
    assert "live_provider_call_not_authorized" in payload["blockers"]
    assert worldview["generation_status"] == "blocked"
    assert worldview["generation_mode"] == "blocked"
    assert worldview["provider_backed"] is False
    assert "sk-live-secret-key" not in serialized
    assert "sk-live-secret-model" not in serialized


def test_preflight_reports_safe_mock_as_non_live(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "mock")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "mock-public")
    client = _client()

    response = client.post("/provider/worldview-preflight", json=_request())

    assert response.status_code == 200
    payload = response.json()
    worldview = payload["worldview"]
    assert payload["preflight_status"] == "safe_mock_available"
    assert payload["provider"]["provider_class"] == "mock"
    assert worldview["generation_mode"] == "safe_mock"
    assert worldview["creation_mode"] == "safe_mock_non_live"
    assert worldview["llm_backed"] is False
    assert worldview["provider_backed"] is False


def test_preflight_rejects_private_markers_without_echo() -> None:
    client = _client()

    response = client.post(
        "/provider/worldview-preflight",
        json=_request(worldview_premise="public world raw_prompt sk-live-secret"),
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["code"] == 30
    assert "raw_prompt" not in serialized
    assert "sk-live-secret" not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_manifest_and_openapi_expose_preflight_surface() -> None:
    client = _client()

    manifest = client.get("/manifest").json()
    surfaces = {
        (surface["method"], surface["path"]): surface
        for surface in manifest["public_surfaces"]
    }
    surface = surfaces[("POST", "/provider/worldview-preflight")]
    assert surface["operation_id"] == "provider_worldview_preflight"
    assert surface["status"] == "available"
    assert surface["validation_status"] == "pass"

    openapi = client.get("/openapi.json").json()
    route = openapi["paths"]["/provider/worldview-preflight"]["post"]
    assert route["operationId"] == "provider_worldview_preflight"
