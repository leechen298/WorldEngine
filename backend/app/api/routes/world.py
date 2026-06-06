import hashlib
from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from app.agent.provider_config import provider_readiness_from_env
from app.core.event_bus import InMemoryEventLog
from app.core.agent_continuity import evaluate_agent_continuity
from app.core.external_projection import (
    evaluate_diagnostic_dialogue,
    evaluate_narrative_projection,
)
from app.core.rule_linked_evolution import evaluate_world_event_candidate
from app.schemas.agent_continuity import (
    AgentContinuityEvaluationRequest,
    AgentContinuityEvaluationResponse,
)
from app.schemas.api import ApiResponse
from app.schemas.event import EventPage, EventStepPage
from app.schemas.event import Event
from app.schemas.external_projection import (
    DiagnosticDialogueEvaluationRequest,
    DiagnosticDialogueEvaluationResponse,
    NarrativeProjectionRequest,
    NarrativeProjectionResponse,
)
from app.schemas.params import ParamPatchItem
from app.schemas.world import (
    DirectorGuidanceRequest,
    DirectorGuidanceResponse,
    HandoffManifest,
    PublicAgentState,
    PublicInitialWorldState,
    PublicSurface,
    PublicVisualizationPayload,
    PublicWorldCreateRequest,
    PublicWorldCreationResponse,
)
from app.schemas.world_direction import (
    WorldDirectionRequest,
    WorldDirectionResponse,
    WorldDirectionQueueItem,
    classify_world_direction,
)
from app.schemas.world_evolution import (
    WorldEventLegalityDiagnostic,
    WorldEventEvaluationRequest,
    WorldEventEvaluationResponse,
)

router = APIRouter(prefix="/world", tags=["world"])
public_router = APIRouter(tags=["worlds"])


def get_event_log(request: Request) -> InMemoryEventLog:
    return request.app.state.event_log


@router.get("/events", response_model=ApiResponse[EventPage])
def get_world_events(
    from_tick: Optional[int] = Query(default=None, ge=0),
    to_tick: Optional[int] = Query(default=None, ge=0),
    cursor: Optional[str] = Query(default=None),
    limit: int = Query(default=20, ge=1, le=200),
    event_log: InMemoryEventLog = Depends(get_event_log),
) -> ApiResponse[EventPage]:
    try:
        page = event_log.list_page(
            cursor=cursor,
            from_tick=from_tick,
            to_tick=to_tick,
            limit=limit,
        )
    except KeyError as exc:
        raise HTTPException(status_code=400, detail=f"Unknown cursor: {exc.args[0]}") from exc

    return ApiResponse(data=page)


@router.get("/event-steps", response_model=ApiResponse[EventStepPage])
def get_world_event_steps(
    from_tick: Optional[int] = Query(default=None, ge=0),
    to_tick: Optional[int] = Query(default=None, ge=0),
    cursor: Optional[str] = Query(default=None),
    limit: int = Query(default=20, ge=1, le=200),
    event_log: InMemoryEventLog = Depends(get_event_log),
) -> ApiResponse[EventStepPage]:
    try:
        page = event_log.list_step_page(
            cursor=cursor,
            from_tick=from_tick,
            to_tick=to_tick,
            limit=limit,
        )
    except KeyError as exc:
        raise HTTPException(status_code=400, detail=f"Unknown cursor: {exc.args[0]}") from exc

    return ApiResponse(data=page)


def _public_surfaces() -> list[PublicSurface]:
    return [
        PublicSurface(
            path="/health",
            method="GET",
            operation_id="get_health",
            status="available",
        ),
        PublicSurface(
            path="/openapi.json",
            method="GET",
            operation_id="openapi",
            status="available",
        ),
        PublicSurface(
            path="/manifest",
            method="GET",
            operation_id="get_handoff_manifest",
            status="available",
        ),
        PublicSurface(
            path="/worlds",
            method="POST",
            operation_id="create_world",
            status="available",
        ),
        PublicSurface(
            path="/worlds/{world_id}/director-guidance",
            method="POST",
            operation_id="submit_director_guidance",
            status="available",
        ),
        PublicSurface(
            path="/worlds/{world_id}/direction",
            method="POST",
            operation_id="submit_world_direction",
            status="available",
        ),
        PublicSurface(
            path="/worlds/{world_id}/evolution/evaluate-event",
            method="POST",
            operation_id="evaluate_world_event_candidate",
            status="available",
        ),
        PublicSurface(
            path="/worlds/{world_id}/agents/{agent_id}/continuity/evaluate",
            method="POST",
            operation_id="evaluate_agent_continuity",
            status="available",
        ),
        PublicSurface(
            path="/worlds/{world_id}/narrative/project",
            method="POST",
            operation_id="project_world_narrative",
            status="available",
        ),
        PublicSurface(
            path="/worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate",
            method="POST",
            operation_id="evaluate_agent_diagnostic_dialogue",
            status="available",
        ),
        PublicSurface(
            path="/provider/live-smoke",
            method="POST",
            operation_id="provider_live_smoke",
            status="available",
        ),
        PublicSurface(
            path="/world/generation/worldview",
            method="POST",
            operation_id="generate_world_from_worldview",
            status="available",
        ),
    ]


