"""Non-live public worldview generation helpers."""

from __future__ import annotations

import hashlib
import re
from typing import List

from app.schemas.world import PublicProviderReadiness
from app.schemas.world_generation import (
    GenerationDiagnostic,
    PublicGeneratedWorldModel,
    PublicWorldCreationSummary,
    WorldviewGenerationRequest,
    WorldviewGenerationResponse,
    WorldviewGenerationValidationMetadata,
)


def generate_worldview_response(
    request: WorldviewGenerationRequest,
    provider: PublicProviderReadiness,
) -> WorldviewGenerationResponse:
    premise_digest = hashlib.sha256(
        request.worldview_premise.encode("utf-8")
    ).hexdigest()[:12]
    generation_id = f"worldview-generation-{premise_digest}"
    world_id = f"world-{premise_digest}"
    public_tags = _public_premise_tags(request.worldview_premise)
    public_model = _public_world_model(
        premise_digest=premise_digest,
        public_tags=public_tags,
        constraints_keys=sorted(request.public_constraints.keys()),
    )

    diagnostics: List[GenerationDiagnostic] = []
    warnings: List[str] = []
    blockers: List[str] = []
    generation_mode = "blocked"
    generation_status = "blocked"
    creation_mode = "blocked"
    llm_backed = False
    provider_backed = False
    provider_status = "blocked"
    runtime_ready = "blocked"

    if provider.provider_class == "mock":
        generation_mode = "safe_mock"
        generation_status = "fallback"
        creation_mode = "safe_mock_non_live"
        provider_status = "safe_mock_non_live"
        runtime_ready = "true"
        warnings.append("safe mock generation is non-live and not provider-backed")
    elif provider.provider_readiness == "not_configured":
        if request.allow_deterministic_fallback:
            generation_mode = "deterministic_fallback"
            generation_status = "fallback"
            creation_mode = "deterministic_generic_fallback"
            provider_status = "deterministic_fallback"
            runtime_ready = "true"
            warnings.append("provider not configured; deterministic fallback is labeled non-LLM")
        else:
            generation_mode = "not_configured"
            generation_status = "not_configured"
            creation_mode = "provider_not_configured"
            provider_status = "not_configured"
            blockers.append("provider_not_configured")
            diagnostics.append(
                _diagnostic(
                    "provider_not_configured",
                    "provider is not configured for LLM-backed worldview generation",
                    "/provider",
                )
            )
    elif provider.provider_readiness == "configured":
        generation_mode = "blocked"
        generation_status = "blocked"
        creation_mode = "blocked"
        provider_status = "blocked"
        blockers.append("live_provider_call_not_authorized")
        diagnostics.append(
            _diagnostic(
                "live_provider_call_not_authorized",
                "live provider-backed world generation is not authorized in this package",
                "/provider",
            )
        )
    else:
        blockers.append("unsupported_or_blocked_provider")
        diagnostics.append(
            _diagnostic(
                "unsupported_or_blocked_provider",
                "provider is unsupported or blocked for worldview generation",
                "/provider",
            )
        )

    deterministic_generic_fallback_detected = creation_mode == "deterministic_generic_fallback"
    summary = PublicWorldCreationSummary(
        premise_specific="true" if runtime_ready == "true" else "unknown",
        system_digestible=runtime_ready == "true",
        redacted=True,
        runtime_ready=runtime_ready,
        distinct_from_deterministic_generic_response=runtime_ready == "true",
        creation_mode=creation_mode,
        llm_backed=llm_backed,
        provider_backed=provider_backed,
        deterministic_generic_fallback_detected=deterministic_generic_fallback_detected,
        public_initial_state_refs={
            "world_id": world_id,
            "agent_ref": f"agent.{premise_digest[:6]}",
            "environment_ref": f"environment.{premise_digest[:6]}",
        },
        visualization_refs={
            "tilemap_ref": f"tilemap.{premise_digest[:6]}",
            "entity_count": len(public_model.agents_outline) + len(public_model.entities_outline),
        },
    )
    validation = WorldviewGenerationValidationMetadata(
        premise_specific=summary.premise_specific,
        system_digestible=summary.system_digestible,
        runtime_ready=summary.runtime_ready,
        deterministic_generic_response=False,
        deterministic_generic_fallback_detected=deterministic_generic_fallback_detected,
        redaction_status="passed",
        provider_generation_status=provider_status,
        diagnostics_count=len(diagnostics),
    )
    return WorldviewGenerationResponse(
        world_id=world_id,
        generation_id=generation_id,
        generation_status=generation_status,
        generation_mode=generation_mode,
        creation_mode=creation_mode,
        llm_backed=llm_backed,
        provider_backed=provider_backed,
        deterministic_generic_fallback_detected=deterministic_generic_fallback_detected,
        provider_class=provider.provider_class,
        model_label=provider.model_label,
        premise_digest=premise_digest,
        public_world_model=public_model,
        world_creation_summary=summary,
        validation_metadata=validation,
        warnings=warnings,
        blockers=blockers,
        diagnostics=diagnostics,
    )


