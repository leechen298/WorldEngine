from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from pydantic_core import PydanticCustomError


SCHEMA_VERSION = "worldengine.engine.v1"
CONTRACT_VERSION = "0.13.0"
STATE_HASH_ALGORITHM = "sha256-canonical-json-v1"

_PRIVATE_VALUE_MARKERS = (
    "api_key",
    "api key",
    "access token",
    "authorization",
    "bearer",
    "chain-of-thought",
    "chain_of_thought",
    "chain of thought",
    "client secret",
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
    "provider token",
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
    "secret key",
    "self_state",
    "sk-live-",
    "sk-test-",
)

_PRIVATE_FIELD_NAMES = {
    "access_token",
    "api_key",
    "apikey",
    "authorization",
    "client_secret",
    "credential",
    "password",
    "private_memory",
    "provider_secret",
    "provider_trace",
    "raw_prompt",
    "raw_provider_request",
    "raw_provider_response",
    "raw_request",
    "raw_response",
    "secret",
    "self_state",
    "token",
}


def _validate_public_text(value: str) -> str:
    normalized = value.casefold()
    if any(marker in normalized for marker in _PRIVATE_VALUE_MARKERS):
        raise PydanticCustomError(
            "engine_v1_private_marker",
            "public text contains a private or provider marker",
        )
    return value


def _validate_public_value(value: Any) -> None:
    if isinstance(value, str):
        _validate_public_text(value)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            public_key = str(key)
            normalized_key = public_key.casefold().strip().replace("-", "_").replace(" ", "_")
            if normalized_key in _PRIVATE_FIELD_NAMES:
                raise PydanticCustomError(
                    "engine_v1_private_field",
                    "public payload contains a private or provider field",
                )
            _validate_public_text(public_key)
            _validate_public_value(item)
        return
    if isinstance(value, (list, tuple, set)):
        for item in value:
            _validate_public_value(item)


class EngineV1Model(BaseModel):
    model_config = ConfigDict(extra="forbid")


class PublicInputModel(EngineV1Model):
    @model_validator(mode="after")
    def reject_private_markers(self) -> "PublicInputModel":
        _validate_public_value(self.model_dump(mode="python"))
        return self


class StateVariableSpec(EngineV1Model):
    key: str = Field(min_length=1, pattern=r"^[a-z][a-z0-9_]{0,63}$")
    initial: int = 0
    minimum: int = -1000
    maximum: int = 1000
    step: int = Field(default=1, ge=1, le=100)

    @model_validator(mode="after")
    def validate_range(self) -> "StateVariableSpec":
        if self.minimum >= self.maximum:
            raise PydanticCustomError(
                "engine_v1_invalid_variable_range",
                "minimum must be less than maximum",
            )
        if not self.minimum <= self.initial <= self.maximum:
            raise PydanticCustomError(
                "engine_v1_invalid_variable_initial",
                "initial must be inside the declared range",
            )
        can_increase = self.initial + self.step <= self.maximum
        can_decrease = self.initial - self.step >= self.minimum
        if not can_increase and not can_decrease:
            raise PydanticCustomError(
                "engine_v1_variable_has_no_runnable_step",
                "initial value must allow at least one declared step",
            )
        return self


class WorldScaleBounds(EngineV1Model):
    minimum_locations: Literal[1] = 1
    maximum_locations: Literal[1] = 1
    minimum_agents: Literal[1] = 1
    maximum_agents: Literal[1] = 1
    minimum_state_variables: int = Field(default=1, ge=1, le=16)
    maximum_state_variables: int = Field(default=16, ge=1, le=16)

    @model_validator(mode="after")
    def validate_state_variable_bounds(self) -> "WorldScaleBounds":
        if self.minimum_state_variables > self.maximum_state_variables:
            raise PydanticCustomError(
                "engine_v1_invalid_scale_bounds",
                "minimum_state_variables must not exceed maximum_state_variables",
            )
        return self


class WorldBrief(PublicInputModel):
    seed: str = Field(min_length=1, max_length=128)
    premise: str = Field(min_length=1, max_length=1000)
    constraints: Dict[str, Any] = Field(default_factory=dict)
    scale_bounds: WorldScaleBounds = Field(default_factory=WorldScaleBounds)
    state_variables: List[StateVariableSpec] = Field(
        default_factory=lambda: [StateVariableSpec(key="world_signal")],
        min_length=1,
        max_length=16,
    )
    agent_count: Literal[1] = 1
    step_seconds: float = Field(default=1.0, gt=0, le=3600)

    _premise_is_public = field_validator("premise")(_validate_public_text)

    @model_validator(mode="after")
    def validate_unique_state_keys(self) -> "WorldBrief":
        keys = [item.key for item in self.state_variables]
        if len(keys) != len(set(keys)):
            raise PydanticCustomError(
                "engine_v1_duplicate_variable_key",
                "state variable keys must be unique",
            )
        count = len(keys)
        if not (
            self.scale_bounds.minimum_state_variables
            <= count
            <= self.scale_bounds.maximum_state_variables
        ):
            raise PydanticCustomError(
                "engine_v1_state_variable_count_out_of_bounds",
                "state variable count is outside scale_bounds",
            )
        return self


