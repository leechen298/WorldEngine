from app.schemas.entity import EntityRef
from app.schemas.world_cell import WorldCell, WorldSpec


def _schema_smoke_payload() -> dict:
    return {
        "schema_version": "0.2",
        "id": "schema-smoke-world",
        "label": "Schema Smoke World",
        "metadata": {
            "purpose": "schema-smoke",
            "version": "0.2",
        },
        "root": {
            "id": "root",
            "label": "Root",
            "kind": "world",
            "entity_refs": [
                {
                    "id": "entity-a",
                    "kind": "generic",
                    "label": "Entity A",
                    "metadata": {
                        "role": "schema-smoke",
                    },
                }
            ],
            "child_cells": [
                {
                    "id": "cell-a",
                    "label": "Cell A",
                    "kind": "world",
                    "entity_refs": [],
                    "child_cells": [
                        {
                            "id": "cell-b",
                            "label": "Cell B",
                            "kind": "world",
                            "entity_refs": [
                                {
                                    "id": "entity-b",
                                    "kind": "generic",
                                    "label": "Entity B",
                                }
                            ],
                            "child_cells": [],
                            "metadata": {
                                "role": "nested",
                            },
                        }
                    ],
                    "metadata": {
                        "role": "child",
                    },
                }
            ],
            "metadata": {
                "role": "root",
            },
        },
    }


def test_entity_ref_accepts_generic_reference() -> None:
    entity_ref = EntityRef(id="entity-a", kind="generic", label="Entity A")

    assert entity_ref.id == "entity-a"
    assert entity_ref.kind == "generic"
    assert entity_ref.label == "Entity A"


def test_world_cell_accepts_recursive_children() -> None:
    cell = WorldCell.model_validate(_schema_smoke_payload()["root"])

    assert cell.id == "root"
    assert cell.kind == "world"
    assert cell.child_cells[0].id == "cell-a"
    assert cell.child_cells[0].child_cells[0].id == "cell-b"


def test_worldspec_validates_schema_smoke_payload() -> None:
    spec = WorldSpec.model_validate(_schema_smoke_payload())

    assert spec.schema_version == "0.2"
    assert spec.id == "schema-smoke-world"
    assert isinstance(spec.root, WorldCell)
    assert spec.root.id == "root"
    assert spec.root.entity_refs
    assert isinstance(spec.root.entity_refs[0], EntityRef)


def test_worldspec_round_trips_child_cells_and_entity_refs() -> None:
    spec = WorldSpec.model_validate(_schema_smoke_payload())

    reconstructed = WorldSpec.model_validate(spec.model_dump())

    assert reconstructed == spec
    assert reconstructed.root.child_cells[0].child_cells[0].id == "cell-b"
    assert reconstructed.root.child_cells[0].child_cells[0].entity_refs[0].id == "entity-b"
