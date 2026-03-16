from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Request

from app.core.event_bus import InMemoryEventLog
from app.schemas.event import Event

router = APIRouter(prefix="/world", tags=["world"])


def get_event_log(request: Request) -> InMemoryEventLog:
    return request.app.state.event_log


@router.get("/events", response_model=List[Event])
def get_world_events(
    from_tick: Optional[int] = Query(default=None, ge=0),
    to_tick: Optional[int] = Query(default=None, ge=0),
    limit: int = Query(default=200, ge=1, le=200),
    event_log: InMemoryEventLog = Depends(get_event_log),
) -> List[Event]:
    return event_log.list(from_tick=from_tick, to_tick=to_tick, limit=limit)
