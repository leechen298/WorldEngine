from typing import Any, Dict

from pydantic import BaseModel, Field


class Event(BaseModel):
    id: str
    tick_id: int
    world_time_seconds: int
    type: str
    source: str = Field(default="system")
    payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: str
