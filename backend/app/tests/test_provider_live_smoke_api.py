from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _client() -> TestClient:
    return TestClient(create_app())


def _forbidden_markers() -> set[str]:
    return {
        "api_key",
        "apikey",
        "authorization",
        "bearer",
        "hidden context",
        "hidden_context",
        "private memory",
        "private goal",
        "provider_secret",
        "raw prompt",
        "raw_prompt",
        "raw request",
        "raw_request",
        "raw response",
        "raw_response",
        "raw thought",
        "raw_thought",
        "self_state",
    }


def _public_value_text(value) -> str:
    if isinstance(value, dict):
        return " ".join(_public_value_text(item) for item in value.values())
    if isinstance(value, list):
        return " ".join(_public_value_text(item) for item in value)
    return str(value).lower()


def test_provider_live_smoke_reports_not_configured_without_call(monkeypatch) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    monkeypatch.delenv("WORLDENGINE_LLM_MODEL", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    client = _client()

    response = client.post("/provider/live-smoke", json={})

    assert response.status_code == 200
    payload = response.json()
    assert payload["schema_version"] == "0.9.1"
    assert payload["provider_class"] == "unconfigured"
    assert payload["model_label"] == "unconfigured"
    assert payload["call_attempted"] is False
    assert payload["call_status"] == "not_configured"
    assert payload["public_failure_category"] == "not_configured"
    assert payload["worldengine_owned_call"] is True
    assert all(value is False for value in payload["redaction"].values())


def test_provider_live_smoke_accepts_empty_body(monkeypatch) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    client = _client()

    response = client.post("/provider/live-smoke")

    assert response.status_code == 200
    assert response.json()["call_status"] == "not_configured"


def test_provider_live_smoke_blocks_unknown_provider_without_private_details(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "private-provider")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "sk-live-secret-model")
    client = _client()

    response = client.post("/provider/live-smoke", json={})

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["provider_class"] == "unknown"
    assert payload["model_label"] == "unknown"
    assert payload["call_attempted"] is False
    assert payload["call_status"] == "blocked"
    assert payload["public_failure_category"] == "unsupported_provider"
    assert "private-provider" not in serialized
    assert "sk-live-secret-model" not in serialized


def test_provider_live_smoke_returns_safe_mock_success_without_network(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "mock")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "mock-public")
    app = create_app()

    async def smoke_runner(*, provider_class: str) -> dict:
        assert provider_class == "mock"
        return {
            "call_status": "success",
            "latency_ms": 12,
            "token_usage_bucket": "1-100",
            "public_failure_category": "none",
        }

    app.state.provider_smoke_runner = smoke_runner
    app.state.provider_smoke_runner_mode = "safe_mock"
    client = TestClient(app)

    response = client.post("/provider/live-smoke", json={})

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["provider_class"] == "mock"
    assert payload["model_label"] == "mock-public"
    assert payload["call_attempted"] is True
    assert payload["call_status"] == "success"
    assert payload["latency_ms"] == 12
    assert payload["token_usage_bucket"] == "1-100"
    assert payload["public_failure_category"] == "none"
    assert all(value is False for value in payload["redaction"].values())
    assert not any(marker in _public_value_text(payload) for marker in _forbidden_markers())


def test_provider_live_smoke_redaction_failure_does_not_echo_private_result(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "mock")
    app = create_app()

    def unsafe_runner(*, provider_class: str) -> dict:
        assert provider_class == "mock"
        return {
            "call_status": "success",
            "raw_response": "provider_secret=sk-live-secret-key",
        }

    app.state.provider_smoke_runner = unsafe_runner
    app.state.provider_smoke_runner_mode = "safe_mock"
    client = TestClient(app)

    response = client.post("/provider/live-smoke", json={})

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["call_attempted"] is True
    assert payload["call_status"] == "failure"
    assert payload["public_failure_category"] == "redaction_failure"
    assert payload["redaction"]["raw_provider_responses_included"] is True
    assert payload["redaction"]["api_keys_included"] is True
    assert "sk-live-secret-key" not in serialized
    assert "provider_secret=sk-live-secret-key" not in serialized


