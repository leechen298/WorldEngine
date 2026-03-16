from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class ValidationError:
    path: str
    reason: str
    expected: Any | None = None
    got: Any | None = None
    detail: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    errors: list[ValidationError] = field(default_factory=list)

