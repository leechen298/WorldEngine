from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_core import PydanticCustomError


AgentContinuityState = Literal[
    "observe",
    "intent",
    "action",
    "no_intent",
    "wait",
    "rest",
    "sleep",
    "consolidating",
    "reacting",
]
AgentContinuityStatus = Literal["accepted", "rejected"]
AgentContinuityRedactionStatus = Literal["passed", "failed"]
AgentActionProvenance = Literal[
    "worldengine_agent_loop",
    "client_scripted",
    "fixture_script",
    "external_validation_script",
    "unknown",
]
AgentConsolidationStatus = Literal["active", "completed"]


class AgentContinuityEvidenceRef(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ref_id: str = Field(min_length=1)
    ref_type: str = Field(min_length=1)
    role: Optional[str] = Field(default=None, min_length=1)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AgentContinuityDiagnostic(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str = Field(min_length=1)
    message: str = Field(min_length=1)
    path: Optional[str] = None
    severity: Literal["error", "warning"] = "error"


class AgentAutonomousActionEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    action_event_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    action_result_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    continuity_artifact_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    input_provenance: AgentActionProvenance
    public_action_summary: str = Field(min_length=1)
    redaction_status: AgentContinuityRedactionStatus = "passed"


class AgentEventReactionEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    event_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    reaction_summary: str = Field(min_length=1)
    selected_state: AgentContinuityState = "reacting"
    continuity_artifact_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    redaction_status: AgentContinuityRedactionStatus = "passed"


class AgentConsolidationArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.8"
    phase_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    status: AgentConsolidationStatus
    start_tick: int = Field(ge=0)
    end_tick: Optional[int] = Field(default=None, ge=0)
    start_world_time_seconds: int = Field(ge=0)
    end_world_time_seconds: Optional[int] = Field(default=None, ge=0)
    source_short_term_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    emitted_long_term_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    event_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    personality_summary_status: Literal["stable", "bounded_drift", "unchanged"] = "unchanged"
    skill_summary_status: Literal["stable", "bounded_drift", "unchanged"] = "unchanged"
    public_explanation: str = Field(min_length=1)
    redaction_status: AgentContinuityRedactionStatus = "passed"

    @model_validator(mode="after")
    def _end_window_is_bounded(self) -> "AgentConsolidationArtifact":
        if self.status == "completed":
            if self.end_tick is None or self.end_world_time_seconds is None:
                raise PydanticCustomError(
                    "missing_consolidation_end",
                    "completed consolidation requires end tick and world time",
                )
            if self.end_tick < self.start_tick:
                raise PydanticCustomError(
                    "invalid_consolidation_tick_window",
                    "end_tick must be greater than or equal to start_tick",
                )
            if self.end_world_time_seconds < self.start_world_time_seconds:
                raise PydanticCustomError(
                    "invalid_consolidation_time_window",
                    "end_world_time_seconds must be greater than or equal to start_world_time_seconds",
                )
        return self


class AgentContinuityArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.8"
    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    tick_id: int = Field(ge=0)
    world_time_seconds: int = Field(ge=0)
    state: AgentContinuityState
    perception_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    working_memory_summary: Optional[str] = Field(default=None, min_length=1)
    long_term_memory_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    personality_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    skill_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    intent_summary: Optional[str] = Field(default=None, min_length=1)
    autonomous_action_evidence: Optional[AgentAutonomousActionEvidence] = None
    event_reaction_evidence: Optional[AgentEventReactionEvidence] = None
    consolidation_phase_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    evidence_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    redaction_status: AgentContinuityRedactionStatus = "passed"


class ClientScriptedAutonomyRejection(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: Literal["client_scripted_autonomy_rejected"] = "client_scripted_autonomy_rejected"
    public_reason: str = "Rejected because the action provenance is not WorldEngine-owned Agent loop behavior."
    redaction_status: AgentContinuityRedactionStatus = "passed"


class AgentContinuityEvaluationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    state: AgentContinuityState
    perception_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    working_memory_summary: Optional[str] = Field(default=None, min_length=1)
    long_term_memory_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    personality_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    skill_summary_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    intent_summary: Optional[str] = Field(default=None, min_length=1)
    autonomous_action_evidence: Optional[AgentAutonomousActionEvidence] = None
    event_reaction_evidence: Optional[AgentEventReactionEvidence] = None
    consolidation_artifact: Optional[AgentConsolidationArtifact] = None
    evidence_refs: List[AgentContinuityEvidenceRef] = Field(default_factory=list)
    apply: bool = False


class AgentContinuityEvaluationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    status: AgentContinuityStatus
    diagnostics: List[AgentContinuityDiagnostic] = Field(default_factory=list)
    continuity_artifact: Optional[AgentContinuityArtifact] = None
    consolidation_artifact: Optional[AgentConsolidationArtifact] = None
    scripted_autonomy_rejection: Optional[ClientScriptedAutonomyRejection] = None
    applied_event_ids: List[str] = Field(default_factory=list)
    redaction_status: AgentContinuityRedactionStatus = "passed"
