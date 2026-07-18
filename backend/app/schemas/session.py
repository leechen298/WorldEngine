from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_core import PydanticCustomError

from app.schemas.agent_memory import EpisodicMemoryRecord, WorkingMemoryRecord
from app.schemas.external_projection import (
    ExternalProjectionEvidenceRef,
    ExternalProjectionProvenance,
    ProjectionBoundaryDiagnostic,
)
from app.schemas.runtime import RuntimeRunSummary
from app.schemas.snapshot import Snapshot
from app.schemas.world_direction import WorldDirectionQueueItem
from app.schemas.world_generation import PublicWorldRuleSummary, RuleParameterValidationResult


SessionStatus = Literal["created", "ready", "paused", "blocked", "closed"]
SessionInspectionStatus = Literal["accepted", "rejected"]
SessionInspectionRedactionStatus = Literal["passed", "failed"]
SessionAgentState = Literal[
    "observing",
    "no_intent",
    "acting",
    "waiting",
    "resting",
    "blocked",
]

_PRIVATE_MARKERS = (
    "api_key",
    "api key",
    "apikey",
    "authorization",
    "bearer",
    "chain-of-thought",
    "chain_of_thought",
    "chain of thought",
    "credential",
    "hidden context",
    "hidden_context",
    "private evaluator data",
    "private_evaluator_data",
    "private goal",
    "private_goal",
    "private memory",
    "private_memory",
    "private prompt",
    "private_prompt",
    "provider secret",
    "provider_secret",
    "provider trace",
    "provider_trace",
    "raw prompt",
    "raw_prompt",
    "raw provider request",
    "raw_provider_request",
    "raw provider response",
    "raw_provider_response",
    "raw request",
    "raw_request",
    "raw response",
    "raw_response",
    "raw thought",
    "raw_thought",
    "secret",
    "self_state",
    "sk-live-",
    "sk-test-",
    "token",
)


class _PublicInspectionBaseModel(BaseModel):
    @model_validator(mode="after")
    def _reject_private_markers(self):
        if _contains_private_marker(self.model_dump()):
            raise PydanticCustomError(
                "private_marker_detected",
                "public inspection evidence contains private or unsupported markers",
            )
        return self


