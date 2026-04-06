from __future__ import annotations

from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.schemas.event import Event
from app.world.service import get_default_module_tree
from app.world.state import WorldState
from app.world.validation.policy import WorldValidationPolicy
from app.world.validation.types import ValidationError


@dataclass(frozen=True)
class SimulationReport:
    ok: bool
    metrics: dict[str, Any] = field(default_factory=dict)
    errors: list[ValidationError] = field(default_factory=list)


class ParamDryRunValidator:
    def __init__(self, default_policy: WorldValidationPolicy) -> None:
        self._default_policy = default_policy

    def validate(
        self,
        patches: list[object],
        *,
        world_state: WorldState,
        step_seconds: int,
    ) -> SimulationReport:
        policy = WorldValidationPolicy.merged(
            self._default_policy,
            world_state.get_validation_override(),
        )
        sandbox_world_state = world_state.clone()
        sandbox_world_state.apply_patch(patches)

        dry_run_ticks = max(1, policy.dry_run_steps)

        sandbox_event_log = InMemoryEventLog()
        sandbox_engine = RuntimeEngine(
            step_seconds=step_seconds,
            event_log=sandbox_event_log,
            world_root_module=get_default_module_tree(),
            params_provider=sandbox_world_state.get_params,
        )

        for _ in range(dry_run_ticks):
            sandbox_engine.step()

        sim_events = sandbox_event_log.snapshot()
        metrics = self._build_metrics(sim_events, patches, dry_run_ticks)
        metrics["policy"] = policy.model_dump()
        errors = self._build_errors(sim_events, patches, metrics, policy)
        return SimulationReport(ok=not errors, metrics=metrics, errors=errors)

    def _build_metrics(self, sim_events: list[Event], patches: list[object], dry_run_ticks: int) -> dict[str, Any]:
        total_events = len(sim_events)
        avg_events_per_tick = total_events / dry_run_ticks
        counter_values = [
            event.payload.get("counter")
            for event in sim_events
            if event.type == "module.counter"
        ]
        counter_increments = [
            event.payload.get("increment")
            for event in sim_events
            if event.type == "module.counter"
        ]
        duplicate_set_paths = self._duplicate_set_paths(patches)

        return {
            "dry_run_ticks": dry_run_ticks,
            "total_events": total_events,
            "avg_events_per_tick": avg_events_per_tick,
            "final_counter": counter_values[-1] if counter_values else 0,
            "counter_increment_samples": counter_increments[: min(5, len(counter_increments))],
            "duplicate_set_paths": duplicate_set_paths,
        }

    def _build_errors(
        self,
        sim_events: list[Event],
        patches: list[object],
        metrics: dict[str, Any],
        policy: WorldValidationPolicy,
    ) -> list[ValidationError]:
        errors: list[ValidationError] = []

        if (
            metrics["avg_events_per_tick"] > policy.max_avg_events_per_tick
            or metrics["total_events"] > policy.max_total_events
        ):
            errors.append(
                ValidationError(
                    path="",
                    reason="event_flood",
                    expected={"max_avg": policy.max_avg_events_per_tick, "max_total": policy.max_total_events},
                    got={"avg": metrics["avg_events_per_tick"], "total": metrics["total_events"]},
                    detail=(
                        f"Simulation produced too many events "
                        f"(avg {metrics['avg_events_per_tick']:.1f}/tick, max {policy.max_avg_events_per_tick})."
                    ),
                )
            )

        if metrics["final_counter"] > policy.max_final_counter:
            errors.append(
                ValidationError(
                    path="counter.increment",
                    reason="numeric_divergence",
                    expected={"max_final_counter": policy.max_final_counter},
                    got=metrics["final_counter"],
                    detail=(
                        f"Counter diverged to {metrics['final_counter']} "
                        f"(max {policy.max_final_counter})."
                    ),
                )
            )

        if metrics["duplicate_set_paths"]:
            for dup_path in metrics["duplicate_set_paths"]:
                errors.append(
                    ValidationError(
                        path=dup_path,
                        reason="high_frequency_toggle",
                        detail="Path is set multiple times in the same patch list.",
                    ),
                )

        requested_increment = self._requested_counter_increment(patches)
        if requested_increment is not None and requested_increment != 1:
            observed_increments = [
                event.payload.get("increment")
                for event in sim_events
                if event.type == "module.counter"
            ]
            if observed_increments and all(increment == 1 for increment in observed_increments):
                errors.append(
                    ValidationError(
                        path="counter.increment",
                        reason="no_effect",
                        expected=requested_increment,
                        got=observed_increments[: min(5, len(observed_increments))],
                        detail=(
                            f"Expected increment {requested_increment} "
                            f"but observed all increments = 1."
                        ),
                    ),
                )

        return errors

    @staticmethod
    def _duplicate_set_paths(patches: list[object]) -> list[str]:
        set_paths = [
            getattr(patch, "path", "")
            for patch in patches
            if getattr(patch, "op", None) in {"add", "set"}
        ]
        counts = Counter(path for path in set_paths if path)
        return sorted(path for path, count in counts.items() if count > 1)

    @staticmethod
    def _requested_counter_increment(patches: list[object]) -> int | None:
        requested_value: int | None = None

        for patch in patches:
            if getattr(patch, "path", None) != "counter.increment":
                continue
            if getattr(patch, "op", None) not in {"add", "set"}:
                continue

            raw_value = getattr(patch, "value", None)
            if isinstance(raw_value, Mapping) and "value" in raw_value:
                raw_value = raw_value["value"]

            if isinstance(raw_value, int) and not isinstance(raw_value, bool):
                requested_value = raw_value

        return requested_value