@public_router.get(
    "/manifest",
    response_model=HandoffManifest,
    operation_id="get_handoff_manifest",
)
def get_handoff_manifest() -> HandoffManifest:
    warnings = ["provider readiness is not live provider call proof"]
    provider = provider_readiness_from_env()
    if provider.provider_readiness == "not_configured":
        warnings.append("provider credentials are not configured")
    return HandoffManifest(
        provider=provider,
        public_surfaces=_public_surfaces(),
        warnings=warnings,
    )


@public_router.post(
    "/worlds",
    response_model=PublicWorldCreationResponse,
    operation_id="create_world",
)
def create_world(request_body: PublicWorldCreateRequest) -> PublicWorldCreationResponse:
    digest = hashlib.sha256(request_body.world_prompt.encode("utf-8")).hexdigest()[:12]
    world_id = f"world-{digest}"
    return PublicWorldCreationResponse(
        world_id=world_id,
        public_initial_state=PublicInitialWorldState(
            summary="A generic public WorldEngine world was created from the supplied world prompt.",
            public_agents=[
                PublicAgentState(
                    agent_id="agent.observer",
                    display_name="Observer",
                    location="origin",
                    public_status="idle",
                    visible_action="observing the initial world state",
                )
            ],
            environment={
                "prompt_digest": digest,
                "world_prompt_summary": "public prompt accepted",
            },
        ),
        visualization=PublicVisualizationPayload(
            tilemap={
                "width": 3,
                "height": 3,
                "origin": [1, 1],
            },
            entities=[
                {
                    "entity_id": "agent.observer",
                    "kind": "agent",
                    "x": 1,
                    "y": 1,
                }
            ],
        ),
    )


@public_router.post(
    "/worlds/{world_id}/direction",
    response_model=WorldDirectionResponse,
    operation_id="submit_world_direction",
)
def submit_world_direction(
    world_id: str,
    request_body: WorldDirectionRequest,
    request: Request,
) -> WorldDirectionResponse:
    runtime_state = request.app.state.runtime_engine.get_state()
    public_context_keys = sorted(request_body.public_context.keys())
    classification = classify_world_direction(
        request_body.instruction_text,
        branch_id=request_body.branch_id,
        public_context_keys=public_context_keys,
        public_context_values=request_body.public_context.values(),
    )
    event_branch_id = None if classification.redaction_status == "redacted" else request_body.branch_id
    event_public_context_keys = [] if classification.redaction_status == "redacted" else public_context_keys

    if classification.allowed:
        direction_id = str(uuid4())
        queue_item = WorldDirectionQueueItem(
            direction_id=direction_id,
            world_id=world_id,
            classification=classification,
            public_summary=classification.public_reason,
            apply_after_tick=request_body.apply_after_tick,
            expires_after_tick=request_body.expires_after_tick,
            public_context_keys=event_public_context_keys,
            redaction_status=classification.redaction_status,
        )
        _world_direction_queue(request).append(queue_item)
        request.app.state.event_log.append(
            Event(
                id=str(uuid4()),
                tick_id=runtime_state.tick_id,
                world_time_seconds=runtime_state.world_time_seconds,
                type="world.direction.queued",
                source="director",
                payload={
                    "world_id": world_id,
                    "direction_id": direction_id,
                    "instruction_text_length": len(request_body.instruction_text),
                    "branch_id": event_branch_id,
                    "classification": classification.model_dump(),
                    "apply_after_tick": request_body.apply_after_tick,
                    "expires_after_tick": request_body.expires_after_tick,
                    "public_context_keys": event_public_context_keys,
                    "direct_state_mutation_applied": False,
                },
                created_at=datetime.now(timezone.utc).isoformat(),
            )
        )
        return WorldDirectionResponse(
            world_id=world_id,
            status="queued",
            classification=classification,
            queue_item=queue_item,
            public_explanation=classification.public_reason,
            direct_state_mutation_applied=False,
        )

    request.app.state.event_log.append(
        Event(
            id=str(uuid4()),
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            type="world.direction.rejected",
            source="director",
            payload={
                "world_id": world_id,
                "instruction_text_length": len(request_body.instruction_text),
                "branch_id": event_branch_id,
                "classification": classification.model_dump(),
                "public_context_keys": event_public_context_keys,
                "direct_state_mutation_applied": False,
            },
            created_at=datetime.now(timezone.utc).isoformat(),
        )
    )
    return WorldDirectionResponse(
        world_id=world_id,
        status="rejected",
        classification=classification,
        queue_item=None,
        rejection_reason=classification.category,
        public_explanation=classification.public_reason,
        direct_state_mutation_applied=False,
    )


