# Test Plan

Chinese mirror: `test-plan.zh.md`.

Run from `backend` unless noted.

## Focused Tests

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py
```

Required coverage:

- session run advances bounded ticks and reports public run evidence.
- session run rejects unbounded or over-guard requests.
- pause blocks session run until resume.
- session snapshot list returns bounded public snapshots.
- unknown sessions return existing 404 envelope.
- manifest exposes implemented session runtime/snapshot surfaces.
- existing `/runtime/*` tests still pass.
- redaction markers are absent from public session run and snapshot payloads.

## Expanded Focused Regression

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_llm_worldview_generation_api.py
```

This keeps 0.10.3 worldview-to-session behavior compatible while session
runtime wrappers are added.

## Non-Run Tests

Do not run live provider checks, browser E2E, Validation Client checks, or
external checker suites for this package unless a later contract explicitly
authorizes them.
