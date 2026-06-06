from __future__ import annotations

from typing import Any, Collection
from uuid import uuid4

from app.schemas.external_projection import (
    DiagnosticDialogueArtifact,
    DiagnosticDialogueEvaluationRequest,
    DiagnosticDialogueEvaluationResponse,
    ExternalProjectionEvidenceRef,
    NarrativeProjectionArtifact,
    NarrativeProjectionRequest,
    NarrativeProjectionResponse,
    ProjectionBoundaryDecision,
    ProjectionBoundaryDiagnostic,
)


_PRIVATE_MARKERS = (
    "api_key",
    "api key",
    "apikey",
    "authorization",
    "bearer",
    "chain-of-thought",
    "chain_of_thought",
    "chain of thought",
    "credential",
    "hidden context",
    "hidden_context",
    "private evaluator data",
    "private_evaluator_data",
    "private goal",
    "private_goal",
    "private memory",
    "private_memory",
    "private prompt",
    "private_prompt",
    "provider secret",
    "provider_secret",
    "provider trace",
    "provider_trace",
    "raw prompt",
    "raw_prompt",
    "raw provider request",
    "raw_provider_request",
    "raw provider response",
    "raw_provider_response",
    "raw request",
    "raw_request",
    "raw response",
    "raw_response",
    "raw thought",
    "raw_thought",
    "secret",
    "self_state",
    "sk-live-",
    "sk-test-",
    "token",
)


def evaluate_narrative_projection(
    *,
    world_id: str,
    request: NarrativeProjectionRequest,
    public_event_ids: Collection[str],
    public_snapshot_ids: Collection[str],
) -> NarrativeProjectionResponse:
    diagnostics = _base_diagnostics(request.model_dump())
    diagnostics.extend(
        _required_evidence_diagnostics(
            [
                request.source_event_refs,
                request.source_snapshot_refs,
                request.source_agent_continuity_refs,
            ],
            path="/source_refs",
        )
    )
    diagnostics.extend(
        _ref_diagnostics(
            request.source_event_refs,
            allowed_ref_type="event",
            known_ids=public_event_ids,
            base_path="/source_event_refs",
        )
    )
    diagnostics.extend(
        _ref_diagnostics(
            request.source_snapshot_refs,
            allowed_ref_type="snapshot",
            known_ids=public_snapshot_ids,
            base_path="/source_snapshot_refs",
        )
    )
    diagnostics.extend(
        _type_only_ref_diagnostics(
            request.source_agent_continuity_refs,
            allowed_ref_type="agent_continuity",
            base_path="/source_agent_continuity_refs",
        )
    )
    redaction_status = _redaction_status(diagnostics)
    if diagnostics:
        return NarrativeProjectionResponse(
            world_id=world_id,
            status="rejected",
            boundary_decision=_decision(
                status="rejected",
                classification="external_projection",
                reason="narrative projection remains outside canonical state and failed boundary checks",
                redaction_status=redaction_status,
            ),
            diagnostics=diagnostics,
            redaction_status=redaction_status,
        )

    artifact = NarrativeProjectionArtifact(
        projection_id=f"projection-{uuid4()}",
        world_id=world_id,
        source_event_refs=request.source_event_refs,
        source_snapshot_refs=request.source_snapshot_refs,
        source_agent_continuity_refs=request.source_agent_continuity_refs,
        public_narrative_summary=request.public_narrative_summary,
        projection_provenance=request.projection_provenance,
        redaction_status="passed",
    )
    return NarrativeProjectionResponse(
        world_id=world_id,
        status="accepted",
        boundary_decision=_decision(
            status="accepted",
            classification="external_projection",
            reason="narrative projection is external inspection evidence and does not mutate canonical state",
        ),
        narrative_projection=artifact,
    )


def evaluate_diagnostic_dialogue(
    *,
    world_id: str,
    agent_id: str,
    request: DiagnosticDialogueEvaluationRequest,
    public_event_ids: Collection[str],
) -> DiagnosticDialogueEvaluationResponse:
    diagnostics = _base_diagnostics(request.model_dump())
    diagnostics.extend(
        _required_evidence_diagnostics(
            [
                request.source_event_refs,
                request.source_agent_continuity_refs,
            ],
            path="/source_refs",
        )
    )
    diagnostics.extend(
        _ref_diagnostics(
            request.source_event_refs,
            allowed_ref_type="event",
            known_ids=public_event_ids,
            base_path="/source_event_refs",
        )
    )
    diagnostics.extend(
        _type_only_ref_diagnostics(
            request.source_agent_continuity_refs,
            allowed_ref_type="agent_continuity",
            base_path="/source_agent_continuity_refs",
        )
    )
    redaction_status = _redaction_status(diagnostics)
    if diagnostics:
        return DiagnosticDialogueEvaluationResponse(
            world_id=world_id,
            agent_id=agent_id,
            status="rejected",
            boundary_decision=_decision(
                status="rejected",
                classification="out_of_world_diagnostic",
                reason="diagnostic dialogue remains outside world state and failed boundary checks",
                redaction_status=redaction_status,
            ),
            diagnostics=diagnostics,
            redaction_status=redaction_status,
        )

    artifact = DiagnosticDialogueArtifact(
        dialogue_id=f"diagnostic-{uuid4()}",
        world_id=world_id,
        agent_id=agent_id,
        question_summary=request.question_summary,
        response_summary=request.response_summary,
        source_event_refs=request.source_event_refs,
        source_agent_continuity_refs=request.source_agent_continuity_refs,
        diagnostic_provenance=request.diagnostic_provenance,
        redaction_status="passed",
    )
    return DiagnosticDialogueEvaluationResponse(
        world_id=world_id,
        agent_id=agent_id,
        status="accepted",
        boundary_decision=_decision(
            status="accepted",
            classification="out_of_world_diagnostic",
            reason="diagnostic dialogue is external inspection evidence and does not enter world timeline or Agent memory",
        ),
        diagnostic_dialogue=artifact,
    )


