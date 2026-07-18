from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_core import PydanticCustomError

from app.schemas.world_generation import (
    GeneratedRuleParameterSet,
    WorldRuleOperation,
    _private_mapping_markers,
)


WorldEventLegalityStatus = Literal["accepted", "rejected", "blocked"]
WorldEventLegalityClassification = Literal["legal", "illegal", "blocked"]
WorldEvolutionRedactionStatus = Literal["passed", "failed"]


class WorldParameterPatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    parameter_ref: str = Field(min_length=1)
    op: WorldRuleOperation
    value: Any = None
    rule_ref: str = Field(min_length=1)
    public_explanation: str = Field(min_length=1)


class WorldEventCandidate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.7"
    candidate_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    branch_id: Optional[str] = Field(default=None, min_length=1)
    event_type: str = Field(min_length=1)
    source: str = Field(default="world_rule", min_length=1)
    proposed_tick: Optional[int] = Field(default=None, ge=0)
    proposed_world_time_seconds: Optional[int] = Field(default=None, ge=0)
    rule_refs: List[str] = Field(min_length=1)
    parameter_patches: List[WorldParameterPatch] = Field(min_length=1)
    direction_refs: List[str] = Field(default_factory=list)
    cause_refs: List[str] = Field(min_length=1)
    location_refs: List[str] = Field(default_factory=list)
    probability_evidence: Dict[str, Any] = Field(default_factory=dict)
    causality_evidence: Dict[str, Any] = Field(default_factory=dict)
    public_summary: str = Field(min_length=1)

    @model_validator(mode="after")
    def _reject_private_markers(self) -> "WorldEventCandidate":
        if _private_mapping_markers(self.model_dump()):
            raise PydanticCustomError(
                "private_event_candidate_marker",
                "event candidate contains private or unsupported fields",
            )
        return self


class WorldEventLegalityDiagnostic(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str = Field(min_length=1)
    message: str = Field(min_length=1)
    path: Optional[str] = None
    severity: Literal["error", "warning"] = "error"


class WorldStateDiffItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    parameter_ref: str = Field(min_length=1)
    path: str = Field(min_length=1)
    old_public_value: Any = None
    new_public_value: Any = None
    op: WorldRuleOperation
    rule_id: str = Field(min_length=1)
    constraint_ids: List[str] = Field(default_factory=list)
    public_explanation: str = Field(min_length=1)


class WorldStateDiff(BaseModel):
    model_config = ConfigDict(extra="forbid")

    changed_parameter_ids: List[str] = Field(default_factory=list)
    items: List[WorldStateDiffItem] = Field(default_factory=list)
    direct_private_mutation_applied: bool = False
    redaction_status: WorldEvolutionRedactionStatus = "passed"


class WorldEvolutionEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.7"
    world_id: str = Field(min_length=1)
    candidate_id: str = Field(min_length=1)
    legality_status: WorldEventLegalityStatus
    matched_rule_ids: List[str] = Field(default_factory=list)
    checked_constraint_ids: List[str] = Field(default_factory=list)
    referenced_parameter_ids: List[str] = Field(default_factory=list)
    direction_refs: List[str] = Field(default_factory=list)
    state_snapshot_refs: Dict[str, Any] = Field(default_factory=dict)
    diagnostics_count: int = Field(default=0, ge=0)
    state_diff_summary: Dict[str, Any] = Field(default_factory=dict)
    redaction_status: WorldEvolutionRedactionStatus = "passed"
    direct_state_mutation_applied: bool = False


class WorldEventLegalityResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: WorldEventLegalityStatus
    legality_classification: WorldEventLegalityClassification
    diagnostics: List[WorldEventLegalityDiagnostic] = Field(default_factory=list)
    matched_rule_ids: List[str] = Field(default_factory=list)
    checked_constraint_ids: List[str] = Field(default_factory=list)
    referenced_parameter_ids: List[str] = Field(default_factory=list)
    timing_evidence: Dict[str, Any] = Field(default_factory=dict)
    probability_evidence: Dict[str, Any] = Field(default_factory=dict)
    causality_evidence: Dict[str, Any] = Field(default_factory=dict)
    redaction_status: WorldEvolutionRedactionStatus = "passed"
    state_diff: Optional[WorldStateDiff] = None
    evidence: Optional[WorldEvolutionEvidence] = None
    applied_event_id: Optional[str] = None
    direct_state_mutation_applied: bool = False


class WorldEventEvaluationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    candidate: WorldEventCandidate
    rule_set: GeneratedRuleParameterSet
    apply: bool = False


class WorldEventEvaluationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: str = Field(min_length=1)
    result: WorldEventLegalityResult


class SessionEvolutionStepRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    apply: bool = True


class SessionEvolutionStepResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    status: WorldEventLegalityStatus
    candidate: Optional[WorldEventCandidate] = None
    result: WorldEventLegalityResult
    replay_event_id: Optional[str] = None
    direct_state_mutation_applied: bool = False
    redaction_status: WorldEvolutionRedactionStatus = "passed"
