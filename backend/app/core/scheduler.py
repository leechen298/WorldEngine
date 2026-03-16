from dataclasses import dataclass, field
from typing import Callable, List


Task = Callable[[], None]


@dataclass
class Scheduler:
    """Placeholder in-process scheduler."""

    tasks: List[Task] = field(default_factory=list)

    def register(self, task: Task) -> None:
        self.tasks.append(task)
