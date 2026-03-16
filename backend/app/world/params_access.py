from __future__ import annotations

from typing import Any


def get_param_raw(params: dict[str, Any], path: str) -> Any:
    current: Any = params

    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]

    return current


def get_param_value(params: dict[str, Any], path: str) -> Any:
    raw = get_param_raw(params, path)
    if isinstance(raw, dict) and "value" in raw:
        return raw["value"]
    return raw
