# Test Plan

## Red Tests Before Implementation

Run these before adding implementation support and record the expected
failures in `review.md`:

```bash
cd frontend && pnpm exec playwright test e2e/agent-loop.spec.ts
```

Expected before file creation: Playwright reports no matching test file or the
file is missing.

```bash
cd backend && .venv/bin/python -m pytest ../tools/testing/test_validate_agent_smoke_result.py -q
```

After adding the new checker test but before checker implementation, expected:
the new `dashboard-agent-autotune` fixture/helper/checker test fails because
the scenario is unsupported.

## Focused Verification

After implementation, run:

```bash
cd frontend && pnpm exec playwright test e2e/agent-loop.spec.ts
```

```bash
cd frontend && pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-agent-autotune"
```

```bash
cd backend && .venv/bin/python -m pytest ../tools/testing/test_validate_agent_smoke_result.py -q
```

```bash
make validate-agent-smoke-fixtures
```

## Broad Verification

Run the existing E2E suite:

```bash
make test-e2e
```

Run backend/API v0.4 compatibility checks:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
```

## Live Agent Smoke Run

Execute a live `dashboard-agent-autotune` Agent smoke run and validate it:

```bash
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/<timestamp>
```

The run directory must contain:

- `result.json`
- `operation-log.jsonl`
- `transcript.md`
- `console.log`
- `api-summary.json`
- `screenshots/`

## Acceptance Criteria

- New Agent Loop API Playwright spec passes.
- Strengthened dashboard Auto-Tune compatibility E2E passes and verifies the
  existing `agent.params` event source.
- Existing Playwright dashboard E2E suite passes or any failure is recorded
  with exact failing spec and artifact path.
- Agent smoke checker tests pass.
- `make validate-agent-smoke-fixtures` passes and keeps the invalid fixture
  failing as expected.
- Live `dashboard-agent-autotune` Agent smoke result validates with
  `verdict_source: "deterministic_checker"`.
- No direct API operation is recorded as an Agent operation.
- No runtime, schema, API implementation, frontend product UI, migration,
  external repository, or legacy `backend/worldengine/` file changes.

## Not Run

Broader scorecard-based autonomous validation is not part of this package. If
requested, record it as not run because the broader autonomous checker remains
future scope.
