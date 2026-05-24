import json
from pathlib import Path

from app.schemas.entity import EntityRef
from app.schemas.world_cell import WorldCell, WorldSpec


FIXTURE_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "world_specs"
    / "tiny_village.world.json"
)


def _load_fixture_dict() -> dict:
    assert FIXTURE_PATH.exists(), f"missing fixture: {FIXTURE_PATH}"
    return json.loads(FIXTURE_PATH.read_text())


def _load_fixture_spec() -> WorldSpec:
    return WorldSpec.model_validate(_load_fixture_dict())


def test_imports_worldspec_fixture_schema_models() -> None:
    assert EntityRef.__name__ == "EntityRef"
    assert WorldCell.__name__ == "WorldCell"
    assert WorldSpec.__name__ == "WorldSpec"


def test_tiny_village_worldspec_fixture_exists() -> None:
    assert FIXTURE_PATH.exists()


def test_tiny_village_fixture_parses_and_validates_with_worldspec() -> None:
    fixture = _load_fixture_dict()
    spec = WorldSpec.model_validate(fixture)

    assert spec.schema_version == "0.2"
    assert spec.id == "tiny-village"
    assert spec.label == "Tiny Village"
    assert spec.metadata["purpose"] == "reference-fixture"
    assert spec.metadata["version"] == "0.2"


def test_tiny_village_fixture_contains_recursive_world_cells_and_entity_refs() -> None:
    spec = _load_fixture_spec()

    assert isinstance(spec.root, WorldCell)
    assert spec.root.id == "root"
    assert spec.root.label == "Tiny Village Root"
    assert spec.root.kind == "world"
    assert spec.root.entity_refs
    assert isinstance(spec.root.entity_refs[0], EntityRef)
    assert spec.root.entity_refs[0].id == "village-square"

    child_ids = {child.id for child in spec.root.child_cells}
    assert {"village-square", "workshop"}.issubset(child_ids)

    nested_entity_refs = [
        entity_ref
        for child_cell in spec.root.child_cells
        for entity_ref in child_cell.entity_refs
    ]
    assert nested_entity_refs
    assert all(isinstance(entity_ref, EntityRef) for entity_ref in nested_entity_refs)


def test_tiny_village_fixture_round_trips_through_model_dump() -> None:
    spec = _load_fixture_spec()

    reconstructed = WorldSpec.model_validate(spec.model_dump())

    assert reconstructed == spec
    assert reconstructed.root.child_cells[0].kind == "world"
