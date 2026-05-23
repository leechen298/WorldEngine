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
