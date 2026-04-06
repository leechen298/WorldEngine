from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any, Iterable


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class WorldState:
    def __init__(self, params: dict[str, Any] | None = None) -> None:
        self._params: dict[str, Any] = deepcopy(params or {})
        self._validation_override: dict[str, Any] = {}
        self.updated_at = _utc_now_iso()

    def get_validation_override(self) -> dict[str, Any]:
        return deepcopy(self._validation_override)

    def set_validation_override(self, override: dict[str, Any]) -> None:
        self._validation_override = deepcopy(override)

    def clone(self) -> "WorldState":
        cloned = WorldState(params=self._params)
        cloned.updated_at = self.updated_at
        return cloned

    def get_params(self) -> dict[str, Any]:
        return deepcopy(self._params)

    def apply_patch(self, patches: Iterable[object]) -> dict[str, Any]:
        for patch in patches:
            op = getattr(patch, "op")
            path = getattr(patch, "path")
            value = getattr(patch, "value", None)

            if op in {"add", "set"}:
                self.set_param(path, value)
            elif op == "remove":
                self.remove_param(path)
            else:
                raise ValueError(f"Unsupported patch op: {op}")

        return self.get_params()

    def set_param(self, path: str, value: Any) -> None:
        keys = self._split_path(path)
        current = self._params

        for key in keys[:-1]:
            nested = current.get(key)
            if not isinstance(nested, dict):
                nested = {}
                current[key] = nested
            current = nested

        current[keys[-1]] = deepcopy(value)
        self.updated_at = _utc_now_iso()

    def remove_param(self, path: str) -> None:
        keys = self._split_path(path)
        current = self._params
        parents: list[tuple[dict[str, Any], str]] = []

        for key in keys[:-1]:
            nested = current.get(key)
            if not isinstance(nested, dict):
                return
            parents.append((current, key))
            current = nested

        removed = current.pop(keys[-1], None)
        if removed is None:
            return

        for parent, key in reversed(parents):
            nested = parent.get(key)
            if isinstance(nested, dict) and not nested:
                parent.pop(key, None)
            else:
                break

        self.updated_at = _utc_now_iso()

    @staticmethod
    def _split_path(path: str) -> list[str]:
        keys = [segment for segment in path.split(".") if segment]
        if not keys:
            raise ValueError("Param path must not be empty")
        return keys
