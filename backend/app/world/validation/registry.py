from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Literal


ExpectedType = Literal["int", "bool", "float", "string", "json"]


@dataclass(frozen=True)
class ParamRule:
    expected_type: ExpectedType
    constraints: Mapping[str, Any] = field(default_factory=dict)
    allow_structured: bool = True


class ParamRegistry:
    def __init__(
        self,
        rules: Mapping[str, ParamRule],
        reserved_prefixes: tuple[str, ...] = ("system", "runtime", "_internal"),
    ) -> None:
        self._rules = dict(rules)
        self._reserved_prefixes = reserved_prefixes

    @classmethod
    def default(cls) -> "ParamRegistry":
        return cls(
            rules={
                "counter.increment": ParamRule(
                    expected_type="int",
                    constraints={"min": 1, "max": 1000},
                ),
                "heartbeat.enabled": ParamRule(expected_type="bool"),
                "scene.weather": ParamRule(expected_type="string"),
            }
        )

    def get_rule(self, path: str) -> ParamRule | None:
        return self._rules.get(path)

    def is_reserved_path(self, path: str) -> bool:
        return any(
            path == prefix or path.startswith(f"{prefix}.")
            for prefix in self._reserved_prefixes
        )

