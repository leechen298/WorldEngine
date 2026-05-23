# E2E Scenario Contracts

Status: current-code scenario contracts

This directory defines dashboard E2E scenario contracts for current v0.1
behavior. Implemented scenarios map to deterministic Playwright assertions.
Contract-only scenarios describe future E2E work and must not be reported as
passed until implemented and run.

## Verdict Source

E2E PASS comes from Playwright assertion. It does not come from Codex
observation or manual narration.

Playwright E2E may use API reads as deterministic test-script assertion
evidence. Those API reads are not Agent operations.

## Scenario Index

| Scenario | Status | Current State |
|---|---|---|
| `dashboard-basic-runtime` | `implemented` | Implemented in `frontend/e2e/dashboard.spec.ts`. |
| `dashboard-params-flow` | `implemented` | Implemented in `frontend/e2e/dashboard.spec.ts`. |
| `dashboard-invalid-param` | `implemented` | Implemented in `frontend/e2e/dashboard.spec.ts`. |
| `dashboard-agent-autotune` | `scenario-contract-only / not-implemented` | Current UI/backend capability and stable selectors exist; Playwright implementation and deterministic assertions are still missing. |
| `dashboard-timeline-navigation` | `scenario-contract-only / not-implemented` | Timeline controls and expanded-detail selectors exist; Playwright implementation is still missing. |
| `dashboard-archive-summary` | `scenario-contract-only / not-implemented` | MemoryPanel selectors exist; Playwright implementation and low archive interval test environment are still missing. |

## Execution Rule

Only `implemented` scenarios may be treated as runnable current E2E coverage.
All other scenario files are contracts for a later implementation package.
