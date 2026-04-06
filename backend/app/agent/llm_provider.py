"""LLM provider protocol and mock implementation for params agent."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class LLMProvider(Protocol):
    async def complete_json(
        self,
        *,
        system: str,
        user: str,
        schema_hint: str | None = None,
    ) -> dict[str, Any]: ...


class MockLLMProvider:
    """Returns pre-configured responses in sequence (for testing)."""

    def __init__(self, responses: list[dict[str, Any]]) -> None:
        self._responses = list(responses)
        self._call_index = 0

    async def complete_json(
        self,
        *,
        system: str,
        user: str,
        schema_hint: str | None = None,
    ) -> dict[str, Any]:
        if self._call_index >= len(self._responses):
            return self._responses[-1]
        response = self._responses[self._call_index]
        self._call_index += 1
        return response
