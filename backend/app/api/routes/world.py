import hashlib
import os
import re
from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from app.core.event_bus import InMemoryEventLog
from app.schemas.api import ApiResponse
from app.schemas.event import EventPage, EventStepPage
from app.schemas.event import Event
from app.schemas.world import (
    DirectorGuidanceRequest,
    DirectorGuidanceResponse,
    HandoffManifest,
    PublicAgentState,
    PublicInitialWorldState,
    PublicProviderReadiness,
    PublicSurface,
    PublicVisualizationPayload,
    PublicWorldCreateRequest,
    PublicWorldCreationResponse,
)

router = APIRouter(prefix="/world", tags=["world"])
public_router = APIRouter(tags=["worlds"])


def _public_label(value: str, fallback: str) -> str:
    stripped = value.strip()
    if not stripped:
        return fallback
    lowered = stripped.lower()
    private_markers = (
        "api_key",
        "apikey",
        "api-key",
        "authorization",
        "bearer",
        "password",
        "private",
        "secret",
        "sk-live-",
        "sk-test-",
        "token",
        "credential",
    )
    private_patterns = (
        r"\bapi[-_ ]?key\b",
        r"\bpassword\s*[:=]",
        r"\bbearer\s+\S+",
        r"\bsk-(live|test)-[a-z0-9]",
    )
    if any(marker in lowered for marker in private_markers):
        return "redacted"
    if any(re.search(pattern, lowered) for pattern in private_patterns):
        return "redacted"
    return stripped


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


def _provider_readiness_from_env() -> PublicProviderReadiness:
    raw_provider = os.getenv("WORLDENGINE_LLM_PROVIDER", "").strip().lower()
    provider_map = {
        "deepseek": "deepseek_api",
        "deepseek_api": "deepseek_api",
        "kimi_code": "kimi_code_subscription",
        "kimi_for_coding": "kimi_code_subscription",
        "kimi_code_subscription": "kimi_code_subscription",
        "kimi": "kimi_platform_api",
        "kimi_platform": "kimi_platform_api",
        "kimi_platform_api": "kimi_platform_api",
        "moonshot": "moonshot_api",
        "moonshot_api": "moonshot_api",
        "mock": "mock",
    }
    provider_class = provider_map.get(raw_provider, "unconfigured")
    model_label = _public_label(os.getenv("WORLDENGINE_LLM_MODEL", ""), "")
    key_env_by_provider = {
        "deepseek_api": "DEEPSEEK_API_KEY",
        "kimi_code_subscription": "KIMI_CODE_API_KEY",
        "kimi_platform_api": "KIMI_PLATFORM_API_KEY",
        "moonshot_api": "MOONSHOT_API_KEY",
    }
    key_env = key_env_by_provider.get(provider_class)
    has_key = bool(key_env and os.getenv(key_env, "").strip())
    if provider_class == "mock":
        readiness = "configured"
        credential_source = "none"
        model_label = model_label or "mock"
    elif provider_class == "unconfigured":
        readiness = "not_configured"
        credential_source = "none"
        model_label = "unconfigured"
    else:
        readiness = "configured" if has_key else "not_configured"
        credential_source = "environment" if has_key else "none"
        model_label = model_label or provider_class
    return PublicProviderReadiness(
        provider_class=provider_class,
        provider_readiness=readiness,
        credential_source_class=credential_source,
        model_label=model_label,
    )


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
    ]


@public_router.get(
    "/manifest",
    response_model=HandoffManifest,
    operation_id="get_handoff_manifest",
)
def get_handoff_manifest() -> HandoffManifest:
    warnings = ["live provider calls are outside 0.8.9.1"]
    provider = _provider_readiness_from_env()
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