class WorldPackageCreateRequest(PublicInputModel):
    request_id: str = Field(min_length=1, max_length=128)
    brief: WorldBrief


class PackageReadiness(EngineV1Model):
    status: Literal["ready", "invalid"]
    diagnostics: List[Dict[str, Any]] = Field(default_factory=list)


class RunnableWorldPackage(EngineV1Model):
    schema_version: Literal[SCHEMA_VERSION] = SCHEMA_VERSION
    package_id: str
    package_hash: str = Field(pattern=r"^[a-f0-9]{64}$")
    brief: WorldBrief
    world_spec: Dict[str, Any]
    rule_catalog: List[Dict[str, Any]]
    action_catalog: List[Dict[str, Any]]
    agent_seed_set: List[Dict[str, Any]]
    projection_manifest: Dict[str, Any]
    evidence_policy: Dict[str, Any]
    readiness: PackageReadiness


class SessionCreateRequest(PublicInputModel):
    request_id: str = Field(min_length=1, max_length=128)
    package_id: str = Field(min_length=1)
    package_hash: str = Field(pattern=r"^[a-f0-9]{64}$")


class InterventionWindow(EngineV1Model):
    window_id: str
    open_tick: int = Field(ge=0)
    status: Literal["open", "closed"]


class AgentExperienceRef(EngineV1Model):
    ref_id: str
    ref_type: Literal["event", "action_result"]
    source_tick: int = Field(ge=0)
    public_effect: str


class AgentPublicState(EngineV1Model):
    agent_id: str
    location_id: str
    cycle_count: int = Field(ge=0)
    last_intent: str
    decision_mode: str
    experience_refs: List[AgentExperienceRef] = Field(default_factory=list)


class PublicProjection(EngineV1Model):
    schema_version: Literal[SCHEMA_VERSION] = SCHEMA_VERSION
    session_id: str
    world_id: str
    source_package_hash: str
    status: Literal["ready", "paused", "closed"]
    tick: int = Field(ge=0)
    world_time_seconds: float = Field(ge=0)
    revision: int = Field(ge=0)
    state_hash: str = Field(pattern=r"^[a-f0-9]{64}$")
    variables: Dict[str, int]
    feedback_count: int = Field(ge=0)
    locations: List[Dict[str, Any]]
    entities: List[Dict[str, Any]]
    agents: List[AgentPublicState]
    allowed_actions: List[str]
    active_intervention_window: InterventionWindow
    event_cursor: int = Field(ge=0)


class WorldSessionView(EngineV1Model):
    schema_version: Literal[SCHEMA_VERSION] = SCHEMA_VERSION
    session_id: str
    package_id: str
    source_package_hash: str
    initial_snapshot_id: str
    projection: PublicProjection


class SessionStepRequest(PublicInputModel):
    request_id: str = Field(min_length=1, max_length=128)
    step_count: int = Field(default=1, ge=1, le=100)
    expected_revision: Optional[int] = Field(default=None, ge=0)


class DirectionRequest(PublicInputModel):
    request_id: str = Field(min_length=1, max_length=128)
    window_id: str = Field(min_length=1)
    expected_revision: Optional[int] = Field(default=None, ge=0)
    kind: Literal["bounded_pressure", "direct_final_fact"]
    target_ref: str = Field(min_length=1)
    summary: str = Field(min_length=1, max_length=500)
    magnitude: Optional[int] = Field(default=None, ge=-100, le=100)
    final_value: Optional[int] = None

    _summary_is_public = field_validator("summary")(_validate_public_text)

    @model_validator(mode="after")
    def validate_direction_shape(self) -> "DirectionRequest":
        if self.kind == "bounded_pressure" and self.magnitude is None:
            raise PydanticCustomError(
                "engine_v1_missing_direction_magnitude",
                "bounded_pressure requires magnitude",
            )
        if self.kind == "direct_final_fact" and self.final_value is None:
            raise PydanticCustomError(
                "engine_v1_missing_direction_final_value",
                "direct_final_fact requires final_value",
            )
        return self


class DirectionDecision(EngineV1Model):
    request_id: str
    window_id: str
    status: Literal["accepted", "rejected", "conflict"]
    reason_code: str
    public_reason: str
    queued: bool
    rule_refs: List[str]
    event_ref: str
    application_event_refs: List[str] = Field(default_factory=list)
    applied_diff_refs: List[str] = Field(default_factory=list)
    tick: int = Field(ge=0)
    revision: int = Field(ge=0)
    state_hash_before: str
    state_hash_after: str


