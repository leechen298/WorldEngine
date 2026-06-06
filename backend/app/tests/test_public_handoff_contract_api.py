from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _client() -> TestClient:
    return TestClient(create_app())


def test_manifest_returns_public_readiness_without_secrets(monkeypatch) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "deepseek")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "sk-live-secret-model")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "sk-live-secret-key")
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["schema_version"] == "0.8.9.1"
    assert payload["provider"] == {
        "provider_class": "deepseek_api",
        "provider_readiness": "configured",
        "credential_source_class": "environment",
        "model_label": "redacted",
        "quota_status": "not_checked",
        "rate_limit_note": "not checked",
    }
    assert payload["redaction"] == {
        "secrets_included": False,
        "private_prompts_included": False,
        "provider_raw_traces_included": False,
        "private_agent_state_included": False,
    }
    assert "sk-live-secret-key" not in serialized
    assert "sk-live-secret-model" not in serialized
    assert "api_key" not in serialized
    assert "raw_response" not in serialized


def test_manifest_reports_not_configured_provider_without_fake_ready(monkeypatch) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    monkeypatch.delenv("WORLDENGINE_LLM_MODEL", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    provider = response.json()["provider"]
    assert provider["provider_class"] == "unconfigured"
    assert provider["provider_readiness"] == "not_configured"
    assert provider["credential_source_class"] == "none"


def test_openapi_exposes_world_creation_with_required_operation_id() -> None:
    client = _client()

    response = client.get("/openapi.json")

    assert response.status_code == 200
    openapi = response.json()
    world_post = openapi["paths"]["/worlds"]["post"]
    assert world_post["operationId"] == "create_world"
    assert "worlds" in world_post["tags"]
    assert "/manifest" in openapi["paths"]


def test_create_world_returns_top_level_public_world_contract() -> None:
    client = _client()

    response = client.post(
        "/worlds",
        json={"world_prompt": "一个可观察的小型像素世界"},
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert set(payload.keys()) == {
        "world_id",
        "status",
        "public_initial_state",
        "visualization",
    }
    assert payload["world_id"].startswith("world-")
    assert payload["status"] == "created"
    assert payload["public_initial_state"]["public_agents"][0]["agent_id"] == "agent.observer"
    assert payload["visualization"]["entities"][0]["entity_id"] == "agent.observer"
    assert "api_key" not in serialized
    assert "private_prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "raw_response" not in serialized


def test_director_guidance_endpoint_accepts_public_direction_without_private_mutation() -> None:
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
    forbidden_public_markers = {
        "api_key",
        "apikey",
        "authorization",
        "credential",
        "hidden context",
        "hidden_context",
        "private goal",
        "private memory",
        "private prompt",
        "private_prompt",
        "provider_secret",
        "raw request",
        "raw_request",
        "raw response",
        "raw_response",
        "relationship internals",
        "self_state",
    }
    public_explanation = payload["public_explanation"].lower()
    assert not any(marker in public_explanation for marker in forbidden_public_markers)

    events = client.get("/world/events").json()["data"]["items"]
    director_events = [event for event in events if event["type"] == "director.guidance.accepted"]
    assert len(director_events) == 1
    event_payload = director_events[0]["payload"]
    assert event_payload["instruction_text_length"] == len("让天气逐渐转冷")
    assert "让天气逐渐转冷" not in str(event_payload)
    assert "self_state" not in str(event_payload)


def test_public_contract_rejects_extra_private_fields_with_existing_error_envelope() -> None:
    client = _client()

    response = client.post(
        "/worlds",
        json={
            "world_prompt": "public world",
            "provider_trace": "private trace",
        },
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["code"] == 30
    assert payload["data"]["errors"][0]["type"] == "extra_forbidden"
    assert "private trace" not in serialized
    assert "provider_trace" not in serialized
    assert "input" not in payload["data"]["errors"][0]
