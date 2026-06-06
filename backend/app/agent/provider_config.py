"""Public provider readiness helpers."""

from __future__ import annotations

import os
import re

from app.schemas.world import PublicProviderReadiness


PROVIDER_ALIASES = {
    "deepseek": "deepseek_api",
    "deepseek_api": "deepseek_api",
    "kimi_code": "kimi_code_subscription",
    "kimi_for_coding": "kimi_code_subscription",
    "kimi_code_subscription": "kimi_code_subscription",
    "kimi": "kimi_platform_api",
    "kimi_platform": "kimi_platform_api",
    "kimi_platform_api": "kimi_platform_api",
    "moonshot": "moonshot_api",
    "moonshot_api": "moonshot_api",
    "mock": "mock",
}

KEY_ENV_BY_PROVIDER = {
    "deepseek_api": "DEEPSEEK_API_KEY",
    "kimi_code_subscription": "KIMI_CODE_API_KEY",
    "kimi_platform_api": "KIMI_PLATFORM_API_KEY",
    "moonshot_api": "MOONSHOT_API_KEY",
}


def public_label(value: str, fallback: str) -> str:
    stripped = value.strip()
    if not stripped:
        return fallback
    lowered = stripped.lower()
    private_markers = (
        "api_key",
        "apikey",
        "api-key",
        "authorization",
        "bearer",
        "password",
        "private",
        "secret",
        "sk-live-",
        "sk-test-",
        "token",
        "credential",
    )
    private_patterns = (
        r"\bapi[-_ ]?key\b",
        r"\bpassword\s*[:=]",
        r"\bbearer\s+\S+",
        r"\bsk-(live|test)-[a-z0-9]",
    )
    if any(marker in lowered for marker in private_markers):
        return "redacted"
    if any(re.search(pattern, lowered) for pattern in private_patterns):
        return "redacted"
    return stripped


def provider_readiness_from_env() -> PublicProviderReadiness:
    raw_provider = os.getenv("WORLDENGINE_LLM_PROVIDER", "").strip().lower()
    if not raw_provider:
        return PublicProviderReadiness(
            provider_class="unconfigured",
            provider_readiness="not_configured",
            credential_source_class="none",
            model_label="unconfigured",
        )

    provider_class = PROVIDER_ALIASES.get(raw_provider)
    if provider_class is None:
        return PublicProviderReadiness(
            provider_class="unknown",
            provider_readiness="blocked",
            credential_source_class="none",
            model_label="unknown",
        )

    model_label = public_label(os.getenv("WORLDENGINE_LLM_MODEL", ""), "")
    if provider_class == "mock":
        return PublicProviderReadiness(
            provider_class=provider_class,
            provider_readiness="configured",
            credential_source_class="none",
            model_label=model_label or "mock",
        )

    key_env = KEY_ENV_BY_PROVIDER.get(provider_class)
    has_key = bool(key_env and os.getenv(key_env, "").strip())
    return PublicProviderReadiness(
        provider_class=provider_class,
        provider_readiness="configured" if has_key else "not_configured",
        credential_source_class="environment" if has_key else "none",
        model_label=model_label or provider_class,
    )
