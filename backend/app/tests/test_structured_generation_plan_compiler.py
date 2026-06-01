from copy import deepcopy

import pytest

from app.core.runtime_context import build_runtime_context, summarize_runtime_context
from app.core.world_generation import generate_worldspec_from_plan, validate_generation_plan
from app.core.worldspec_loader import load_worldspec
from app.schemas.world_generation import GenerationPlan, PlanCell, PlanGenerationRequest


def _plan() -> GenerationPlan:
    return GenerationPlan(
        id="generic-plan",
        version="1",
        root=PlanCell(
            id="root",
            label="Generic Root",
            entity_refs=[{"id": "entity-alpha", "kind": "generic-agent"}],
            child_cells=[{"id": "child", "label": "Generic Child"}],
        ),
        metadata={"category": "generic"},
        constraints={"allowed_entity_kinds": ["generic-agent"]},
    )


def _request(seed_material: object = "seed-alpha") -> PlanGenerationRequest:
    return PlanGenerationRequest(
        request_id="request-alpha",
        plan=_plan(),
        seed_material=seed_material,
    )


def test_plan_validation_accepts_generic_plan() -> None:
    assert validate_generation_plan(_plan()) == []


def test_plan_generation_is_deterministic_and_loader_compatible() -> None:
    first = generate_worldspec_from_plan(_request())
    second = generate_worldspec_from_plan(_request())

    assert first.model_dump() == second.model_dump()
    assert first.worldspec is not None
    assert first.worldspec.schema_version == "0.2"
    assert first.worldspec.root.kind == "world"
    assert first.metadata.validation_status == "passed"
    assert first.metadata.source_kind == "plan"
    assert first.metadata.plan_id == "generic-plan"
    assert first.metadata.plan_version == "1"

    loaded = load_worldspec(first.worldspec.model_dump(), source_label=first.metadata.generation_id)
    assert loaded.success is True
    assert loaded.loaded is not None

    context = build_runtime_context(loaded.loaded)
    assert context.success is True
    assert context.context is not None
    summary = summarize_runtime_context(context.context)

    assert summary.worldspec_id == first.worldspec.id
    assert summary.root_cell_id == "root"


def test_plan_generation_changes_seed_digest_for_different_seed_material() -> None:
    first = generate_worldspec_from_plan(_request(seed_material="seed-alpha"))
    second = generate_worldspec_from_plan(_request(seed_material="seed-beta"))

    assert first.worldspec is not None
    assert second.worldspec is not None
    assert first.metadata.seed_digest != second.metadata.seed_digest
    assert first.worldspec.id != second.worldspec.id
    assert first.worldspec.root.id == second.worldspec.root.id == "root"


def test_plan_generation_does_not_mutate_plan_input() -> None:
    request = _request()
    before = deepcopy(request.plan.model_dump())

    generate_worldspec_from_plan(request)

    assert request.plan.model_dump() == before


def test_invalid_plan_returns_diagnostics_without_worldspec() -> None:
    request = PlanGenerationRequest(
        request_id="request-alpha",
        plan=GenerationPlan(
            id="generic-plan",
            version="1",
            root=PlanCell(id="root", child_cells=[{"id": "root"}]),
        ),
        seed_material="seed-alpha",
    )

    result = generate_worldspec_from_plan(request)

    assert result.worldspec is None
    assert result.metadata.validation_status == "failed"
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("duplicate_cell_id", "/root/child_cells/0/id")
    ]


def test_plan_validation_reports_duplicate_entity_refs_and_bounds() -> None:
    plan = GenerationPlan(
        id="generic-plan",
        version="1",
        root=PlanCell(
            id="root",
            entity_refs=[
                {"id": "entity-alpha", "kind": "generic-agent"},
                {"id": "entity-alpha", "kind": "generic-agent"},
            ],
        ),
        constraints={"min_child_cells": 1},
    )

    diagnostics = validate_generation_plan(plan)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("invalid_plan_bounds", "/root/child_cells"),
        ("duplicate_entity_ref", "/root/entity_refs/1/id"),
    ]


def test_plan_validation_reports_unsupported_plan_version() -> None:
    plan = GenerationPlan(id="generic-plan", version="unsupported", root=PlanCell(id="root"))

    diagnostics = validate_generation_plan(plan)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("unsupported_plan_version", "/version")
    ]


