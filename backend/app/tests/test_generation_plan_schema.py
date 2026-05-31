from pydantic import ValidationError

from app.schemas.world_generation import GenerationPlan, PlanCell, PlanGenerationRequest


def test_generation_plan_accepts_generic_recursive_cells_and_defaults() -> None:
    plan = GenerationPlan(
        id="generic-plan",
        version="1",
        root=PlanCell(
            id="root",
            label="Generic Root",
            entity_refs=[{"id": "entity-alpha", "kind": "generic-agent"}],
            child_cells=[{"id": "child"}],
        ),
    )

    assert plan.id == "generic-plan"
    assert plan.version == "1"
    assert plan.root.id == "root"
    assert plan.root.child_cells[0].id == "child"
    assert plan.root.entity_refs[0].kind == "generic-agent"
    assert plan.metadata == {}
    assert plan.constraints == {}


def test_plan_generation_request_accepts_plan_constraints_and_seed_material() -> None:
    request = PlanGenerationRequest(
        request_id="request-alpha",
        plan={"id": "generic-plan", "version": "1", "root": {"id": "root"}},
        seed_material={"variant": "alpha"},
        constraints={"allowed_entity_kinds": ["generic-agent"]},
    )

    assert request.plan.id == "generic-plan"
    assert request.seed_material == {"variant": "alpha"}
    assert request.constraints == {"allowed_entity_kinds": ["generic-agent"]}


def test_generation_plan_schema_rejects_empty_required_fields() -> None:
    with_errors = [
        lambda: PlanCell(id=""),
        lambda: GenerationPlan(id="", version="1", root={"id": "root"}),
        lambda: GenerationPlan(id="generic-plan", version="", root={"id": "root"}),
        lambda: PlanGenerationRequest(
            request_id="",
            plan={"id": "generic-plan", "version": "1", "root": {"id": "root"}},
        ),
    ]

    for factory in with_errors:
        try:
            factory()
        except ValidationError:
            continue
        raise AssertionError("expected validation error")
