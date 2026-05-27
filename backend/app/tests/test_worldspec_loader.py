import json

from app.core.worldspec_loader import load_worldspec
from app.schemas.world_cell import WorldSpec


def _minimal_payload() -> dict:
    return {
        "schema_version": "0.2",
        "id": "worldspec-example",
        "label": "WorldSpec Example",
        "root": {
            "id": "cell-root",
            "label": "Cell Root",
            "kind": "world",
            "entity_refs": [],
            "child_cells": [],
            "metadata": {},
        },
        "metadata": {"purpose": "loader-test"},
    }


def test_load_worldspec_accepts_valid_mapping() -> None:
    result = load_worldspec(_minimal_payload(), source_label="mapping-input")

    assert result.success is True
    assert result.loaded is not None
    assert result.errors == ()
    assert isinstance(result.loaded.worldspec, WorldSpec)
    assert result.loaded.worldspec.id == "worldspec-example"
    assert result.loaded.source_type == "mapping"
    assert result.loaded.source_label == "mapping-input"
    assert result.loaded.schema_version == "0.2"


def test_load_worldspec_accepts_valid_json_string() -> None:
    payload = json.dumps(_minimal_payload())

    result = load_worldspec(payload, source_label="json-string-input")

    assert result.success is True
    assert result.loaded is not None
    assert result.loaded.worldspec.id == "worldspec-example"
    assert result.loaded.source_type == "json"
    assert result.loaded.source_label == "json-string-input"
    assert result.loaded.schema_version == "0.2"


def test_load_worldspec_accepts_valid_json_bytes() -> None:
    payload = json.dumps(_minimal_payload()).encode("utf-8")

    result = load_worldspec(payload)

    assert result.success is True
    assert result.loaded is not None
    assert result.loaded.worldspec.root.id == "cell-root"
    assert result.loaded.source_type == "json"
    assert result.loaded.source_label is None


def test_load_worldspec_rejects_unsupported_input_type() -> None:
    result = load_worldspec(["not", "a", "mapping"])

    assert result.success is False
    assert result.loaded is None
    assert len(result.errors) == 1
    error = result.errors[0]
    assert error.code == "unsupported_input"
    assert error.path is None
    assert error.source_type == "unsupported"
    assert error.source_label is None


def test_load_worldspec_rejects_malformed_json() -> None:
    result = load_worldspec('{"schema_version": ')

    assert result.success is False
    assert result.loaded is None
    assert len(result.errors) == 1
    error = result.errors[0]
    assert error.code == "parse_error"
    assert error.path is None
    assert error.source_type == "json"


def test_load_worldspec_rejects_unsupported_schema_version_with_pointer_path() -> None:
    payload = _minimal_payload()
    payload["schema_version"] = "9.9"

    result = load_worldspec(payload)

    assert result.success is False
    assert result.loaded is None
    assert any(
        error.code == "schema_validation_error" and error.path == "/schema_version"
        for error in result.errors
    )


def test_load_worldspec_rejects_invalid_root_cell_with_pointer_path() -> None:
    payload = _minimal_payload()
    payload["root"]["id"] = ""

    result = load_worldspec(payload, source_label="invalid-root-input")

    assert result.success is False
    assert result.loaded is None
    assert any(
        error.code == "schema_validation_error"
        and error.path == "/root/id"
        and error.source_type == "mapping"
        and error.source_label == "invalid-root-input"
        for error in result.errors
    )
