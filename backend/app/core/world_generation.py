import hashlib
import json
import math
from dataclasses import asdict
from copy import deepcopy
from typing import Any, Dict, List, Optional, Set

from app.core.runtime_context import build_runtime_context, summarize_runtime_context
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.core.worldspec_loader import load_worldspec
from app.agent.action_adapter import ActionResultAdapter
from app.agent.loop_service import AgentLoopService
from app.agent.perception import PerceptionBuilder
from app.schemas.agent_loop import LoopStepRequest
from app.schemas.world_cell import WorldCell, WorldSpec
from app.schemas.world_generation import (
    AgentLoopProbeEvidence,
    GenerationDiagnostic,
    GenerationCoreReadinessRequest,
    GenerationCoreReadinessResult,
    GenerationLineage,
    GenerationMetadata,
    GenerationPlan,
    GenerationPreviewMetadata,
    GenerationPreviewRequest,
    GenerationPreviewResponse,
    GenerationRegenerationRequest,
    GenerationRegenerationResult,
    IsolatedRuntimeStepEvidence,
    PlanCell,
    PlanGenerationRequest,
    PlanImportRequest,
    PlanImportResult,
    RuntimeReadinessRequest,
    RuntimeReadinessResult,
    TemplateCell,
    TemplateGenerationRequest,
    TemplateGenerationResult,
    WorldTemplate,
)
from app.world.dry_run import ParamDryRunValidator
from app.world.state import WorldState
from app.world.validation import ParamRegistry, ParamValidator
from app.world.validation.policy import WorldValidationPolicy


SUPPORTED_TEMPLATE_VERSIONS = {"1"}
SUPPORTED_PLAN_VERSIONS = {"1"}
SENSITIVE_PREVIEW_METADATA_KEYS = {
    "api_key",
    "credential",
    "credentials",
    "oracle",
    "private_prompt",
    "prompt",
    "provider_trace",
    "provider_traces",
    "raw_prompt",
    "secret",
    "secrets",
    "token",
    "validation_oracle",
}
SAFE_PREVIEW_METADATA_USAGE_KEYS = {
    "cached_tokens",
    "completion_tokens",
    "prompt_tokens",
    "total_tokens",
    "token_count",
    "token_usage",
}
PREVIEW_SUMMARY_TEXT_LIMIT = 120


def validate_template(
    template: WorldTemplate, request_constraints: Optional[Dict[str, Any]] = None
) -> List[GenerationDiagnostic]:
    diagnostics: List[GenerationDiagnostic] = []
    seen_cell_ids: Set[str] = set()
    seen_entity_refs: Set[str] = set()
    _append_json_compatibility_diagnostic(
        diagnostics,
        "unsupported_template_metadata",
        "template metadata must be JSON-compatible",
        "/metadata",
        template.metadata,
    )
    _append_json_compatibility_diagnostic(
        diagnostics,
        "unsupported_template_constraints",
        "template constraints must be JSON-compatible",
        "/constraints",
        template.constraints,
    )
    if request_constraints is not None:
        _append_json_compatibility_diagnostic(
            diagnostics,
            "unsupported_generation_constraints",
            "generation constraints must be JSON-compatible",
            "/constraints",
            request_constraints,
        )
    constraints = _merge_constraints(template.constraints, request_constraints or {})
    allowed_entity_kinds = _allowed_entity_kinds(constraints)
    max_child_cells = _optional_int_constraint(constraints, "max_child_cells")
    min_child_cells = _optional_int_constraint(constraints, "min_child_cells")

    if template.version not in SUPPORTED_TEMPLATE_VERSIONS:
        diagnostics.append(
            _diagnostic(
                "unsupported_template_version",
                f"unsupported template version: {template.version}",
                "/version",
                {"version": template.version},
            )
        )

    def visit(cell: TemplateCell, path: str) -> None:
        _append_json_compatibility_diagnostic(
            diagnostics,
            "unsupported_template_metadata",
            "template cell metadata must be JSON-compatible",
            f"{path}/metadata",
            cell.metadata,
        )
        if cell.id in seen_cell_ids:
            diagnostics.append(
                _diagnostic(
                    "duplicate_cell_id",
                    f"duplicate template cell id: {cell.id}",
                    f"{path}/id",
                    {"cell_id": cell.id},
                )
            )
        else:
            seen_cell_ids.add(cell.id)

        child_count = len(cell.child_cells)
        if max_child_cells is not None and child_count > max_child_cells:
            diagnostics.append(
                _diagnostic(
                    "invalid_template_bounds",
                    f"child cell count exceeds max_child_cells: {child_count} > {max_child_cells}",
                    f"{path}/child_cells",
                    {"max_child_cells": max_child_cells, "actual": child_count},
                )
            )
        if min_child_cells is not None and child_count < min_child_cells:
            diagnostics.append(
                _diagnostic(
                    "invalid_template_bounds",
                    f"child cell count is below min_child_cells: {child_count} < {min_child_cells}",
                    f"{path}/child_cells",
                    {"min_child_cells": min_child_cells, "actual": child_count},
                )
            )

        for index, entity_ref in enumerate(cell.entity_refs):
            ref_key = f"{entity_ref.kind}:{entity_ref.id}"
            ref_path = f"{path}/entity_refs/{index}"
            if ref_key in seen_entity_refs:
                diagnostics.append(
                    _diagnostic(
                        "duplicate_entity_ref",
                        f"duplicate entity reference: {ref_key}",
                        f"{ref_path}/id",
                        {"entity_ref": ref_key},
                    )
                )
            else:
                seen_entity_refs.add(ref_key)
            if allowed_entity_kinds is not None and entity_ref.kind not in allowed_entity_kinds:
                diagnostics.append(
                    _diagnostic(
                        "entity_kind_not_allowed",
                        f"entity kind is not allowed: {entity_ref.kind}",
                        f"{ref_path}/kind",
                        {"kind": entity_ref.kind},
                    )
                )

        for index, child in enumerate(cell.child_cells):
            visit(child, f"{path}/child_cells/{index}")

    visit(template.root, "/root")
    return diagnostics


