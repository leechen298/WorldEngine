from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from app.agent.provider_config import provider_readiness_from_env
from app.agent.worldview_generation import generate_worldview_response
from app.core.rule_linked_evolution import (
    build_rule_bound_session_event_candidate,
    evaluate_world_event_candidate,
)
from app.core.world_session import InMemoryWorldSessionStore
from app.schemas.api import ApiResponse
from app.schemas.agent_memory import (
    EpisodicMemoryRecord,
    MemoryEvidenceRef,
    WorkingMemoryRecord,
)
from app.schemas.event import Event
from app.schemas.external_projection import (
    ExternalProjectionEvidenceRef,
    ProjectionBoundaryDiagnostic,
)
from app.schemas.params import ParamPatchItem
from app.schemas.runtime import RuntimeControlState, RuntimeRunRequest
from app.schemas.session import (
    SessionDiagnosticInspectionRequest,
    SessionDiagnosticInspectionResponse,
    SessionAgentEventEvidence,
    SessionAgentListResponse,
    SessionAgentMemoryConsolidationRequest,
    SessionAgentMemoryConsolidationResponse,
    SessionAgentMemorySummaryResponse,
    SessionAgentPublicState,
    SessionAgentStepRequest,
    SessionAgentStepResponse,
    SessionCreateRequest,
    SessionDirectionSummaryResponse,
    SessionEventEvidence,
    SessionGenerationSummary,
    SessionNarrativeProjectionRequest,
    SessionNarrativeProjectionResponse,
    SessionListResponse,
    SessionRuleSummaryResponse,
    SessionRunEvidenceResponse,
    SessionRuntimeDelta,
    SessionSnapshotEvidence,
    SessionSnapshotListResponse,
    SessionStatusResponse,
    SessionInspectionTickRange,
    WorldSession,
)
from app.schemas.world_direction import (
    WorldDirectionClassification,
    WorldDirectionRequest,
    WorldDirectionResponse,
)
from app.schemas.world_evolution import (
    SessionEvolutionStepRequest,
    SessionEvolutionStepResponse,
    WorldEventLegalityDiagnostic,
    WorldEventLegalityResult,
)
from app.schemas.world_generation import (
    GeneratedRuleParameterSet,
    WorldviewGenerationRequest,
    WorldviewGenerationResponse,
)

router = APIRouter(prefix="/sessions", tags=["sessions"])


def get_session_store(request: Request) -> InMemoryWorldSessionStore:
    return request.app.state.world_session_store


def _unknown_session() -> HTTPException:
    return HTTPException(status_code=404, detail="Unknown session_id")


def _timeline_label(session_id: str) -> str:
    return f"timeline branch for session {session_id}"


def _direction_event_payload(
    *,
    session_id: str,
    world_id: str,
    request_body: WorldDirectionRequest,
    response_status: str,
    classification: WorldDirectionClassification,
    direction_id: str | None = None,
) -> dict[str, object]:
    redacted = getattr(classification, "redaction_status") == "redacted"
    payload: dict[str, object] = {
        "session_id": session_id,
        "world_id": world_id,
        "status": response_status,
        "instruction_text_length": len(request_body.instruction_text),
        "branch_id": None if redacted else request_body.branch_id,
        "classification": classification.model_dump(),
        "apply_after_tick": request_body.apply_after_tick,
        "expires_after_tick": request_body.expires_after_tick,
        "public_context_keys": [] if redacted else sorted(request_body.public_context.keys()),
        "direct_state_mutation_applied": False,
    }
    if direction_id is not None:
        payload["direction_id"] = direction_id
    return payload


def _append_session_direction_event(
    *,
    request: Request,
    session_id: str,
    world_id: str,
    event_type: str,
    request_body: WorldDirectionRequest,
    response_status: str,
    classification: WorldDirectionClassification,
    direction_id: str | None = None,
) -> None:
    runtime_state = request.app.state.runtime_engine.get_state()
    request.app.state.event_log.append(
        Event(
            id=str(uuid4()),
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            type=event_type,
            source="director",
            payload=_direction_event_payload(
                session_id=session_id,
                world_id=world_id,
                request_body=request_body,
                response_status=response_status,
                classification=classification,
                direction_id=direction_id,
            ),
            created_at=datetime.now(timezone.utc).isoformat(),
        )
    )


