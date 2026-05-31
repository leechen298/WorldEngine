from __future__ import annotations

from app.agent.action_adapter import ActionResultAdapter
from app.agent.loop_service import AgentLoopService
from app.agent.perception import PerceptionBuilder
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.schemas.agent_loop import ActionIntent, LoopStepRequest
from app.schemas.event import Event
from app.world.dry_run import ParamDryRunValidator
from app.world.state import WorldState
from app.world.validation import ParamRegistry, ParamValidator
from app.world.validation.policy import WorldValidationPolicy


def _event(event_id: str, tick_id: int) -> Event:
    return Event(
        id=event_id,
        tick_id=tick_id,
        world_time_seconds=tick_id * 600,
        type="test.event",
        source="test",
        payload={"tick": tick_id},
        created_at=f"2026-05-30T00:0{tick_id}:00+00:00",
    )


def _service(
    *,
    world_state: WorldState | None = None,
    event_log: InMemoryEventLog | None = None,
) -> AgentLoopService:
    state = world_state or WorldState()
    log = event_log or InMemoryEventLog()
    runtime_engine = RuntimeEngine(
        event_log=log,
        params_provider=state.get_params,
    )
    return AgentLoopService(
        perception_builder=PerceptionBuilder(
            runtime_engine=runtime_engine,
            event_log=log,
            world_state=state,
        ),
        action_adapter=ActionResultAdapter(
            world_state=state,
            event_log=log,
            runtime_engine=runtime_engine,
            param_validator=ParamValidator(ParamRegistry.default()),
            param_dry_run_validator=ParamDryRunValidator(
                default_policy=WorldValidationPolicy(),
            ),
        ),
    )


def test_loop_step_without_intent_uses_deterministic_noop() -> None:
    event_log = InMemoryEventLog()
    event_log.append(_event("event-1", 1))
    event_log.append(_event("event-2", 2))

    response = _service(event_log=event_log).step(
        LoopStepRequest(event_limit=1)
    )

    assert response.intent.type == "noop"
    assert response.intent.reason == "default deterministic noop"
    assert response.result.status == "noop"
    assert response.result.applied is False
    assert [event.id for event in response.perception.recent_events] == ["event-2"]
    assert [event.id for event in event_log.snapshot()] == ["event-1", "event-2"]


def test_loop_step_applies_params_patch_after_perception() -> None:
    world_state = WorldState(params={"counter": {"increment": 1}})
    event_log = InMemoryEventLog()

    response = _service(world_state=world_state, event_log=event_log).step(
        LoopStepRequest(
            intent=ActionIntent(
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
    )

    assert response.perception.params == {"counter": {"increment": 1}}
    assert response.intent.type == "params.patch"
    assert response.result.status == "accepted"
    assert response.result.applied is True
    assert response.result.params == {"counter": {"increment": {"value": 3, "type": "number"}}}
    assert world_state.get_params() == response.result.params

    events = event_log.snapshot()
    assert len(events) == 1
    assert events[0].id == response.result.event_id
    assert events[0].type == "params.applied"
    assert events[0].source == "agent.loop"


def test_loop_step_rejected_action_returns_result_without_mutation() -> None:
    world_state = WorldState(params={"counter": {"increment": 2}})
    event_log = InMemoryEventLog()

    response = _service(world_state=world_state, event_log=event_log).step(
        LoopStepRequest(
            intent=ActionIntent(type="world.spawn", metadata={"source": "test"})
        )
    )

    assert response.result.status == "rejected"
    assert response.result.applied is False
    assert response.result.errors[0]["reason"] == "unsupported_action"
    assert world_state.get_params() == {"counter": {"increment": 2}}
    assert event_log.snapshot() == []