def generate_worldspec_from_template(
    request: TemplateGenerationRequest,
) -> TemplateGenerationResult:
    template = request.template.model_copy(deep=True)
    diagnostics = validate_template(template, request.constraints)
    seed_digest = ""
    seed_payload = {
        "request_id": request.request_id,
        "template": template.model_dump(),
        "request_constraints": request.constraints,
        "seed_material": request.seed_material,
    }
    try:
        seed_digest = _seed_digest(seed_payload)
    except (TypeError, ValueError):
        if not _is_json_compatible(request.seed_material):
            diagnostics.append(
                _diagnostic(
                    "unsupported_seed_material",
                    "seed material must be JSON-compatible",
                    "/seed_material",
                    {"type": type(request.seed_material).__name__},
                )
            )
        seed_digest = _seed_digest(
            {
                "request_id": request.request_id,
                "template_id": template.id,
                "template_version": template.version,
                "request_constraints": _json_compatible_or_none(request.constraints),
                "seed_material": _json_compatible_or_none(request.seed_material),
            }
        )
    generation_id = f"generation-{seed_digest[:16]}"
    metadata_base = {
        "generation_id": generation_id,
        "request_id": request.request_id,
        "template_id": template.id,
        "template_version": template.version,
        "seed_digest": seed_digest,
        "diagnostics_count": len(diagnostics),
    }

    if diagnostics:
        return TemplateGenerationResult(
            metadata=GenerationMetadata(
                **metadata_base,
                validation_status="failed",
            ),
            diagnostics=diagnostics,
        )

    worldspec = WorldSpec(
        id=f"worldspec-{seed_digest[:16]}",
        label=template.root.label,
        root=_world_cell_from_template(template.root),
        metadata={
            "generation_id": generation_id,
            "template_id": template.id,
            "template_version": template.version,
            "seed_digest": seed_digest,
            **deepcopy(template.metadata),
        },
    )
    return TemplateGenerationResult(
        worldspec=worldspec,
        metadata=GenerationMetadata(
            **metadata_base,
            validation_status="passed",
        ),
    )


