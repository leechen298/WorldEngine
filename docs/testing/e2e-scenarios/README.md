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
| `dashboard-archive-summary` | `implemented` | Implemented in `frontend/e2e/dashboard.spec.ts` with low archive intervals scoped to the Playwright backend web server. |
| `dashboard-agent-autotune` | `implemented` | Implemented in `frontend/e2e/dashboard.spec.ts` with deterministic params-agent patch assertions. |
| `dashboard-timeline-navigation` | `implemented` | Implemented in `frontend/e2e/dashboard.spec.ts` with generated events, pagination, and expanded-detail assertions. |
| `agent-loop-step` | `implemented` | Implemented in `frontend/e2e/agent-loop.spec.ts` with Playwright request assertions for the v0.4 Agent Loop API. |

## Execution Rule

Only `implemented` scenarios may be treated as runnable current E2E coverage.
All other scenario files are contracts for a later implementation package.
