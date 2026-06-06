from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_core import PydanticCustomError


RuntimeControlStatus = Literal["idle", "running", "paused"]
RuntimeRunStatus = Literal["completed", "blocked"]
RuntimeRunStopReason = Literal[
    "requested_ticks_reached",
    "requested_duration_reached",
    "max_ticks_reached",
    "max_duration_reached",
    "paused",
]


class RuntimeRunRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ticks: Optional[int] = Field(default=None, ge=1)
    duration_seconds: Optional[int] = Field(default=None, ge=1)
    max_ticks: int = Field(default=100, ge=1, le=10000)
    max_duration_seconds: int = Field(default=86400, ge=1)
    max_provider_calls: int = Field(default=0, ge=0)
    max_estimated_cost_units: int = Field(default=0, ge=0)

    @model_validator(mode="after")
    def _bounded_target_and_guards(self) -> "RuntimeRunRequest":
        if self.ticks is None and self.duration_seconds is None:
            raise PydanticCustomError(
                "runtime_run_unbounded",
                "runtime run request requires exactly one bounded target",
            )
        if self.ticks is not None and self.duration_seconds is not None:
            raise PydanticCustomError(
                "runtime_run_ambiguous_target",
                "runtime run request requires ticks or duration_seconds, not both",
            )
        if self.ticks is not None and self.ticks > self.max_ticks:
            raise PydanticCustomError(
                "runtime_run_tick_guard_exceeded",
                "runtime run ticks must not exceed max_ticks",
            )
        if (
            self.duration_seconds is not None
            and self.duration_seconds > self.max_duration_seconds
        ):
            raise PydanticCustomError(
                "runtime_run_duration_guard_exceeded",
                "runtime run duration_seconds must not exceed max_duration_seconds",
            )
        return self


class RuntimeControlState(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: RuntimeControlStatus


class RuntimeRunSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "0.9.5"
    status: RuntimeRunStatus
    stop_reason: RuntimeRunStopReason
    start_tick: int = Field(ge=0)
    end_tick: int = Field(ge=0)
    start_world_time_seconds: int = Field(ge=0)
    end_world_time_seconds: int = Field(ge=0)
    step_seconds: int = Field(ge=1)
    ticks_requested: Optional[int] = Field(default=None, ge=1)
    duration_requested_seconds: Optional[int] = Field(default=None, ge=1)
    ticks_executed: int = Field(ge=0)
    guard_summary: dict[str, int]
    provider_calls_used: int = 0
    estimated_cost_units_used: int = 0
    redaction_status: Literal["passed"] = "passed"
    control_status: RuntimeControlStatus
