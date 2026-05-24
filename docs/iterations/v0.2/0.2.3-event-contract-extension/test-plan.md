# Test Plan

## Unit Tests

After this documentation gate is reviewed and approved, add
`backend/app/tests/test_event_schema_compat.py` with tests for:

- Existing Event construction without refs still works.
- Event.refs defaults to empty list.
- Event accepts refs with id, kind, role, and metadata.
- EventRef rejects empty id.
- EventRef rejects empty kind.
- Event.model_dump includes refs when provided.
- Event.model_validate round-trip preserves refs.
- EventPage validates Event with and without refs.
- EventStep validates items with Event refs.
- EventStepPage validates nested EventStep values.
- Existing current event examples remain compatible.
- Import smoke for EventRef and Event.

## Regression Tests

Existing backend tests must continue to pass because this package must not
change event log storage, runtime engine behavior, modules, API routes,
frontend behavior, or `backend/worldengine/`.

## Commands

Documentation-stage commands for this package:

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.3-event-contract-extension -maxdepth 1 -type f | sort
rg -n "0.2.3-event-contract-extension|ready for review|EventRef|refs|Event Contract|backward compatible|payload|EventPage|EventStep|EventStepPage" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|village|migration|agent memory|pseudo-self|referential integrity|resolve refs|frontend|API route" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
git status --porcelain=v1 -uall | awk '{print $2}' | rg -v '^docs/iterations/v0.2/'
```

Implementation-stage commands to document but not run until code is added
after review approval:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
cd backend && .venv/bin/python - <<'PY'
from app.schemas.event import Event, EventRef
print(Event, EventRef)
PY
```

## Acceptance Criteria

- The documentation gate changes only `docs/iterations/v0.2/`.
- The package directory contains the complete English seven-file set and
  complete `.zh.md` mirrors.
- v0.2 README and plan documents show 0.2.3 as `ready for review`.
- `review.md` and `review.zh.md` record documentation-stage evidence and state
  that implementation has not started.
- No backend, frontend, runtime, schema implementation, API, UI, fixture,
  loader, generator, or test implementation file is changed during the
  documentation stage.
- Implementation may start only after this package is reviewed and approved.

## Not Run

Backend, frontend, runtime, E2E, UI smoke, Agent smoke, and implementation
tests are not run during the documentation stage because no code, runtime,
schema implementation, API, UI, fixture, loader, generator, or test
implementation files change.
