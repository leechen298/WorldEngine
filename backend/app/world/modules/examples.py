from __future__ import annotations

from typing import Any, Optional

from app.world.module_types import ModuleResult, TickContext
from app.world.modules.base import WorldModule, build_module_event


class HeartbeatModule(WorldModule):
    def on_tick(self, ctx: TickContext) -> ModuleResult:
        enabled = _get_param(ctx.params, "heartbeat.enabled")
        if isinstance(enabled, bool) and not enabled:
            return ModuleResult(
                events=[],
                summary=f"{self.module_path} heartbeat disabled",
                state_delta={},
            )

        summary = f"{self.module_path} heartbeat at tick {ctx.tick_id}"
        return ModuleResult(
            events=[
                build_module_event(
                    ctx,
                    event_type="module.tick",
                    module_path=self.module_path,
                    payload={"summary": summary},
                )
            ],
            summary=summary,
            state_delta={},
        )


class CounterModule(WorldModule):
    def __init__(self, name: str, module_path: Optional[str] = None) -> None:
        super().__init__(name=name, module_path=module_path)
        self._counter = 0

    def on_tick(self, ctx: TickContext) -> ModuleResult:
        increment = _get_param(ctx.params, "counter.increment")
        if not (isinstance(increment, int) and not isinstance(increment, bool)):
            increment = 1

        self._counter += increment
        summary = f"{self.module_path} counter={self._counter}"
        return ModuleResult(
            events=[
                build_module_event(
                    ctx,
                    event_type="module.counter",
                    module_path=self.module_path,
                    payload={
                        "increment": increment,
                        "counter": self._counter,
                        "summary": summary,
                    },
                )
            ],
            summary=summary,
            state_delta={},
        )


def _get_param(params: dict[str, Any], path: str) -> Any:
    current: Any = params
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current
