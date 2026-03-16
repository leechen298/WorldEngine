from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Event(BaseModel):
    id: str
    tick_id: int
    world_time_seconds: int
    type: str
    source: str = Field(default="system")
    payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: str


class EventPage(BaseModel):
    items: List[Event]
    next_cursor: Optional[str] = None
    has_more: bool
    limit: int
