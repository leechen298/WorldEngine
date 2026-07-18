# Test Plan

Chinese mirror: `test-plan.zh.md`.

Run from `frontend` unless noted.

## Frontend Unit Tests

```bash
pnpm test
```

Required coverage:

- API client methods call public session endpoints and unwrap API payloads.
- dashboard renders session shell and existing status panels.
- create session action displays session id/status/generation summary.
- run action displays runtime/event/snapshot evidence and refreshes runtime
  and timeline state.
- pause/resume actions call session-scoped APIs.
- existing RuntimeControls one-step behavior remains covered or is explicitly
  adapted.

## Frontend Build

```bash
pnpm build
```

## Targeted E2E

```bash
pnpm test:e2e -- dashboard.spec.ts
```

Run this only if the backend and frontend dev server can be started in the
current environment. If unavailable, record BLOCKED/PARTIAL honestly with
command output.

## Backend Compatibility

Run from `backend`:

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py
```

Do not run live provider, Validation Client, or external checker suites for
this package.
