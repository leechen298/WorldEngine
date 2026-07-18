# 0.10.3 Worldview To Runtime Session Creation

Chinese mirror: `README.zh.md`.

Status: final / focused verification passed
Type: mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Create a public session from user worldview input by reusing the existing
redacted worldview generation contract and deterministic/mock fallback labels.

This package connects worldview input to the `0.10.2` session unit. It does
not run the session, generate snapshots, build dashboard UI, or make live
provider calls.

## Scope

Allowed after review:

- Add `POST /sessions/from-worldview`.
- Reuse `generate_worldview_response()` and `provider_readiness_from_env()`.
- Create a session whose `world_id` and public metadata come from the
  generated public world model.
- Add public generation/session summary fields to the session payload.
- Update manifest discovery and focused backend tests.

Allowed files:

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_world_session_api.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- package and parent v0.10 docs/reviews.

Forbidden:

- No live provider call authorization.
- No runtime run controls, snapshot generation, dashboard, durable
  persistence, checker fixtures, Validation Client implementation, generated
  result writing, external validation, or `backend/worldengine/` changes.

## Deliverables

- Reviewed package docs and mirrors.
- Worldview-to-session API.
- Session payload includes public generation mode/status and redacted
  generation/session refs.
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
