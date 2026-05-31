from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.event import Event
from app.schemas.params import ParamPatchItem


class RuntimeStateSummary(BaseModel):
    tick_id: int
    world_time_seconds: int
    step_seconds: int
    is_running: bool
    updated_at: Optional[str] = None


class RuntimeContextSummary(BaseModel):
    worldspec_id: str
    schema_version: str
    root_cell_id: str
    root_cell_type: str
    source_type: str
    source_label: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PerceptionFrame(BaseModel):
    runtime: RuntimeStateSummary
    params: Dict[str, Any] = Field(default_factory=dict)
    recent_events: List[Event] = Field(default_factory=list)
    runtime_context_summary: Optional[RuntimeContextSummary] = None


class ActionParamPatchItem(ParamPatchItem):
    model_config = ConfigDict(extra="forbid")


class ActionIntent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: str
    patches: List[ActionParamPatchItem] = Field(default_factory=list)
    reason: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ActionResult(BaseModel):
    status: str
    applied: bool = False
    action_type: str
    patches: List[Dict[str, Any]] = Field(default_factory=list)
    errors: List[Dict[str, Any]] = Field(default_factory=list)
    metrics: Dict[str, Any] = Field(default_factory=dict)
    params: Dict[str, Any] = Field(default_factory=dict)
    event_id: Optional[str] = None
    message: str


class LoopStepRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    intent: Optional[ActionIntent] = None
    event_limit: int = Field(default=20, ge=1, le=200)


class LoopStepResponse(BaseModel):
    perception: PerceptionFrame
    intent: ActionIntent
    result: ActionResult