def test_provider_live_smoke_detects_contract_forbidden_marker_variants(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "mock")
    app = create_app()

    def unsafe_runner(*, provider_class: str) -> dict:
        assert provider_class == "mock"
        return {
            "call_status": "success",
            "api key": "redacted",
            "raw provider request": "redacted",
            "raw_provider_request": "redacted",
            "raw provider response": "redacted",
            "raw_provider_response": "redacted",
            "provider trace": "redacted",
            "private evaluator data": "redacted",
        }

    app.state.provider_smoke_runner = unsafe_runner
    app.state.provider_smoke_runner_mode = "safe_mock"
    client = TestClient(app)

    response = client.post("/provider/live-smoke", json={})

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["call_status"] == "failure"
    assert payload["public_failure_category"] == "redaction_failure"
    assert payload["redaction"]["api_keys_included"] is True
    assert payload["redaction"]["raw_provider_requests_included"] is True
    assert payload["redaction"]["raw_provider_responses_included"] is True
    assert payload["redaction"]["provider_traces_included"] is True
    assert payload["redaction"]["private_evaluator_data_included"] is True
    assert "private evaluator data" not in serialized


def test_provider_live_smoke_blocks_runner_without_safe_mock_authorization(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "mock")
    app = create_app()
    called = False

    def runner(*, provider_class: str) -> dict:
        nonlocal called
        called = True
        return {"call_status": "success"}

    app.state.provider_smoke_runner = runner
    client = TestClient(app)

    response = client.post("/provider/live-smoke", json={})

    assert response.status_code == 200
    payload = response.json()
    assert payload["call_attempted"] is False
    assert payload["call_status"] == "blocked"
    assert payload["public_failure_category"] == "blocked"
    assert called is False


def test_provider_live_smoke_detects_hidden_context_in_runner_result(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "mock")
    app = create_app()

    def unsafe_runner(*, provider_class: str) -> dict:
        return {
            "call_status": "success",
            "token_usage_bucket": "raw_thought hidden context",
        }

    app.state.provider_smoke_runner = unsafe_runner
    app.state.provider_smoke_runner_mode = "safe_mock"
    client = TestClient(app)

    response = client.post("/provider/live-smoke", json={})

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["call_status"] == "failure"
    assert payload["public_failure_category"] == "redaction_failure"
    assert payload["redaction"]["raw_thought_included"] is True
    assert payload["redaction"]["hidden_context_included"] is True
    assert "raw_thought hidden context" not in serialized


def test_provider_live_smoke_request_rejects_private_extra_fields() -> None:
    client = _client()

    response = client.post(
        "/provider/live-smoke",
        json={"mode": "safe", "raw_prompt": "private"},
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["code"] == 30
    assert payload["data"]["errors"][0]["type"] == "extra_forbidden"
    assert "private" not in serialized
    assert "raw_prompt" not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_provider_live_smoke_is_openapi_discoverable_and_manifest_additive() -> None:
    client = _client()

    openapi = client.get("/openapi.json").json()
    manifest = client.get("/manifest").json()

    smoke_post = openapi["paths"]["/provider/live-smoke"]["post"]
    assert smoke_post["operationId"] == "provider_live_smoke"
    assert "provider" in smoke_post["tags"]
    surfaces = manifest["public_surfaces"]
    assert any(
        surface["path"] == "/provider/live-smoke"
        and surface["method"] == "POST"
        and surface["operation_id"] == "provider_live_smoke"
        for surface in surfaces
    )
    assert manifest["provider"]["provider_readiness"] == "not_configured"
    assert "provider readiness is not live provider call proof" in manifest["warnings"]


def test_manifest_reports_unknown_provider_as_blocked_without_private_label(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "private-provider")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "sk-live-secret-model")
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["provider"]["provider_class"] == "unknown"
    assert payload["provider"]["provider_readiness"] == "blocked"
    assert payload["provider"]["model_label"] == "unknown"
    assert "private-provider" not in serialized
    assert "sk-live-secret-model" not in serialized
