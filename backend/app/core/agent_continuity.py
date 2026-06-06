from __future__ import annotations

from typing import Any, Mapping

from app.schemas.agent_continuity import (
    AgentAutonomousActionEvidence,
    AgentConsolidationArtifact,
    AgentContinuityArtifact,
    AgentContinuityDiagnostic,
    AgentContinuityEvaluationRequest,
    AgentContinuityEvaluationResponse,
    ClientScriptedAutonomyRejection,
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
    "provider trace",
    "provider_trace",
    "provider secret",
    "provider_secret",
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


def evaluate_agent_continuity(
    *,
    world_id: str,
    agent_id: str,
    tick_id: int,
    world_time_seconds: int,
    request: AgentContinuityEvaluationRequest,
    public_event_index: Mapping[str, Mapping[str, str]] | None = None,
) -> AgentContinuityEvaluationResponse:
    diagnostics: list[AgentContinuityDiagnostic] = []
    event_index = public_event_index or {}
    if _contains_private_marker(request.model_dump()):
        diagnostics.append(
            _diagnostic(
                "private_marker_detected",
                "continuity evidence contains private or unsupported markers",
                "/",
            )
        )
    if not request.evidence_refs:
        diagnostics.append(
            _diagnostic(
                "missing_public_evidence_ref",
                "accepted continuity artifacts require at least one public evidence ref",
                "/evidence_refs",
            )
        )

    if request.state == "action":
        diagnostics.extend(
            _action_diagnostics(
                request.autonomous_action_evidence,
                public_event_index=event_index,
            )
        )
    if request.state == "reacting":
        if request.event_reaction_evidence is None or not request.event_reaction_evidence.event_refs:
            diagnostics.append(
                _diagnostic(
                    "missing_public_event_ref",
                    "reacting state requires public event reaction refs",
                    "/event_reaction_evidence/event_refs",
                )
            )
        elif missing_ref_path := _first_missing_public_event_ref(
            request.event_reaction_evidence.event_refs,
            public_event_index=event_index,
        ):
            diagnostics.append(
                _diagnostic(
                    "non_canonical_event_ref",
                    "reacting state requires canonical public event refs",
                    missing_ref_path,
                )
            )
    if request.state == "consolidating":
        diagnostics.extend(
            _consolidation_diagnostics(
                world_id=world_id,
                agent_id=agent_id,
                artifact=request.consolidation_artifact,
                public_event_index=event_index,
            )
        )
    if _per_tick_mutation_flag(request.model_dump()):
        diagnostics.append(
            _diagnostic(
                "automatic_per_tick_mutation",
                "continuity evidence must not model personality, long-term memory, or skill mutation as automatic per-tick drift",
                "/",
            )
        )

    redaction_status = (
        "failed"
        if any(diagnostic.code == "private_marker_detected" for diagnostic in diagnostics)
        else "passed"
    )
    if diagnostics:
        return AgentContinuityEvaluationResponse(
            world_id=world_id,
            agent_id=agent_id,
            status="rejected",
            diagnostics=diagnostics,
            scripted_autonomy_rejection=(
                ClientScriptedAutonomyRejection()
                if any(diagnostic.code == "client_scripted_autonomy" for diagnostic in diagnostics)
                else None
            ),
            redaction_status=redaction_status,
        )

    continuity_artifact = AgentContinuityArtifact(
        world_id=world_id,
        agent_id=agent_id,
        tick_id=tick_id,
        world_time_seconds=world_time_seconds,
        state=request.state,
        perception_summary_refs=request.perception_summary_refs,
        working_memory_summary=request.working_memory_summary,
        long_term_memory_summary_refs=request.long_term_memory_summary_refs,
        personality_summary_refs=request.personality_summary_refs,
        skill_summary_refs=request.skill_summary_refs,
        intent_summary=request.intent_summary,
        autonomous_action_evidence=request.autonomous_action_evidence,
        event_reaction_evidence=request.event_reaction_evidence,
        consolidation_phase_refs=(
            [
                {
                    "ref_id": request.consolidation_artifact.phase_id,
                    "ref_type": "agent_consolidation_phase",
                    "role": "active_phase",
                }
            ]
            if request.consolidation_artifact is not None
            else []
        ),
        evidence_refs=request.evidence_refs,
        redaction_status="passed",
    )
    return AgentContinuityEvaluationResponse(
        world_id=world_id,
        agent_id=agent_id,
        status="accepted",
        continuity_artifact=continuity_artifact,
        consolidation_artifact=request.consolidation_artifact,
        redaction_status="passed",
    )


def _action_diagnostics(
    evidence: AgentAutonomousActionEvidence | None,
    *,
    public_event_index: Mapping[str, Mapping[str, str]],
) -> list[AgentContinuityDiagnostic]:
    if evidence is None:
        return [
            _diagnostic(
                "missing_autonomous_action_evidence",
                "action state requires public autonomous action evidence",
                "/autonomous_action_evidence",
            )
        ]
    diagnostics: list[AgentContinuityDiagnostic] = []
    if evidence.input_provenance != "worldengine_agent_loop":
        diagnostics.append(
            _diagnostic(
                "client_scripted_autonomy",
                "accepted autonomous action evidence requires WorldEngine-owned provenance",
                "/autonomous_action_evidence/input_provenance",
            )
        )
    if not evidence.action_event_refs:
        diagnostics.append(
            _diagnostic(
                "missing_action_event_ref",
                "accepted autonomous action evidence requires public action event refs",
                "/autonomous_action_evidence/action_event_refs",
            )
        )
    elif missing_ref_path := _first_missing_public_event_ref(
        evidence.action_event_refs,
        public_event_index=public_event_index,
        required_source="agent.loop",
        base_path="/autonomous_action_evidence/action_event_refs",
    ):
        diagnostics.append(
            _diagnostic(
                "non_canonical_action_event_ref",
                "accepted autonomous action evidence requires canonical Agent loop action event refs",
                missing_ref_path,
            )
        )
    if not evidence.action_result_refs:
        diagnostics.append(
            _diagnostic(
                "missing_action_result_ref",
                "accepted autonomous action evidence requires public action result refs",
                "/autonomous_action_evidence/action_result_refs",
            )
        )
    elif missing_ref_path := _first_missing_public_event_ref(
        evidence.action_result_refs,
        public_event_index=public_event_index,
        required_source="agent.loop",
        base_path="/autonomous_action_evidence/action_result_refs",
    ):
        diagnostics.append(
            _diagnostic(
                "non_canonical_action_result_ref",
                "accepted autonomous action evidence requires canonical Agent loop action result refs",
                missing_ref_path,
            )
        )
    return diagnostics


def _consolidation_diagnostics(
    *,
    world_id: str,
    agent_id: str,
    artifact: AgentConsolidationArtifact | None,
    public_event_index: Mapping[str, Mapping[str, str]],
) -> list[AgentContinuityDiagnostic]:
    if artifact is None:
        return [
            _diagnostic(
                "missing_consolidation_artifact",
                "consolidating state requires a public consolidation artifact",
                "/consolidation_artifact",
            )
        ]
    diagnostics: list[AgentContinuityDiagnostic] = []
    if artifact.world_id != world_id:
        diagnostics.append(
            _diagnostic(
                "world_id_mismatch",
                "consolidation artifact world_id must match request path",
                "/consolidation_artifact/world_id",
            )
        )
    if artifact.agent_id != agent_id:
        diagnostics.append(
            _diagnostic(
                "agent_id_mismatch",
                "consolidation artifact agent_id must match request path",
                "/consolidation_artifact/agent_id",
            )
        )
    if missing_ref_path := _first_missing_public_event_ref(
        artifact.event_refs,
        public_event_index=public_event_index,
        base_path="/consolidation_artifact/event_refs",
    ):
        diagnostics.append(
            _diagnostic(
                "non_canonical_event_ref",
                "consolidation event refs must point to canonical public events",
                missing_ref_path,
            )
        )
    return diagnostics


def _first_missing_public_event_ref(
    refs: list[Any],
    *,
    public_event_index: Mapping[str, Mapping[str, str]],
    required_source: str | None = None,
    base_path: str = "/event_refs",
) -> str | None:
    for index, ref in enumerate(refs):
        ref_type = getattr(ref, "ref_type", None)
        ref_id = getattr(ref, "ref_id", None)
        if ref_type != "event" or not isinstance(ref_id, str):
            return f"{base_path}/{index}"
        event = public_event_index.get(ref_id)
        if event is None:
            return f"{base_path}/{index}/ref_id"
        if required_source is not None and event.get("source") != required_source:
            return f"{base_path}/{index}/ref_id"
    return None


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


def _per_tick_mutation_flag(value: Any) -> bool:
    if isinstance(value, dict):
        for key, item in value.items():
            lowered_key = str(key).casefold()
            if "per_tick" in lowered_key and item is True:
                return True
            if _per_tick_mutation_flag(item):
                return True
    if isinstance(value, list):
        return any(_per_tick_mutation_flag(item) for item in value)
    if isinstance(value, str):
        lowered = value.casefold()
        return "per-tick mutation" in lowered or "automatic per-tick" in lowered
    return False


def _diagnostic(
    code: str,
    message: str,
    path: str,
) -> AgentContinuityDiagnostic:
    return AgentContinuityDiagnostic(
        code=code,
        message=message,
        path=path,
    )
