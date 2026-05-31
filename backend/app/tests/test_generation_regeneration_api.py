from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _cell(cell_id: str, label: str, child_id: str | None = None) -> Dict[str, Any]:
    cell: Dict[str, Any] = {
        "id": cell_id,
        "label": label,
        "entity_refs": [{"id": f"entity.{cell_id}", "kind": "agent"}],
        "metadata": {"visibility": "public"},
        "child_cells": [],
    }
    if child_id:
        cell["child_cells"] = [_cell(child_id, f"{label} Child")]
    return cell


def _template_generation_request(request_id: str = "regen-template-base") -> Dict[str, Any]:
    return {
        "request_id": request_id,
        "template": {
            "id": "template.regen",
            "version": "1",
            "root": _cell("root", "Root", "child"),
            "metadata": {"category": "generic"},
            "constraints": {},
        },
        "seed_material": {"seed": "base-seed"},
        "constraints": {},
    }


def _preview_request(request_id: str = "regen-preview-base") -> Dict[str, Any]:
    return {
        "request_id": request_id,
        "source_kind": "template",
        "template_request": _template_generation_request(f"{request_id}-template"),
    }


def _worldspec_payload() -> Dict[str, Any]:
    return {
        "schema_version": "0.2",
        "id": "worldspec-runtime-ready",
        "label": "Runtime Ready WorldSpec",
        "root": {
            "id": "cell-root",
            "label": "Cell Root",
            "kind": "world",
            "entity_refs": [],
            "child_cells": [],
            "metadata": {},
        },
        "metadata": {"purpose": "runtime-readiness-test"},
    }


def _client() -> TestClient:
    return TestClient(create_app())


def test_regenerate_returns_lineage_preview_and_runtime_readiness() -> None:
    client = _client()

    response = client.post(
        "/world/generation/regenerate",
        json={
            "request_id": "regen-success",
            "base_preview_request": _preview_request(),
            "parent_generation_id": "generation-parent",
            "reason": "operator requested a new seed",
            "seed_material": {"seed": "regen-seed"},
            "constraints": {"max_child_cells": 3},
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == 0
    assert body["msg"] == "ok"

    data = body["data"]
    assert data["request_id"] == "regen-success"
    assert data["validation_status"] == "passed"
    assert data["diagnostics"] == []

    preview = data["preview"]
    assert preview["request_id"] == "regen-success"
    assert preview["validation_status"] == "passed"
    assert preview["worldspec_preview"]["root"]["id"] == "root"

    lineage = data["lineage"]
    assert lineage["lineage_id"].startswith("lineage-")
    assert lineage["source_request_id"] == "regen-preview-base"
    assert lineage["parent_generation_id"] == "generation-parent"
    assert lineage["regenerated_generation_id"] == preview["metadata"]["generation_id"]
    assert lineage["reason"] == "operator requested a new seed"
    assert lineage["changed_fields"] == ["constraints", "seed_material"]

    readiness = data["runtime_readiness"]
    assert readiness["validation_status"] == "passed"
    assert readiness["loader_passed"] is True
    assert readiness["runtime_context_passed"] is True
    assert readiness["does_not_mutate_runtime"] is True
    assert readiness["diagnostics"] == []
    summary = readiness["runtime_context_summary"]
    assert summary["root_cell_id"] == "root"
    assert "worldspec" not in summary
    assert "root" not in summary


def test_regenerate_changes_lineage_when_seed_changes_without_mutating_input() -> None:
    client = _client()
    base_preview_request = _preview_request("regen-stable-base")
    original = deepcopy(base_preview_request)

    first = client.post(
        "/world/generation/regenerate",
        json={
            "request_id": "regen-seed-a",
            "base_preview_request": base_preview_request,
            "seed_material": {"seed": "a"},
        },
    ).json()["data"]
    second = client.post(
        "/world/generation/regenerate",
        json={
            "request_id": "regen-seed-b",
            "base_preview_request": base_preview_request,
            "seed_material": {"seed": "b"},
        },
    ).json()["data"]

    assert first["lineage"]["lineage_id"] != second["lineage"]["lineage_id"]
    assert (
        first["preview"]["metadata"]["generation_id"]
        != second["preview"]["metadata"]["generation_id"]
    )
    assert base_preview_request == original


def test_invalid_regeneration_request_uses_existing_api_error_envelope() -> None:
    client = _client()

    response = client.post(
        "/world/generation/regenerate",
        json={
            "request_id": "regen-extra",
            "base_preview_request": _preview_request("regen-extra-base"),
            "provider_trace": "must not be accepted",
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "extra_forbidden"


def test_regeneration_generation_failure_returns_failed_result_and_diagnostics() -> None:
    client = _client()

    response = client.post(
        "/world/generation/regenerate",
        json={
            "request_id": "regen-failed-generation",
            "base_preview_request": _preview_request("regen-failed-generation-base"),
            "constraints": {"allowed_entity_kinds": ["location"]},
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["validation_status"] == "failed"
    assert data["preview"]["validation_status"] == "failed"
    assert data["preview"]["worldspec_preview"] is None
    assert data["runtime_readiness"]["validation_status"] == "failed"
    assert data["runtime_readiness"]["loader_passed"] is False
    assert [item["code"] for item in data["diagnostics"]] == [
        "entity_kind_not_allowed",
        "entity_kind_not_allowed",
        "preview_failed",
    ]


def test_runtime_readiness_validates_candidate_worldspec() -> None:
    client = _client()

    response = client.post(
        "/world/generation/runtime-readiness",
        json={
            "request_id": "readiness-success",
            "worldspec": _worldspec_payload(),
            "source_label": "candidate.manual",
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["request_id"] == "readiness-success"
    assert data["validation_status"] == "passed"
    assert data["loader_passed"] is True
    assert data["runtime_context_passed"] is True
    assert data["does_not_mutate_runtime"] is True
    assert data["diagnostics"] == []
    assert data["runtime_context_summary"] == {
        "worldspec_id": "worldspec-runtime-ready",
        "schema_version": "0.2",
        "root_cell_id": "cell-root",
        "root_cell_type": "world",
        "source_type": "mapping",
        "source_label": "candidate.manual",
        "metadata": {},
    }


def test_runtime_readiness_failure_returns_loader_diagnostics() -> None:
    client = _client()
    invalid_worldspec = _worldspec_payload()
    invalid_worldspec["schema_version"] = "9.9"

    response = client.post(
        "/world/generation/runtime-readiness",
        json={
            "request_id": "readiness-failed",
            "worldspec": invalid_worldspec,
            "source_label": "candidate.invalid",
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["validation_status"] == "failed"
    assert data["loader_passed"] is False
    assert data["runtime_context_passed"] is False
    assert data["runtime_context_summary"] is None
    assert data["does_not_mutate_runtime"] is True
    assert data["diagnostics"][0]["code"] == "schema_validation_error"
    assert data["diagnostics"][0]["path"] == "/schema_version"