def _append_session_evolution_event(
    *,
    request: Request,
    event_type: str,
    source: str,
    payload: dict[str, object],
) -> str:
    runtime_state = request.app.state.runtime_engine.get_state()
    event_id = str(uuid4())
    request.app.state.event_log.append(
        Event(
            id=event_id,
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            type=event_type,
            source=source,
            payload=payload,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
    )
    return event_id


def _append_session_agent_event(
    *,
    request: Request,
    event_type: str,
    payload: dict[str, object],
) -> str:
    runtime_state = request.app.state.runtime_engine.get_state()
    event_id = str(uuid4())
    request.app.state.event_log.append(
        Event(
            id=event_id,
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            type=event_type,
            source="session.agent",
            payload=payload,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
    )
    return event_id


def _memory_evidence_ref(event_id: str, ref_type: str = "event") -> MemoryEvidenceRef:
    return MemoryEvidenceRef(type=ref_type, id=event_id)


def _inspection_ref(
    ref_id: str,
    ref_type: str,
    role: str,
    metadata: dict[str, object] | None = None,
) -> ExternalProjectionEvidenceRef:
    return ExternalProjectionEvidenceRef(
        ref_id=ref_id,
        ref_type=ref_type,
        role=role,
        metadata=metadata or {},
    )


def _inspection_diagnostic(
    code: str,
    message: str,
    path: str,
) -> ProjectionBoundaryDiagnostic:
    return ProjectionBoundaryDiagnostic(code=code, message=message, path=path)


def _mutation_requested(request_body: object) -> bool:
    return any(
        bool(getattr(request_body, field, False))
        for field in (
            "canonical_state_mutation_applied",
            "canonical_event_appended",
            "agent_memory_write_applied",
            "in_world_dialogue_recorded",
        )
    )


def _event_matches_inspection(
    event: Event,
    *,
    tick_start: int,
    tick_end: int,
    branch_id: str | None,
    agent_id: str | None,
) -> bool:
    if event.tick_id < tick_start or event.tick_id > tick_end:
        return False
    if branch_id is not None:
        event_branch_id = event.payload.get("branch_id")
        if event_branch_id is not None and event_branch_id != branch_id:
            return False
    if agent_id is not None:
        event_agent_id = event.payload.get("agent_id")
        if event_agent_id is not None and event_agent_id != agent_id:
            return False
    return True


def _session_memory_refs(
    *,
    request: Request,
    session: WorldSession,
    agent_id: str,
) -> list[ExternalProjectionEvidenceRef]:
    working = request.app.state.agent_memory_store.list_working_memory(
        agent_id=agent_id,
        world_id=session.world_id,
        limit=10,
    )
    episodic = request.app.state.agent_memory_store.list_episodic_memory(
        agent_id=agent_id,
        world_id=session.world_id,
        limit=10,
    )
    refs: list[ExternalProjectionEvidenceRef] = []
    refs.extend(
        _inspection_ref(
            record.memory_id,
            "summary",
            "working_memory",
            {"source": record.source},
        )
        for record in working
    )
    refs.extend(
        _inspection_ref(
            record.memory_id,
            "summary",
            "episodic_memory",
            {"source": record.source},
        )
        for record in episodic
    )
    return refs


def _known_session_memory_ids(
    *,
    request: Request,
    session: WorldSession,
    agent_id: str | None,
    store: InMemoryWorldSessionStore,
) -> set[str]:
    agent_ids = [agent_id] if agent_id is not None else [
        agent.agent_id for agent in store.list_agents(session.session_id) or []
    ]
    memory_ids: set[str] = set()
    for current_agent_id in agent_ids:
        working = request.app.state.agent_memory_store.list_working_memory(
            agent_id=current_agent_id,
            world_id=session.world_id,
            limit=200,
        )
        episodic = request.app.state.agent_memory_store.list_episodic_memory(
            agent_id=current_agent_id,
            world_id=session.world_id,
            limit=200,
        )
        memory_ids.update(record.memory_id for record in working)
        memory_ids.update(record.memory_id for record in episodic)
    return memory_ids


def _known_snapshot_ids(request: Request) -> set[str]:
    snapshots, _ = request.app.state.snapshot_store.list(limit=200)
    return {snapshot.id for snapshot in snapshots}


def _validated_caller_refs(
    refs: list[ExternalProjectionEvidenceRef],
    *,
    allowed_ref_type: str,
    known_ids: set[str],
    base_path: str,
) -> tuple[list[ExternalProjectionEvidenceRef], list[ProjectionBoundaryDiagnostic]]:
    diagnostics: list[ProjectionBoundaryDiagnostic] = []
    for index, ref in enumerate(refs):
        if ref.ref_type != allowed_ref_type:
            diagnostics.append(
                _inspection_diagnostic(
                    "invalid_public_ref_type",
                    "inspection source refs must use the expected public ref type",
                    f"{base_path}/{index}/ref_type",
                )
            )
            continue
        if ref.ref_id not in known_ids:
            diagnostics.append(
                _inspection_diagnostic(
                    "non_canonical_public_ref",
                    "inspection source refs must point to canonical public evidence",
                    f"{base_path}/{index}/ref_id",
                )
            )
    return ([] if diagnostics else refs), diagnostics


def _session_inspection_sources(
    *,
    request: Request,
    session: WorldSession,
    tick_start: int,
    tick_end: int,
    branch_id: str | None,
    agent_id: str | None,
    store: InMemoryWorldSessionStore,
) -> tuple[
    list[ExternalProjectionEvidenceRef],
    list[ExternalProjectionEvidenceRef],
    list[ExternalProjectionEvidenceRef],
    list[ProjectionBoundaryDiagnostic],
]:
    diagnostics: list[ProjectionBoundaryDiagnostic] = []
    events = [
        event
        for event in request.app.state.event_log.snapshot()
        if _event_matches_inspection(
            event,
            tick_start=tick_start,
            tick_end=tick_end,
            branch_id=branch_id,
            agent_id=agent_id,
        )
    ]
    event_refs = [
        _inspection_ref(
            event.id,
            "event",
            "source_event",
            {"event_type": event.type, "tick_id": event.tick_id},
        )
        for event in events
    ]
    agent_refs: list[ExternalProjectionEvidenceRef] = []
    memory_refs: list[ExternalProjectionEvidenceRef] = []
    if agent_id is not None:
        agent = store.get_agent(session.session_id, agent_id)
        if agent is None:
            raise HTTPException(status_code=404, detail="Unknown agent_id")
        memory_refs = _session_memory_refs(
            request=request,
            session=session,
            agent_id=agent_id,
        )
        if event_refs or memory_refs:
            agent_refs.append(
                _inspection_ref(
                    agent.agent_id,
                    "agent_continuity",
                    "agent_public_state",
                    {
                        "state": agent.state,
                        "public_status": agent.public_status,
                    },
                )
            )
    if not event_refs and not agent_refs and not memory_refs:
        diagnostics.append(
            _inspection_diagnostic(
                "missing_public_evidence_ref",
                "accepted inspection artifacts require public session evidence",
                "/source_refs",
            )
        )
    return event_refs, agent_refs, memory_refs, diagnostics


def _inspection_tick_range(
    tick_start: int,
    tick_end: int | None,
    request: Request,
) -> SessionInspectionTickRange:
    runtime_state = request.app.state.runtime_engine.get_state()
    return SessionInspectionTickRange(
        start=tick_start,
        end=runtime_state.tick_id if tick_end is None else tick_end,
    )


def _blocked_evolution_result(code: str, message: str, path: str) -> WorldEventLegalityResult:
    return WorldEventLegalityResult(
        status="blocked",
        legality_classification="blocked",
        diagnostics=[
            WorldEventLegalityDiagnostic(
                code=code,
                message=message,
                path=path,
            )
        ],
        direct_state_mutation_applied=False,
    )


@router.post("", response_model=ApiResponse[WorldSession], operation_id="create_world_session")
def create_world_session(
    request_body: SessionCreateRequest,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[WorldSession]:
    return ApiResponse(data=store.create(request_body))


def _generation_summary(
    request_id: str,
    generation: WorldviewGenerationResponse,
) -> SessionGenerationSummary:
    return SessionGenerationSummary(
        request_id=request_id,
        generation_id=generation.generation_id,
        generation_status=generation.generation_status,
        generation_mode=generation.generation_mode,
        creation_mode=generation.creation_mode,
        provider_class=generation.provider_class,
        provider_backed=generation.provider_backed,
        llm_backed=generation.llm_backed,
        deterministic_generic_fallback_detected=(
            generation.deterministic_generic_fallback_detected
        ),
        premise_digest=generation.premise_digest,
        runtime_ready=generation.validation_metadata.runtime_ready,
        blockers=generation.blockers,
        warnings=generation.warnings,
        public_world_model_refs={
            "title_label": generation.public_world_model.title_label,
            "premise_summary": generation.public_world_model.premise_summary,
            "public_initial_state_refs": (
                generation.world_creation_summary.public_initial_state_refs
            ),
            "visualization_refs": generation.world_creation_summary.visualization_refs,
        },
    )


@router.post(
    "/from-worldview",
    response_model=ApiResponse[WorldSession],
    operation_id="create_world_session_from_worldview",
)
def create_world_session_from_worldview(
    request_body: WorldviewGenerationRequest,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[WorldSession]:
    provider = provider_readiness_from_env()
    generation = generate_worldview_response(request_body, provider)
    session_status = (
        "created"
        if generation.validation_metadata.runtime_ready == "true"
        else "blocked"
    )
    session_request = SessionCreateRequest(
        world_id=generation.world_id,
        public_label=generation.public_world_model.title_label,
    )
    summary = _generation_summary(request_body.request_id, generation)
    return ApiResponse(
        data=store.create(
            session_request,
            status=session_status,
            generation_summary=summary,
        )
    )


@router.post(
    "/{session_id}/rules",
    response_model=ApiResponse[SessionRuleSummaryResponse],
    operation_id="attach_world_session_rules",
)
def attach_world_session_rules(
    session_id: str,
    request_body: GeneratedRuleParameterSet,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionRuleSummaryResponse]:
    result = store.attach_rules(session_id, request_body)
    if result is None:
        raise _unknown_session()
    return ApiResponse(data=result)


@router.get(
    "/{session_id}/rules",
    response_model=ApiResponse[SessionRuleSummaryResponse],
    operation_id="get_world_session_rules",
)
def get_world_session_rules(
    session_id: str,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionRuleSummaryResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()
    if session.rule_summary is None:
        return ApiResponse(
            data=SessionRuleSummaryResponse(
                session_id=session.session_id,
                world_id=session.world_id,
                attachment_status="not_attached",
            )
        )
    return ApiResponse(
        data=SessionRuleSummaryResponse(
            session_id=session.session_id,
            world_id=session.world_id,
            attachment_status="attached",
            summary=session.rule_summary,
            validation=session.rule_validation,
            redaction_status=session.rule_summary.redaction_status,
        )
    )


@router.post(
    "/{session_id}/directions",
    response_model=ApiResponse[WorldDirectionResponse],
    operation_id="submit_world_session_direction",
)
def submit_world_session_direction(
    session_id: str,
    request_body: WorldDirectionRequest,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[WorldDirectionResponse]:
    classified = store.classify_direction(session_id, request_body)
    if classified is None:
        raise _unknown_session()
    session, classification = classified

    if classification.allowed:
        queued = store.queue_direction(session_id, request_body, classification)
        if queued is None:
            raise _unknown_session()
        _, queue_item = queued
        _append_session_direction_event(
            request=request,
            session_id=session_id,
            world_id=session.world_id,
            event_type="world.session_direction.queued",
            request_body=request_body,
            response_status="queued",
            classification=classification,
            direction_id=queue_item.direction_id,
        )
        return ApiResponse(
            data=WorldDirectionResponse(
                world_id=session.world_id,
                status="queued",
                classification=classification,
                queue_item=queue_item,
                public_explanation=classification.public_reason,
                direct_state_mutation_applied=False,
            )
        )

    updated = store.reject_direction(session_id)
    if updated is None:
        raise _unknown_session()
    _append_session_direction_event(
        request=request,
        session_id=session_id,
        world_id=session.world_id,
        event_type="world.session_direction.rejected",
        request_body=request_body,
        response_status="rejected",
        classification=classification,
    )
    return ApiResponse(
        data=WorldDirectionResponse(
            world_id=session.world_id,
            status="rejected",
            classification=classification,
            queue_item=None,
            rejection_reason=classification.category,
            public_explanation=classification.public_reason,
            direct_state_mutation_applied=False,
        )
    )


@router.get(
    "/{session_id}/directions",
    response_model=ApiResponse[SessionDirectionSummaryResponse],
    operation_id="get_world_session_directions",
)
def get_world_session_directions(
    session_id: str,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionDirectionSummaryResponse]:
    summary = store.direction_summary(session_id)
    if summary is None:
        raise _unknown_session()
    return ApiResponse(data=summary)


@router.post(
    "/{session_id}/narrative/project",
    response_model=ApiResponse[SessionNarrativeProjectionResponse],
    operation_id="project_session_narrative",
)
def project_session_narrative(
    session_id: str,
    request_body: SessionNarrativeProjectionRequest,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionNarrativeProjectionResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()
    tick_range = _inspection_tick_range(
        request_body.tick_start,
        request_body.tick_end,
        request,
    )
    diagnostics: list[ProjectionBoundaryDiagnostic] = []
    if tick_range.end < tick_range.start:
        diagnostics.append(
            _inspection_diagnostic(
                "invalid_tick_range",
                "tick_end must be greater than or equal to tick_start",
                "/tick_end",
            )
        )
    if _mutation_requested(request_body):
        diagnostics.append(
            _inspection_diagnostic(
                "canonical_mutation_attempt",
                "inspection surfaces must not mutate canonical state, events, dialogue, or Agent memory",
                "/",
            )
        )
    caller_event_refs, caller_event_diagnostics = _validated_caller_refs(
        request_body.source_event_refs,
        allowed_ref_type="event",
        known_ids={event.id for event in request.app.state.event_log.snapshot()},
        base_path="/source_event_refs",
    )
    caller_snapshot_refs, caller_snapshot_diagnostics = _validated_caller_refs(
        request_body.source_snapshot_refs,
        allowed_ref_type="snapshot",
        known_ids=_known_snapshot_ids(request),
        base_path="/source_snapshot_refs",
    )
    caller_agent_refs, caller_agent_diagnostics = _validated_caller_refs(
        request_body.source_agent_refs,
        allowed_ref_type="agent_continuity",
        known_ids={agent.agent_id for agent in store.list_agents(session_id) or []},
        base_path="/source_agent_refs",
    )
    caller_memory_refs, caller_memory_diagnostics = _validated_caller_refs(
        request_body.source_memory_refs,
        allowed_ref_type="summary",
        known_ids=_known_session_memory_ids(
            request=request,
            session=session,
            agent_id=request_body.agent_id,
            store=store,
        ),
        base_path="/source_memory_refs",
    )
    diagnostics.extend(caller_event_diagnostics)
    diagnostics.extend(caller_snapshot_diagnostics)
    diagnostics.extend(caller_agent_diagnostics)
    diagnostics.extend(caller_memory_diagnostics)
    event_refs: list[ExternalProjectionEvidenceRef] = []
    agent_refs: list[ExternalProjectionEvidenceRef] = []
    memory_refs: list[ExternalProjectionEvidenceRef] = []
    if not diagnostics:
        event_refs, agent_refs, memory_refs, source_diagnostics = _session_inspection_sources(
            request=request,
            session=session,
            tick_start=tick_range.start,
            tick_end=tick_range.end,
            branch_id=request_body.branch_id,
            agent_id=request_body.agent_id,
            store=store,
        )
        diagnostics.extend(source_diagnostics)
    event_refs = [*caller_event_refs, *event_refs]
    snapshot_refs = list(caller_snapshot_refs)
    agent_refs = [*caller_agent_refs, *agent_refs]
    memory_refs = [*caller_memory_refs, *memory_refs]
    status = "rejected" if diagnostics else "accepted"
    public_summary = None
    if status == "accepted":
        focus = f" for Agent {request_body.agent_id}" if request_body.agent_id else ""
        branch = f" on branch {request_body.branch_id}" if request_body.branch_id else ""
        hint = f" Hint: {request_body.summary_hint}" if request_body.summary_hint else ""
        public_summary = (
            f"Session {session_id}{focus}{branch} has {len(event_refs)} public "
            f"event ref(s), {len(agent_refs)} Agent ref(s), and "
            f"{len(memory_refs)} memory summary ref(s) between ticks "
            f"{tick_range.start} and {tick_range.end}.{hint}"
        )
    return ApiResponse(
        data=SessionNarrativeProjectionResponse(
            session_id=session_id,
            world_id=session.world_id,
            status=status,
            tick_range=tick_range,
            branch_id=request_body.branch_id,
            agent_id=request_body.agent_id,
            public_narrative_summary=public_summary,
            source_event_refs=event_refs,
            source_snapshot_refs=snapshot_refs,
            source_agent_refs=agent_refs,
            source_memory_refs=memory_refs,
            diagnostics=diagnostics,
        )
    )


@router.post(
    "/{session_id}/diagnostics/inspect",
    response_model=ApiResponse[SessionDiagnosticInspectionResponse],
    operation_id="inspect_session_diagnostics",
)
def inspect_session_diagnostics(
    session_id: str,
    request_body: SessionDiagnosticInspectionRequest,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionDiagnosticInspectionResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()
    tick_range = _inspection_tick_range(
        request_body.tick_start,
        request_body.tick_end,
        request,
    )
    diagnostics: list[ProjectionBoundaryDiagnostic] = []
    if tick_range.end < tick_range.start:
        diagnostics.append(
            _inspection_diagnostic(
                "invalid_tick_range",
                "tick_end must be greater than or equal to tick_start",
                "/tick_end",
            )
        )
    if _mutation_requested(request_body):
        diagnostics.append(
            _inspection_diagnostic(
                "canonical_mutation_attempt",
                "inspection surfaces must not mutate canonical state, events, dialogue, or Agent memory",
                "/",
            )
        )
    caller_event_refs, caller_event_diagnostics = _validated_caller_refs(
        request_body.source_event_refs,
        allowed_ref_type="event",
        known_ids={event.id for event in request.app.state.event_log.snapshot()},
        base_path="/source_event_refs",
    )
    caller_agent_refs, caller_agent_diagnostics = _validated_caller_refs(
        request_body.source_agent_refs,
        allowed_ref_type="agent_continuity",
        known_ids={agent.agent_id for agent in store.list_agents(session_id) or []},
        base_path="/source_agent_refs",
    )
    caller_memory_refs, caller_memory_diagnostics = _validated_caller_refs(
        request_body.source_memory_refs,
        allowed_ref_type="summary",
        known_ids=_known_session_memory_ids(
            request=request,
            session=session,
            agent_id=request_body.agent_id,
            store=store,
        ),
        base_path="/source_memory_refs",
    )
    diagnostics.extend(caller_event_diagnostics)
    diagnostics.extend(caller_agent_diagnostics)
    diagnostics.extend(caller_memory_diagnostics)
    event_refs: list[ExternalProjectionEvidenceRef] = []
    agent_refs: list[ExternalProjectionEvidenceRef] = []
    memory_refs: list[ExternalProjectionEvidenceRef] = []
    if not diagnostics:
        event_refs, agent_refs, memory_refs, source_diagnostics = _session_inspection_sources(
            request=request,
            session=session,
            tick_start=tick_range.start,
            tick_end=tick_range.end,
            branch_id=request_body.branch_id,
            agent_id=request_body.agent_id,
            store=store,
        )
        diagnostics.extend(source_diagnostics)
    event_refs = [*caller_event_refs, *event_refs]
    agent_refs = [*caller_agent_refs, *agent_refs]
    memory_refs = [*caller_memory_refs, *memory_refs]
    status = "rejected" if diagnostics else "accepted"
    public_answer = None
    if status == "accepted":
        public_answer = (
            f"Diagnostic inspection answered from public evidence only: "
            f"{len(event_refs)} event ref(s), {len(agent_refs)} Agent ref(s), "
            f"and {len(memory_refs)} memory summary ref(s). The inspection is "
            "out-of-world and is not recorded as Agent memory or dialogue."
        )
    return ApiResponse(
        data=SessionDiagnosticInspectionResponse(
            session_id=session_id,
            world_id=session.world_id,
            status=status,
            tick_range=tick_range,
            branch_id=request_body.branch_id,
            agent_id=request_body.agent_id,
            question_summary=request_body.question_summary,
            public_answer_summary=public_answer,
            source_event_refs=event_refs,
            source_agent_refs=agent_refs,
            source_memory_refs=memory_refs,
            diagnostics=diagnostics,
        )
    )


@router.get(
    "/{session_id}/agents",
    response_model=ApiResponse[SessionAgentListResponse],
    operation_id="list_session_agents",
)
def list_session_agents(
    session_id: str,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionAgentListResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()
    agents = store.list_agents(session_id)
    if agents is None:
        raise _unknown_session()
    return ApiResponse(
        data=SessionAgentListResponse(
            session_id=session.session_id,
            world_id=session.world_id,
            items=agents,
            total=len(agents),
        )
    )


@router.get(
    "/{session_id}/agents/{agent_id}",
    response_model=ApiResponse[SessionAgentPublicState],
    operation_id="get_session_agent",
)
def get_session_agent(
    session_id: str,
    agent_id: str,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionAgentPublicState]:
    agent = store.get_agent(session_id, agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail="Unknown agent_id")
    return ApiResponse(data=agent)


@router.post(
    "/{session_id}/agents/{agent_id}/step",
    response_model=ApiResponse[SessionAgentStepResponse],
    operation_id="run_session_agent_step",
)
def run_session_agent_step(
    session_id: str,
    agent_id: str,
    request_body: SessionAgentStepRequest,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionAgentStepResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()
    previous = store.get_agent(session_id, agent_id)
    if previous is None:
        raise HTTPException(status_code=404, detail="Unknown agent_id")

    runtime_state = request.app.state.runtime_engine.get_state()
    event_count_before = len(request.app.state.event_log.snapshot())
    recent_events = [
        event
        for event in request.app.state.event_log.list_page(
            limit=request_body.event_limit
        ).items
        if event.source != "session.agent"
    ]
    latest_public_event = recent_events[-1] if recent_events else None

    if request_body.mode_hint == "rest":
        state = "resting"
        public_intent = "rest"
        visible_action = "resting after public observation"
    elif latest_public_event is not None:
        state = "acting"
        public_intent = "acknowledge_public_event"
        visible_action = f"acknowledging public event {latest_public_event.type}"
    else:
        state = "waiting"
        public_intent = "maintain_observation"
        visible_action = "waiting for public events"

    observation_summary = (
        f"Observed runtime tick {runtime_state.tick_id} with "
        f"{len(recent_events)} public event(s)."
    )
    base_payload: dict[str, object] = {
        "session_id": session_id,
        "world_id": session.world_id,
        "agent_id": agent_id,
        "agent_state": state,
        "public_observation_summary": observation_summary,
        "public_intent": public_intent,
        "visible_action": visible_action,
        "runtime_tick": runtime_state.tick_id,
        "runtime_world_time_seconds": runtime_state.world_time_seconds,
        "redaction_status": "passed",
        "client_scripted_action": False,
    }
    event_ids = [
        _append_session_agent_event(
            request=request,
            event_type="world.agent.observed",
            payload=base_payload,
        ),
        _append_session_agent_event(
            request=request,
            event_type="world.agent.intent.recorded",
            payload=base_payload,
        ),
    ]
    action_event_type = {
        "acting": "world.agent.action.recorded",
        "resting": "world.agent.rest.recorded",
        "waiting": "world.agent.wait.recorded",
    }[state]
    event_ids.append(
        _append_session_agent_event(
            request=request,
            event_type=action_event_type,
            payload=base_payload,
        )
    )
    event_count_after = len(request.app.state.event_log.snapshot())
    evidence = SessionAgentEventEvidence(
        event_count_before=event_count_before,
        event_count_after=event_count_after,
        event_delta_count=max(0, event_count_after - event_count_before),
        event_ids=event_ids,
    )
    updated = SessionAgentPublicState(
        session_id=session.session_id,
        world_id=session.world_id,
        agent_id=agent_id,
        display_name=previous.display_name,
        state=state,
        public_status="active" if state == "acting" else "ready",
        last_observation_summary=observation_summary,
        current_intent=public_intent,
        visible_action=visible_action,
        runtime_ref=session.runtime_ref,
        evidence_refs=evidence,
        client_scripted_action=False,
        updated_at=datetime.now(timezone.utc).isoformat(),
    )
    stored = store.update_agent(session_id, updated)
    if stored is None:
        raise _unknown_session()

    return ApiResponse(
        data=SessionAgentStepResponse(
            session_id=session.session_id,
            world_id=session.world_id,
            agent_id=agent_id,
            previous_state=previous,
            updated_state=stored,
            public_intent=public_intent,
            visible_action=visible_action,
            event_evidence=evidence,
            client_scripted_action=False,
        )
    )


@router.get(
    "/{session_id}/agents/{agent_id}/memory",
    response_model=ApiResponse[SessionAgentMemorySummaryResponse],
    operation_id="get_session_agent_memory",
)
def get_session_agent_memory(
    session_id: str,
    agent_id: str,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionAgentMemorySummaryResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()
    if store.get_agent(session_id, agent_id) is None:
        raise HTTPException(status_code=404, detail="Unknown agent_id")
    working = request.app.state.agent_memory_store.list_working_memory(
        agent_id=agent_id,
        world_id=session.world_id,
        limit=20,
    )
    episodic = request.app.state.agent_memory_store.list_episodic_memory(
        agent_id=agent_id,
        world_id=session.world_id,
        limit=20,
    )
    return ApiResponse(
        data=SessionAgentMemorySummaryResponse(
            session_id=session_id,
            world_id=session.world_id,
            agent_id=agent_id,
            working_memory=working,
            episodic_memory=episodic,
            consolidation_status="consolidated" if episodic else "not_consolidated",
        )
    )


@router.post(
    "/{session_id}/agents/{agent_id}/memory/consolidate",
    response_model=ApiResponse[SessionAgentMemoryConsolidationResponse],
    operation_id="consolidate_session_agent_memory",
)
def consolidate_session_agent_memory(
    session_id: str,
    agent_id: str,
    request_body: SessionAgentMemoryConsolidationRequest,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionAgentMemoryConsolidationResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()
    agent = store.get_agent(session_id, agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail="Unknown agent_id")

    runtime_state = request.app.state.runtime_engine.get_state()
    event_count_before = len(request.app.state.event_log.snapshot())
    recent_events = request.app.state.event_log.list_page(
        limit=request_body.event_limit
    ).items
    public_event_refs = [
        _memory_evidence_ref(event.id)
        for event in recent_events
        if event.source == "session.agent"
    ][-5:]
    summary = (
        f"Agent {agent_id} publicly rested at tick {runtime_state.tick_id} "
        f"after {len(public_event_refs)} public Agent event(s)."
    )
    now = datetime.now(timezone.utc).isoformat()
    working = WorkingMemoryRecord(
        memory_id=f"working-{uuid4().hex[:12]}",
        agent_id=agent_id,
        world_id=session.world_id,
        content=summary,
        source="session_agent_public_summary",
        evidence_refs=public_event_refs,
        priority=1,
        created_at=now,
        updated_at=now,
        metadata={
            "session_id": session_id,
            "redaction_status": "passed",
            "private_memory_payload_included": False,
        },
    )
    episodic = EpisodicMemoryRecord(
        memory_id=f"episodic-{uuid4().hex[:12]}",
        agent_id=agent_id,
        world_id=session.world_id,
        summary=summary,
        event_refs=public_event_refs,
        tick=runtime_state.tick_id,
        world_time_seconds=runtime_state.world_time_seconds,
        source="session_agent_rest_consolidation",
        action_refs=[_memory_evidence_ref(ref.id, "session_agent_event") for ref in public_event_refs],
        created_at=now,
        metadata={
            "session_id": session_id,
            "personality_mutation_applied": False,
            "skill_mutation_applied": False,
            "private_memory_payload_included": False,
            "redaction_status": "passed",
        },
    )
    stored_working = request.app.state.agent_memory_store.add_working_memory(working)
    stored_episodic = request.app.state.agent_memory_store.add_episodic_memory(episodic)
    base_payload: dict[str, object] = {
        "session_id": session_id,
        "world_id": session.world_id,
        "agent_id": agent_id,
        "public_summary": summary,
        "runtime_tick": runtime_state.tick_id,
        "runtime_world_time_seconds": runtime_state.world_time_seconds,
        "evidence_refs": [ref.model_dump() for ref in public_event_refs],
        "redaction_status": "passed",
        "personality_mutation_applied": False,
        "skill_mutation_applied": False,
        "private_memory_payload_included": False,
    }
    memory_event_id = _append_session_agent_event(
        request=request,
        event_type="world.agent.memory.recorded",
        payload={
            **base_payload,
            "memory_id": stored_working.memory_id,
            "memory_kind": "working",
        },
    )
    consolidation_event_id = _append_session_agent_event(
        request=request,
        event_type="world.agent.consolidation.recorded",
        payload={
            **base_payload,
            "memory_id": stored_episodic.memory_id,
            "memory_kind": "episodic",
        },
    )
    event_count_after = len(request.app.state.event_log.snapshot())
    evidence = SessionAgentEventEvidence(
        event_count_before=event_count_before,
        event_count_after=event_count_after,
        event_delta_count=max(0, event_count_after - event_count_before),
        event_ids=[memory_event_id, consolidation_event_id],
    )

    return ApiResponse(
        data=SessionAgentMemoryConsolidationResponse(
            session_id=session_id,
            world_id=session.world_id,
            agent_id=agent_id,
            consolidation_status="consolidated",
            working_memory=stored_working,
            episodic_memory=stored_episodic,
            event_evidence=evidence,
            personality_mutation_applied=False,
            skill_mutation_applied=False,
            private_memory_payload_included=False,
        )
    )


@router.post(
    "/{session_id}/evolution/step",
    response_model=ApiResponse[SessionEvolutionStepResponse],
    operation_id="run_world_session_evolution_step",
)
def run_world_session_evolution_step(
    session_id: str,
    request_body: SessionEvolutionStepRequest,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionEvolutionStepResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()

    rule_set = store.accepted_rule_set(session_id)
    if rule_set is None:
        result = _blocked_evolution_result(
            "session_rules_not_attached",
            "session requires accepted public rules before rule-bound evolution",
            "/session/rules",
        )
        replay_event_id = _append_session_evolution_event(
            request=request,
            event_type="world.session_evolution.blocked",
            source="world_rule",
            payload={
                "session_id": session_id,
                "world_id": session.world_id,
                "status": result.status,
                "diagnostics": [diagnostic.model_dump() for diagnostic in result.diagnostics],
                "direct_state_mutation_applied": False,
            },
        )
        return ApiResponse(
            data=SessionEvolutionStepResponse(
                session_id=session_id,
                world_id=session.world_id,
                status="blocked",
                result=result,
                replay_event_id=replay_event_id,
            )
        )

    runtime_state = request.app.state.runtime_engine.get_state()
    candidate = build_rule_bound_session_event_candidate(
        world_id=session.world_id,
        rule_set=rule_set,
        current_params=request.app.state.world_state.get_params(),
        runtime_tick=runtime_state.tick_id,
        runtime_world_time_seconds=runtime_state.world_time_seconds,
        direction_queue=session.direction_queue,
    )
    if candidate is None:
        result = _blocked_evolution_result(
            "no_public_candidate_available",
            "no public rule-bound event candidate could be selected",
            "/session/evolution",
        )
        replay_event_id = _append_session_evolution_event(
            request=request,
            event_type="world.session_evolution.blocked",
            source="world_rule",
            payload={
                "session_id": session_id,
                "world_id": session.world_id,
                "status": result.status,
                "diagnostics": [diagnostic.model_dump() for diagnostic in result.diagnostics],
                "direct_state_mutation_applied": False,
            },
        )
        return ApiResponse(
            data=SessionEvolutionStepResponse(
                session_id=session_id,
                world_id=session.world_id,
                status="blocked",
                result=result,
                replay_event_id=replay_event_id,
            )
        )

    result = evaluate_world_event_candidate(
        candidate=candidate,
        rule_set=rule_set,
        current_params=request.app.state.world_state.get_params(),
        runtime_tick=runtime_state.tick_id,
        runtime_world_time_seconds=runtime_state.world_time_seconds,
        direction_queue=session.direction_queue,
    )
    event_type = (
        "world.session_evolution.accepted"
        if result.status == "accepted"
        else "world.session_evolution.rejected"
    )
    if request_body.apply and result.status == "accepted" and result.state_diff is not None:
        patches = [
            ParamPatchItem(op=item.op, path=item.path, value=item.new_public_value)
            for item in result.state_diff.items
        ]
        request.app.state.world_state.apply_patch(patches)

    replay_event_id = _append_session_evolution_event(
        request=request,
        event_type=event_type,
        source=candidate.source,
        payload={
            "session_id": session_id,
            "world_id": session.world_id,
            "status": result.status,
            "candidate_id": candidate.candidate_id,
            "candidate": candidate.model_dump(),
            "matched_rule_ids": result.matched_rule_ids,
            "referenced_parameter_ids": result.referenced_parameter_ids,
            "direction_refs": list(candidate.direction_refs),
            "state_diff": result.state_diff.model_dump() if result.state_diff else None,
            "evidence": result.evidence.model_dump() if result.evidence else None,
            "redaction_status": result.redaction_status,
            "applied": request_body.apply and result.status == "accepted",
            "direct_state_mutation_applied": False,
        },
    )
    result.applied_event_id = replay_event_id if request_body.apply and result.status == "accepted" else None
    return ApiResponse(
        data=SessionEvolutionStepResponse(
            session_id=session_id,
            world_id=session.world_id,
            status=result.status,
            candidate=candidate,
            result=result,
            replay_event_id=replay_event_id,
        )
    )


@router.post(
    "/{session_id}/run",
    response_model=ApiResponse[SessionRunEvidenceResponse],
    operation_id="run_world_session",
)
def run_world_session(
    session_id: str,
    request_body: RuntimeRunRequest,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionRunEvidenceResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()

    event_count_before = len(request.app.state.event_log.snapshot())
    _, snapshot_count_before = request.app.state.snapshot_store.list(limit=200)
    summary = request.app.state.runtime_engine.run_bounded(request_body)
    event_count_after = len(request.app.state.event_log.snapshot())
    snapshots, _ = request.app.state.snapshot_store.list(
        from_tick=summary.start_tick + 1,
        to_tick=summary.end_tick,
        limit=200,
    )
    _, snapshot_count_after = request.app.state.snapshot_store.list(limit=200)
    session_status = "ready" if summary.status == "completed" else session.status
    updated_session = store.set_status(session_id, session_status) or session

    data = SessionRunEvidenceResponse(
        session_id=session_id,
        world_id=updated_session.world_id,
        run_summary=summary,
        runtime_delta=SessionRuntimeDelta(
            start_tick=summary.start_tick,
            end_tick=summary.end_tick,
            start_world_time_seconds=summary.start_world_time_seconds,
            end_world_time_seconds=summary.end_world_time_seconds,
        ),
        event_evidence=SessionEventEvidence(
            event_count_before=event_count_before,
            event_count_after=event_count_after,
            event_delta_count=max(0, event_count_after - event_count_before),
        ),
        snapshot_evidence=SessionSnapshotEvidence(
            snapshot_count_before=snapshot_count_before,
            snapshot_count_after=snapshot_count_after,
            snapshot_delta_count=max(0, snapshot_count_after - snapshot_count_before),
            snapshot_ids=[snapshot.id for snapshot in snapshots],
        ),
        timeline_label=_timeline_label(session_id),
    )
    return ApiResponse(data=data)


@router.post(
    "/{session_id}/pause",
    response_model=ApiResponse[RuntimeControlState],
    operation_id="pause_world_session",
)
def pause_world_session(
    session_id: str,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[RuntimeControlState]:
    if store.get(session_id) is None:
        raise _unknown_session()
    control = request.app.state.runtime_engine.pause()
    store.set_status(session_id, "paused")
    return ApiResponse(data=control)


@router.post(
    "/{session_id}/resume",
    response_model=ApiResponse[WorldSession],
    operation_id="resume_world_session",
)
def resume_world_session(
    session_id: str,
    request: Request,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[WorldSession]:
    if store.get(session_id) is None:
        raise _unknown_session()
    request.app.state.runtime_engine.resume()
    session = store.set_status(session_id, "ready")
    if session is None:
        raise _unknown_session()
    return ApiResponse(data=session)


@router.get(
    "/{session_id}/snapshots",
    response_model=ApiResponse[SessionSnapshotListResponse],
    operation_id="list_world_session_snapshots",
)
def list_world_session_snapshots(
    session_id: str,
    request: Request,
    from_tick: Optional[int] = Query(default=None, ge=0),
    to_tick: Optional[int] = Query(default=None, ge=0),
    limit: int = Query(default=20, ge=1, le=200),
    order: str = Query(default="asc", pattern="^(asc|desc)$"),
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionSnapshotListResponse]:
    session = store.get(session_id)
    if session is None:
        raise _unknown_session()
    snapshots, total = request.app.state.snapshot_store.list(
        from_tick=from_tick,
        to_tick=to_tick,
        limit=limit,
        order=order,
    )
    return ApiResponse(
        data=SessionSnapshotListResponse(
            session_id=session_id,
            world_id=session.world_id,
            items=snapshots,
            total=total,
            limit=max(1, min(limit, 200)),
            timeline_label=_timeline_label(session_id),
        )
    )


@router.get("", response_model=ApiResponse[SessionListResponse], operation_id="list_world_sessions")
def list_world_sessions(
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionListResponse]:
    items = store.list()
    return ApiResponse(data=SessionListResponse(items=items, total=len(items)))


@router.get("/{session_id}", response_model=ApiResponse[WorldSession], operation_id="get_world_session")
def get_world_session(
    session_id: str,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[WorldSession]:
    session = store.get(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Unknown session_id")
    return ApiResponse(data=session)


@router.get(
    "/{session_id}/status",
    response_model=ApiResponse[SessionStatusResponse],
    operation_id="get_world_session_status",
)
def get_world_session_status(
    session_id: str,
    store: InMemoryWorldSessionStore = Depends(get_session_store),
) -> ApiResponse[SessionStatusResponse]:
    status = store.status(session_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Unknown session_id")
    return ApiResponse(data=status)
