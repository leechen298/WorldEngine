from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class ProviderLiveSmokeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mode: Literal["safe"] = "safe"


class ProviderLiveSmokeRedaction(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_keys_included: bool = False
    authorization_headers_included: bool = False
    raw_prompts_included: bool = False
    raw_provider_requests_included: bool = False
    raw_provider_responses_included: bool = False
    provider_traces_included: bool = False
    private_agent_memory_included: bool = False
    private_evaluator_data_included: bool = False
    raw_thought_included: bool = False
    hidden_context_included: bool = False


class ProviderLiveSmokeResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.1"
    provider_class: Literal[
        "deepseek_api",
        "kimi_code_subscription",
        "kimi_platform_api",
        "moonshot_api",
        "mock",
        "unconfigured",
        "unknown",
    ]
    model_label: str = Field(min_length=1)
    call_attempted: bool
    call_status: Literal["success", "failure", "blocked", "not_configured", "not_run"]
    latency_ms: Optional[int] = Field(default=None, ge=0)
    token_usage_bucket: str = Field(default="not_reported", min_length=1)
    public_failure_category: Literal[
        "none",
        "not_configured",
        "network",
        "quota",
        "provider_error",
        "redaction_failure",
        "unsupported_provider",
        "blocked",
        "unknown",
    ]
    worldengine_owned_call: bool = True
    redaction: ProviderLiveSmokeRedaction = Field(default_factory=ProviderLiveSmokeRedaction)
