# 0.10.2 World Session Contract And State Store

Chinese mirror: `README.zh.md`.

Status: final / focused verification passed
Type: mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Add the first public world session contract and in-memory session state store
so clients can create, list, read, and inspect a stable MVP session unit.

This package does not run sessions. It only creates the session identity and
status surface that later packages use for worldview-to-session creation,
bounded runtime, snapshots, dashboard flow, and validation handoff.

## Scope

Allowed implementation scope after review:

- Public session schemas for create/list/read/status payloads.
- In-memory session store attached to FastAPI app state.
- Public session routes for create, list, read, and status.
- Additive manifest updates marking implemented session discovery surfaces.
- Focused backend tests for session lifecycle, isolation, redaction, manifest
  compatibility, and existing world/runtime API compatibility.

Allowed implementation files:

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/__init__.py`
- `backend/app/api/app_factory.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_world_session_api.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- package and parent v0.10 docs/reviews.

Forbidden scope:

- No worldview-to-session generation flow.
- No session runtime run controls, pause/resume wrappers, snapshot generation,
  diff/replay engine, dashboard flow, durable persistence, migrations,
  provider live calls, checker fixtures, Validation Client implementation,
  generated results, external validation, or `backend/worldengine/` changes.

## Deliverables

- Reviewed package docs and mirrors.
- Public in-memory world session contract and store.
- Session create/list/read/status API.
- Manifest discovery update for implemented session surfaces.
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

Current value: `final / focused verification passed`.

This package is complete for session create/list/read/status only. It does
not claim worldview-to-session creation, session runtime, snapshot generation,
dashboard flow, provider live calls, checker output, Validation Client
execution, external validation, or full v0.10 PASS.
