# Testing and Evidence

Status: testing evidence guide

This directory records testing standards and evidence for WorldEngine
iterations.

## Evidence Rules

- Do not claim tests passed unless the command was run in the current work
  session.
- Code packages must list exact commands and results in package `review.md`.
- Runtime, UI, E2E, or live smoke claims must include reviewable evidence.
- Docs-only packages may skip code tests, but must state the no-test rationale
  in `review.md`.

## Result Files

Use `docs/testing/results/` for durable evidence summaries when a package runs
broader verification or manual/runtime checks.

Suggested name format:

```text
YYYY-MM-DD-<version-package>-<slug>.md
```

Each result file should include:

- command or workflow.
- environment assumptions.
- output summary.
- failures or skipped checks.
- link back to the iteration package.

## Agent Smoke

Agent-assisted smoke tests must follow `docs/testing/agent-smoke/`. Codex or any
agent may execute and observe, but PASS/FAIL must come from deterministic
Playwright assertions or `tools/testing/validate_agent_smoke_result.py`.

Historical raw Agent smoke artifacts belong under ignored
`test-results/agent-smoke/<timestamp>/`. The latest reviewed raw record may be
committed under `test-results/agent-smoke/latest/` for audit. Durable summaries
belong under `docs/testing/results/`.

Current Agent smoke scenario contracts live under
`docs/testing/agent-smoke/scenarios/`. Only `dashboard-basic-runtime` is
currently executable. `dashboard-params-flow` and `dashboard-invalid-param` are
defined but not executable until the validator supports those scenarios.

## E2E Scenario Contracts

Current-code E2E scenario contracts live under
`docs/testing/e2e-scenarios/`.

Implemented current E2E coverage:

- `dashboard-basic-runtime`
- `dashboard-params-flow`
- `dashboard-invalid-param`

Contract-only E2E scenarios:

- `dashboard-agent-autotune`
- `dashboard-timeline-navigation`
- `dashboard-archive-summary`

Contract-only scenarios must not be reported as passed until implemented and
verified by Playwright assertion.

## Codex/Test-Runner Autonomous Contracts

Codex/test-runner autonomous test contracts live under
`docs/testing/agent-autonomous/`.

In that directory, "Agent" means a Codex/test-runner agent operating
WorldEngine as a tester. It does not mean a future WorldEngine in-world Agent.

All current autonomous scenarios are `contract-only-do-not-execute`. They
require a scorecard checker before any PASS/FAIL claim.

## Future Implementation Prerequisites

Selector, validator, checker, and test-environment prerequisites are recorded
in `docs/testing/test-implementation-prerequisites.md`.
