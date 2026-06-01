from app.core.world_generation import (
    generate_worldspec_from_plan,
    import_generation_plan,
    validate_plan_import,
)
from app.schemas.world_generation import (
    GenerationPlan,
    PlanCell,
    PlanGenerationRequest,
    PlanImportRequest,
    PlanImportSource,
)


def _plan() -> GenerationPlan:
    return GenerationPlan(
        id="generic-plan",
        version="1",
        root=PlanCell(
            id="root",
            label="Generic Root",
            entity_refs=[{"id": "entity-alpha", "kind": "generic-agent"}],
            child_cells=[{"id": "child", "label": "Generic Child"}],
        ),
        constraints={"allowed_entity_kinds": ["generic-agent"]},
    )


def _source(**overrides: object) -> PlanImportSource:
    payload = {
        "source_kind": "ai_assisted",
        "source_id": "source-alpha",
        "provider_label": "generic-provider",
        "model_label": "generic-model",
        "metadata": {"redacted_trace": "trace-alpha"},
    }
    payload.update(overrides)
    return PlanImportSource(**payload)


def _request(
    plan: object = None,
    source: object = None,
    metadata: object = None,
) -> PlanImportRequest:
    return PlanImportRequest(
        import_id="import-alpha",
        plan=plan or _plan(),
        source=source or _source(),
        metadata={} if metadata is None else metadata,
    )


def test_plan_import_accepts_valid_plan_and_compiler_can_use_it() -> None:
    request = _request()

    assert validate_plan_import(request) == []

    result = import_generation_plan(request)

    assert result.validation_status == "passed"
    assert result.accepted_plan is not None
    assert result.accepted_plan.id == "generic-plan"
    assert result.source is not None
    assert result.source.metadata == {"redacted_trace": "trace-alpha"}

    generated = generate_worldspec_from_plan(
        PlanGenerationRequest(
            request_id="request-alpha",
            plan=result.accepted_plan,
            seed_material={"variant": "alpha"},
        )
    )

    assert generated.worldspec is not None
    assert generated.metadata.validation_status == "passed"


def test_plan_import_rejects_invalid_plan_through_generation_plan_validator() -> None:
    request = _request(
        plan=GenerationPlan(
            id="generic-plan",
            version="1",
            root=PlanCell(id="root", child_cells=[{"id": "root"}]),
        )
    )

    result = import_generation_plan(request)

    assert result.validation_status == "failed"
    assert result.accepted_plan is None
    assert result.source is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("duplicate_cell_id", "/root/child_cells/0/id")
    ]


def test_plan_import_rejects_unredacted_or_non_json_provenance() -> None:
    request = _request(
        source=_source(redacted=False, metadata={"not-json": {"unstable"}})
    )

    diagnostics = validate_plan_import(request)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("unredacted_import_source", "/source/redacted"),
        ("unsupported_import_provenance", "/source/metadata"),
    ]

    result = import_generation_plan(request)
    assert result.validation_status == "failed"
    assert result.accepted_plan is None
    assert result.source is None


def test_plan_import_rejects_sensitive_fields_inside_redacted_metadata() -> None:
    request = _request(
        source=_source(
            metadata={
                "safe_trace": "trace-alpha",
                "prompt": "private prompt",
                "provider_trace": "private provider trace",
                "access_token": "private token",
                "apiKey": "private api key",
                "providerTrace": "private camel trace",
            }
        )
    )

    diagnostics = validate_plan_import(request)

    assert [(d.code, d.path) for d in diagnostics] == [
        ("sensitive_import_provenance", "/source/metadata/prompt"),
        ("sensitive_import_provenance", "/source/metadata/provider_trace"),
        ("sensitive_import_provenance", "/source/metadata/access_token"),
        ("sensitive_import_provenance", "/source/metadata/apiKey"),
        ("sensitive_import_provenance", "/source/metadata/providerTrace"),
    ]

    result = import_generation_plan(request)
    assert result.validation_status == "failed"
    assert result.accepted_plan is None
    assert result.source is None
    assert "private prompt" not in str(result.model_dump())
    assert "private provider trace" not in str(result.model_dump())
    assert "private token" not in str(result.model_dump())


def test_plan_import_rejects_non_json_import_metadata_without_seed_misdiagnosis() -> None:
    request = _request(metadata={"not-json": {"unstable"}})

    result = import_generation_plan(request)

    assert result.validation_status == "failed"
    assert result.accepted_plan is None
    assert [(d.code, d.path) for d in result.diagnostics] == [
        ("unsupported_import_metadata", "/metadata")
    ]


def test_plan_import_diagnostics_are_deterministic() -> None:
    request = _request(
        plan=GenerationPlan(id="generic-plan", version="unsupported", root=PlanCell(id="root")),
        source=_source(redacted=False, metadata={"not-json": {"unstable"}}),
        metadata={"also-not-json": {"unstable"}},
    )

    first = import_generation_plan(request)
    second = import_generation_plan(request)

    assert first.model_dump() == second.model_dump()
    assert [(d.code, d.path) for d in first.diagnostics] == [
        ("unredacted_import_source", "/source/redacted"),
        ("unsupported_import_provenance", "/source/metadata"),
        ("unsupported_import_metadata", "/metadata"),
        ("unsupported_plan_version", "/version"),
    ]
