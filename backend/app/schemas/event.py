from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, model_serializer


class EventRef(BaseModel):
    id: str = Field(min_length=1)
    kind: str = Field(min_length=1)
    role: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Event(BaseModel):
    id: str
    tick_id: int
    world_time_seconds: int
    type: str
    source: str = Field(default="system")
    payload: Dict[str, Any] = Field(default_factory=dict)
    refs: List[EventRef] = Field(default_factory=list)
    created_at: str

    @model_serializer(mode="wrap")
    def serialize_model(self, handler: Any) -> Dict[str, Any]:
        data = handler(self)
        if not self.refs:
            data.pop("refs", None)
        return data


class EventPage(BaseModel):
    items: List[Event]
    next_cursor: Optional[str] = None
    has_more: bool
    limit: int


class EventStep(BaseModel):
    tick_id: int
    world_time_seconds: int
    event_count: int
    created_at: str
    items: List[Event]


class EventStepPage(BaseModel):
    items: List[EventStep]
    next_cursor: Optional[str] = None
    has_more: bool
    limit: int
