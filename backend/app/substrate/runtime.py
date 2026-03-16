from dataclasses import dataclass


@dataclass
class RuntimeContext:
    """Context container passed through runtime loop steps."""

    tick_count: int = 0
