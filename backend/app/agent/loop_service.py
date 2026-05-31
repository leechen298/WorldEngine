from __future__ import annotations

from app.agent.action_adapter import ActionResultAdapter
from app.agent.perception import PerceptionBuilder
from app.schemas.agent_loop import ActionIntent, LoopStepRequest, LoopStepResponse


class AgentLoopService:
    """Runs one request-scoped Agent-in-World loop step."""

    def __init__(
        self,
        *,
        perception_builder: PerceptionBuilder,
        action_adapter: ActionResultAdapter,
    ) -> None:
        self._perception_builder = perception_builder
        self._action_adapter = action_adapter

    def step(self, request: LoopStepRequest) -> LoopStepResponse:
        perception = self._perception_builder.build(
            event_limit=request.event_limit,
        )
        intent = request.intent or self._default_intent()
        result = self._action_adapter.apply(intent)
        return LoopStepResponse(
            perception=perception,
            intent=intent,
            result=result,
        )

    @staticmethod
    def _default_intent() -> ActionIntent:
        return ActionIntent(
            type="noop",
            reason="default deterministic noop",
        )
