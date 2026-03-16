from dataclasses import dataclass

from app.core.clock import Clock
from app.core.event_bus import EventBus
from app.core.scheduler import Scheduler


@dataclass
class RuntimeEngine:
    """Coordinates runtime loop components (placeholder)."""

    clock: Clock
    scheduler: Scheduler
    event_bus: EventBus

    def tick(self) -> None:
        for task in self.scheduler.tasks:
            task()