def validate_generation_plan(
    plan: GenerationPlan, request_constraints: Optional[Dict[str, Any]] = None
) -> List[GenerationDiagnostic]:
    diagnostics: List[GenerationDiagnostic] = []
    seen_cell_ids: Set[str] = set()
    seen_entity_refs: Set[str] = set()
    if request_constraints is not None:
        _append_json_compatibility_diagnostic(
            diagnostics,
            "unsupported_generation_constraints",
            "generation constraints must be JSON-compatible",
            "/constraints",
            request_constraints,
        )
    constraints = _merge_constraints(plan.constraints, request_constraints or {})
    allowed_entity_kinds = _allowed_entity_kinds(constraints)
    max_child_cells = _optional_int_constraint(constraints, "max_child_cells")
    min_child_cells = _optional_int_constraint(constraints, "min_child_cells")

    if plan.version not in SUPPORTED_PLAN_VERSIONS:
        diagnostics.append(
            _diagnostic(
                "unsupported_plan_version",
                f"unsupported generation plan version: {plan.version}",
                "/version",
                {"version": plan.version},
            )
        )
    try:
        _canonical_json_value(plan.metadata)
    except (TypeError, ValueError):
        diagnostics.append(
            _diagnostic(
                "unsupported_plan_metadata",
                "plan metadata must be JSON-compatible",
                "/metadata",
                {"type": type(plan.metadata).__name__},
            )
        )
    _append_json_compatibility_diagnostic(
        diagnostics,
        "unsupported_plan_constraints",
        "plan constraints must be JSON-compatible",
        "/constraints",
        plan.constraints,
    )

    def visit(cell: PlanCell, path: str) -> None:
        if cell.id in seen_cell_ids:
            diagnostics.append(
                _diagnostic(
                    "duplicate_cell_id",
                    f"duplicate plan cell id: {cell.id}",
                    f"{path}/id",
                    {"cell_id": cell.id},
                )
            )
        else:
            seen_cell_ids.add(cell.id)
        try:
            _canonical_json_value(cell.metadata)
        except (TypeError, ValueError):
            diagnostics.append(
                _diagnostic(
                    "unsupported_plan_metadata",
                    "plan cell metadata must be JSON-compatible",
                    f"{path}/metadata",
                    {"type": type(cell.metadata).__name__},
                )
            )

        child_count = len(cell.child_cells)
        if max_child_cells is not None and child_count > max_child_cells:
            diagnostics.append(
                _diagnostic(
                    "invalid_plan_bounds",
                    f"child cell count exceeds max_child_cells: {child_count} > {max_child_cells}",
                    f"{path}/child_cells",
                    {"max_child_cells": max_child_cells, "actual": child_count},
                )
            )
        if min_child_cells is not None and child_count < min_child_cells:
            diagnostics.append(
                _diagnostic(
                    "invalid_plan_bounds",
                    f"child cell count is below min_child_cells: {child_count} < {min_child_cells}",
                    f"{path}/child_cells",
                    {"min_child_cells": min_child_cells, "actual": child_count},
                )
            )

        for index, entity_ref in enumerate(cell.entity_refs):
            ref_key = f"{entity_ref.kind}:{entity_ref.id}"
            ref_path = f"{path}/entity_refs/{index}"
            if ref_key in seen_entity_refs:
                diagnostics.append(
                    _diagnostic(
                        "duplicate_entity_ref",
                        f"duplicate entity reference: {ref_key}",
                        f"{ref_path}/id",
                        {"entity_ref": ref_key},
                    )
                )
            else:
                seen_entity_refs.add(ref_key)
            if allowed_entity_kinds is not None and entity_ref.kind not in allowed_entity_kinds:
                diagnostics.append(
                    _diagnostic(
                        "entity_kind_not_allowed",
                        f"entity kind is not allowed: {entity_ref.kind}",
                        f"{ref_path}/kind",
                        {"kind": entity_ref.kind},
                    )
                )

        for index, child in enumerate(cell.child_cells):
            visit(child, f"{path}/child_cells/{index}")

    visit(plan.root, "/root")
    return diagnostics


def generate_worldspec_from_plan(
    request: PlanGenerationRequest,
) -> TemplateGenerationResult:
    plan = request.plan.model_copy(deep=True)
    diagnostics = validate_generation_plan(plan, request.constraints)
    seed_digest = ""
    seed_payload = {
        "request_id": request.request_id,
        "plan": plan.model_dump(),
        "request_constraints": request.constraints,
        "seed_material": request.seed_material,
    }
    try:
        seed_digest = _seed_digest(seed_payload)
    except (TypeError, ValueError):
        if not _is_json_compatible(request.seed_material):
            diagnostics.append(
                _diagnostic(
                    "unsupported_seed_material",
                    "seed material must be JSON-compatible",
                    "/seed_material",
                    {"type": type(request.seed_material).__name__},
                )
            )
        seed_digest = _seed_digest(
            {
                "request_id": request.request_id,
                "plan_id": plan.id,
                "plan_version": plan.version,
                "request_constraints": _json_compatible_or_none(request.constraints),
                "seed_material": _json_compatible_or_none(request.seed_material),
            }
        )
    generation_id = f"generation-{seed_digest[:16]}"
    metadata_base = {
        "generation_id": generation_id,
        "request_id": request.request_id,
        "source_kind": "plan",
        "plan_id": plan.id,
        "plan_version": plan.version,
        "seed_digest": seed_digest,
        "diagnostics_count": len(diagnostics),
    }

    if diagnostics:
        return TemplateGenerationResult(
            metadata=GenerationMetadata(
                **metadata_base,
                validation_status="failed",
            ),
            diagnostics=diagnostics,
        )

    worldspec = WorldSpec(
        id=f"worldspec-{seed_digest[:16]}",
        label=plan.root.label,
        root=_world_cell_from_plan(plan.root),
        metadata={
            "generation_id": generation_id,
            "source_kind": "plan",
            "plan_id": plan.id,
            "plan_version": plan.version,
            "seed_digest": seed_digest,
            **deepcopy(plan.metadata),
        },
    )
    return TemplateGenerationResult(
        worldspec=worldspec,
        metadata=GenerationMetadata(
            **metadata_base,
            validation_status="passed",
        ),
    )


