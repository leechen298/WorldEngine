from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from app.core.event_bus import InMemoryEventLog
from app.schemas.api import ApiResponse
from app.schemas.event import EventPage, EventStepPage

router = APIRouter(prefix="/world", tags=["world"])


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