def _base_diagnostics(value: Any) -> list[ProjectionBoundaryDiagnostic]:
    diagnostics: list[ProjectionBoundaryDiagnostic] = []
    if _contains_private_marker(value):
        diagnostics.append(
            _diagnostic(
                "private_marker_detected",
                "projection or diagnostic evidence contains private or unsupported markers",
                "/",
            )
        )
    if _mutation_flag(value):
        diagnostics.append(
            _diagnostic(
                "canonical_mutation_attempt",
                "projection and diagnostic surfaces must not mutate canonical state, events, dialogue, or Agent memory by default",
                "/",
            )
        )
    if _textual_mutation_claim(value):
        diagnostics.append(
            _diagnostic(
                "textual_canonical_mutation_claim",
                "projection and diagnostic summaries must not claim direct canonical mutation, event append, Agent memory write, or in-world dialogue recording",
                "/",
            )
        )
    return diagnostics


def _required_evidence_diagnostics(
    ref_groups: list[list[ExternalProjectionEvidenceRef]],
    *,
    path: str,
) -> list[ProjectionBoundaryDiagnostic]:
    if any(ref_groups):
        return []
    return [
        _diagnostic(
            "missing_public_evidence_ref",
            "accepted projection and diagnostic artifacts require at least one public evidence ref",
            path,
        )
    ]


def _ref_diagnostics(
    refs: list[ExternalProjectionEvidenceRef],
    *,
    allowed_ref_type: str,
    known_ids: Collection[str],
    base_path: str,
) -> list[ProjectionBoundaryDiagnostic]:
    diagnostics = _type_only_ref_diagnostics(
        refs,
        allowed_ref_type=allowed_ref_type,
        base_path=base_path,
    )
    for index, ref in enumerate(refs):
        if ref.ref_type == allowed_ref_type and ref.ref_id not in known_ids:
            diagnostics.append(
                _diagnostic(
                    "non_canonical_public_ref",
                    "projection source refs must point to canonical public evidence",
                    f"{base_path}/{index}/ref_id",
                )
            )
    return diagnostics


def _type_only_ref_diagnostics(
    refs: list[ExternalProjectionEvidenceRef],
    *,
    allowed_ref_type: str,
    base_path: str,
) -> list[ProjectionBoundaryDiagnostic]:
    diagnostics: list[ProjectionBoundaryDiagnostic] = []
    for index, ref in enumerate(refs):
        if ref.ref_type != allowed_ref_type:
            diagnostics.append(
                _diagnostic(
                    "invalid_public_ref_type",
                    "projection source refs must use the expected public ref type",
                    f"{base_path}/{index}/ref_type",
                )
            )
    return diagnostics


def _contains_private_marker(value: Any) -> bool:
    if isinstance(value, dict):
        return any(
            _string_has_private_marker(str(key)) or _contains_private_marker(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_private_marker(item) for item in value)
    if isinstance(value, str):
        return _string_has_private_marker(value)
    return False


def _string_has_private_marker(value: str) -> bool:
    lowered = value.casefold()
    return any(marker in lowered for marker in _PRIVATE_MARKERS)


def _mutation_flag(value: Any) -> bool:
    forbidden_keys = {
        "canonical_state_mutation_applied",
        "canonical_event_appended",
        "agent_memory_write_applied",
        "in_world_dialogue_recorded",
    }
    if isinstance(value, dict):
        for key, item in value.items():
            if str(key) in forbidden_keys and item is True:
                return True
            if _mutation_flag(item):
                return True
    if isinstance(value, list):
        return any(_mutation_flag(item) for item in value)
    return False


def _textual_mutation_claim(value: Any) -> bool:
    if isinstance(value, dict):
        return any(_textual_mutation_claim(item) for item in value.values())
    if isinstance(value, list):
        return any(_textual_mutation_claim(item) for item in value)
    if not isinstance(value, str):
        return False
    lowered = value.casefold()
    mutation_terms = (
        "mutated canonical",
        "mutate canonical",
        "changed canonical",
        "canonical state changed",
        "appended a canonical event",
        "canonical event appended",
        "added a canonical event",
        "wrote agent memory",
        "write agent memory",
        "agent memory write",
        "recorded in-world dialogue",
        "in-world dialogue recorded",
        "became in-world dialogue",
    )
    return any(term in lowered for term in mutation_terms)


def _redaction_status(diagnostics: list[ProjectionBoundaryDiagnostic]) -> str:
    return "failed" if any(item.code == "private_marker_detected" for item in diagnostics) else "passed"


def _diagnostic(code: str, message: str, path: str) -> ProjectionBoundaryDiagnostic:
    return ProjectionBoundaryDiagnostic(code=code, message=message, path=path)


def _decision(
    *,
    status: str,
    classification: str,
    reason: str,
    redaction_status: str = "passed",
) -> ProjectionBoundaryDecision:
    return ProjectionBoundaryDecision(
        status=status,
        classification=classification,
        reason=reason,
        redaction_status=redaction_status,
    )