def validate_plan_import(request: PlanImportRequest) -> List[GenerationDiagnostic]:
    diagnostics: List[GenerationDiagnostic] = []

    if not request.source.redacted:
        diagnostics.append(
            _diagnostic(
                "unredacted_import_source",
                "import source provenance must be redacted",
                "/source/redacted",
                {"redacted": request.source.redacted},
            )
        )
    try:
        _canonical_json_value(request.source.metadata)
    except (TypeError, ValueError):
        diagnostics.append(
            _diagnostic(
                "unsupported_import_provenance",
                "import source metadata must be JSON-compatible",
                "/source/metadata",
                {"type": type(request.source.metadata).__name__},
            )
        )
    diagnostics.extend(
        _sensitive_metadata_diagnostics(
            request.source.metadata,
            "/source/metadata",
            "sensitive_import_provenance",
            "import source metadata must not contain prompts, provider traces, secrets, or validation oracles",
        )
    )
    try:
        _canonical_json_value(request.metadata)
    except (TypeError, ValueError):
        diagnostics.append(
            _diagnostic(
                "unsupported_import_metadata",
                "import metadata must be JSON-compatible",
                "/metadata",
                {"type": type(request.metadata).__name__},
            )
        )

    diagnostics.extend(validate_generation_plan(request.plan))
    return diagnostics


def import_generation_plan(request: PlanImportRequest) -> PlanImportResult:
    diagnostics = validate_plan_import(request)
    if diagnostics:
        return PlanImportResult(
            import_id=request.import_id,
            validation_status="failed",
            diagnostics=diagnostics,
        )

    return PlanImportResult(
        import_id=request.import_id,
        validation_status="passed",
        accepted_plan=request.plan.model_copy(deep=True),
        source=request.source.model_copy(deep=True),
    )


def preview_generation(request: GenerationPreviewRequest) -> GenerationPreviewResponse:
    if request.source_kind == "template" and request.template_request is not None:
        result = generate_worldspec_from_template(request.template_request)
        return _preview_response_from_generation_result(request, result)

    if request.source_kind == "plan" and request.plan_request is not None:
        result = generate_worldspec_from_plan(request.plan_request)
        return _preview_response_from_generation_result(request, result)

    if request.source_kind == "imported_plan" and request.import_request is not None:
        import_result = import_generation_plan(request.import_request)
        if import_result.validation_status == "failed":
            return _failed_import_preview_response(request, import_result.diagnostics)

        plan_request = PlanGenerationRequest(
            request_id=request.request_id,
            plan=import_result.accepted_plan,
            seed_material=request.seed_material,
            constraints=request.constraints,
        )
        result = generate_worldspec_from_plan(plan_request)
        return _preview_response_from_generation_result(
            request,
            result,
            import_source=_redacted_import_source(import_result.source)
            if result.metadata.validation_status == "passed"
            else None,
        )

    raise ValueError("unsupported generation preview source")


def regenerate_world(request: GenerationRegenerationRequest) -> GenerationRegenerationResult:
    regenerated_request, changed_fields = _regenerated_preview_request(request)
    preview = preview_generation(regenerated_request)
    lineage = _generation_lineage(request, preview, changed_fields)

    if preview.worldspec_preview is None:
        readiness = RuntimeReadinessResult(
            request_id=request.request_id,
            validation_status="failed",
            loader_passed=False,
            runtime_context_passed=False,
            diagnostics=[
                _diagnostic(
                    "preview_failed",
                    "runtime readiness was skipped because regeneration preview failed",
                    "/preview",
                    {"preview_generation_id": preview.metadata.generation_id},
                )
            ],
        )
    else:
        readiness = check_runtime_readiness(
            RuntimeReadinessRequest(
                request_id=request.request_id,
                worldspec=preview.worldspec_preview.model_dump(mode="json"),
                source_label=preview.metadata.generation_id,
            )
        )

    validation_status = (
        "passed"
        if preview.validation_status == "passed"
        and readiness.validation_status == "passed"
        else "failed"
    )
    diagnostics = deepcopy(preview.diagnostics) + deepcopy(readiness.diagnostics)
    return GenerationRegenerationResult(
        request_id=request.request_id,
        validation_status=validation_status,
        lineage=lineage,
        preview=preview,
        runtime_readiness=readiness,
        diagnostics=diagnostics,
    )


