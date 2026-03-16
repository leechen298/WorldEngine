from __future__ import annotations

from typing import Iterable, List

from app.world.module_types import ModuleResult, TickContext
from app.world.modules.base import WorldModule, build_module_event


class CompositeModule(WorldModule):
    def __init__(self, name: str, children: Iterable[WorldModule]) -> None:
        super().__init__(name=name)
        self.children = list(children)
        self._sync_child_paths()

    def set_module_path(self, module_path: str) -> None:
        super().set_module_path(module_path)
        self._sync_child_paths()

    def on_tick(self, ctx: TickContext) -> ModuleResult:
        events = []
        child_summaries: List[str] = []

        for child in self.children:
            child_result = child.on_tick(ctx)
            events.extend(child_result.events)
            if child_result.summary:
                child_summaries.append(child_result.summary)

        summary = f"{self.module_path} aggregated {len(self.children)} child modules"
        events.append(
            build_module_event(
                ctx,
                event_type="module.aggregate",
                module_path=self.module_path,
                payload={
                    "child_count": len(self.children),
                    "child_summaries": child_summaries,
                    "summary": summary,
                },
            )
        )
        return ModuleResult(events=events, summary=summary, state_delta={})

    def _sync_child_paths(self) -> None:
        for child in self.children:
            child.set_module_path(f"{self.module_path}.{child.name}")
