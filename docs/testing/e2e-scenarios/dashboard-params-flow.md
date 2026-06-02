# E2E Scenario: dashboard-params-flow

Status: implemented

## Current Implementation State

Implemented in `frontend/e2e/dashboard.spec.ts` as:

```text
dashboard-params-flow applies counter increment and proves it through API and events
```

## Purpose

Verify that a valid world param update made through the dashboard UI is applied
and affects the next runtime event.

## Preconditions

- Backend and frontend can start through the Playwright web server config.
- Dashboard is reachable.
- `counter.increment` is accepted by the current params validator.

## Steps

1. Open the dashboard.
2. Set path to `counter.increment`.
3. Set value type to `number`.
4. Set value to `2`.
5. Click `Apply`.
6. Verify params JSON reflects the update.
7. Click `Step`.
8. Inspect deterministic event evidence for the new tick.

## Assertions

- Params JSON includes `counter.increment`.
- `/world/params` deterministic test-script evidence observes value `2`.
- The next `module.counter` event has payload `increment = 2`.

## PASS Source

Playwright assertion.

## Failure-Path Assertions

- UI JSON missing `counter.increment` after Apply is a dashboard params failure.
- `/world/params` evidence not matching the submitted value is an API/UI state
  mismatch.
- A runtime step without a matching `module.counter` increment payload is an
  event evidence failure.

## Artifact Expectations

- HTML report: `test-results/e2e/html-report/index.html`
- Playwright artifacts: `test-results/e2e/artifacts/`
- Failure screenshot and trace are retained under the artifact directory when
  Playwright keeps them.

## Selector / Checker Prerequisites

Current selectors are sufficient:

- `world-params-path-input`
- `world-params-type-select`
- `world-params-value-input`
- `world-params-apply-button`
- `world-params-json`
- `runtime-step-button`