def check_runtime_readiness(request: RuntimeReadinessRequest) -> RuntimeReadinessResult:
    loader_result = load_worldspec(
        deepcopy(request.worldspec),
        source_label=request.source_label or request.request_id,
    )
    if not loader_result.success or loader_result.loaded is None:
        return RuntimeReadinessResult(
            request_id=request.request_id,
            validation_status="failed",
            loader_passed=False,
            runtime_context_passed=False,
            diagnostics=[
                _diagnostic(
                    error.code,
                    error.message,
                    error.path,
                    {
                        "source_type": error.source_type,
                        "source_label": error.source_label,
                    },
                )
                for error in loader_result.errors
            ],
        )

    context_result = build_runtime_context(loader_result.loaded)
    if not context_result.success or context_result.context is None:
        return RuntimeReadinessResult(
            request_id=request.request_id,
            validation_status="failed",
            loader_passed=True,
            runtime_context_passed=False,
            diagnostics=[
                _diagnostic(
                    error.code,
                    error.message,
                    error.path,
                    {
                        "source_type": error.source_type,
                        "source_label": error.source_label,
                    },
                )
                for error in context_result.errors
            ],
        )

    summary = summarize_runtime_context(context_result.context)
    return RuntimeReadinessResult(
        request_id=request.request_id,
        validation_status="passed",
        loader_passed=True,
        runtime_context_passed=True,
        runtime_context_summary=asdict(summary),
    )


def check_core_readiness(
    request: GenerationCoreReadinessRequest,
) -> GenerationCoreReadinessResult:
    preview = None
    worldspec_payload: Optional[Dict[str, Any]] = None
    source_label = _public_core_readiness_source_label(
        request.source_label or request.request_id
    )

    if request.preview_request is not None:
        preview = preview_generation(request.preview_request)
        if preview.validation_status == "failed" or preview.worldspec_preview is None:
            diagnostics = deepcopy(preview.diagnostics)
            diagnostics.append(
                _diagnostic(
                    "preview_failed",
                    "core readiness was skipped because generation preview failed",
                    "/preview_request",
                    {"preview_request_id": preview.request_id},
                )
            )
            return _failed_core_readiness_result(
                request,
                preview=preview,
                diagnostics=diagnostics,
            )
        worldspec_payload = preview.worldspec_preview.model_dump(mode="json")
    else:
        worldspec_payload = deepcopy(request.worldspec) if request.worldspec is not None else None

    readiness = check_runtime_readiness(
        RuntimeReadinessRequest(
            request_id=request.request_id,
            worldspec=worldspec_payload or {},
            source_label=source_label,
        )
    )
    if readiness.validation_status == "failed":
        return GenerationCoreReadinessResult(
            request_id=request.request_id,
            validation_status="failed",
            preview=preview,
            runtime_readiness=readiness,
            diagnostics=deepcopy(readiness.diagnostics),
        )

    loader_result = load_worldspec(
        deepcopy(worldspec_payload),
        source_label=source_label,
    )
    if not loader_result.success or loader_result.loaded is None:
        return _failed_core_readiness_result(
            request,
            preview=preview,
            diagnostics=[
                _diagnostic(
                    error.code,
                    error.message,
                    error.path,
                    {
                        "source_type": error.source_type,
                        "source_label": error.source_label,
                    },
                )
                for error in loader_result.errors
            ],
        )

    context_result = build_runtime_context(loader_result.loaded)
    if not context_result.success or context_result.context is None:
        return _failed_core_readiness_result(
            request,
            preview=preview,
            diagnostics=[
                _diagnostic(
                    error.code,
                    error.message,
                    error.path,
                    {
                        "source_type": error.source_type,
                        "source_label": error.source_label,
                    },
                )
                for error in context_result.errors
            ],
        )

    isolated_event_log = InMemoryEventLog()
    isolated_world_state = WorldState()
    isolated_runtime = RuntimeEngine(
        event_log=isolated_event_log,
        params_provider=isolated_world_state.get_params,
        runtime_context=context_result.context,
    )
    runtime_state = isolated_runtime.step()
    agent_loop = AgentLoopService(
        perception_builder=PerceptionBuilder(
            runtime_engine=isolated_runtime,
            event_log=isolated_event_log,
            world_state=isolated_world_state,
        ),
        action_adapter=ActionResultAdapter(
            world_state=isolated_world_state,
            event_log=isolated_event_log,
            runtime_engine=isolated_runtime,
            param_validator=ParamValidator(ParamRegistry.default()),
            param_dry_run_validator=ParamDryRunValidator(
                default_policy=WorldValidationPolicy(),
            ),
        ),
    )
    loop_response = agent_loop.step(LoopStepRequest(event_limit=request.event_limit))

    return GenerationCoreReadinessResult(
        request_id=request.request_id,
        validation_status="passed",
        preview=preview,
        runtime_readiness=readiness,
        isolated_runtime_step=IsolatedRuntimeStepEvidence(
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            step_seconds=runtime_state.step_seconds,
            updated_at=runtime_state.updated_at,
        ),
        isolated_events=[
            {
                "id": event.id,
                "tick_id": event.tick_id,
                "world_time_seconds": event.world_time_seconds,
                "type": event.type,
                "source": event.source,
            }
            for event in isolated_event_log.list_page(limit=request.event_limit).items
        ],
        agent_loop_probe=AgentLoopProbeEvidence(
            perception=loop_response.perception.model_dump(mode="json"),
            intent=loop_response.intent.model_dump(mode="json"),
            result=loop_response.result.model_dump(mode="json"),
        ),
        does_not_mutate_app_runtime=True,
        diagnostics=[],
    )