class ActionRequest(PublicInputModel):
    request_id: str = Field(min_length=1, max_length=128)
    expected_revision: Optional[int] = Field(default=None, ge=0)
    action_id: str = Field(min_length=1)
    target_ref: str = Field(min_length=1)
    amount: int = Field(ge=-100, le=100)


class ActionResult(EngineV1Model):
    request_id: str
    status: Literal["accepted", "rejected"]
    reason_code: str
    rule_refs: List[str]
    event_ref: str
    applied_diff_refs: List[str] = Field(default_factory=list)
    projection: PublicProjection


class FeedbackRequest(PublicInputModel):
    request_id: str = Field(min_length=1, max_length=128)
    expected_revision: Optional[int] = Field(default=None, ge=0)
    feedback_type: str = Field(min_length=1, max_length=128)
    summary: str = Field(min_length=1, max_length=500)
    related_event_ref: Optional[str] = None

    _summary_is_public = field_validator("summary")(_validate_public_text)


class FeedbackResult(EngineV1Model):
    request_id: str
    status: Literal["accepted", "rejected"]
    reason_code: str
    rule_refs: List[str]
    event_ref: str
    applied_diff_refs: List[str] = Field(default_factory=list)
    projection: PublicProjection


class DiffOperation(EngineV1Model):
    path: str
    before: Any
    after: Any


class DiffRecord(EngineV1Model):
    diff_id: str
    request_id: str
    event_ref: str
    tick: int = Field(ge=0)
    revision: int = Field(ge=1)
    state_hash_before: str
    state_hash_after: str
    operations: List[DiffOperation] = Field(min_length=1)


class EventRecord(EngineV1Model):
    sequence: int = Field(ge=1)
    event_id: str
    event_type: str
    source: str
    status: Literal["accepted", "rejected"]
    request_id: str
    tick: int = Field(ge=0)
    revision: int = Field(ge=0)
    state_hash_before: str
    state_hash_after: str
    rule_refs: List[str]
    diff_refs: List[str]
    payload: Dict[str, Any] = Field(default_factory=dict)


class SnapshotRecord(EngineV1Model):
    snapshot_id: str
    tick: int = Field(ge=0)
    revision: int = Field(ge=0)
    state_hash: str
    canonical_state: Dict[str, Any]


class AgentCycleEvidence(EngineV1Model):
    cycle_id: str
    agent_id: str
    tick: int = Field(ge=0)
    perception: Dict[str, Any]
    decision: Dict[str, Any]
    action_request: Dict[str, Any]
    rule_judgment: Dict[str, Any]
    action_result: Dict[str, Any]
    experience_refs_used: List[AgentExperienceRef]
    event_refs: List[str]
    diff_refs: List[str]


class SessionStepResult(EngineV1Model):
    request_id: str
    status: Literal["completed"]
    step_count: int
    start_tick: int
    end_tick: int
    start_revision: int
    end_revision: int
    start_state_hash: str
    end_state_hash: str
    event_refs: List[str]
    snapshot_refs: List[str]
    projection: PublicProjection


class EventPage(EngineV1Model):
    session_id: str
    after_sequence: int
    items: List[EventRecord]
    next_sequence: int
    has_more: bool


class EvidenceCompleteness(EngineV1Model):
    status: Literal["complete", "incomplete"]
    checks: Dict[str, bool]
    missing: List[str]


class EvidenceBundle(EngineV1Model):
    schema_version: Literal[SCHEMA_VERSION] = SCHEMA_VERSION
    contract_version: Literal[CONTRACT_VERSION] = CONTRACT_VERSION
    state_hash_algorithm: Literal[STATE_HASH_ALGORITHM] = STATE_HASH_ALGORITHM
    package: RunnableWorldPackage
    projection: PublicProjection
    events: List[EventRecord]
    diffs: List[DiffRecord]
    snapshots: List[SnapshotRecord]
    agent_cycles: List[AgentCycleEvidence]
    direction_decisions: List[DirectionDecision]
    request_correlations: List[Dict[str, Any]]
    completeness: EvidenceCompleteness


class CapabilityOperation(EngineV1Model):
    operation_id: str
    method: Literal["GET", "POST"]
    path: str
    maturity: Literal["anchor"] = "anchor"


class CapabilityManifest(EngineV1Model):
    engine_id: Literal["worldengine"] = "worldengine"
    engine_build: str
    instance_id: str
    contract_version: Literal[CONTRACT_VERSION] = CONTRACT_VERSION
    schema_version: Literal[SCHEMA_VERSION] = SCHEMA_VERSION
    state_hash_algorithm: Literal[STATE_HASH_ALGORITHM] = STATE_HASH_ALGORITHM
    operations: List[CapabilityOperation]
