import pytest
from pydantic import ValidationError


def _schema_classes():
    from app.schemas.entity import EntityRef
    from app.schemas.world_cell import WorldCell, WorldSpec

    return EntityRef, WorldCell, WorldSpec


def test_imports_recursive_world_schema_classes() -> None:
    EntityRef, WorldCell, WorldSpec = _schema_classes()

    assert EntityRef.__name__ == "EntityRef"
    assert WorldCell.__name__ == "WorldCell"
    assert WorldSpec.__name__ == "WorldSpec"


def test_entity_ref_accepts_required_identity_fields_and_defaults() -> None:
    EntityRef, _, _ = _schema_classes()

    entity_ref = EntityRef(id="agent-1", kind="agent", label="Agent One")

    assert entity_ref.id == "agent-1"
    assert entity_ref.kind == "agent"
    assert entity_ref.label == "Agent One"
    assert entity_ref.metadata == {}


def test_world_cell_accepts_defaults_and_optional_label() -> None:
    _, WorldCell, _ = _schema_classes()

    cell = WorldCell(id="root", label="Root World")

    assert cell.id == "root"
    assert cell.label == "Root World"
    assert cell.kind == "world"
    assert cell.entity_refs == []
    assert cell.child_cells == []
    assert cell.metadata == {}


def test_world_cell_validates_nested_child_cells_and_entity_refs() -> None:
    _, WorldCell, _ = _schema_classes()

    cell = WorldCell(
        id="root",
        entity_refs=[{"id": "agent-1", "kind": "agent"}],
        child_cells=[
            {
                "id": "inner",
                "label": "Inner World",
                "entity_refs": [{"id": "resource-1", "kind": "resource"}],
            }
        ],
    )

    assert cell.entity_refs[0].id == "agent-1"
    assert cell.child_cells[0].id == "inner"
    assert cell.child_cells[0].kind == "world"
    assert cell.child_cells[0].entity_refs[0].kind == "resource"


def test_world_spec_accepts_root_world_cell() -> None:
    _, WorldCell, WorldSpec = _schema_classes()

    world_spec = WorldSpec(id="spec-1", label="Spec One", root=WorldCell(id="root"))

    assert world_spec.schema_version == "0.2"
    assert world_spec.id == "spec-1"
    assert world_spec.label == "Spec One"
    assert world_spec.root.id == "root"
    assert world_spec.metadata == {}


@pytest.mark.parametrize(
    ("factory_name", "payload"),
    [
        ("EntityRef", {"id": "", "kind": "agent"}),
        ("EntityRef", {"id": "agent-1", "kind": ""}),
        ("WorldCell", {"id": ""}),
        ("WorldSpec", {"id": "", "root": {"id": "root"}}),
    ],
)
def test_id_like_fields_reject_empty_strings(factory_name: str, payload: dict) -> None:
    EntityRef, WorldCell, WorldSpec = _schema_classes()
    factory = {
        "EntityRef": EntityRef,
        "WorldCell": WorldCell,
        "WorldSpec": WorldSpec,
    }[factory_name]

    with pytest.raises(ValidationError):
        factory(**payload)


def test_world_cell_rejects_non_world_kind() -> None:
    _, WorldCell, _ = _schema_classes()

    with pytest.raises(ValidationError):
        WorldCell(id="root", kind="invalid-kind")


def test_world_spec_rejects_unsupported_schema_version() -> None:
    _, _, WorldSpec = _schema_classes()

    with pytest.raises(ValidationError):
        WorldSpec(schema_version="0.3", id="spec-1", root={"id": "root"})


def test_world_cell_rejects_invalid_child_cell_input() -> None:
    _, WorldCell, _ = _schema_classes()

    with pytest.raises(ValidationError):
        WorldCell(id="root", child_cells=[{"label": "Missing ID"}])


def test_world_cell_rejects_invalid_entity_ref_input() -> None:
    _, WorldCell, _ = _schema_classes()

    with pytest.raises(ValidationError):
        WorldCell(id="root", entity_refs=[{"id": "agent-1"}])


def test_world_spec_serializes_nested_structure_with_model_dump() -> None:
    _, WorldCell, WorldSpec = _schema_classes()

    world_spec = WorldSpec(
        id="spec-1",
        root=WorldCell(
            id="root",
            entity_refs=[{"id": "agent-1", "kind": "agent"}],
            child_cells=[{"id": "inner"}],
        ),
        metadata={"source": "test"},
    )

    assert world_spec.model_dump() == {
        "schema_version": "0.2",
        "id": "spec-1",
        "label": None,
        "root": {
            "id": "root",
            "label": None,
            "kind": "world",
            "entity_refs": [
                {
                    "id": "agent-1",
                    "kind": "agent",
                    "label": None,
                    "metadata": {},
                }
            ],
            "child_cells": [
                {
                    "id": "inner",
                    "label": None,
                    "kind": "world",
                    "entity_refs": [],
                    "child_cells": [],
                    "metadata": {},
                }
            ],
            "metadata": {},
        },
        "metadata": {"source": "test"},
    }


def test_world_spec_reconstructs_from_dumped_nested_dictionary() -> None:
    _, WorldCell, WorldSpec = _schema_classes()
    original = WorldSpec(
        id="spec-1",
        root=WorldCell(
            id="root",
            entity_refs=[{"id": "agent-1", "kind": "agent"}],
            child_cells=[{"id": "inner"}],
        ),
    )

    reconstructed = WorldSpec.model_validate(original.model_dump())

    assert reconstructed == original
    assert reconstructed.root.child_cells[0].id == "inner"