def _public_world_model(
    *,
    premise_digest: str,
    public_tags: List[str],
    constraints_keys: List[str],
) -> PublicGeneratedWorldModel:
    tag_label = "-".join(public_tags[:2]) if public_tags else "public"
    short = premise_digest[:6]
    return PublicGeneratedWorldModel(
        title_label=f"generated-world-{tag_label}-{short}",
        premise_summary=(
            f"public premise digest {premise_digest}; "
            f"{len(public_tags)} public premise tags extracted"
        ),
        world_parameters_outline={
            "premise_digest": premise_digest,
            "public_tags": public_tags,
            "constraint_keys": constraints_keys,
            "generation_contract": "0.9.2",
        },
        locations_outline=[
            {
                "location_id": f"location.{short}.origin",
                "public_label": "premise-linked origin",
                "premise_tags": public_tags[:3],
            }
        ],
        entities_outline=[
            {
                "entity_id": f"entity.{short}.environment",
                "kind": "environment",
                "premise_tags": public_tags[:3],
            }
        ],
        agents_outline=[
            {
                "agent_id": f"agent.{short}",
                "public_role": "observer",
                "premise_tags": public_tags[:3],
            }
        ],
        items_outline=[],
        environment_outline={
            "environment_id": f"environment.{short}",
            "premise_tags": public_tags,
            "public_state": "generated candidate",
        },
        rules_outline=[
            {
                "rule_id": f"rule.{short}.premise_boundary",
                "kind": "boundary",
                "public_summary": "generated content must remain tied to public premise tags",
            }
        ],
        boundary_conditions=[
            "public generated model only",
            "no raw prompt or provider trace evidence",
            "rule schema deferred to 0.9.3",
        ],
        runtime_readiness_inputs={
            "worldspec_candidate": "not_persisted",
            "rule_schema_ready": False,
            "can_be_checked_for_structure": True,
        },
        visualization_refs={
            "tilemap_ref": f"tilemap.{short}",
            "agent_ref": f"agent.{short}",
        },
    )


def _public_premise_tags(premise: str) -> List[str]:
    ascii_tokens = re.findall(r"[a-zA-Z0-9]{3,24}", premise.lower())
    tags: List[str] = []
    for token in ascii_tokens:
        if token not in tags:
            tags.append(token)
    non_ascii_chunks = re.findall(r"[^\W\d_]{2,24}", premise, flags=re.UNICODE)
    for chunk in non_ascii_chunks:
        if chunk.isascii():
            continue
        script = "cjk" if any("\u4e00" <= char <= "\u9fff" for char in chunk) else "unicode"
        digest = hashlib.sha256(chunk.encode("utf-8")).hexdigest()[:8]
        tag = f"{script}_{digest}"
        if tag not in tags:
            tags.append(tag)
    if not tags and premise:
        digest = hashlib.sha256(premise.encode("utf-8")).hexdigest()[:8]
        tags.append(f"unicode_{digest}")
    return tags[:6]


def _diagnostic(code: str, message: str, path: str) -> GenerationDiagnostic:
    return GenerationDiagnostic(
        code=code,
        severity="error",
        message=message,
        path=path,
    )