def _contains_private_marker(value: Any) -> bool:
    if isinstance(value, dict):
        return any(
            _string_has_private_marker(str(key)) or _contains_private_marker(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_private_marker(item) for item in value)
    if isinstance(value, str):
        return _string_has_private_marker(value)
    return False


def _string_has_private_marker(value: str) -> bool:
    lowered = value.casefold()
    return any(marker in lowered for marker in _PRIVATE_MARKERS)


class SessionCreateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: Optional[str] = Field(default=None, min_length=1)
    public_label: Optional[str] = Field(default=None, min_length=1, max_length=120)


class SessionRuntimeRef(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tick_id: int = Field(ge=0)
    world_time_seconds: int = Field(ge=0)
    step_seconds: int = Field(ge=1)


class SessionEvidenceRefs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    event_count_at_create: int = Field(ge=0)
    snapshot_count_at_create: int = Field(ge=0)
    current_event_count: int = Field(ge=0)
    current_snapshot_count: int = Field(ge=0)


class SessionGenerationSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    generation_id: str = Field(min_length=1)
    generation_status: str = Field(min_length=1)
    generation_mode: str = Field(min_length=1)
    creation_mode: str = Field(min_length=1)
    provider_class: str = Field(min_length=1)
    provider_backed: bool
    llm_backed: bool
    deterministic_generic_fallback_detected: bool
    premise_digest: str = Field(min_length=1)
    runtime_ready: Literal["true", "false", "blocked"]
    blockers: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    public_world_model_refs: dict[str, Any] = Field(default_factory=dict)


class WorldSession(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    public_label: str = Field(min_length=1)
    status: SessionStatus = "created"
    runtime_ref: SessionRuntimeRef
    evidence_refs: SessionEvidenceRefs
    generation_summary: Optional[SessionGenerationSummary] = None
    rule_summary: Optional[PublicWorldRuleSummary] = None
    rule_validation: Optional[RuleParameterValidationResult] = None
    direction_queue: list[WorldDirectionQueueItem] = Field(default_factory=list)
    direction_rejected_count: int = Field(default=0, ge=0)
    created_at: str = Field(min_length=1)
    updated_at: str = Field(min_length=1)
    persistence: Literal["in_memory"] = "in_memory"


class SessionListResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    items: list[WorldSession] = Field(default_factory=list)
    total: int = Field(ge=0)


class SessionStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    status: SessionStatus
    runtime_ref: SessionRuntimeRef
    evidence_refs: SessionEvidenceRefs
    updated_at: str = Field(min_length=1)


class SessionRuntimeDelta(BaseModel):
    model_config = ConfigDict(extra="forbid")

    start_tick: int = Field(ge=0)
    end_tick: int = Field(ge=0)
    start_world_time_seconds: int = Field(ge=0)
    end_world_time_seconds: int = Field(ge=0)


class SessionEventEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    event_count_before: int = Field(ge=0)
    event_count_after: int = Field(ge=0)
    event_delta_count: int = Field(ge=0)


class SessionSnapshotEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    snapshot_count_before: int = Field(ge=0)
    snapshot_count_after: int = Field(ge=0)
    snapshot_delta_count: int = Field(ge=0)
    snapshot_ids: list[str] = Field(default_factory=list)


class SessionRunEvidenceResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    run_summary: RuntimeRunSummary
    runtime_delta: SessionRuntimeDelta
    event_evidence: SessionEventEvidence
    snapshot_evidence: SessionSnapshotEvidence
    timeline_label: str = Field(min_length=1)
    redaction_status: Literal["passed"] = "passed"


class SessionSnapshotListResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    items: list[Snapshot] = Field(default_factory=list)
    total: int = Field(ge=0)
    limit: int = Field(ge=1, le=200)
    timeline_label: str = Field(min_length=1)
    redaction_status: Literal["passed"] = "passed"


class SessionRuleSummaryResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    attachment_status: Literal["attached", "rejected", "not_attached"]
    summary: Optional[PublicWorldRuleSummary] = None
    validation: Optional[RuleParameterValidationResult] = None
    redaction_status: Literal["passed", "failed", "not_run"] = "not_run"


class SessionDirectionSummaryResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    queued_items: list[WorldDirectionQueueItem] = Field(default_factory=list)
    rejected_count: int = Field(default=0, ge=0)
    queue_status: Literal["empty", "available"] = "empty"
    redaction_status: Literal["passed"] = "passed"


class SessionAgentEventEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    event_count_before: int = Field(ge=0)
    event_count_after: int = Field(ge=0)
    event_delta_count: int = Field(ge=0)
    event_ids: list[str] = Field(default_factory=list)


class SessionAgentPublicState(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    display_name: str = Field(min_length=1)
    state: SessionAgentState = "observing"
    public_status: str = Field(min_length=1)
    last_observation_summary: str = Field(min_length=1)
    current_intent: str = Field(min_length=1)
    visible_action: str = Field(min_length=1)
    runtime_ref: SessionRuntimeRef
    evidence_refs: SessionAgentEventEvidence
    client_scripted_action: bool = False
    redaction_status: Literal["passed"] = "passed"
    updated_at: str = Field(min_length=1)


class SessionAgentListResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    items: list[SessionAgentPublicState] = Field(default_factory=list)
    total: int = Field(ge=0)
    redaction_status: Literal["passed"] = "passed"


class SessionAgentStepRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    event_limit: int = Field(default=20, ge=1, le=200)
    mode_hint: Optional[Literal["auto", "rest"]] = "auto"


class SessionAgentStepResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    previous_state: SessionAgentPublicState
    updated_state: SessionAgentPublicState
    public_intent: str = Field(min_length=1)
    visible_action: str = Field(min_length=1)
    event_evidence: SessionAgentEventEvidence
    client_scripted_action: bool = False
    redaction_status: Literal["passed"] = "passed"


class SessionAgentMemorySummaryResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    working_memory: list[WorkingMemoryRecord] = Field(default_factory=list)
    episodic_memory: list[EpisodicMemoryRecord] = Field(default_factory=list)
    consolidation_status: Literal["not_consolidated", "consolidated"] = (
        "not_consolidated"
    )
    redaction_status: Literal["passed"] = "passed"


class SessionAgentMemoryConsolidationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mode: Literal["rest"] = "rest"
    event_limit: int = Field(default=20, ge=1, le=200)


class SessionAgentMemoryConsolidationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    consolidation_status: Literal["consolidated"]
    working_memory: WorkingMemoryRecord
    episodic_memory: EpisodicMemoryRecord
    event_evidence: SessionAgentEventEvidence
    personality_mutation_applied: bool = False
    skill_mutation_applied: bool = False
    private_memory_payload_included: bool = False
    redaction_status: Literal["passed"] = "passed"


class SessionInspectionTickRange(BaseModel):
    model_config = ConfigDict(extra="forbid")

    start: int = Field(ge=0)
    end: int = Field(ge=0)


class SessionNarrativeProjectionRequest(_PublicInspectionBaseModel):
    model_config = ConfigDict(extra="forbid")

    tick_start: int = Field(default=0, ge=0)
    tick_end: Optional[int] = Field(default=None, ge=0)
    branch_id: Optional[str] = Field(default=None, min_length=1)
    agent_id: Optional[str] = Field(default=None, min_length=1)
    summary_hint: Optional[str] = Field(default=None, min_length=1, max_length=240)
    source_event_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_snapshot_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_agent_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_memory_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False


class SessionDiagnosticInspectionRequest(_PublicInspectionBaseModel):
    model_config = ConfigDict(extra="forbid")

    question_summary: str = Field(min_length=1, max_length=240)
    tick_start: int = Field(default=0, ge=0)
    tick_end: Optional[int] = Field(default=None, ge=0)
    branch_id: Optional[str] = Field(default=None, min_length=1)
    agent_id: Optional[str] = Field(default=None, min_length=1)
    source_event_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_agent_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_memory_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False


class SessionNarrativeProjectionResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    status: SessionInspectionStatus
    tick_range: SessionInspectionTickRange
    branch_id: Optional[str] = None
    agent_id: Optional[str] = None
    public_narrative_summary: Optional[str] = None
    source_event_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_snapshot_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_agent_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_memory_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    inspection_provenance: ExternalProjectionProvenance = "worldengine_public_evidence"
    diagnostics: list[ProjectionBoundaryDiagnostic] = Field(default_factory=list)
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False
    redaction_status: SessionInspectionRedactionStatus = "passed"


class SessionDiagnosticInspectionResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    status: SessionInspectionStatus
    classification: Literal["out_of_world_diagnostic"] = "out_of_world_diagnostic"
    tick_range: SessionInspectionTickRange
    branch_id: Optional[str] = None
    agent_id: Optional[str] = None
    question_summary: str = Field(min_length=1)
    public_answer_summary: Optional[str] = None
    source_event_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_agent_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_memory_refs: list[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    inspection_provenance: ExternalProjectionProvenance = "worldengine_public_evidence"
    diagnostics: list[ProjectionBoundaryDiagnostic] = Field(default_factory=list)
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False
    redaction_status: SessionInspectionRedactionStatus = "passed"