def _world_direction_queue(request: Request) -> list[WorldDirectionQueueItem]:
    if not hasattr(request.app.state, "world_direction_queue"):
        request.app.state.world_direction_queue = []
    return request.app.state.world_direction_queue


def _public_event_ids(request: Request) -> set[str]:
    return {event.id for event in request.app.state.event_log.snapshot()}


def _public_snapshot_ids(request: Request) -> set[str]:
    items, _ = request.app.state.snapshot_store.list(limit=200)
    return {snapshot.id for snapshot in items}


@public_router.post(
    "/worlds/{world_id}/narrative/project",
    response_model=NarrativeProjectionResponse,
    operation_id="project_world_narrative",
)
def project_world_narrative(
    world_id: str,
    request_body: NarrativeProjectionRequest,
    request: Request,
) -> NarrativeProjectionResponse:
    return evaluate_narrative_projection(
        world_id=world_id,
        request=request_body,
        public_event_ids=_public_event_ids(request),
        public_snapshot_ids=_public_snapshot_ids(request),
    )


@public_router.post(
    "/worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate",
    response_model=DiagnosticDialogueEvaluationResponse,
    operation_id="evaluate_agent_diagnostic_dialogue",
)
def evaluate_agent_diagnostic_dialogue(
    world_id: str,
    agent_id: str,
    request_body: DiagnosticDialogueEvaluationRequest,
    request: Request,
) -> DiagnosticDialogueEvaluationResponse:
    return evaluate_diagnostic_dialogue(
        world_id=world_id,
        agent_id=agent_id,
        request=request_body,
        public_event_ids=_public_event_ids(request),
    )


@public_router.post(
    "/worlds/{world_id}/agents/{agent_id}/continuity/evaluate",
    response_model=AgentContinuityEvaluationResponse,
    operation_id="evaluate_agent_continuity",
)
def evaluate_agent_continuity_route(
    world_id: str,
    agent_id: str,
    request_body: AgentContinuityEvaluationRequest,
    request: Request,
) -> AgentContinuityEvaluationResponse:
    runtime_state = request.app.state.runtime_engine.get_state()
    public_event_index = {
        event.id: {"type": event.type, "source": event.source}
        for event in request.app.state.event_log.snapshot()
    }
    result = evaluate_agent_continuity(
        world_id=world_id,
        agent_id=agent_id,
        tick_id=runtime_state.tick_id,
        world_time_seconds=runtime_state.world_time_seconds,
        request=request_body,
        public_event_index=public_event_index,
    )
    if request_body.apply and result.status == "accepted" and result.continuity_artifact is not None:
        applied_event_ids: list[str] = []
        continuity_event_id = str(uuid4())
        request.app.state.event_log.append(
            Event(
                id=continuity_event_id,
                tick_id=runtime_state.tick_id,
                world_time_seconds=runtime_state.world_time_seconds,
                type="agent.continuity.recorded",
                source="agent.continuity",
                payload={
                    "world_id": world_id,
                    "agent_id": agent_id,
                    "state": result.continuity_artifact.state,
                    "continuity_artifact": result.continuity_artifact.model_dump(),
                    "redaction_status": result.redaction_status,
                    "direct_private_mutation_applied": False,
                },
                created_at=datetime.now(timezone.utc).isoformat(),
            )
        )
        applied_event_ids.append(continuity_event_id)

        if result.continuity_artifact.state == "action":
            action_event_id = str(uuid4())
            request.app.state.event_log.append(
                Event(
                    id=action_event_id,
                    tick_id=runtime_state.tick_id,
                    world_time_seconds=runtime_state.world_time_seconds,
                    type="agent.action.continuity.recorded",
                    source="agent.continuity",
                    payload={
                        "world_id": world_id,
                        "agent_id": agent_id,
                        "autonomous_action_evidence": (
                            result.continuity_artifact.autonomous_action_evidence.model_dump()
                            if result.continuity_artifact.autonomous_action_evidence is not None
                            else None
                        ),
                        "redaction_status": result.redaction_status,
                        "client_scripted_action": False,
                    },
                    created_at=datetime.now(timezone.utc).isoformat(),
                )
            )
            applied_event_ids.append(action_event_id)

        if result.consolidation_artifact is not None:
            consolidation_event_id = str(uuid4())
            request.app.state.event_log.append(
                Event(
                    id=consolidation_event_id,
                    tick_id=runtime_state.tick_id,
                    world_time_seconds=runtime_state.world_time_seconds,
                    type="agent.consolidation.recorded",
                    source="agent.continuity",
                    payload={
                        "world_id": world_id,
                        "agent_id": agent_id,
                        "consolidation_artifact": result.consolidation_artifact.model_dump(),
                        "redaction_status": result.redaction_status,
                        "automatic_per_tick_mutation": False,
                    },
                    created_at=datetime.now(timezone.utc).isoformat(),
                )
            )
            applied_event_ids.append(consolidation_event_id)
        result.applied_event_ids = applied_event_ids
    return result


