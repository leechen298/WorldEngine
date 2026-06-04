from pydantic import ValidationError

from app.schemas.world import (
    HandoffManifest,
    PublicProviderReadiness,
    PublicWorldCreateRequest,
    PublicWorldCreationResponse,
)
from app.schemas.world_generation import (
    GenerationDiagnostic,
    GenerationMetadata,
    TemplateCell,
    TemplateGenerationRequest,
    TemplateGenerationResult,
    WorldTemplate,
)


def test_world_template_accepts_generic_recursive_cells_and_defaults() -> None:
    template = WorldTemplate(
        id="generic-template",
        version="1",
        root=TemplateCell(
            id="root",
            label="Generic Root",
            entity_refs=[{"id": "entity-alpha", "kind": "generic-agent"}],
            child_cells=[{"id": "child"}],
        ),
    )

    assert template.id == "generic-template"
    assert template.version == "1"
    assert template.root.id == "root"
    assert template.root.child_cells[0].id == "child"
    assert template.root.entity_refs[0].kind == "generic-agent"
    assert template.metadata == {}
    assert template.constraints == {}


def test_generation_schema_rejects_empty_required_fields() -> None:
    with_errors = [
        lambda: TemplateCell(id=""),
        lambda: WorldTemplate(id="", version="1", root={"id": "root"}),
        lambda: WorldTemplate(id="template", version="", root={"id": "root"}),
        lambda: TemplateGenerationRequest(request_id="", template={"id": "template", "version": "1", "root": {"id": "root"}}),
        lambda: GenerationDiagnostic(code="", severity="error", message="message"),
        lambda: GenerationDiagnostic(code="invalid", severity="", message="message"),
        lambda: GenerationDiagnostic(code="invalid", severity="error", message=""),
    ]

    for factory in with_errors:
        try:
            factory()
        except ValidationError:
            continue
        raise AssertionError("expected validation error")


def test_generation_result_contains_worldspec_only_for_passed_status() -> None:
    metadata = GenerationMetadata(
        generation_id="generation-1",
        request_id="request-1",
        template_id="template",
        template_version="1",
        seed_digest="seed-digest",
        validation_status="passed",
    )
    result = TemplateGenerationResult(
        worldspec={"schema_version": "0.2", "id": "spec", "root": {"id": "root"}},
        metadata=metadata,
    )

    assert result.worldspec is not None
    assert result.metadata.diagnostics_count == 0
    assert result.diagnostics == []


def test_generation_result_rejects_worldspec_for_failed_status() -> None:
    metadata = GenerationMetadata(
        generation_id="generation-1",
        request_id="request-1",
        template_id="template",
        template_version="1",
        seed_digest="seed-digest",
        validation_status="failed",
        diagnostics_count=1,
    )

    try:
        TemplateGenerationResult(
            worldspec={"schema_version": "0.2", "id": "spec", "root": {"id": "root"}},
            metadata=metadata,
            diagnostics=[
                GenerationDiagnostic(
                    code="invalid_template",
                    severity="error",
                    message="template is invalid",
                )
            ],
        )
    except ValidationError:
        return
    raise AssertionError("expected validation error")


def test_public_handoff_manifest_schema_forbids_private_extra_fields() -> None:
    provider = PublicProviderReadiness(
        provider_class="deepseek_api",
        provider_readiness="configured",
        credential_source_class="environment",
        model_label="deepseek-v4-flash",
    )
    manifest = HandoffManifest(provider=provider)

    assert manifest.redaction.secrets_included is False
    assert manifest.redaction.private_prompts_included is False
    assert manifest.redaction.provider_raw_traces_included is False

    try:
        HandoffManifest(
            provider=provider,
            api_key="must-not-be-accepted",
        )
    except ValidationError:
        return
    raise AssertionError("expected validation error")


def test_public_world_creation_schema_requires_top_level_public_fields() -> None:
    request = PublicWorldCreateRequest(world_prompt="a public world")
    response = PublicWorldCreationResponse(
        world_id="world-1",
        public_initial_state={
            "summary": "created",
            "public_agents": [
                {
                    "agent_id": "agent-1",
                    "display_name": "Observer",
                    "location": "origin",
                    "public_status": "idle",
                    "visible_action": "observing",
                }
            ],
        },
        visualization={"tilemap": {"width": 1, "height": 1}, "entities": []},
    )

    dumped = response.model_dump()
    assert request.world_prompt == "a public world"
    assert dumped["world_id"] == "world-1"
    assert dumped["status"] == "created"
    assert "public_initial_state" in dumped
    assert "visualization" in dumped
    assert "api_key" not in str(dumped).lower()
