from __future__ import annotations

from app.agent.action_adapter import ActionResultAdapter
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.schemas.agent_loop import ActionIntent
from app.world.dry_run import ParamDryRunValidator
from app.world.state import WorldState
from app.world.validation import ParamRegistry, ParamValidator
from app.world.validation.policy import WorldValidationPolicy


def _adapter(
    *,
    world_state: WorldState | None = None,
    event_log: InMemoryEventLog | None = None,
) -> ActionResultAdapter:
    return ActionResultAdapter(
        world_state=world_state or WorldState(),
        event_log=event_log or InMemoryEventLog(),
        runtime_engine=RuntimeEngine(),
        param_validator=ParamValidator(ParamRegistry.default()),
        param_dry_run_validator=ParamDryRunValidator(
            default_policy=WorldValidationPolicy(),
        ),
    )


def test_noop_intent_returns_no_effect_result() -> None:
    world_state = WorldState(params={"counter": {"increment": 2}})
    event_log = InMemoryEventLog()

    result = _adapter(world_state=world_state, event_log=event_log).apply(
        ActionIntent(type="noop", reason="wait")
    )

    assert result.status == "noop"
    assert result.applied is False
    assert result.action_type == "noop"
    assert result.message == "No action applied."
    assert world_state.get_params() == {"counter": {"increment": 2}}
    assert event_log.snapshot() == []


def test_noop_intent_rejects_unexpected_patches_without_event() -> None:
    world_state = WorldState(params={"counter": {"increment": 2}})
    event_log = InMemoryEventLog()

    result = _adapter(world_state=world_state, event_log=event_log).apply(
        ActionIntent(
            type="noop",
            patches=[
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": 3,
                }
            ],
        )
    )

    assert result.status == "rejected"
    assert result.applied is False
    assert result.action_type == "noop"
    assert result.errors == [
        {
            "path": "patches",
            "reason": "unexpected_payload",
            "detail": "noop does not accept patches.",
        }
    ]
    assert world_state.get_params() == {"counter": {"increment": 2}}
    assert event_log.snapshot() == []


def test_unknown_intent_type_is_rejected_without_mutation() -> None:
    world_state = WorldState(params={"counter": {"increment": 2}})
    event_log = InMemoryEventLog()

    result = _adapter(world_state=world_state, event_log=event_log).apply(
        ActionIntent(type="world.spawn", metadata={"source": "test"})
    )

    assert result.status == "rejected"
    assert result.applied is False
    assert result.action_type == "world.spawn"
    assert result.errors[0]["reason"] == "unsupported_action"
    assert world_state.get_params() == {"counter": {"increment": 2}}
    assert event_log.snapshot() == []


def test_params_patch_static_validation_failure_does_not_mutate_state() -> None:
    world_state = WorldState(params={"counter": {"increment": 2}})
    event_log = InMemoryEventLog()

    result = _adapter(world_state=world_state, event_log=event_log).apply(
        ActionIntent(
            type="params.patch",
            patches=[
                {
                    "op": "set",
                    "path": "runtime.secret",
                    "value": 3,
                }
            ],
        )
    )

    assert result.status == "rejected"
    assert result.applied is False
    assert result.errors[0]["reason"] == "reserved_prefix"
    assert world_state.get_params() == {"counter": {"increment": 2}}
    assert event_log.snapshot() == []


def test_empty_params_patch_is_rejected_without_event() -> None:
    world_state = WorldState(params={"counter": {"increment": 2}})
    event_log = InMemoryEventLog()

    result = _adapter(world_state=world_state, event_log=event_log).apply(
        ActionIntent(type="params.patch", patches=[])
    )

    assert result.status == "rejected"
    assert result.applied is False
    assert result.errors == [
        {
            "path": "patches",
            "reason": "empty_patch",
            "detail": "params.patch requires at least one patch.",
        }
    ]
    assert world_state.get_params() == {"counter": {"increment": 2}}
    assert event_log.snapshot() == []


def test_params_patch_dry_run_failure_does_not_mutate_state() -> None:
    world_state = WorldState(params={"counter": {"increment": 2}})
    world_state.set_validation_override({"max_final_counter": 10})
    event_log = InMemoryEventLog()

    result = _adapter(world_state=world_state, event_log=event_log).apply(
        ActionIntent(
            type="params.patch",
            patches=[
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": 1000,
                }
            ],
        )
    )

    assert result.status == "rejected"
    assert result.applied is False
    assert result.errors[0]["reason"] == "numeric_divergence"
    assert result.metrics["final_counter"] > 10
    assert world_state.get_params() == {"counter": {"increment": 2}}
    assert event_log.snapshot() == []


def test_params_patch_applies_valid_patch_and_emits_agent_loop_event() -> None:
    world_state = WorldState()
    event_log = InMemoryEventLog()

    result = _adapter(world_state=world_state, event_log=event_log).apply(
        ActionIntent(
            type="params.patch",
            reason="increase counter",
            patches=[
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": {"value": 3, "type": "number"},
                }
            ],
        )
    )

    assert result.status == "accepted"
    assert result.applied is True
    assert result.action_type == "params.patch"
    assert result.params == {
        "counter": {
            "increment": {
                "value": 3,
                "type": "number",
            }
        }
    }
    assert result.event_id is not None

    events = event_log.snapshot()
    assert len(events) == 1
    event = events[0]
    assert event.id == result.event_id
    assert event.type == "params.applied"
    assert event.source == "agent.loop"
    assert event.tick_id == 0
    assert event.world_time_seconds == 0
    assert event.created_at == world_state.updated_at
    assert event.payload == {
        "patches": result.patches,
        "updated_at": world_state.updated_at,
        "reason": "increase counter",
    }
