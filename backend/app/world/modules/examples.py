from __future__ import annotations

from typing import Optional

from app.world.module_types import ModuleResult, TickContext
from app.world.modules.base import WorldModule, build_module_event


class HeartbeatModule(WorldModule):
    def on_tick(self, ctx: TickContext) -> ModuleResult:
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
        self._counter += 1
        summary = f"{self.module_path} counter={self._counter}"
        return ModuleResult(
            events=[
                build_module_event(
                    ctx,
                    event_type="module.counter",
                    module_path=self.module_path,
                    payload={
                        "counter": self._counter,
                        "summary": summary,
                    },
                )
            ],
            summary=summary,
            state_delta={},
        )
