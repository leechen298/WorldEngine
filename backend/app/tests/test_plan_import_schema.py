import pytest
from pydantic import ValidationError

from app.schemas.world_generation import (
    GenerationDiagnostic,
    GenerationPlan,
    PlanCell,
    PlanImportRequest,
    PlanImportResult,
    PlanImportSource,
)


def _plan() -> GenerationPlan:
    return GenerationPlan(
        id="generic-plan",
        version="1",
        root=PlanCell(id="root", child_cells=[{"id": "child"}]),
    )


def _source() -> PlanImportSource:
    return PlanImportSource(
        source_kind="ai_assisted",
        source_id="source-alpha",
        provider_label="generic-provider",
        model_label="generic-model",
        metadata={"redacted_trace": "trace-alpha"},
    )


def test_plan_import_schema_accepts_redacted_provider_independent_provenance() -> None:
    request = PlanImportRequest(
        import_id="import-alpha",
        plan=_plan(),
        source=_source(),
        metadata={"operator_review": "accepted"},
    )

    assert request.import_id == "import-alpha"
    assert request.source.redacted is True
    assert request.source.provider_label == "generic-provider"
    assert request.source.metadata == {"redacted_trace": "trace-alpha"}
    assert request.metadata == {"operator_review": "accepted"}


def test_plan_import_result_accepts_passed_plan_and_source() -> None:
    result = PlanImportResult(
        import_id="import-alpha",
        validation_status="passed",
        accepted_plan=_plan(),
        source=_source(),
    )

    assert result.validation_status == "passed"
    assert result.accepted_plan is not None
    assert result.accepted_plan.id == "generic-plan"
    assert result.source is not None
    assert result.diagnostics == []


def test_plan_import_result_rejects_inconsistent_status_payloads() -> None:
    with pytest.raises(ValidationError):
        PlanImportResult(import_id="import-alpha", validation_status="passed")

    with pytest.raises(ValidationError):
        PlanImportResult(
            import_id="import-alpha",
            validation_status="failed",
            accepted_plan=_plan(),
            source=_source(),
            diagnostics=[
                GenerationDiagnostic(
                    code="invalid_import",
                    severity="error",
                    message="invalid import",
                )
            ],
        )


def test_plan_import_schema_rejects_empty_required_fields() -> None:
    factories = [
        lambda: PlanImportSource(source_kind="ai_assisted", source_id=""),
        lambda: PlanImportRequest(import_id="", plan=_plan(), source=_source()),
        lambda: PlanImportResult(
            import_id="",
            validation_status="failed",
            diagnostics=[
                GenerationDiagnostic(
                    code="invalid_import",
                    severity="error",
                    message="invalid import",
                )
            ],
        ),
    ]

    for factory in factories:
        with pytest.raises(ValidationError):
            factory()


def test_plan_import_schema_rejects_prompt_and_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        PlanImportSource(source_kind="ai_assisted", prompt="hidden prompt")

    with pytest.raises(ValidationError):
        PlanImportRequest(
            import_id="import-alpha",
            plan=_plan(),
            source=_source(),
            prompt="hidden prompt",
        )

    assert "prompt" not in PlanImportSource.model_fields
    assert "prompt" not in PlanImportRequest.model_fields
    assert "api_key" not in PlanImportSource.model_fields


def test_plan_import_schema_rejects_prompt_fields_inside_untrusted_plan_payload() -> None:
    with pytest.raises(ValidationError):
        PlanImportRequest(
            import_id="import-alpha",
            plan={
                "id": "generic-plan",
                "version": "1",
                "root": {"id": "root"},
                "prompt": "hidden prompt",
            },
            source=_source(),
        )

    with pytest.raises(ValidationError):
        PlanImportRequest(
            import_id="import-alpha",
            plan={
                "id": "generic-plan",
                "version": "1",
                "root": {"id": "root", "prompt": "hidden prompt"},
            },
            source=_source(),
        )
