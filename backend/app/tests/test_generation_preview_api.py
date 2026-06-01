from __future__ import annotations

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


def _template_generation_request(request_id: str = "preview-template") -> Dict[str, Any]:
    return {
        "request_id": request_id,
        "template": {
            "id": "template.basic",
            "version": "1",
            "root": _cell("root", "Root", "child"),
            "metadata": {"category": "generic"},
            "constraints": {},
        },
        "seed_material": {"seed": "template-seed"},
        "constraints": {},
    }


def _plan_generation_request(request_id: str = "preview-plan") -> Dict[str, Any]:
    return {
        "request_id": request_id,
        "plan": {
            "id": "plan.basic",
            "version": "1",
            "root": _cell("plan-root", "Plan Root", "plan-child"),
            "metadata": {"category": "generic"},
            "constraints": {},
        },
        "seed_material": {"seed": "plan-seed"},
        "constraints": {},
    }


def _import_request(request_id: str = "preview-import") -> Dict[str, Any]:
    plan_request = _plan_generation_request(request_id)
    return {
        "import_id": "import.basic",
        "plan": plan_request["plan"],
        "source": {
            "source_kind": "ai_assisted",
            "source_id": "source.redacted",
            "provider_label": "provider.redacted",
            "model_label": "model.redacted",
            "redacted": True,
            "metadata": {"trace": "redacted"},
        },
        "metadata": {"reviewed": True},
    }


def _client() -> TestClient:
    return TestClient(create_app())


def test_template_generation_preview_returns_standard_success_envelope() -> None:
    client = _client()

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-template",
            "source_kind": "template",
            "template_request": _template_generation_request(),
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == 0
    assert body["msg"] == "ok"

    data = body["data"]
    assert data["request_id"] == "preview-template"
    assert data["source_kind"] == "template"
    assert data["validation_status"] == "passed"
    assert data["diagnostics"] == []
    assert data["worldspec_preview"]["root"]["id"] == "root"
    assert data["worldspec_preview"]["root"]["child_cells"][0]["id"] == "child"

    metadata = data["metadata"]
    assert metadata["source_kind"] == "template"
    assert metadata["generation_id"].startswith("generation-")
    assert metadata["template_id"] == "template.basic"
    assert metadata["preview_summary"] == {
        "root_world_id": data["worldspec_preview"]["id"],
        "root_label": "Root",
        "total_cell_count": 2,
        "max_child_depth": 2,
        "entity_ref_count": 2,
    }
    assert "template_request" not in metadata
    assert "prompt" not in str(body).lower()


def test_plan_generation_preview_returns_public_worldspec_preview() -> None:
    client = _client()

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-plan",
            "source_kind": "plan",
            "plan_request": _plan_generation_request(),
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["source_kind"] == "plan"
    assert data["validation_status"] == "passed"
    assert data["worldspec_preview"]["root"]["label"] == "Plan Root"
    assert data["metadata"]["plan_id"] == "plan.basic"
    assert data["metadata"]["preview_summary"]["total_cell_count"] == 2


def test_imported_plan_preview_redacts_import_provenance() -> None:
    client = _client()

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-import",
            "source_kind": "imported_plan",
            "import_request": _import_request(),
            "seed_material": {"seed": "import-seed"},
            "constraints": {},
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["source_kind"] == "imported_plan"
    assert data["validation_status"] == "passed"
    assert data["worldspec_preview"]["root"]["id"] == "plan-root"
    assert data["metadata"]["import_source"] == {
        "source_kind": "ai_assisted",
        "source_id": "source.redacted",
        "provider_label": "provider.redacted",
        "model_label": "model.redacted",
        "redacted": True,
    }
    assert "accepted_plan" not in str(data)


def test_imported_plan_preview_redacts_sensitive_worldspec_metadata() -> None:
    client = _client()
    import_request = _import_request("preview-sensitive-import")
    import_request["plan"]["metadata"] = {
        "safe": "keep",
        "prompt": "private prompt",
        "provider_trace": "private trace",
    }
    import_request["plan"]["root"]["metadata"] = {
        "visibility": "public",
        "prompt": "private cell prompt",
    }

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-sensitive-import",
            "source_kind": "imported_plan",
            "import_request": import_request,
        },
    )

    assert response.status_code == 200
    worldspec = response.json()["data"]["worldspec_preview"]
    assert worldspec["metadata"]["safe"] == "keep"
    assert "prompt" not in worldspec["metadata"]
    assert "provider_trace" not in worldspec["metadata"]
    assert worldspec["root"]["metadata"]["visibility"] == "public"
    assert "prompt" not in worldspec["root"]["metadata"]


def test_preview_summary_bounds_root_label() -> None:
    client = _client()
    template_request = _template_generation_request("preview-long-label")
    template_request["template"]["root"]["label"] = "x" * 200

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-long-label",
            "source_kind": "template",
            "template_request": template_request,
        },
    )

    assert response.status_code == 200
    root_label = response.json()["data"]["metadata"]["preview_summary"]["root_label"]
    assert len(root_label) <= 120


def test_invalid_template_preview_returns_failed_result_without_worldspec() -> None:
    client = _client()
    template_request = _template_generation_request("preview-invalid-template")
    template_request["template"]["root"]["child_cells"][0]["id"] = "root"

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-invalid-template",
            "source_kind": "template",
            "template_request": template_request,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == 0
    data = body["data"]
    assert data["validation_status"] == "failed"
    assert data["worldspec_preview"] is None
    assert [item["code"] for item in data["diagnostics"]] == ["duplicate_cell_id"]


