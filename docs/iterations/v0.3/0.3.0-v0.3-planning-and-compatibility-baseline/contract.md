# Contract

Status: ready for review

## Public Concept Changes

This package establishes v0.3 as WorldSpec Loader and Runtime Bridge planning.
It adds no new runtime behavior and no new public API behavior.

## Allowed Changes

- Create v0.3 iteration docs.
- Create 0.3.0 package docs.
- Update roadmap v0.2 status wording if still inconsistent with v0.2 final
  closeout.
- Add v0.3 release placeholder docs.
- Add compatibility baseline requirements.

## Forbidden Changes

- Runtime changes.
- Schema changes.
- API changes.
- Frontend changes.
- Backend test changes.
- Fixture changes.
- Loader implementation.
- Bridge implementation.
- Agent implementation.
- Memory or self-continuity implementation.
- Generation implementation.
- Projection implementation.
- External repository creation.
- Concrete demo world details.
- Concrete external validation world details.
- Product UI or game backend behavior.

## Compatibility Requirements

Future v0.3 packages must provide current-session compatibility evidence
before changing:

- `RuntimeEngine` tick behavior.
- `world_time_seconds` behavior.
- API envelope or response shape.
- `/runtime/step`.
- `/world/events`.
- `/world/event-steps`.
- event storage or optional `Event.refs` behavior.
- world params behavior.
- archive snapshot or summary behavior.
- frontend-facing behavior.
- legacy `backend/worldengine/` boundary.

## Relationship To North Star And Roadmap

This package supports the north star by preparing generic WorldSpec loading and
runtime bridge work without narrowing WorldEngine into a demo-specific backend.
It keeps v0.4 Agent-in-World, v0.5 memory, v0.6 generation, and later
projection work outside current scope.
