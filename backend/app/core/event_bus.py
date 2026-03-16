from collections import defaultdict
from typing import Callable, DefaultDict, Dict, List


EventHandler = Callable[[Dict[str, str]], None]


class EventBus:
    """Placeholder pub/sub bus for runtime events."""

    def __init__(self) -> None:
        self._subscribers: DefaultDict[str, List[EventHandler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        self._subscribers[topic].append(handler)

    def publish(self, topic: str, payload: Dict[str, str]) -> None:
        for handler in self._subscribers[topic]:
            handler(payload)
