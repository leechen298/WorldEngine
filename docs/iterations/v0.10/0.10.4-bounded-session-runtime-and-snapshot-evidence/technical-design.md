# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Affected Files

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_world_session_api.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- `backend/app/tests/test_runtime_bounded_run.py`
- package and parent v0.10 docs/reviews.

## Design

Add session-specific response schemas in `app.schemas.session`:

- `SessionRunSummary`
- `SessionSnapshotListResponse`
- small evidence/reference models if needed.

Extend `InMemoryWorldSessionStore` with helpers that refresh session status
after runtime actions. The store remains process-local and does not own
snapshot storage.

Implement session runtime routes in `app.api.routes.session`:

- retrieve the session or return `404`.
- capture event and snapshot counts before running.
- call the existing runtime engine bounded run/pause/resume methods.
- capture event and snapshot counts after running.
- list snapshots from the existing snapshot store, bounded by query params.
- return public evidence summary with branch-ready timeline labels.

Update manifest discovery in `app.api.routes.world`:

- mark `/sessions/{session_id}/run`, `/pause`, `/resume`, and `/snapshots` as
  available/pass after tests.
- keep dashboard and external validation surfaces planned/not_run.

## Redaction

Do not include raw prompts, raw provider responses, provider traces, secrets,
private memory, hidden context, or private evaluator data in run or snapshot
payloads. Reuse existing validation-error sanitization behavior.

## Non-Goals

No durable session runtime partitioning, no database migration, no external
checker fixture, no Validation Client code, and no dashboard UI.