@public_router.post(
    "/worlds/{world_id}/evolution/evaluate-event",
    response_model=WorldEventEvaluationResponse,
    operation_id="evaluate_world_event_candidate",
)
def evaluate_world_event(
    world_id: str,
    request_body: WorldEventEvaluationRequest,
    request: Request,
) -> WorldEventEvaluationResponse:
    runtime_state = request.app.state.runtime_engine.get_state()
    result = evaluate_world_event_candidate(
        candidate=request_body.candidate,
        rule_set=request_body.rule_set,
        current_params=request.app.state.world_state.get_params(),
        runtime_tick=runtime_state.tick_id,
        runtime_world_time_seconds=runtime_state.world_time_seconds,
        direction_queue=_world_direction_queue(request),
    )
    if world_id != request_body.candidate.world_id and not any(
        diagnostic.code == "world_id_mismatch" for diagnostic in result.diagnostics
    ):
        result.diagnostics.append(
            WorldEventLegalityDiagnostic(
                code="world_id_mismatch",
                message="path world_id must match candidate world_id",
                path="/world_id",
            )
        )
        result.status = "rejected"
        result.legality_classification = "illegal"
        result.state_diff = None
        result.evidence = None

    if request_body.apply and result.status == "accepted" and result.state_diff is not None:
        patches = [
            ParamPatchItem(op=item.op, path=item.path, value=item.new_public_value)
            for item in result.state_diff.items
        ]
        event_id = str(uuid4())
        accepted_event = Event(
            id=event_id,
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            type="world.evolution.accepted",
            source=request_body.candidate.source,
            payload={
                "world_id": world_id,
                "candidate_id": request_body.candidate.candidate_id,
                "legality_status": result.status,
                "matched_rule_ids": result.matched_rule_ids,
                "changed_parameter_ids": result.state_diff.changed_parameter_ids,
                "state_diff": result.state_diff.model_dump(),
                "evidence": (
                    result.evidence.model_dump()
                    if result.evidence is not None
                    else None
                ),
                "redaction_status": result.redaction_status,
                "direct_state_mutation_applied": False,
            },
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        request.app.state.world_state.apply_patch(patches)
        request.app.state.event_log.append(accepted_event)
        result.applied_event_id = event_id

    return WorldEventEvaluationResponse(
        world_id=world_id,
        result=result,
    )


@public_router.post(
    "/worlds/{world_id}/director-guidance",
    response_model=DirectorGuidanceResponse,
    operation_id="submit_director_guidance",
)
def submit_director_guidance(
    world_id: str,
    request_body: DirectorGuidanceRequest,
    request: Request,
) -> DirectorGuidanceResponse:
    runtime_state = request.app.state.runtime_engine.get_state()
    event_id = str(uuid4())
    request.app.state.event_log.append(
        Event(
            id=event_id,
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            type="director.guidance.accepted",
            source="director",
            payload={
                "world_id": world_id,
                "instruction_text_length": len(request_body.instruction_text),
                "branch_id": request_body.branch_id,
                "tick": request_body.tick,
                "public_context_keys": sorted(request_body.public_context.keys()),
            },
            created_at=datetime.now(timezone.utc).isoformat(),
        )
    )
    return DirectorGuidanceResponse(
        world_id=world_id,
        status="accepted",
        public_explanation=(
            "Public director guidance was accepted as external "
            "world-environment direction. It was recorded as guidance only, "
            "with no direct entity-state change applied."
        ),
        applied_event_id=event_id,
    )
