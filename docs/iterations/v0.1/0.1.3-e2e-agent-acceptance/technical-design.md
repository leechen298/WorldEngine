# Technical Design

## Playwright E2E

Playwright lives in `frontend/` because the browser tests target the dashboard.

`frontend/playwright.config.ts`:

- starts the FastAPI backend on `127.0.0.1:8000`.
- starts the Vite dashboard on `127.0.0.1:5173`.
- runs with one worker because the backend runtime state is process-local and
  in-memory.
- writes E2E artifacts under `test-results/e2e/`.
- keeps screenshots and traces on failure.

First-time browser setup:

```bash
cd frontend
pnpm exec playwright install chromium
```

## Stable Selectors

Dashboard E2E selectors use `data-test` attributes only. The initial selector
set is:

- `backend-health-status`
- `runtime-tick-id`
- `runtime-step-button`
- `timeline-panel`
- `world-panel`
- `world-params-json`
- `world-params-path-input`
- `world-params-type-select`
- `world-params-value-input`
- `world-params-apply-button`
- `world-params-error`

Selectors are test observability only. They must not change user-visible UI or
runtime behavior.

## E2E Scenarios

`dashboard-basic-runtime` reads the current tick through API, steps through the
UI, then proves `afterTick === beforeTick + 1` through API and timeline evidence.

`dashboard-params-flow` sets `counter.increment = 2` through the UI, proves the
change through `/world/params`, then steps and proves a `module.counter` event
with `payload.increment === 2`.

`dashboard-invalid-param` records `beforeParams`, sends an invalid UI patch,
checks the UI error, then deep-compares `afterParams` against `beforeParams`.

## Agent Smoke

Agent smoke is not a normal CI test. It is agent-assisted exploratory smoke with
deterministic evidence validation.

Required local artifact layout:

```text
test-results/agent-smoke/<timestamp>/
├── result.json
├── transcript.md
├── console.log
├── api-summary.json
└── screenshots/
```

`result.json` must name `verdict_source: "deterministic_checker"`. If the
verdict source is `agent`, validation fails.

## Validator

`tools/testing/validate_agent_smoke_result.py` reads a result directory and
checks:

- required files exist.
- command records exist.
- assertions exist and include evidence.
- `verdict_source` is deterministic.
- `dashboard-basic-runtime` API summary proves tick increment.

`make validate-agent-smoke-fixtures` verifies both the valid fixture and an
invalid `verdict_source = agent` fixture. The Make target exits `0` only when
the invalid fixture fails as expected.