def _failed_core_readiness_result(
    request: GenerationCoreReadinessRequest,
    *,
    diagnostics: List[GenerationDiagnostic],
    preview: Optional[GenerationPreviewResponse] = None,
) -> GenerationCoreReadinessResult:
    readiness = RuntimeReadinessResult(
        request_id=request.request_id,
        validation_status="failed",
        loader_passed=False,
        runtime_context_passed=False,
        diagnostics=deepcopy(diagnostics),
    )
    return GenerationCoreReadinessResult(
        request_id=request.request_id,
        validation_status="failed",
        preview=preview,
        runtime_readiness=readiness,
        diagnostics=deepcopy(diagnostics),
    )


def _public_core_readiness_source_label(label: str) -> str:
    lowered = label.lower()
    private_markers = (
        "/",
        "\\",
        "private",
        "secret",
        "token",
        "credential",
        "repo",
    )
    if any(marker in lowered for marker in private_markers):
        return "redacted"
    return label


def _regenerated_preview_request(
    request: GenerationRegenerationRequest,
) -> tuple[GenerationPreviewRequest, List[str]]:
    base = request.base_preview_request.model_copy(deep=True)
    original_seed, original_constraints = _active_generation_overrides(base)
    seed_overridden = "seed_material" in request.model_fields_set
    constraints_overridden = "constraints" in request.model_fields_set

    base.request_id = request.request_id
    if seed_overridden:
        base.seed_material = deepcopy(request.seed_material)
    if constraints_overridden:
        base.constraints = deepcopy(request.constraints)

    if base.source_kind == "template" and base.template_request is not None:
        base.template_request.request_id = request.request_id
        if seed_overridden:
            base.template_request.seed_material = deepcopy(request.seed_material)
        if constraints_overridden:
            base.template_request.constraints = deepcopy(request.constraints)
    elif base.source_kind == "plan" and base.plan_request is not None:
        base.plan_request.request_id = request.request_id
        if seed_overridden:
            base.plan_request.seed_material = deepcopy(request.seed_material)
        if constraints_overridden:
            base.plan_request.constraints = deepcopy(request.constraints)

    changed_fields: List[str] = []
    if constraints_overridden and request.constraints != original_constraints:
        changed_fields.append("constraints")
    if seed_overridden and request.seed_material != original_seed:
        changed_fields.append("seed_material")
    return base, changed_fields


def _active_generation_overrides(request: GenerationPreviewRequest) -> tuple[Any, Dict[str, Any]]:
    if request.source_kind == "template" and request.template_request is not None:
        return request.template_request.seed_material, request.template_request.constraints
    if request.source_kind == "plan" and request.plan_request is not None:
        return request.plan_request.seed_material, request.plan_request.constraints
    return request.seed_material, request.constraints


