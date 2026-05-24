# Technical Design

## Current State

The active backend path is `backend/app/`. The current Event schema lives in
`backend/app/schemas/event.py` and defines Event, EventPage, EventStep, and
EventStepPage with Pydantic `BaseModel` and `Field`.

Event currently has `id`, `tick_id`, `world_time_seconds`, `type`, `source`,
`payload`, and `created_at`. EventPage, EventStep, and EventStepPage wrap Event
values. There is no structured reference list on Event today.

## Contract Alignment and Invariants

- The implementation must be additive.
- Existing Event construction without refs must remain valid.
- Existing Event payload behavior must remain unchanged.
- EventPage, EventStep, and EventStepPage must remain compatible with old and
  new Event values.
- EventRef must stay event-local and lightweight.
- EventRef must be defined in `backend/app/schemas/event.py`.
- `backend/app/schemas/event.py` must not import EntityRef, WorldCell, or
  WorldSpec for this package.

## Proposed Implementation

After review approval, update `backend/app/schemas/event.py` only by:

- adding `EventRef`.
- adding `refs: List[EventRef] = Field(default_factory=list)` to Event.
- adding validation that rejects empty `EventRef.id` and empty `EventRef.kind`.

Add `backend/app/tests/test_event_schema_compat.py` with focused schema tests.
Tests should construct models directly and avoid app factory, HTTP routes,
runtime stepping, event log storage, fixtures, loaders, or frontend behavior.

## Affected Surfaces

- Schemas: Event gains optional `refs`; EventRef is added.
- Tests: a focused event schema compatibility test file is added.
- Event log storage: not affected.
- Runtime engine: not affected.
- Modules: not affected.
- API routes: not affected.
- Frontend: not affected.
- `backend/worldengine/`: not affected.

## Data Model / Schema Changes

`EventRef` fields:

```python
id: str
kind: str
role: Optional[str] = None
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`Event` adds:

```python
refs: List[EventRef] = Field(default_factory=list)
```

`kind` is intentionally a string rather than `Literal` because future
reference kinds are not finalized. `role` is optional so later event producers
can distinguish subject, target, actor, location, source_cell, affected_cell,
or future roles without another schema migration.

## Runtime / Service Design

No runtime or service design changes are included. The implementation must not
resolve refs, enforce referential integrity, connect EventRef to WorldCell
runtime, modify event log storage, or alter API route behavior.

## Compatibility

Compatibility is preserved because `refs` defaults to an empty list and old
Event dictionaries without refs remain valid. `payload` remains the flexible
escape hatch for event-specific data and is not removed, renamed, narrowed, or
reinterpreted.

## Risks

- Risk: EventRef accidentally imports recursive-world schemas. Detection:
  contract review and implementation diff review must confirm no EntityRef,
  WorldCell, or WorldSpec import in `event.py`.
- Risk: old events without refs fail validation. Detection: focused schema
  compatibility tests.
- Risk: EventPage, EventStep, or EventStepPage wrappers reject new Event refs.
  Detection: wrapper validation tests.
- Risk: payload semantics are changed while adding refs. Detection: test old
  event examples and review the event schema diff.
- Risk: implementation widens into runtime, API route, frontend, loader,
  village, migration, agent memory, or pseudo-self work. Detection:
  changed-file scope checks.
