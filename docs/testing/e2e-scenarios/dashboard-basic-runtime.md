# E2E Scenario: dashboard-basic-runtime

Status: implemented

## Current Implementation State

Implemented in `frontend/e2e/dashboard.spec.ts` as:

```text
dashboard-basic-runtime advances one tick and records timeline evidence
```

## Purpose

Verify that the dashboard loads, backend health is visible, the runtime can
advance through the UI, and timeline evidence exists after the step.

## Preconditions

- Backend and frontend can start through the Playwright web server config.
- Dashboard is reachable.
- The initial tick is not assumed to be `0`.

## Steps

1. Read the current runtime tick through deterministic test-script evidence.
2. Open the dashboard.
3. Verify backend health is `ok`.
4. Verify the displayed tick matches the current runtime tick.
5. Click the dashboard `Step` button.
6. Wait until the runtime tick increments by one.
7. Verify timeline evidence appears for the new tick.

## Assertions

- Health status is `ok`.
- `after_tick === before_tick + 1`.
- Timeline contains `tick.advanced` or a `module.*` event.

## PASS Source

Playwright assertion.

## Failure-Path Assertions

- Backend health not `ok` is a setup/server failure, not runtime PASS.
- Tick not increasing by one after the UI `Step` click is a runtime/UI sync
  failure.
- Tick increases but timeline lacks `tick.advanced` or `module.*` evidence is a
  UI/event evidence failure.

## Artifact Expectations

- HTML report: `test-results/e2e/html-report/index.html`
- Playwright artifacts: `test-results/e2e/artifacts/`
- Failure screenshot and trace are retained under the artifact directory when
  Playwright keeps them.

## Selector / Checker Prerequisites

Current selectors are sufficient:

- `backend-health-status`
- `runtime-tick-id`
- `runtime-step-button`
- `timeline-panel`