def _generation_lineage(
    request: GenerationRegenerationRequest,
    preview: GenerationPreviewResponse,
    changed_fields: List[str],
) -> GenerationLineage:
    lineage_payload = {
        "request_id": request.request_id,
        "source_request_id": request.base_preview_request.request_id,
        "parent_generation_id": request.parent_generation_id,
        "regenerated_generation_id": preview.metadata.generation_id,
        "reason": request.reason,
        "changed_fields": changed_fields,
    }
    lineage_id = f"lineage-{_seed_digest(lineage_payload)[:16]}"
    return GenerationLineage(
        lineage_id=lineage_id,
        source_request_id=request.base_preview_request.request_id,
        parent_generation_id=request.parent_generation_id,
        regenerated_generation_id=preview.metadata.generation_id,
        reason=request.reason,
        changed_fields=changed_fields,
    )


def _world_cell_from_template(cell: TemplateCell) -> WorldCell:
    return WorldCell(
        id=cell.id,
        label=cell.label,
        entity_refs=deepcopy(cell.entity_refs),
        child_cells=[_world_cell_from_template(child) for child in cell.child_cells],
        metadata=deepcopy(cell.metadata),
    )


def _world_cell_from_plan(cell: PlanCell) -> WorldCell:
    return WorldCell(
        id=cell.id,
        label=cell.label,
        entity_refs=deepcopy(cell.entity_refs),
        child_cells=[_world_cell_from_plan(child) for child in cell.child_cells],
        metadata=deepcopy(cell.metadata),
    )


def _preview_response_from_generation_result(
    request: GenerationPreviewRequest,
    result: TemplateGenerationResult,
    import_source: Optional[Dict[str, Any]] = None,
) -> GenerationPreviewResponse:
    metadata = GenerationPreviewMetadata(
        generation_id=result.metadata.generation_id,
        request_id=request.request_id,
        source_kind=request.source_kind,
        template_id=result.metadata.template_id,
        template_version=result.metadata.template_version,
        plan_id=result.metadata.plan_id,
        plan_version=result.metadata.plan_version,
        seed_digest=result.metadata.seed_digest,
        validation_status=result.metadata.validation_status,
        diagnostics_count=len(result.diagnostics),
        preview_summary=_preview_summary(result.worldspec),
        import_source=import_source,
    )
    return GenerationPreviewResponse(
        request_id=request.request_id,
        source_kind=request.source_kind,
        validation_status=result.metadata.validation_status,
        metadata=metadata,
        diagnostics=deepcopy(result.diagnostics),
        worldspec_preview=_public_worldspec_preview(result.worldspec),
    )


def _failed_import_preview_response(
    request: GenerationPreviewRequest,
    diagnostics: List[GenerationDiagnostic],
) -> GenerationPreviewResponse:
    seed_digest = _seed_digest(
        {
            "request_id": request.request_id,
            "import_id": request.import_request.import_id
            if request.import_request is not None
            else None,
            "diagnostics": [diagnostic.model_dump() for diagnostic in diagnostics],
        }
    )
    metadata = GenerationPreviewMetadata(
        generation_id=f"generation-{seed_digest[:16]}",
        request_id=request.request_id,
        source_kind=request.source_kind,
        seed_digest=seed_digest,
        validation_status="failed",
        diagnostics_count=len(diagnostics),
    )
    return GenerationPreviewResponse(
        request_id=request.request_id,
        source_kind=request.source_kind,
        validation_status="failed",
        metadata=metadata,
        diagnostics=deepcopy(diagnostics),
    )


def _preview_summary(worldspec: Optional[WorldSpec]) -> Dict[str, Any]:
    if worldspec is None:
        return {}

    def visit(cell: WorldCell, depth: int) -> Dict[str, int]:
        total = 1
        max_depth = depth
        entity_ref_count = len(cell.entity_refs)
        for child in cell.child_cells:
            child_summary = visit(child, depth + 1)
            total += child_summary["total_cell_count"]
            max_depth = max(max_depth, child_summary["max_child_depth"])
            entity_ref_count += child_summary["entity_ref_count"]
        return {
            "total_cell_count": total,
            "max_child_depth": max_depth,
            "entity_ref_count": entity_ref_count,
        }

    counts = visit(worldspec.root, 1)
    return {
        "root_world_id": worldspec.id,
        "root_label": _bounded_text(worldspec.root.label),
        **counts,
    }


def _public_worldspec_preview(worldspec: Optional[WorldSpec]) -> Optional[WorldSpec]:
    if worldspec is None:
        return None

    preview = worldspec.model_copy(deep=True)
    preview.metadata = _redacted_preview_metadata(preview.metadata)
    _redact_cell_preview_metadata(preview.root)
    return preview


def _redact_cell_preview_metadata(cell: WorldCell) -> None:
    cell.metadata = _redacted_preview_metadata(cell.metadata)
    for child in cell.child_cells:
        _redact_cell_preview_metadata(child)


