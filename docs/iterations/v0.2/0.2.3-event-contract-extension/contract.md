# Contract

## Public Concepts

- `EventRef`: a lightweight event-local pointer. It is not a resolved runtime
  object, not storage state, and not a WorldCell or EntityRef binding.
- `Event.refs`: an optional additive list of EventRef values on Event.
- `payload`: the existing flexible event-specific data field. It remains
  unchanged and fully backward compatible.

## Current Event Schema

The current Event schema has:

```python
id: str
tick_id: int
world_time_seconds: int
type: str
source: str
payload: Dict[str, Any]
created_at: str
```

`EventPage`, `EventStep`, and `EventStepPage` wrap Event values. Existing
event construction and API response compatibility must be preserved.

## Allowed Changes

After this documentation gate is reviewed and approved, implementation may
only:

- Add `EventRef` in `backend/app/schemas/event.py`.
- Add optional `refs: List[EventRef] = Field(default_factory=list)` to Event.
- Add focused compatibility tests in
  `backend/app/tests/test_event_schema_compat.py`.
- Update this package's `review.md` and `review.zh.md` during closeout.

## Forbidden Changes

- Do not implement code in this documentation stage.
- Do not change Event `id`, `tick_id`, `world_time_seconds`, `type`, `source`,
  `payload`, or `created_at` semantics.
- Do not remove or rename `payload`.
- Do not require `refs` for existing events.
- Do not modify event log storage.
- Do not modify runtime engine behavior.
- Do not modify modules.
- Do not modify API routes.
- Do not modify frontend.
- Do not modify `backend/worldengine/`.
- Do not connect EventRef to WorldCell runtime.
- Do not resolve refs.
- Do not enforce referential integrity.
- Do not implement a WorldSpec loader.
- Do not implement concrete demo runtime.
- Do not implement agent memory or pseudo-self.
- Do not start 0.2.4.

## Schema Contract

`EventRef` must be defined in `backend/app/schemas/event.py` and must not
import `EntityRef`, `WorldCell`, or `WorldSpec`.

`EventRef` must use the current backend Pydantic style and provide:

```python
id: str
kind: str
role: Optional[str] = None
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`Event` must add:

```python
refs: List[EventRef] = Field(default_factory=list)
```

`kind` remains a string, not a `Literal`, because future reference kinds are
not finalized. `role` remains optional so an event can distinguish subject,
target, actor, location, source_cell, affected_cell, or future roles without
schema churn.

## Validation Contract

- `EventRef.id` must reject empty strings.
- `EventRef.kind` must reject empty strings.
- `EventRef.role` is optional.
- `EventRef.metadata` defaults to an empty dict.
- `Event.refs` defaults to an empty list.
- Existing Event instances without `refs` must still validate.
- Existing Event payload remains unchanged and fully backward compatible.
- Event values with refs must validate inside `EventPage`.
- Event values with refs must validate inside `EventStep`.
- Nested EventStep values with Event refs must validate inside `EventStepPage`.
- `model_dump()` / `model_validate()` round-trip must preserve refs.

## Compatibility Constraints

The extension must be additive. Existing event construction, existing API
response compatibility, EventPage wrapping, EventStep wrapping, EventStepPage
wrapping, and old event examples must remain valid.

`payload` remains the escape hatch for event-specific data. `refs` adds only a
structured pointer slot and does not replace payload.

## North Star Check

EventRef creates an event evidence hook for future recursive worlds,
projections, agent memory, and pseudo-self work without forcing those later
systems into the v0.2 runtime. It keeps the Event Contract broad enough for the
engine north star and narrow enough to preserve current behavior.

## Out-of-Scope Follow-ups

- 0.2.4 WorldSpec Reference Fixture.
- v0.3 WorldSpec loader and runtime bridge.
- Runtime ref resolution and referential integrity.
- Event-driven agent memory or pseudo-self continuity.
- Concrete demo runtime and product surface.
