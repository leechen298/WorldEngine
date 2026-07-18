# 0.10.4 Bounded Session Runtime And Snapshot Evidence

Chinese mirror: `README.zh.md`.

Status: final / focused verification passed
Type: mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Add bounded session runtime controls and public snapshot evidence for the
in-memory MVP session unit created in 0.10.2 and 0.10.3.

This package lets a client run a known session for bounded ticks or duration,
pause/resume the session runtime, and inspect public snapshot evidence. It does
not create autonomous Agent behavior, dashboard UI, Validation Client behavior,
or durable persistence.

## Scope

Allowed after review:

- Add session-scoped run, pause, resume, and snapshot-list APIs.
- Reuse the existing bounded `RuntimeRunRequest` and runtime engine guards.
- Add public session run summary fields that reference session id, runtime
  deltas, event counts, snapshot counts, and branch-ready timeline labels.
- Update manifest discovery for session runtime and snapshot surfaces.
- Add focused backend tests for bounds, pause/resume, snapshot evidence,
  redaction, and existing runtime compatibility.

Allowed files:

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_world_session_api.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- `backend/app/tests/test_runtime_bounded_run.py`
- package and parent v0.10 docs/reviews.

Forbidden:

- No infinite default run.
- No live provider calls or provider-cost execution.
- No dashboard UI.
- No checker fixtures or Validation Client implementation.
- No generated result files or external validation.
- No durable persistence or migration.
- No `backend/worldengine/` changes.
- No replay/worldline wording that implies parent/child worlds or source
  worlds.

## Deliverables

- Reviewed package docs and mirrors.
- Session run/pause/resume APIs.
- Session snapshot list API.
- Public session run summary and evidence references.
- Manifest discovery update.
- Focused backend tests and review evidence.

## Status Checklist

- [x] Package documents drafted.
- [x] Documentation / contract evaluator complete.
- [x] Implementation authorized.
- [x] Implementation complete.
- [x] Focused verification complete.
- [x] Evaluator closeout complete.
- [x] Review evidence updated.

## Final Assessment State

Current value: `PASS`.
