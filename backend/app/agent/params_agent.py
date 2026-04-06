"""ParamsAgent: LLM-driven propose-and-apply loop for world params."""

from __future__ import annotations

import json
from typing import Any
from uuid import uuid4

from app.agent.llm_provider import LLMProvider
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.schemas.event import Event
from app.schemas.params import ParamPatchItem
from app.world.dry_run import ParamDryRunValidator
from app.world.state import WorldState
from app.world.validation import ParamValidator
from app.world.validation.registry import ParamRegistry


PROPOSE_SYSTEM = (
    "You are a WorldEngine params agent. You output ONLY valid JSON, no other text.\n\n"
    "Output format:\n"
    '{{"patches":[{{"op":"set","path":"<param_path>","value":<value_or_structured>}}]}}\n\n'
    "Allowed paths and types (from registry):\n"
    "{registry_rules}\n\n"
    'Value can be a plain value or structured: {{"value": <val>, "type": "<type_name>"}}\n\n'
    "NEVER modify paths starting with system./ runtime./ _internal.\n\n"
    "Example:\n"
    '{{"patches":[{{"op":"set","path":"counter.increment","value":{{"value":2,"type":"number"}}}}]}}'
)

PROPOSE_USER = (
    "Current state:\n"
    "- tick_id: {tick_id}\n"
    "- world_time_seconds: {world_time_seconds}\n"
    "- params: {params}\n"
    "- recent_events (last {event_count}): {recent_events}\n\n"
    "Goal: {goal}\n\n"
    "Produce patches JSON to move the world toward the goal."
)

FIX_USER = (
    "Your previous patches failed validation.\n\n"
    "Previous patches: {patches}\n"
    "Errors: {errors}\n"
    "Metrics: {metrics}\n\n"
    "Fix ONLY the failing fields. Do NOT introduce new paths. Output corrected patches JSON."
)


def _format_registry_rules(registry: ParamRegistry) -> str:
    lines = []
    for path, rule in registry._rules.items():
        constraints = dict(rule.constraints) if rule.constraints else {}
        lines.append(f"  {path}: type={rule.expected_type}, constraints={constraints}")
    return "\n".join(lines)


def _utc_now_iso() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat()


class ParamsAgent:
    def __init__(
        self,
        *,
        llm: LLMProvider,
        param_validator: ParamValidator,
        param_dry_run_validator: ParamDryRunValidator,
        world_state: WorldState,
        event_log: InMemoryEventLog,
        runtime_engine: RuntimeEngine,
        registry: ParamRegistry,
        max_attempts: int = 3,
    ) -> None:
        self._llm = llm
        self._param_validator = param_validator
        self._dry_run_validator = param_dry_run_validator
        self._world_state = world_state
        self._event_log = event_log
        self._runtime_engine = runtime_engine
        self._registry = registry
        self._max_attempts = max(1, max_attempts)

    async def propose_and_apply(self, goal: str | None = None) -> dict[str, Any]:
        runtime_state = self._runtime_engine.get_state()
        params = self._world_state.get_params()
        recent_events = self._event_log.list(limit=20)

        system_prompt = PROPOSE_SYSTEM.format(
            registry_rules=_format_registry_rules(self._registry),
        )
        user_prompt = PROPOSE_USER.format(
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            params=json.dumps(params, default=str),
            event_count=len(recent_events),
            recent_events=json.dumps(
                [{"type": e.type, "source": e.source, "payload": e.payload} for e in recent_events],
                default=str,
            ),
            goal=goal or "improve the world state",
        )

        last_errors: list[dict[str, Any]] = []
        last_metrics: dict[str, Any] = {}
        patches_dicts: list[dict[str, Any]] = []

        for attempt in range(1, self._max_attempts + 1):
            # Call LLM
            try:
                llm_output = await self._llm.complete_json(
                    system=system_prompt,
                    user=user_prompt,
                )
            except Exception as exc:
                last_errors = [{"path": "", "reason": "llm_call_failed", "detail": str(exc)}]
                continue

            # Parse patches
            if not isinstance(llm_output, dict) or "patches" not in llm_output:
                last_errors = [{"path": "", "reason": "llm_invalid_json", "detail": "Missing 'patches' key"}]
                user_prompt = FIX_USER.format(
                    patches=json.dumps(llm_output, default=str),
                    errors=json.dumps(last_errors),
                    metrics="{}",
                )
                continue

            patches_dicts = llm_output["patches"]
            if not isinstance(patches_dicts, list):
                last_errors = [{"path": "", "reason": "llm_invalid_json", "detail": "'patches' is not a list"}]
                user_prompt = FIX_USER.format(
                    patches=json.dumps(llm_output, default=str),
                    errors=json.dumps(last_errors),
                    metrics="{}",
                )
                continue

            # Build ParamPatchItem list
            try:
                patch_items = [
                    ParamPatchItem(op=p["op"], path=p["path"], value=p.get("value"))
                    for p in patches_dicts
                ]
            except (KeyError, TypeError) as exc:
                last_errors = [{"path": "", "reason": "llm_invalid_json", "detail": f"Bad patch format: {exc}"}]
                user_prompt = FIX_USER.format(
                    patches=json.dumps(patches_dicts, default=str),
                    errors=json.dumps(last_errors),
                    metrics="{}",
                )
                continue

            # Step 5.1: static validation
            validation_result = self._param_validator.validate(patch_items)
            if not validation_result.ok:
                last_errors = [e.to_dict() for e in validation_result.errors]
                last_metrics = {}
                user_prompt = FIX_USER.format(
                    patches=json.dumps(patches_dicts, default=str),
                    errors=json.dumps(last_errors),
                    metrics="{}",
                )
                continue

            # Step 5.2: dry-run validation
            dry_run_report = self._dry_run_validator.validate(
                patch_items,
                world_state=self._world_state,
                step_seconds=runtime_state.step_seconds,
            )
            if not dry_run_report.ok:
                last_errors = [e.to_dict() for e in dry_run_report.errors]
                last_metrics = dry_run_report.metrics
                user_prompt = FIX_USER.format(
                    patches=json.dumps(patches_dicts, default=str),
                    errors=json.dumps(last_errors),
                    metrics=json.dumps(last_metrics, default=str),
                )
                continue

            # All validations passed — apply
            self._world_state.apply_patch(patch_items)

            self._event_log.append(
                Event(
                    id=str(uuid4()),
                    tick_id=runtime_state.tick_id,
                    world_time_seconds=runtime_state.world_time_seconds,
                    type="params.applied",
                    source="agent.params",
                    payload={
                        "patches": patches_dicts,
                        "updated_at": self._world_state.updated_at,
                    },
                    created_at=self._world_state.updated_at,
                )
            )

            return {
                "applied": True,
                "patches": patches_dicts,
                "attempts": attempt,
            }

        # All attempts exhausted — reject
        self._event_log.append(
            Event(
                id=str(uuid4()),
                tick_id=runtime_state.tick_id,
                world_time_seconds=runtime_state.world_time_seconds,
                type="params.proposal_rejected",
                source="agent.params",
                payload={
                    "last_errors": last_errors,
                    "last_metrics": last_metrics,
                    "attempts": self._max_attempts,
                },
                created_at=_utc_now_iso(),
            )
        )

        return {
            "applied": False,
            "errors": last_errors,
            "metrics": last_metrics,
            "attempts": self._max_attempts,
        }
