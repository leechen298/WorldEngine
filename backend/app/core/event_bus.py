from __future__ import annotations

from collections import defaultdict
from typing import Callable, DefaultDict, Dict, List, Optional

from app.schemas.event import Event, EventPage

EventHandler = Callable[[Dict[str, str]], None]


class InMemoryEventLog:
    """In-memory append-only event timeline."""

    def __init__(self) -> None:
        self._events: List[Event] = []
        self._event_index_by_id: Dict[str, int] = {}

    def append(self, event: Event) -> None:
        self._event_index_by_id[event.id] = len(self._events)
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

    def list_page(
        self,
        *,
        cursor: Optional[str] = None,
        from_tick: Optional[int] = None,
        to_tick: Optional[int] = None,
        limit: int = 20,
    ) -> EventPage:
        capped_limit = max(1, min(limit, 200))

        if cursor is None:
            current_index = len(self._events) - 1
        else:
            cursor_index = self._event_index_by_id.get(cursor)
            if cursor_index is None:
                raise KeyError(cursor)
            current_index = cursor_index - 1

        items: List[Event] = []
        has_more = False

        while current_index >= 0:
            event = self._events[current_index]
            current_index -= 1

            if from_tick is not None and event.tick_id < from_tick:
                continue
            if to_tick is not None and event.tick_id > to_tick:
                continue

            if len(items) < capped_limit:
                items.append(event)
                continue

            has_more = True
            break

        next_cursor = items[-1].id if has_more and items else None
        return EventPage(
            items=items,
            next_cursor=next_cursor,
            has_more=has_more,
            limit=capped_limit,
        )


class EventBus:
    """Placeholder pub/sub bus for runtime events."""

    def __init__(self) -> None:
        self._subscribers: DefaultDict[str, List[EventHandler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        self._subscribers[topic].append(handler)

    def publish(self, topic: str, payload: Dict[str, str]) -> None:
        for handler in self._subscribers[topic]:
            handler(payload)
