from __future__ import annotations

from typing import Any
from uuid import uuid4

from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.schemas.agent_loop import ActionIntent, ActionResult
from app.schemas.event import Event
from app.world.dry_run import ParamDryRunValidator
from app.world.state import WorldState
from app.world.validation import ParamValidator


def _utc_now_iso() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).isoformat()


class ActionResultAdapter:
    def __init__(
        self,
        *,
        world_state: WorldState,
        event_log: InMemoryEventLog,
        runtime_engine: RuntimeEngine,
        param_validator: ParamValidator,
        param_dry_run_validator: ParamDryRunValidator,
    ) -> None:
        self._world_state = world_state
        self._event_log = event_log
        self._runtime_engine = runtime_engine
        self._param_validator = param_validator
        self._param_dry_run_validator = param_dry_run_validator

    def apply(self, intent: ActionIntent) -> ActionResult:
        if intent.type == "noop":
            if intent.patches:
                return self._rejected(
                    intent,
                    errors=[
                        {
                            "path": "patches",
                            "reason": "unexpected_payload",
                            "detail": "noop does not accept patches.",
                        }
                    ],
                )
            return ActionResult(
                status="noop",
                applied=False,
                action_type=intent.type,
                message="No action applied.",
            )

        if intent.type != "params.patch":
            return self._rejected(
                intent,
                errors=[
                    {
                        "path": "",
                        "reason": "unsupported_action",
                        "detail": "Action type is not supported in v0.4.",
                    }
                ],
            )

        if not intent.patches:
            return self._rejected(
                intent,
                errors=[
                    {
                        "path": "patches",
                        "reason": "empty_patch",
                        "detail": "params.patch requires at least one patch.",
                    }
                ],
            )

        validation_result = self._param_validator.validate(intent.patches)
        if not validation_result.ok:
            return self._rejected(
                intent,
                errors=[error.to_dict() for error in validation_result.errors],
            )

        runtime_state = self._runtime_engine.get_state()
        dry_run_report = self._param_dry_run_validator.validate(
            intent.patches,
            world_state=self._world_state,
            step_seconds=runtime_state.step_seconds,
        )
        if not dry_run_report.ok:
            return self._rejected(
                intent,
                errors=[error.to_dict() for error in dry_run_report.errors],
                metrics=dry_run_report.metrics,
            )

        params = self._world_state.apply_patch(intent.patches)
        patches = self._patch_dicts(intent)
        event_id = str(uuid4())
        updated_at = self._world_state.updated_at or _utc_now_iso()
        self._event_log.append(
            Event(
                id=event_id,
                tick_id=runtime_state.tick_id,
                world_time_seconds=runtime_state.world_time_seconds,
                type="params.applied",
                source="agent.loop",
                payload={
                    "patches": patches,
                    "updated_at": updated_at,
                    "reason": intent.reason,
                },
                created_at=updated_at,
            )
        )

        return ActionResult(
            status="accepted",
            applied=True,
            action_type=intent.type,
            patches=patches,
            params=params,
            event_id=event_id,
            message="Action applied.",
        )

    def _rejected(
        self,
        intent: ActionIntent,
        *,
        errors: list[dict[str, Any]],
        metrics: dict[str, Any] | None = None,
    ) -> ActionResult:
        return ActionResult(
            status="rejected",
            applied=False,
            action_type=intent.type,
            errors=errors,
            metrics=metrics or {},
            message="Action rejected.",
        )

    @staticmethod
    def _patch_dicts(intent: ActionIntent) -> list[dict[str, Any]]:
        return [patch.model_dump() for patch in intent.patches]
