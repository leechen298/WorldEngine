from __future__ import annotations

from collections import defaultdict
from typing import Callable, DefaultDict, Dict, List, Optional

from app.schemas.event import Event

EventHandler = Callable[[Dict[str, str]], None]


class InMemoryEventLog:
    """In-memory append-only event timeline."""

    def __init__(self) -> None:
        self._events: List[Event] = []

    def append(self, event: Event) -> None:
        self._events.append(event)

    def list(
        self,
        from_tick: Optional[int] = None,
        to_tick: Optional[int] = None,
        limit: int = 200,
    ) -> List[Event]:
        capped_limit = max(1, min(limit, 200))
        filtered = [
            event
            for event in self._events
            if (from_tick is None or event.tick_id >= from_tick)
            and (to_tick is None or event.tick_id <= to_tick)
        ]
        return filtered[:capped_limit]


class EventBus:
    """Placeholder pub/sub bus for runtime events."""

    def __init__(self) -> None:
        self._subscribers: DefaultDict[str, List[EventHandler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        self._subscribers[topic].append(handler)

    def publish(self, topic: str, payload: Dict[str, str]) -> None:
        for handler in self._subscribers[topic]:
            handler(payload)
