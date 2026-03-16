from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Clock:
    """Simple wall-clock provider for runtime code."""

    def now_utc(self) -> datetime:
        return datetime.now(timezone.utc)
