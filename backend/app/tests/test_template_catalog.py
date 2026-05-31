from app.core.world_generation import validate_template
from app.schemas.world_generation import TemplateCell, WorldTemplate


def test_template_validation_accepts_generic_template() -> None:
    template = WorldTemplate(
        id="generic-template",
        version="1",
        root=TemplateCell(
            id="root",
            entity_refs=[{"id": "entity-alpha", "kind": "generic-agent"}],
            child_cells=[{"id": "child"}],
        ),
        constraints={"max_child_cells": 3, "allowed_entity_kinds": ["generic-agent"]},
    )

    diagnostics = validate_template(template)

    assert diagnostics == []


def test_template_validation_reports_duplicate_cell_ids_with_paths() -> None:
    template = WorldTemplate(
        id="generic-template",
        version="1",
        root=TemplateCell(id="root", child_cells=[{"id": "root"}]),
    )

    diagnostics = validate_template(template)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("duplicate_cell_id", "/root/child_cells/0/id")
    ]


def test_template_validation_reports_entity_kind_allowlist_violations() -> None:
    template = WorldTemplate(
        id="generic-template",
        version="1",
        root=TemplateCell(
            id="root",
            entity_refs=[{"id": "entity-alpha", "kind": "forbidden-kind"}],
        ),
        constraints={"allowed_entity_kinds": ["generic-agent"]},
    )

    diagnostics = validate_template(template)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("entity_kind_not_allowed", "/root/entity_refs/0/kind")
    ]


def test_template_validation_reports_child_count_bounds() -> None:
    template = WorldTemplate(
        id="generic-template",
        version="1",
        root=TemplateCell(id="root", child_cells=[{"id": "child-a"}, {"id": "child-b"}]),
        constraints={"max_child_cells": 1},
    )

    diagnostics = validate_template(template)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("invalid_template_bounds", "/root/child_cells")
    ]


def test_template_validation_reports_duplicate_entity_refs() -> None:
    template = WorldTemplate(
        id="generic-template",
        version="1",
        root=TemplateCell(
            id="root",
            entity_refs=[
                {"id": "entity-alpha", "kind": "generic-agent"},
                {"id": "entity-alpha", "kind": "generic-agent"},
            ],
        ),
    )

    diagnostics = validate_template(template)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("duplicate_entity_ref", "/root/entity_refs/1/id")
    ]


def test_template_validation_reports_min_child_count_bounds() -> None:
    template = WorldTemplate(
        id="generic-template",
        version="1",
        root=TemplateCell(id="root"),
        constraints={"min_child_cells": 1},
    )

    diagnostics = validate_template(template)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("invalid_template_bounds", "/root/child_cells")
    ]


def test_template_validation_reports_unsupported_template_version() -> None:
    template = WorldTemplate(
        id="generic-template",
        version="unsupported",
        root=TemplateCell(id="root"),
    )

    diagnostics = validate_template(template)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("unsupported_template_version", "/version")
    ]