def test_plan_validation_reports_non_json_metadata() -> None:
    plan = GenerationPlan(
        id="generic-plan",
        version="1",
        root=PlanCell(id="root"),
        metadata={"not-json": {"unstable"}},
    )

    diagnostics = validate_generation_plan(plan)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("unsupported_plan_metadata", "/metadata")
    ]


def test_plan_validation_reports_non_json_constraints() -> None:
    plan = _plan()
    plan.constraints = {"not-json": {"unstable"}}

    diagnostics = validate_generation_plan(plan)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("unsupported_plan_constraints", "/constraints")
    ]


def test_plan_validation_reports_non_json_cell_metadata_paths() -> None:
    plan = GenerationPlan(
        id="generic-plan",
        version="1",
        root=PlanCell(
            id="root",
            metadata={"not-json": {"unstable"}},
            child_cells=[
                {
                    "id": "child",
                    "metadata": {"also-not-json": {"unstable-child"}},
                }
            ],
        ),
    )

    diagnostics = validate_generation_plan(plan)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("unsupported_plan_metadata", "/root/metadata"),
        ("unsupported_plan_metadata", "/root/child_cells/0/metadata"),
    ]


def test_plan_generation_reports_cell_metadata_instead_of_seed_material() -> None:
    request = PlanGenerationRequest(
        request_id="request-alpha",
        plan=GenerationPlan(
            id="generic-plan",
            version="1",
            root=PlanCell(id="root", metadata={"not-json": {"unstable"}}),
        ),
        seed_material="seed-alpha",
    )

    result = generate_worldspec_from_plan(request)

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_plan_metadata", "/root/metadata")
    ]


def test_failed_plan_generation_preserves_valid_seed_material_in_fallback_digest() -> None:
    alpha_plan = _plan()
    alpha_plan.metadata = {"not-json": {"unstable"}}
    beta_plan = _plan()
    beta_plan.metadata = {"not-json": {"unstable"}}

    alpha = generate_worldspec_from_plan(
        PlanGenerationRequest(
            request_id="request-alpha",
            plan=alpha_plan,
            seed_material="seed-alpha",
        )
    )
    beta = generate_worldspec_from_plan(
        PlanGenerationRequest(
            request_id="request-alpha",
            plan=beta_plan,
            seed_material="seed-beta",
        )
    )

    assert alpha.worldspec is None
    assert beta.worldspec is None
    assert [(d.code, d.path) for d in alpha.diagnostics] == [
        ("unsupported_plan_metadata", "/metadata")
    ]
    assert [(d.code, d.path) for d in beta.diagnostics] == [
        ("unsupported_plan_metadata", "/metadata")
    ]
    assert alpha.metadata.seed_digest != beta.metadata.seed_digest
    assert alpha.metadata.generation_id != beta.metadata.generation_id


def test_plan_request_constraints_participate_in_validation() -> None:
    request = PlanGenerationRequest(
        request_id="request-alpha",
        plan=_plan(),
        seed_material="seed-alpha",
        constraints={"allowed_entity_kinds": ["different-kind"]},
    )

    result = generate_worldspec_from_plan(request)

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("entity_kind_not_allowed", "/root/entity_refs/0/kind")
    ]


def test_plan_generation_reports_non_json_request_constraints_without_seed_misdiagnosis() -> None:
    result = generate_worldspec_from_plan(
        PlanGenerationRequest(
            request_id="request-alpha",
            plan=_plan(),
            seed_material="seed-alpha",
            constraints={"not-json": {"unstable"}},
        )
    )

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_generation_constraints", "/constraints")
    ]


@pytest.mark.parametrize(
    "seed_material",
    [{"unstable"}, ("tuple", "seed"), float("nan"), float("inf"), float("-inf")],
)
def test_non_json_plan_seed_material_returns_deterministic_diagnostic(
    seed_material: object,
) -> None:
    result = generate_worldspec_from_plan(_request(seed_material=seed_material))

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_seed_material", "/seed_material")
    ]


def test_plan_generated_content_remains_generic() -> None:
    result = generate_worldspec_from_plan(_request())
    assert result.worldspec is not None

    dumped = str(result.worldspec.model_dump()).lower()

    forbidden_terms = ["castle", "dragon", "quest", "sku", "inventory", "oracle"]
    assert all(term not in dumped for term in forbidden_terms)
