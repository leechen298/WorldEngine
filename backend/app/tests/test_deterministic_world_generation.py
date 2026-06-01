from copy import deepcopy

import pytest

from app.core.runtime_context import build_runtime_context, summarize_runtime_context
from app.core.world_generation import generate_worldspec_from_template
from app.core.worldspec_loader import load_worldspec
from app.schemas.world_generation import TemplateCell, TemplateGenerationRequest, WorldTemplate


def _template() -> WorldTemplate:
    return WorldTemplate(
        id="generic-template",
        version="1",
        root=TemplateCell(
            id="root",
            label="Generic Root",
            entity_refs=[{"id": "entity-alpha", "kind": "generic-agent"}],
            child_cells=[{"id": "child", "label": "Generic Child"}],
        ),
        metadata={"category": "generic"},
        constraints={"allowed_entity_kinds": ["generic-agent"]},
    )


def _request(seed_material: object = "seed-alpha") -> TemplateGenerationRequest:
    return TemplateGenerationRequest(
        request_id="request-alpha",
        template=_template(),
        seed_material=seed_material,
    )


def test_generation_is_deterministic_for_same_request() -> None:
    first = generate_worldspec_from_template(_request())
    second = generate_worldspec_from_template(_request())

    assert first.model_dump() == second.model_dump()
    assert first.worldspec is not None
    assert first.worldspec.schema_version == "0.2"
    assert first.worldspec.root.kind == "world"
    assert first.metadata.validation_status == "passed"


def test_generation_changes_seed_digest_for_different_seed_material() -> None:
    first = generate_worldspec_from_template(_request(seed_material="seed-alpha"))
    second = generate_worldspec_from_template(_request(seed_material="seed-beta"))

    assert first.worldspec is not None
    assert second.worldspec is not None
    assert first.metadata.seed_digest != second.metadata.seed_digest
    assert first.worldspec.id != second.worldspec.id
    assert first.worldspec.root.id == second.worldspec.root.id == "root"


def test_generation_does_not_mutate_template_input() -> None:
    request = _request()
    before = request.template.model_dump()

    generate_worldspec_from_template(request)

    assert request.template.model_dump() == before


def test_generated_worldspec_passes_loader_and_runtime_context_bridge() -> None:
    result = generate_worldspec_from_template(_request())
    assert result.worldspec is not None

    loaded = load_worldspec(result.worldspec.model_dump(), source_label=result.metadata.generation_id)
    assert loaded.success is True
    assert loaded.loaded is not None

    context = build_runtime_context(loaded.loaded)
    assert context.success is True
    assert context.context is not None
    summary = summarize_runtime_context(context.context)

    assert summary.worldspec_id == result.worldspec.id
    assert summary.root_cell_id == "root"
    assert "worldspec" not in summary.__dict__
    assert "root" not in summary.__dict__


def test_invalid_template_returns_diagnostics_without_worldspec() -> None:
    request = TemplateGenerationRequest(
        request_id="request-alpha",
        template=WorldTemplate(
            id="generic-template",
            version="1",
            root=TemplateCell(id="root", child_cells=[{"id": "root"}]),
        ),
        seed_material="seed-alpha",
    )

    result = generate_worldspec_from_template(request)

    assert result.worldspec is None
    assert result.metadata.validation_status == "failed"
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("duplicate_cell_id", "/root/child_cells/0/id")
    ]


def test_request_constraints_participate_in_validation() -> None:
    request = TemplateGenerationRequest(
        request_id="request-alpha",
        template=_template(),
        seed_material="seed-alpha",
        constraints={"allowed_entity_kinds": ["different-kind"]},
    )

    result = generate_worldspec_from_template(request)

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("entity_kind_not_allowed", "/root/entity_refs/0/kind")
    ]


def test_template_generation_reports_non_json_metadata_paths() -> None:
    template = _template()
    template.metadata = {"not-json": {"unstable"}}
    template.root.metadata = {"also-not-json": {"unstable-root"}}
    template.root.child_cells[0].metadata = {"child-not-json": {"unstable-child"}}

    result = generate_worldspec_from_template(
        TemplateGenerationRequest(
            request_id="request-alpha",
            template=template,
            seed_material="seed-alpha",
        )
    )

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_template_metadata", "/metadata"),
        ("unsupported_template_metadata", "/root/metadata"),
        ("unsupported_template_metadata", "/root/child_cells/0/metadata"),
    ]


def test_failed_template_generation_preserves_valid_seed_material_in_fallback_digest() -> None:
    alpha_template = _template()
    alpha_template.metadata = {"not-json": {"unstable"}}
    beta_template = _template()
    beta_template.metadata = {"not-json": {"unstable"}}

    alpha = generate_worldspec_from_template(
        TemplateGenerationRequest(
            request_id="request-alpha",
            template=alpha_template,
            seed_material="seed-alpha",
        )
    )
    beta = generate_worldspec_from_template(
        TemplateGenerationRequest(
            request_id="request-alpha",
            template=beta_template,
            seed_material="seed-beta",
        )
    )

    assert alpha.worldspec is None
    assert beta.worldspec is None
    assert [(d.code, d.path) for d in alpha.diagnostics] == [
        ("unsupported_template_metadata", "/metadata")
    ]
    assert [(d.code, d.path) for d in beta.diagnostics] == [
        ("unsupported_template_metadata", "/metadata")
    ]
    assert alpha.metadata.seed_digest != beta.metadata.seed_digest
    assert alpha.metadata.generation_id != beta.metadata.generation_id


def test_template_generation_reports_non_json_template_constraints() -> None:
    template = _template()
    template.constraints = {"not-json": {"unstable"}}

    result = generate_worldspec_from_template(
        TemplateGenerationRequest(
            request_id="request-alpha",
            template=template,
            seed_material="seed-alpha",
        )
    )

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_template_constraints", "/constraints")
    ]


def test_template_generation_reports_non_json_request_constraints_without_seed_misdiagnosis() -> None:
    result = generate_worldspec_from_template(
        TemplateGenerationRequest(
            request_id="request-alpha",
            template=_template(),
            seed_material="seed-alpha",
            constraints={"not-json": {"unstable"}},
        )
    )

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_generation_constraints", "/constraints")
    ]


def test_non_json_seed_material_returns_deterministic_diagnostic() -> None:
    request = _request(seed_material={"unstable"})

    result = generate_worldspec_from_template(request)

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_seed_material", "/seed_material")
    ]


@pytest.mark.parametrize("seed_material", [float("nan"), float("inf"), float("-inf")])
def test_non_finite_float_seed_material_returns_deterministic_diagnostic(
    seed_material: float,
) -> None:
    result = generate_worldspec_from_template(_request(seed_material=seed_material))

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_seed_material", "/seed_material")
    ]


def test_tuple_seed_material_returns_deterministic_diagnostic() -> None:
    result = generate_worldspec_from_template(_request(seed_material=("tuple", "seed")))

    assert result.worldspec is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_seed_material", "/seed_material")
    ]


def test_generated_content_remains_generic() -> None:
    result = generate_worldspec_from_template(_request())
    assert result.worldspec is not None

    dumped = str(result.worldspec.model_dump()).lower()

    forbidden_terms = ["castle", "dragon", "quest", "sku", "inventory", "oracle"]
    assert all(term not in dumped for term in forbidden_terms)
