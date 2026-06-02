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
