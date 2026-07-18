from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class WorldSnapshot(BaseModel):
    world_id: str = Field(default="world-v1")
    label: str = Field(default="WorldEngine Seed World")


class PublicProviderReadiness(BaseModel):
    model_config = ConfigDict(extra="forbid")

    provider_class: Literal[
        "deepseek_api",
        "kimi_code_subscription",
        "kimi_platform_api",
        "moonshot_api",
        "mock",
        "unconfigured",
        "unknown",
    ]
    provider_readiness: Literal[
        "configured",
        "not_configured",
        "unknown",
        "unavailable",
        "blocked",
    ]
    credential_source_class: Literal["environment", "none", "unknown"] = "none"
    model_label: str = Field(min_length=1)
    quota_status: Literal["unknown", "not_checked"] = "not_checked"
    rate_limit_note: str = "not checked"


class PublicRedactionStatus(BaseModel):
    model_config = ConfigDict(extra="forbid")

    secrets_included: bool = False
    private_prompts_included: bool = False
    provider_raw_traces_included: bool = False
    private_agent_state_included: bool = False


class PublicSurface(BaseModel):
    model_config = ConfigDict(extra="forbid")

    path: str = Field(min_length=1)
    method: str = Field(min_length=1)
    operation_id: str = Field(min_length=1)
    status: Literal["available", "unavailable"]
    maturity: Literal["implemented", "planned", "blocked", "deprecated"] = "implemented"
    validation_status: Literal["pass", "fail", "blocked", "not_run"] = "not_run"
    required_for_mvp: bool = False
    notes: List[str] = Field(default_factory=list)


class PublicStatusDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["pass", "fail", "blocked", "not_run"]
    meaning: str = Field(min_length=1)


class CheckerArtifactRef(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    required_for_mvp: bool = False
    status: Literal["pass", "fail", "blocked", "not_run"] = "not_run"
    redaction_required: bool = True


class CheckerHandoff(BaseModel):
    model_config = ConfigDict(extra="forbid")

    checker_contract: str = Field(default="worldengine-mvp-debug-handoff")
    validation_client_role: Literal["display_export_only"] = "display_export_only"
    evaluator_role: Literal["worldengine_checker_or_second_agent_review"] = (
        "worldengine_checker_or_second_agent_review"
    )
    expected_result_statuses: List[Literal["pass", "fail", "blocked", "not_run"]] = Field(
        default_factory=lambda: ["pass", "fail", "blocked", "not_run"]
    )
    artifact_index: List[CheckerArtifactRef] = Field(default_factory=list)
    unsupported_items: List[str] = Field(default_factory=list)


class HandoffManifest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = Field(default="0.8.9.1")
    worldengine_version: str = Field(default="v0.10")
    mvp_contract_version: str = Field(default="v0.10-debug-handoff")
    manifest_status: Literal["pass", "fail", "blocked", "not_run"] = "blocked"
    provider: PublicProviderReadiness
    validation_client_role: Literal["display_export_only"] = "display_export_only"
    provider_owner: Literal["worldengine"] = "worldengine"
    evaluator_role: Literal["worldengine_checker_or_second_agent_review"] = (
        "worldengine_checker_or_second_agent_review"
    )
    status_taxonomy: List[PublicStatusDefinition] = Field(default_factory=list)
    public_surfaces: List[PublicSurface] = Field(default_factory=list)
    checker_handoff: CheckerHandoff = Field(default_factory=CheckerHandoff)
    worldline_branch_semantics: str = Field(
        default=(
            "Worldline branches are comparable timeline branches for replay "
            "and debugging; they are branch-like alternatives on the same "
            "timeline model, with no origin hierarchy."
        ),
        min_length=1,
    )
    redaction: PublicRedactionStatus = Field(default_factory=PublicRedactionStatus)
    blockers: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)


class PublicWorldCreateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    world_prompt: str = Field(min_length=1)


class PublicAgentState(BaseModel):
    model_config = ConfigDict(extra="forbid")

    agent_id: str = Field(min_length=1)
    display_name: str = Field(min_length=1)
    location: str = Field(min_length=1)
    public_status: str = Field(min_length=1)
    visible_action: str = Field(min_length=1)


class PublicInitialWorldState(BaseModel):
    model_config = ConfigDict(extra="forbid")

    summary: str = Field(min_length=1)
    public_agents: List[PublicAgentState] = Field(default_factory=list)
    environment: Dict[str, Any] = Field(default_factory=dict)


class PublicVisualizationPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tilemap: Dict[str, Any] = Field(default_factory=dict)
    entities: List[Dict[str, Any]] = Field(default_factory=list)


class PublicWorldCreationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: str = Field(min_length=1)
    status: Literal["created"] = "created"
    public_initial_state: PublicInitialWorldState
    visualization: PublicVisualizationPayload


class DirectorGuidanceRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    instruction_text: str = Field(min_length=1)
    branch_id: Optional[str] = Field(default=None, min_length=1)
    tick: Optional[int] = Field(default=None, ge=0)
    public_context: Dict[str, Any] = Field(default_factory=dict)


class DirectorGuidanceResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: str = Field(min_length=1)
    status: Literal["accepted", "applied", "blocked", "unavailable"] = "accepted"
    public_explanation: str = Field(min_length=1)
    applied_event_id: Optional[str] = Field(default=None, min_length=1)
    error_message: Optional[str] = None
