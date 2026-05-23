# E2E Scenario: dashboard-invalid-param

Status: implemented

## Current Implementation State

Implemented in `frontend/e2e/dashboard.spec.ts` as:

```text
dashboard-invalid-param shows an error and leaves params unchanged
```

## Purpose

Verify that an invalid world param update made through the dashboard UI is
rejected and does not pollute world params.

## Preconditions

- Backend and frontend can start through the Playwright web server config.
- Dashboard is reachable.
- `system.secret` is rejected by the current params validator.

## Steps

1. Record current world params through deterministic test-script evidence.
2. Open the dashboard.
3. Set path to `system.secret`.
4. Set value to `blocked`.
5. Click `Apply`.
6. Observe the UI error.
7. Record world params again through deterministic test-script evidence.

## Assertions

- UI displays a params validation error.
- Params after the invalid apply equal params before the invalid apply.

## PASS Source

Playwright assertion.

## Selector / Checker Prerequisites

Current selectors are sufficient:

- `world-params-path-input`
- `world-params-value-input`
- `world-params-apply-button`
- `world-params-error`
