# E2E / Integration Validation Report

Status: passed

## Report Fields

- Reviewed branch: `v0.3`
- Execution branch: `v0.3`
- Evidence commit: `da63cb8f28b484fba22596eb44fa5f09a218e45a`
- Final documentation closeout commit:
  `6712123b402fa8d454ede7779cc6a401d82ce684`
- Evidence-to-closeout implementation delta: none for runtime, schema, API,
  frontend, backend tests, fixtures, or migrations.
- Validation date: 2026-05-29
- Executor: Codex

## Commands Run

```text
git status --short --branch
git rev-parse HEAD
git diff --check
make check-backend
make check-frontend
cd backend && .venv/bin/python -m pytest app/tests
cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_loader.py
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py
cd backend && .venv/bin/python -m pytest app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_step.py
make test-e2e
make test-e2e  # approved rerun outside sandbox after local port bind was denied
```

## Results

- Branch / commit recording: `git status --short --branch` reported
  `## v0.3...origin/v0.3`; `git rev-parse HEAD` reported
  `da63cb8f28b484fba22596eb44fa5f09a218e45a`.
- Documentation check: `git diff --check` exited `0`.
- Dependency checks: `make check-backend` and `make check-frontend` exited `0`.
- Backend deterministic result: `cd backend && .venv/bin/python -m pytest app/tests`
  exited `0` with `112 passed in 0.80s`.
- WorldSpec loader result:
  `cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_loader.py`
  exited `0` with `7 passed in 0.04s`.
- Runtime context bridge result:
  `cd backend && .venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py`
  exited `0` with `11 passed in 0.05s`.
- Event API compatibility result:
  `cd backend && .venv/bin/python -m pytest app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py`
  exited `0` with `12 passed in 0.18s`.
- API smoke result:
  `cd backend && .venv/bin/python -m pytest app/tests/test_runtime_step.py`
  exited `0` with `16 passed in 0.28s`; this covers FastAPI TestClient
  checks for health, runtime step, `/world/events`, and `/world/event-steps`.
- E2E result: initial sandboxed `make test-e2e` failed to bind
  `127.0.0.1:8000` with `operation not permitted`. The approved rerun outside
  the sandbox exited `0` with `6 passed (6.4s)`.
- Release claim check: current evidence supports the v0.3 release claim as
  loader/runtime-bridge infrastructure while preserving the existing v0.3
  final / closeout complete status.
- Compatibility review: backend, loader, bridge, runtime, Event.refs, API
  smoke, and browser dashboard E2E validation all passed in the current
  campaign.
- Concrete demo-world regression check: no runtime, schema, API, frontend,
  backend test, fixture, migration, or external repository files were edited
  in this execution package.

## P1/P2/P3 Findings

- P1: none identified.
- P2: none identified.
- P3: none identified. The first E2E attempt required sandbox escalation for
  local port binding, but the approved rerun passed and does not indicate a
  product or repository defect.

## Blockers

None. The transient sandbox local-port denial was resolved by rerunning the
same `make test-e2e` command with approval.

## Final Assessment

Current value: `passed`.
