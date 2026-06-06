from __future__ import annotations

import inspect
from typing import Any, Optional

from fastapi import APIRouter, Request

from app.agent.provider_config import provider_readiness_from_env, public_label
from app.schemas.provider import (
    ProviderLiveSmokeRedaction,
    ProviderLiveSmokeRequest,
    ProviderLiveSmokeResponse,
)

router = APIRouter(prefix="/provider", tags=["provider"])

_FORBIDDEN_RESULT_MARKERS = {
    "api_key": "api_keys_included",
    "api key": "api_keys_included",
    "apikey": "api_keys_included",
    "secret": "api_keys_included",
    "sk-live-": "api_keys_included",
    "sk-test-": "api_keys_included",
    "token": "api_keys_included",
    "authorization": "authorization_headers_included",
    "bearer": "authorization_headers_included",
    "hidden context": "hidden_context_included",
    "hidden_context": "hidden_context_included",
    "private goal": "hidden_context_included",
    "private_goal": "hidden_context_included",
    "private memory": "private_agent_memory_included",
    "private_memory": "private_agent_memory_included",
    "private evaluator": "private_evaluator_data_included",
    "private_evaluator": "private_evaluator_data_included",
    "private evaluator data": "private_evaluator_data_included",
    "private_evaluator_data": "private_evaluator_data_included",
    "evaluator data": "private_evaluator_data_included",
    "evaluator_data": "private_evaluator_data_included",
    "provider trace": "provider_traces_included",
    "provider_trace": "provider_traces_included",
    "raw prompt": "raw_prompts_included",
    "raw_prompt": "raw_prompts_included",
    "raw request": "raw_provider_requests_included",
    "raw_request": "raw_provider_requests_included",
    "raw provider request": "raw_provider_requests_included",
    "raw_provider_request": "raw_provider_requests_included",
    "raw response": "raw_provider_responses_included",
    "raw_response": "raw_provider_responses_included",
    "raw provider response": "raw_provider_responses_included",
    "raw_provider_response": "raw_provider_responses_included",
    "raw thought": "raw_thought_included",
    "raw_thought": "raw_thought_included",
    "self_state": "private_agent_memory_included",
}

_SAFE_RESULT_KEYS = {
    "call_status",
    "latency_ms",
    "public_failure_category",
    "token_usage_bucket",
}


def _collect_private_text(value: Any, *, scan_keys: bool = True) -> str:
    if isinstance(value, dict):
        parts: list[str] = []
        for key, item in value.items():
            key_text = str(key)
            if scan_keys and key_text not in _SAFE_RESULT_KEYS:
                parts.append(key_text)
            parts.append(_collect_private_text(item, scan_keys=scan_keys))
        return " ".join(parts)
    if isinstance(value, list):
        return " ".join(_collect_private_text(item, scan_keys=scan_keys) for item in value)
    return str(value)


def _redaction_from_private_result(result: Any) -> ProviderLiveSmokeRedaction:
    text = _collect_private_text(result).lower()
    flags = {field: False for field in ProviderLiveSmokeRedaction.model_fields}
    for marker, field in _FORBIDDEN_RESULT_MARKERS.items():
        if marker in text:
            flags[field] = True
    return ProviderLiveSmokeRedaction(**flags)


def _has_redaction_failure(redaction: ProviderLiveSmokeRedaction) -> bool:
    return any(redaction.model_dump().values())


async def _run_smoke_runner(runner: Any, provider_class: str) -> dict[str, Any]:
    result = runner(provider_class=provider_class)
    if inspect.isawaitable(result):
        result = await result
    if not isinstance(result, dict):
        return {"call_status": "failure", "public_failure_category": "provider_error"}
    return result


@router.post(
    "/live-smoke",
    response_model=ProviderLiveSmokeResponse,
    operation_id="provider_live_smoke",
)
async def provider_live_smoke(
    request: Request,
    request_body: Optional[ProviderLiveSmokeRequest] = None,
) -> ProviderLiveSmokeResponse:
    provider = provider_readiness_from_env()
    if provider.provider_class == "unknown":
        return ProviderLiveSmokeResponse(
            provider_class=provider.provider_class,
            model_label=provider.model_label,
            call_attempted=False,
            call_status="blocked",
            public_failure_category="unsupported_provider",
        )
    if provider.provider_readiness == "not_configured":
        return ProviderLiveSmokeResponse(
            provider_class=provider.provider_class,
            model_label=provider.model_label,
            call_attempted=False,
            call_status="not_configured",
            public_failure_category="not_configured",
        )

    runner = getattr(request.app.state, "provider_smoke_runner", None)
    runner_mode = getattr(request.app.state, "provider_smoke_runner_mode", None)
    if runner is None or runner_mode != "safe_mock":
        return ProviderLiveSmokeResponse(
            provider_class=provider.provider_class,
            model_label=provider.model_label,
            call_attempted=False,
            call_status="blocked",
            public_failure_category="blocked",
        )

    result = await _run_smoke_runner(runner, provider.provider_class)
    redaction = _redaction_from_private_result(result)
    if _has_redaction_failure(redaction):
        return ProviderLiveSmokeResponse(
            provider_class=provider.provider_class,
            model_label=provider.model_label,
            call_attempted=True,
            call_status="failure",
            public_failure_category="redaction_failure",
            redaction=redaction,
        )

    call_status = result.get("call_status", "success")
    if call_status not in {"success", "failure", "blocked", "not_configured", "not_run"}:
        call_status = "failure"
    public_failure_category = result.get("public_failure_category", "none")
    if public_failure_category not in {
        "none",
        "not_configured",
        "network",
        "quota",
        "provider_error",
        "redaction_failure",
        "unsupported_provider",
        "blocked",
        "unknown",
    }:
        public_failure_category = "unknown"
    latency_ms = result.get("latency_ms")
    if not isinstance(latency_ms, int) or latency_ms < 0:
        latency_ms = None
    token_usage_bucket = public_label(str(result.get("token_usage_bucket", "not_reported")), "not_reported")

    return ProviderLiveSmokeResponse(
        provider_class=provider.provider_class,
        model_label=provider.model_label,
        call_attempted=True,
        call_status=call_status,
        latency_ms=latency_ms,
        token_usage_bucket=token_usage_bucket,
        public_failure_category=public_failure_category,
        redaction=redaction,
    )