def test_invalid_import_preview_returns_failed_result_without_generation() -> None:
    client = _client()
    import_request = _import_request("preview-invalid-import")
    import_request["source"]["redacted"] = False

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-invalid-import",
            "source_kind": "imported_plan",
            "import_request": import_request,
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["validation_status"] == "failed"
    assert data["worldspec_preview"] is None
    assert [item["code"] for item in data["diagnostics"]] == [
        "unredacted_import_source"
    ]


def test_imported_plan_preview_rejects_sensitive_redacted_provenance() -> None:
    client = _client()
    import_request = _import_request("preview-sensitive-provenance")
    import_request["source"]["metadata"] = {
        "safe_trace": "trace-alpha",
        "prompt": "private prompt",
        "provider_trace": "private trace",
        "access_token": "private token",
    }

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-sensitive-provenance",
            "source_kind": "imported_plan",
            "import_request": import_request,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == 0
    data = body["data"]
    assert data["validation_status"] == "failed"
    assert data["worldspec_preview"] is None
    assert data["metadata"]["import_source"] is None
    assert [item["code"] for item in data["diagnostics"]] == [
        "sensitive_import_provenance",
        "sensitive_import_provenance",
        "sensitive_import_provenance",
    ]
    assert [item["path"] for item in data["diagnostics"]] == [
        "/source/metadata/prompt",
        "/source/metadata/provider_trace",
        "/source/metadata/access_token",
    ]
    assert "private prompt" not in str(body)
    assert "private trace" not in str(body)
    assert "private token" not in str(body)


def test_imported_plan_preview_allows_redacted_usage_metric_provenance() -> None:
    client = _client()
    import_request = _import_request("preview-usage-metrics")
    import_request["source"]["metadata"] = {
        "usage": {
            "prompt_tokens": 12,
            "completion_tokens": 8,
            "total_tokens": 20,
            "token_count": 20,
            "token_usage": {"cached_tokens": 2},
        }
    }

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-usage-metrics",
            "source_kind": "imported_plan",
            "import_request": import_request,
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["validation_status"] == "passed"
    assert data["worldspec_preview"] is not None
    assert data["metadata"]["import_source"] == {
        "source_kind": "ai_assisted",
        "source_id": "source.redacted",
        "provider_label": "provider.redacted",
        "model_label": "model.redacted",
        "redacted": True,
    }
    assert "prompt_tokens" not in str(data["metadata"]["import_source"])


def test_imported_plan_generation_failure_does_not_return_import_source() -> None:
    client = _client()

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-import-generation-failed",
            "source_kind": "imported_plan",
            "import_request": _import_request("preview-import-generation-failed"),
            "constraints": {"allowed_entity_kinds": ["location"]},
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["source_kind"] == "imported_plan"
    assert data["validation_status"] == "failed"
    assert data["worldspec_preview"] is None
    assert data["metadata"]["import_source"] is None
    assert [item["code"] for item in data["diagnostics"]] == [
        "entity_kind_not_allowed",
        "entity_kind_not_allowed",
    ]


def test_invalid_plan_preview_returns_failed_result_without_worldspec() -> None:
    client = _client()
    plan_request = _plan_generation_request("preview-invalid-plan")
    plan_request["plan"]["root"]["child_cells"][0]["id"] = "plan-root"

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-invalid-plan",
            "source_kind": "plan",
            "plan_request": plan_request,
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["validation_status"] == "failed"
    assert data["worldspec_preview"] is None
    assert [item["code"] for item in data["diagnostics"]] == ["duplicate_cell_id"]


def test_preview_request_shape_errors_use_existing_api_error_envelope() -> None:
    client = _client()

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-mismatch",
            "source_kind": "template",
            "plan_request": _plan_generation_request("preview-mismatch"),
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["msg"]
    assert body["data"]["errors"]


def test_preview_request_rejects_missing_source_payload() -> None:
    client = _client()

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-missing-source",
            "source_kind": "template",
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "invalid_preview_source"


def test_preview_request_rejects_multiple_source_payloads() -> None:
    client = _client()

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-multiple-sources",
            "source_kind": "template",
            "template_request": _template_generation_request("preview-multiple-sources"),
            "plan_request": _plan_generation_request("preview-multiple-sources"),
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "invalid_preview_source"


def test_preview_request_rejects_nested_prompt_fields() -> None:
    client = _client()
    template_request = _template_generation_request("preview-nested-prompt")
    template_request["template"]["root"]["prompt"] = "must not be accepted"

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-nested-prompt",
            "source_kind": "template",
            "template_request": template_request,
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "extra_forbidden"


def test_preview_request_rejects_nested_plan_request_extras() -> None:
    client = _client()
    plan_request = _plan_generation_request("preview-plan-extra")
    plan_request["provider_trace"] = "must not be accepted"

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-plan-extra",
            "source_kind": "plan",
            "plan_request": plan_request,
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "extra_forbidden"


def test_preview_request_rejects_unexpected_fields() -> None:
    client = _client()

    response = client.post(
        "/world/generation/preview",
        json={
            "request_id": "preview-extra",
            "source_kind": "template",
            "template_request": _template_generation_request("preview-extra"),
            "prompt": "must not be accepted",
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "extra_forbidden"
