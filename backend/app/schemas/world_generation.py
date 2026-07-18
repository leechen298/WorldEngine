from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_core import PydanticCustomError

from app.schemas.entity import EntityRef
from app.schemas.world_cell import WorldSpec


class TemplateCell(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    label: Optional[str] = None
    entity_refs: List[EntityRef] = Field(default_factory=list)
    child_cells: List["TemplateCell"] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class WorldTemplate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    version: str = Field(min_length=1)
    root: TemplateCell
    metadata: Dict[str, Any] = Field(default_factory=dict)
    constraints: Dict[str, Any] = Field(default_factory=dict)


class PlanCell(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    label: Optional[str] = None
    entity_refs: List[EntityRef] = Field(default_factory=list)
    child_cells: List["PlanCell"] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class GenerationPlan(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    version: str = Field(min_length=1)
    root: PlanCell
    metadata: Dict[str, Any] = Field(default_factory=dict)
    constraints: Dict[str, Any] = Field(default_factory=dict)


class TemplateGenerationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    template: WorldTemplate
    seed_material: Any = None
    constraints: Dict[str, Any] = Field(default_factory=dict)


class PlanGenerationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    plan: GenerationPlan
    seed_material: Any = None
    constraints: Dict[str, Any] = Field(default_factory=dict)


class PlanImportSource(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_kind: Literal["ai_assisted", "tool", "user"]
    source_id: Optional[str] = Field(default=None, min_length=1)
    provider_label: Optional[str] = Field(default=None, min_length=1)
    model_label: Optional[str] = Field(default=None, min_length=1)
    redacted: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PlanImportRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    import_id: str = Field(min_length=1)
    plan: GenerationPlan
    source: PlanImportSource
    metadata: Dict[str, Any] = Field(default_factory=dict)


GenerationPreviewSourceKind = Literal["template", "plan", "imported_plan"]


class GenerationPreviewRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    source_kind: GenerationPreviewSourceKind
    template_request: Optional[TemplateGenerationRequest] = None
    plan_request: Optional[PlanGenerationRequest] = None
    import_request: Optional[PlanImportRequest] = None
    seed_material: Any = None
    constraints: Dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _source_payload_matches_kind(self) -> "GenerationPreviewRequest":
        payloads = {
            "template": self.template_request,
            "plan": self.plan_request,
            "imported_plan": self.import_request,
        }
        present = [kind for kind, value in payloads.items() if value is not None]
        if present != [self.source_kind]:
            raise PydanticCustomError(
                "invalid_preview_source",
                "generation preview request requires exactly one matching source payload"
            )
        return self


class GenerationDiagnostic(BaseModel):
    code: str = Field(min_length=1)
    severity: str = Field(min_length=1)
    message: str = Field(min_length=1)
    path: Optional[str] = None
    source_context: Dict[str, Any] = Field(default_factory=dict)


class GenerationMetadata(BaseModel):
    generation_id: str = Field(min_length=1)
    request_id: str = Field(min_length=1)
    source_kind: Literal["template", "plan"] = "template"
    template_id: Optional[str] = Field(default=None, min_length=1)
    template_version: Optional[str] = Field(default=None, min_length=1)
    plan_id: Optional[str] = Field(default=None, min_length=1)
    plan_version: Optional[str] = Field(default=None, min_length=1)
    seed_digest: str = Field(min_length=1)
    validation_status: Literal["passed", "failed"]
    diagnostics_count: int = Field(default=0, ge=0)
    lineage: Dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _source_fields_match_kind(self) -> "GenerationMetadata":
        if self.source_kind == "template" and not (self.template_id and self.template_version):
            raise ValueError("template generation metadata requires template_id and template_version")
        if self.source_kind == "plan" and not (self.plan_id and self.plan_version):
            raise ValueError("plan generation metadata requires plan_id and plan_version")
        return self


class TemplateGenerationResult(BaseModel):
    worldspec: Optional[WorldSpec] = None
    metadata: GenerationMetadata
    diagnostics: List[GenerationDiagnostic] = Field(default_factory=list)

    @model_validator(mode="after")
    def _worldspec_matches_status(self) -> "TemplateGenerationResult":
        if self.metadata.validation_status == "failed" and self.worldspec is not None:
            raise ValueError("failed generation result must not include worldspec")
        if self.metadata.validation_status == "passed" and self.worldspec is None:
            raise ValueError("passed generation result must include worldspec")
        if self.metadata.diagnostics_count != len(self.diagnostics):
            raise ValueError("diagnostics_count must match diagnostics length")
        return self


class PlanImportResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    import_id: str = Field(min_length=1)
    validation_status: Literal["passed", "failed"]
    accepted_plan: Optional[GenerationPlan] = None
    source: Optional[PlanImportSource] = None
    diagnostics: List[GenerationDiagnostic] = Field(default_factory=list)

    @model_validator(mode="after")
    def _payload_matches_status(self) -> "PlanImportResult":
        if self.validation_status == "passed":
            if self.accepted_plan is None or self.source is None:
                raise ValueError("passed import result requires accepted_plan and source")
            if self.diagnostics:
                raise ValueError("passed import result must not include diagnostics")
        if self.validation_status == "failed":
            if self.accepted_plan is not None or self.source is not None:
                raise ValueError("failed import result must not include accepted plan or source")
            if not self.diagnostics:
                raise ValueError("failed import result requires diagnostics")
        return self


class GenerationPreviewMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    generation_id: str = Field(min_length=1)
    request_id: str = Field(min_length=1)
    source_kind: GenerationPreviewSourceKind
    template_id: Optional[str] = Field(default=None, min_length=1)
    template_version: Optional[str] = Field(default=None, min_length=1)
    plan_id: Optional[str] = Field(default=None, min_length=1)
    plan_version: Optional[str] = Field(default=None, min_length=1)
    seed_digest: str = Field(min_length=1)
    validation_status: Literal["passed", "failed"]
    diagnostics_count: int = Field(default=0, ge=0)
    preview_summary: Dict[str, Any] = Field(default_factory=dict)
    import_source: Optional[Dict[str, Any]] = None


class GenerationPreviewResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    source_kind: GenerationPreviewSourceKind
    validation_status: Literal["passed", "failed"]
    metadata: GenerationPreviewMetadata
    diagnostics: List[GenerationDiagnostic] = Field(default_factory=list)
    worldspec_preview: Optional[WorldSpec] = None

    @model_validator(mode="after")
    def _preview_matches_status(self) -> "GenerationPreviewResponse":
        if self.validation_status == "passed" and self.worldspec_preview is None:
            raise ValueError("passed preview requires worldspec_preview")
        if self.validation_status == "failed" and self.worldspec_preview is not None:
            raise ValueError("failed preview must not include worldspec_preview")
        if self.metadata.validation_status != self.validation_status:
            raise ValueError("preview metadata validation_status must match response")
        if self.metadata.diagnostics_count != len(self.diagnostics):
            raise ValueError("diagnostics_count must match diagnostics length")
        return self


class GenerationLineage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    lineage_id: str = Field(min_length=1)
    source_request_id: str = Field(min_length=1)
    parent_generation_id: Optional[str] = Field(default=None, min_length=1)
    regenerated_generation_id: str = Field(min_length=1)
    reason: Optional[str] = Field(default=None, min_length=1)
    changed_fields: List[str] = Field(default_factory=list)


class RuntimeReadinessRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    worldspec: Dict[str, Any]
    source_label: Optional[str] = Field(default=None, min_length=1)


class RuntimeReadinessResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    validation_status: Literal["passed", "failed"]
    loader_passed: bool
    runtime_context_passed: bool
    does_not_mutate_runtime: bool = True
    runtime_context_summary: Optional[Dict[str, Any]] = None
    diagnostics: List[GenerationDiagnostic] = Field(default_factory=list)


class GenerationCoreReadinessRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    worldspec: Optional[Dict[str, Any]] = None
    preview_request: Optional[GenerationPreviewRequest] = None
    source_label: Optional[str] = Field(default=None, min_length=1)
    event_limit: int = Field(default=20, ge=1, le=200)

    @model_validator(mode="after")
    def _exactly_one_candidate_source(self) -> "GenerationCoreReadinessRequest":
        source_count = sum(
            1
            for value in (self.worldspec, self.preview_request)
            if value is not None
        )
        if source_count != 1:
            raise PydanticCustomError(
                "invalid_core_readiness_source",
                "core readiness requires exactly one of worldspec or preview_request",
            )
        return self


class IsolatedRuntimeStepEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tick_id: int
    world_time_seconds: int
    step_seconds: int
    updated_at: Optional[str] = None


class AgentLoopProbeEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    perception: Dict[str, Any]
    intent: Dict[str, Any]
    result: Dict[str, Any]


class GenerationCoreReadinessResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    validation_status: Literal["passed", "failed"]
    preview: Optional[GenerationPreviewResponse] = None
    runtime_readiness: RuntimeReadinessResult
    isolated_runtime_step: Optional[IsolatedRuntimeStepEvidence] = None
    isolated_events: List[Dict[str, Any]] = Field(default_factory=list)
    agent_loop_probe: Optional[AgentLoopProbeEvidence] = None
    does_not_mutate_app_runtime: bool = True
    diagnostics: List[GenerationDiagnostic] = Field(default_factory=list)


class GenerationRegenerationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    base_preview_request: GenerationPreviewRequest
    parent_generation_id: Optional[str] = Field(default=None, min_length=1)
    reason: Optional[str] = Field(default=None, min_length=1)
    seed_material: Any = None
    constraints: Dict[str, Any] = Field(default_factory=dict)


class GenerationRegenerationResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    validation_status: Literal["passed", "failed"]
    lineage: GenerationLineage
    preview: GenerationPreviewResponse
    runtime_readiness: RuntimeReadinessResult
    diagnostics: List[GenerationDiagnostic] = Field(default_factory=list)


WorldviewGenerationMode = Literal[
    "provider_backed",
    "deterministic_fallback",
    "safe_mock",
    "not_configured",
    "blocked",
]
WorldviewCreationMode = Literal[
    "llm_backed_generation",
    "deterministic_generic_fallback",
    "safe_mock_non_live",
    "provider_not_configured",
    "blocked",
]
WorldviewGenerationStatus = Literal[
    "generated",
    "fallback",
    "not_configured",
    "blocked",
    "failed",
    "redaction_failure",
]


class WorldviewGenerationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    worldview_premise: str = Field(min_length=1, max_length=4000)
    allow_deterministic_fallback: bool = True
    public_constraints: Dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _reject_private_prompt_markers(self) -> "WorldviewGenerationRequest":
        forbidden_values = _private_worldview_markers(self.worldview_premise)
        forbidden_values.extend(_private_mapping_markers(self.public_constraints))
        if forbidden_values:
            raise PydanticCustomError(
                "private_worldview_input",
                "worldview generation request contains private or unsupported fields",
            )
        return self


class PublicGeneratedWorldModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title_label: str = Field(min_length=1)
    premise_summary: str = Field(min_length=1)
    world_parameters_outline: Dict[str, Any] = Field(default_factory=dict)
    locations_outline: List[Dict[str, Any]] = Field(default_factory=list)
    entities_outline: List[Dict[str, Any]] = Field(default_factory=list)
    agents_outline: List[Dict[str, Any]] = Field(default_factory=list)
    items_outline: List[Dict[str, Any]] = Field(default_factory=list)
    environment_outline: Dict[str, Any] = Field(default_factory=dict)
    rules_outline: List[Dict[str, Any]] = Field(default_factory=list)
    boundary_conditions: List[str] = Field(default_factory=list)
    runtime_readiness_inputs: Dict[str, Any] = Field(default_factory=dict)
    visualization_refs: Dict[str, Any] = Field(default_factory=dict)


class WorldviewGenerationRedaction(BaseModel):
    model_config = ConfigDict(extra="forbid")

    raw_prompt_included: bool = False
    raw_provider_request_included: bool = False
    raw_provider_response_included: bool = False
    provider_trace_included: bool = False
    hidden_context_included: bool = False
    private_agent_memory_included: bool = False
    raw_thought_included: bool = False
    secrets_included: bool = False
    validation_client_content_included: bool = False
    concrete_fixture_included: bool = False


class WorldviewGenerationValidationMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    premise_specific: Literal["true", "false", "unknown"]
    system_digestible: bool
    runtime_ready: Literal["true", "false", "blocked"]
    deterministic_generic_response: bool
    deterministic_generic_fallback_detected: bool
    redaction_status: Literal["passed", "failed"]
    provider_generation_status: Literal[
        "provider_backed",
        "deterministic_fallback",
        "safe_mock_non_live",
        "not_configured",
        "blocked",
        "failed",
    ]
    diagnostics_count: int = Field(default=0, ge=0)


class PublicWorldCreationSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")

    premise_specific: Literal["true", "false", "unknown"]
    system_digestible: bool
    redacted: bool
    runtime_ready: Literal["true", "false", "blocked"]
    distinct_from_deterministic_generic_response: bool
    creation_mode: WorldviewCreationMode
    llm_backed: bool
    provider_backed: bool
    deterministic_generic_fallback_detected: bool
    public_initial_state_refs: Dict[str, Any] = Field(default_factory=dict)
    visualization_refs: Dict[str, Any] = Field(default_factory=dict)


class WorldviewGenerationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.2"
    world_id: str = Field(min_length=1)
    generation_id: str = Field(min_length=1)
    generation_status: WorldviewGenerationStatus
    generation_mode: WorldviewGenerationMode
    creation_mode: WorldviewCreationMode
    llm_backed: bool
    provider_backed: bool
    deterministic_generic_fallback_detected: bool
    provider_class: str = Field(min_length=1)
    model_label: str = Field(min_length=1)
    worldengine_owned_generation: bool = True
    premise_digest: str = Field(min_length=1)
    public_world_model: PublicGeneratedWorldModel
    world_creation_summary: PublicWorldCreationSummary
    validation_metadata: WorldviewGenerationValidationMetadata
    redaction: WorldviewGenerationRedaction = Field(default_factory=WorldviewGenerationRedaction)
    warnings: List[str] = Field(default_factory=list)
    blockers: List[str] = Field(default_factory=list)
    diagnostics: List[GenerationDiagnostic] = Field(default_factory=list)

    @model_validator(mode="after")
    def _metadata_matches_response(self) -> "WorldviewGenerationResponse":
        if self.validation_metadata.diagnostics_count != len(self.diagnostics):
            raise ValueError("diagnostics_count must match diagnostics length")
        if self.world_creation_summary.creation_mode != self.creation_mode:
            raise ValueError("summary creation_mode must match response")
        if self.world_creation_summary.llm_backed != self.llm_backed:
            raise ValueError("summary llm_backed must match response")
        if self.world_creation_summary.provider_backed != self.provider_backed:
            raise ValueError("summary provider_backed must match response")
        return self


WorldParameterValueType = Literal["int", "float", "bool", "string", "json"]
WorldParameterVisibility = Literal["public", "internal_public"]
WorldRuleKind = Literal[
    "environment_trend",
    "resource_drift",
    "agent_public_pressure",
    "boundary",
    "constraint",
]
WorldRuleOperation = Literal["add", "set", "remove"]


class WorldParameterRef(BaseModel):
    model_config = ConfigDict(extra="forbid")

    parameter_id: str = Field(min_length=1)
    path: str = Field(min_length=1)


class WorldParameterDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    parameter_id: str = Field(min_length=1)
    path: str = Field(min_length=1)
    value_type: WorldParameterValueType
    initial_value: Any
    visibility: WorldParameterVisibility = "public"
    description: str = Field(min_length=1)
    constraints: Dict[str, Any] = Field(default_factory=dict)
    source: Dict[str, Any] = Field(default_factory=dict)
    rule_refs: List[str] = Field(default_factory=list)


class WorldRuleEffect(BaseModel):
    model_config = ConfigDict(extra="forbid")

    op: WorldRuleOperation
    parameter_ref: str = Field(min_length=1)
    value_expression: Dict[str, Any] = Field(default_factory=dict)


class WorldEvolutionRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    rule_id: str = Field(min_length=1)
    rule_kind: WorldRuleKind
    trigger: Dict[str, Any] = Field(default_factory=dict)
    conditions: List[Dict[str, Any]] = Field(default_factory=list)
    effects: List[WorldRuleEffect] = Field(default_factory=list)
    target_parameter_refs: List[str] = Field(default_factory=list)
    allowed_ops: List[WorldRuleOperation] = Field(default_factory=list)
    priority: int = 0
    cooldown: Dict[str, Any] = Field(default_factory=dict)
    evidence: Dict[str, Any] = Field(default_factory=dict)


class WorldConstraint(BaseModel):
    model_config = ConfigDict(extra="forbid")

    constraint_id: str = Field(min_length=1)
    scope: Literal["parameter", "rule", "set"]
    target_refs: List[str] = Field(default_factory=list)
    rule_refs: List[str] = Field(default_factory=list)
    expression: Dict[str, Any] = Field(default_factory=dict)
    public_explanation: str = Field(min_length=1)


class WorldBoundary(BaseModel):
    model_config = ConfigDict(extra="forbid")

    boundary_id: str = Field(min_length=1)
    category: str = Field(min_length=1)
    target_refs: List[str] = Field(default_factory=list)
    public_explanation: str = Field(min_length=1)


class GeneratedRuleParameterSet(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.3"
    world_id: str = Field(min_length=1)
    generation_id: str = Field(min_length=1)
    premise_digest: str = Field(min_length=1)
    parameters: List[WorldParameterDefinition] = Field(default_factory=list)
    rules: List[WorldEvolutionRule] = Field(default_factory=list)
    constraints: List[WorldConstraint] = Field(default_factory=list)
    boundaries: List[WorldBoundary] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class RuleParameterDiagnostic(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str = Field(min_length=1)
    severity: Literal["error", "warning"] = "error"
    message: str = Field(min_length=1)
    path: Optional[str] = None


class RuleParameterValidationResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    validation_status: Literal["accepted", "rejected"]
    diagnostics: List[RuleParameterDiagnostic] = Field(default_factory=list)
    accepted_parameter_count: int = Field(default=0, ge=0)
    accepted_rule_count: int = Field(default=0, ge=0)
    rejected_parameter_count: int = Field(default=0, ge=0)
    rejected_rule_count: int = Field(default=0, ge=0)
    redaction_status: Literal["passed", "failed"] = "passed"
    compatibility_summary: Dict[str, Any] = Field(default_factory=dict)


class PublicWorldRuleSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.3"
    world_id: str = Field(min_length=1)
    generation_id: str = Field(min_length=1)
    premise_digest: str = Field(min_length=1)
    validation_status: Literal["accepted", "rejected"]
    parameter_paths: List[str] = Field(default_factory=list)
    rule_ids: List[str] = Field(default_factory=list)
    boundary_ids: List[str] = Field(default_factory=list)
    diagnostics_count: int = Field(default=0, ge=0)
    redaction_status: Literal["passed", "failed"] = "passed"


WorldviewFidelityStatus = Literal["pass", "fail", "blocked", "not_run"]
WorldviewContradictionCategory = Literal[
    "missing_premise",
    "generic_fallback",
    "runtime_contradiction",
    "rule_contradiction",
    "redaction",
    "evidence_gap",
    "checker_gap",
]


class WorldviewContradiction(BaseModel):
    model_config = ConfigDict(extra="forbid")

    category: WorldviewContradictionCategory
    severity: Literal["critical", "warning"] = "critical"
    path: Optional[str] = None
    public_summary: str = Field(min_length=1)


class ImmediateWorldviewFidelityArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.4"
    world_id: str = Field(min_length=1)
    generation_id: str = Field(min_length=1)
    premise_digest: str = Field(min_length=1)
    status: WorldviewFidelityStatus
    evaluated_indicators: List[str] = Field(default_factory=list)
    covered_indicators: List[str] = Field(default_factory=list)
    missing_indicators: List[str] = Field(default_factory=list)
    creation_mode: WorldviewCreationMode
    deterministic_generic_fallback_detected: bool
    system_digestible: bool
    redaction_status: Literal["passed", "failed"] = "passed"
    contradictions: List[WorldviewContradiction] = Field(default_factory=list)
    evidence_refs: Dict[str, Any] = Field(default_factory=dict)


class BoundedRunWorldviewFidelityArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.4"
    world_id: str = Field(min_length=1)
    generation_id: str = Field(min_length=1)
    premise_digest: str = Field(min_length=1)
    status: WorldviewFidelityStatus
    evaluated_indicators: List[str] = Field(default_factory=list)
    covered_indicators: List[str] = Field(default_factory=list)
    missing_indicators: List[str] = Field(default_factory=list)
    runtime_summary_present: bool = False
    redaction_status: Literal["passed", "failed"] = "passed"
    contradictions: List[WorldviewContradiction] = Field(default_factory=list)
    evidence_refs: Dict[str, Any] = Field(default_factory=dict)


class WorldviewFidelityScorecard(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.4"
    world_id: str = Field(min_length=1)
    generation_id: str = Field(min_length=1)
    premise_digest: str = Field(min_length=1)
    final_status: WorldviewFidelityStatus
    verdict_source: Literal["deterministic_worldview_fidelity_helper"] = (
        "deterministic_worldview_fidelity_helper"
    )
    score_items: Dict[str, WorldviewFidelityStatus] = Field(default_factory=dict)
    critical_failures: List[WorldviewContradiction] = Field(default_factory=list)
    unverified_items: List[str] = Field(default_factory=list)
    redaction_status: Literal["passed", "failed"] = "passed"
    immediate: ImmediateWorldviewFidelityArtifact
    bounded_run: BoundedRunWorldviewFidelityArtifact


_PRIVATE_WORLDVIEW_MARKERS = (
    "api_key",
    "api key",
    "apikey",
    "authorization",
    "bearer",
    "chain-of-thought",
    "credential",
    "hidden context",
    "hidden_context",
    "private memory",
    "private goal",
    "private evaluator",
    "private_evaluator",
    "private evaluator data",
    "private_evaluator_data",
    "evaluator data",
    "evaluator_data",
    "private_prompt",
    "provider_secret",
    "provider trace",
    "provider_trace",
    "raw prompt",
    "raw_prompt",
    "raw request",
    "raw_request",
    "raw provider request",
    "raw_provider_request",
    "raw response",
    "raw_response",
    "raw provider response",
    "raw_provider_response",
    "raw thought",
    "raw_thought",
    "secret",
    "self_state",
    "sk-live-",
    "sk-test-",
    "token",
    "validation client generated",
    "validation_client_generated",
)


def _private_worldview_markers(value: str) -> List[str]:
    lowered = value.lower()
    return [marker for marker in _PRIVATE_WORLDVIEW_MARKERS if marker in lowered]


def _private_mapping_markers(value: Any) -> List[str]:
    if isinstance(value, dict):
        markers: List[str] = []
        for key, item in value.items():
            markers.extend(_private_worldview_markers(str(key)))
            markers.extend(_private_mapping_markers(item))
        return markers
    if isinstance(value, list):
        markers = []
        for item in value:
            markers.extend(_private_mapping_markers(item))
        return markers
    if isinstance(value, str):
        return _private_worldview_markers(value)
    return []