def _redacted_preview_metadata(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _redacted_preview_metadata(item)
            for key, item in value.items()
            if not _is_sensitive_metadata_key(key)
        }
    if isinstance(value, list):
        return [_redacted_preview_metadata(item) for item in value]
    return deepcopy(value)


def _bounded_text(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    return value[:PREVIEW_SUMMARY_TEXT_LIMIT]


def _redacted_import_source(source: Optional[Any]) -> Optional[Dict[str, Any]]:
    if source is None:
        return None
    return {
        "source_kind": source.source_kind,
        "source_id": source.source_id,
        "provider_label": source.provider_label,
        "model_label": source.model_label,
        "redacted": source.redacted,
    }


def _diagnostic(
    code: str, message: str, path: Optional[str], source_context: Dict[str, Any]
) -> GenerationDiagnostic:
    return GenerationDiagnostic(
        code=code,
        severity="error",
        message=message,
        path=path,
        source_context=source_context,
    )


def _append_json_compatibility_diagnostic(
    diagnostics: List[GenerationDiagnostic],
    code: str,
    message: str,
    path: str,
    value: Any,
) -> None:
    try:
        _canonical_json_value(value)
    except (TypeError, ValueError):
        diagnostics.append(
            _diagnostic(
                code,
                message,
                path,
                {"type": type(value).__name__},
            )
        )


def _is_sensitive_metadata_key(key: str) -> bool:
    normalized = "".join(character for character in key.lower() if character.isalnum())
    safe_usage_keys = {
        "".join(character for character in safe_key.lower() if character.isalnum())
        for safe_key in SAFE_PREVIEW_METADATA_USAGE_KEYS
    }
    if normalized in safe_usage_keys:
        return False
    sensitive_exact = {
        "".join(character for character in sensitive_key.lower() if character.isalnum())
        for sensitive_key in SENSITIVE_PREVIEW_METADATA_KEYS
    }
    if normalized in sensitive_exact:
        return True
    return any(
        token in normalized
        for token in (
            "apikey",
            "credential",
            "oracle",
            "prompt",
            "providertrace",
            "secret",
            "token",
        )
    )


def _sensitive_metadata_diagnostics(
    value: Any,
    path: str,
    code: str,
    message: str,
) -> List[GenerationDiagnostic]:
    diagnostics: List[GenerationDiagnostic] = []
    if isinstance(value, dict):
        for key, item in value.items():
            next_path = f"{path}/{key}"
            if isinstance(key, str) and _is_sensitive_metadata_key(key):
                diagnostics.append(
                    _diagnostic(
                        code,
                        message,
                        next_path,
                        {"key": key},
                    )
                )
            diagnostics.extend(_sensitive_metadata_diagnostics(item, next_path, code, message))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            diagnostics.extend(
                _sensitive_metadata_diagnostics(item, f"{path}/{index}", code, message)
            )
    return diagnostics


def _seed_digest(value: Any) -> str:
    payload = json.dumps(
        _canonical_json_value(value),
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _canonical_json_value(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, bool)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise TypeError("JSON-compatible numbers must be finite")
        return value
    if isinstance(value, list):
        return [_canonical_json_value(item) for item in value]
    if isinstance(value, dict):
        result: Dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise TypeError("JSON-compatible objects require string keys")
            result[key] = _canonical_json_value(item)
        return result
    raise TypeError(f"unsupported JSON-compatible value: {type(value).__name__}")


def _json_compatible_or_none(value: Any) -> Any:
    try:
        return _canonical_json_value(value)
    except (TypeError, ValueError):
        return None


def _is_json_compatible(value: Any) -> bool:
    try:
        _canonical_json_value(value)
    except (TypeError, ValueError):
        return False
    return True


def _merge_constraints(
    template_constraints: Dict[str, Any], request_constraints: Dict[str, Any]
) -> Dict[str, Any]:
    merged = deepcopy(template_constraints)
    for key, value in request_constraints.items():
        merged[key] = deepcopy(value)
    return merged


def _allowed_entity_kinds(constraints: Dict[str, Any]) -> Optional[Set[str]]:
    raw = constraints.get("allowed_entity_kinds")
    if raw is None:
        return None
    if not isinstance(raw, list):
        return set()
    return {str(item) for item in raw}


def _optional_int_constraint(constraints: Dict[str, Any], key: str) -> Optional[int]:
    raw = constraints.get(key)
    if raw is None:
        return None
    try:
        return int(raw)
    except (TypeError, ValueError):
        return None
