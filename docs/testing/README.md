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
`docs/testing/agent-smoke/scenarios/`. `dashboard-basic-runtime` is executable.
`dashboard-params-flow` and `dashboard-invalid-param` are
`live-smoke-recorded`. The current raw `latest/` directory points to
`dashboard-invalid-param`; 0.1.8 params-flow evidence is preserved through
`docs/testing/results/2026-05-24-v0.1.8-params-flow-live-smoke.md` and commit
`c6da552`.

## E2E Scenario Contracts

Current-code E2E scenario contracts live under
`docs/testing/e2e-scenarios/`.

Implemented current E2E coverage:

- `dashboard-basic-runtime`
- `dashboard-params-flow`
- `dashboard-invalid-param`
- `dashboard-agent-autotune`
- `dashboard-timeline-navigation`
- `dashboard-archive-summary`

E2E PASS still requires a current-session Playwright assertion result.

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
