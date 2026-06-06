from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_core import PydanticCustomError


ExternalProjectionRedactionStatus = Literal["passed", "failed"]
ExternalProjectionStatus = Literal["accepted", "rejected"]
ExternalProjectionClassification = Literal["external_projection", "out_of_world_diagnostic"]
ExternalProjectionProvenance = Literal[
    "worldengine_public_evidence",
    "client_supplied_public_summary",
    "external_validation_summary",
    "unknown",
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


class _RedactedBaseModel(BaseModel):
    @model_validator(mode="after")
    def _reject_private_markers(self):
        if _contains_private_marker(self.model_dump()):
            raise PydanticCustomError(
                "private_marker_detected",
                "public projection evidence contains private or unsupported markers",
            )
        return self


class ExternalProjectionEvidenceRef(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    ref_id: str = Field(min_length=1)
    ref_type: Literal["event", "snapshot", "agent_continuity", "summary", "diagnostic"]
    role: Optional[str] = Field(default=None, min_length=1)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ProjectionBoundaryDecision(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    status: ExternalProjectionStatus
    classification: ExternalProjectionClassification
    reason: str = Field(min_length=1)
    path: Optional[str] = None
    redaction_status: ExternalProjectionRedactionStatus = "passed"


class ProjectionBoundaryDiagnostic(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str = Field(min_length=1)
    message: str = Field(min_length=1)
    path: Optional[str] = None
    severity: Literal["error", "warning"] = "error"


class NarrativeProjectionArtifact(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.9"
    projection_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    source_event_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_snapshot_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_agent_continuity_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    public_narrative_summary: str = Field(min_length=1)
    projection_provenance: ExternalProjectionProvenance
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False
    redaction_status: ExternalProjectionRedactionStatus = "passed"


class DiagnosticDialogueArtifact(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.9"
    dialogue_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    question_summary: str = Field(min_length=1)
    response_summary: str = Field(min_length=1)
    source_event_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_agent_continuity_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    diagnostic_provenance: ExternalProjectionProvenance
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False
    redaction_status: ExternalProjectionRedactionStatus = "passed"


class NarrativeProjectionRequest(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    public_narrative_summary: str = Field(min_length=1)
    projection_provenance: ExternalProjectionProvenance = "worldengine_public_evidence"
    source_event_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_snapshot_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_agent_continuity_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False


class DiagnosticDialogueEvaluationRequest(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    question_summary: str = Field(min_length=1)
    response_summary: str = Field(min_length=1)
    diagnostic_provenance: ExternalProjectionProvenance = "worldengine_public_evidence"
    source_event_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    source_agent_continuity_refs: List[ExternalProjectionEvidenceRef] = Field(default_factory=list)
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False


class NarrativeProjectionResponse(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: str = Field(min_length=1)
    status: ExternalProjectionStatus
    boundary_decision: ProjectionBoundaryDecision
    diagnostics: List[ProjectionBoundaryDiagnostic] = Field(default_factory=list)
    narrative_projection: Optional[NarrativeProjectionArtifact] = None
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False
    redaction_status: ExternalProjectionRedactionStatus = "passed"


class DiagnosticDialogueEvaluationResponse(_RedactedBaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    status: ExternalProjectionStatus
    boundary_decision: ProjectionBoundaryDecision
    diagnostics: List[ProjectionBoundaryDiagnostic] = Field(default_factory=list)
    diagnostic_dialogue: Optional[DiagnosticDialogueArtifact] = None
    canonical_state_mutation_applied: bool = False
    canonical_event_appended: bool = False
    agent_memory_write_applied: bool = False
    in_world_dialogue_recorded: bool = False
    redaction_status: ExternalProjectionRedactionStatus = "passed"


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
