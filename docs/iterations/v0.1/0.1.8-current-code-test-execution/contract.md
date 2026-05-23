# Contract

## Public Concepts

### Live Agent smoke run

A live Agent smoke run is a real execution record for one Agent smoke scenario.
Codex may operate the app through UI and CLI commands, but the PASS verdict
must come from deterministic project tooling.

For 0.1.8-A, the only live Agent smoke scenario is
`dashboard-params-flow`.

### Helper-generated API evidence

`api-summary.json` for live Agent smoke must be produced or verified by
`tools/testing/agent_smoke_evidence.py`. Codex must not manually author this
file.

The helper may read backend APIs internally to generate checker artifacts.
Those reads are not Agent operations and must not appear as direct API
operation records in `operation-log.jsonl`.

### Archive-summary E2E

`dashboard-archive-summary` is a Playwright E2E scenario that proves a backend
archive summary is generated after enough runtime steps and displayed through
the dashboard MemoryPanel.

Playwright may use API reads as deterministic test-script assertions. Those
API reads are E2E assertion evidence, not Agent operations.

## Compatibility Constraints

- Existing runtime behavior must stay compatible.
- Existing API response shapes must stay compatible.
- Existing dashboard user-visible behavior must stay compatible except for any
  test-only timing environment used by Playwright.
- Existing E2E scenarios must keep passing.
- Existing Agent smoke validator behavior from 0.1.7 must keep passing.
- Test environment interval overrides must be scoped to Playwright web-server
  execution only.

## Allowed Changes

0.1.8-A may:

- Create or update live Agent smoke evidence under
  `test-results/agent-smoke/latest/`.
- Record `dashboard-params-flow` raw evidence files:
  - `result.json`
  - `operation-log.jsonl`
  - `transcript.md`
  - `console.log`
  - helper-generated `api-summary.json`
  - at least one file under `screenshots/`
- Optionally retain helper input such as `api-baseline.json` in the run
  directory.
- Update Agent smoke docs and test maps to mark `dashboard-params-flow` as
  live-smoke-recorded only after validation passes.
- Update this package `review.md` with live execution evidence.

0.1.8-B may:

- Modify `frontend/playwright.config.ts` to set
  `WORLD_SUMMARY_INTERVAL_TICKS=2` and
  `WORLD_SNAPSHOT_INTERVAL_TICKS=2` for the Playwright backend web server
  only.
- Modify `frontend/e2e/dashboard.spec.ts` to implement
  `dashboard-archive-summary`.
- Update E2E scenario docs and test maps to mark `dashboard-archive-summary`
  as implemented only after `make test-e2e` passes.
- Update this package `review.md` with E2E implementation evidence.

## Forbidden Changes

- Do not run live `dashboard-invalid-param` in this package.
- Do not run Codex/test-runner autonomous scenarios.
- Do not add API curl smoke.
- Do not record direct API calls as Agent operations.
- Do not hand-author live `api-summary.json`.
- Do not change backend runtime behavior.
- Do not change backend API contracts.
- Do not modify `backend/worldengine/`.
- Do not implement `dashboard-agent-autotune` E2E.
- Do not implement `dashboard-timeline-navigation` E2E.
- Do not add WorldSpec, WorldCell, world generation, agent memory, or
  pseudo-self behavior.

## Live Agent Smoke Rules

0.1.8-A must run this sequence:

1. Start backend and frontend services for the dashboard.
2. Run `tools/testing/agent_smoke_evidence.py baseline` before scenario UI
   actions.
3. Operate the dashboard UI for `dashboard-params-flow`.
4. Run `tools/testing/agent_smoke_evidence.py collect --scenario
   dashboard-params-flow` after the UI actions.
5. Save raw evidence under `test-results/agent-smoke/latest/`.
6. Run `make validate-agent-smoke-result
   RESULT_DIR=test-results/agent-smoke/latest`.

The operation log must contain UI targets required by the 0.1.7 validator:

- `dashboard`
- `world-params-path-input`
- `world-params-type-select`
- `world-params-value-input`
- `world-params-apply-button`
- `runtime-step-button`

`result.json` must use:

```json
{
  "scenario": "dashboard-params-flow",
  "status": "pass",
  "verdict_source": "deterministic_checker"
}
```

## Archive E2E Rules

0.1.8-B must implement `dashboard-archive-summary` through Playwright
assertions.

The Playwright backend web server must run with:

```text
WORLD_SUMMARY_INTERVAL_TICKS=2
WORLD_SNAPSHOT_INTERVAL_TICKS=2
```

These values must not become backend defaults, shell profile state, or
non-test runtime behavior.

The E2E should use MemoryPanel selectors:

- `memory-panel`
- `memory-summary-text`
- `memory-summary-stats`
- `memory-summary-empty`

The E2E may use API reads inside the Playwright test to prove summary creation
and stats. It must not depend on Codex narration.

## Status Update Rules

After 0.1.8-A succeeds:

- `dashboard-params-flow` may be marked `live-smoke-recorded`.
- `dashboard-invalid-param` must remain validator-supported with no live run
  recorded.

After 0.1.8-B succeeds:

- `dashboard-archive-summary` may be marked `implemented`.

## North Star Check

This package records evidence for current runtime, params, events, and archive
summary behavior. It does not add village-specific runtime logic or shift the
engine away from the recursive world and agent-continuity north star.

## Out-of-Scope Follow-ups

- A later package may run live `dashboard-invalid-param`.
- A later package may run or refresh `dashboard-basic-runtime` live smoke.
- A later package may implement `dashboard-agent-autotune` E2E.
- A later package may implement `dashboard-timeline-navigation` E2E.
- A later package may add Codex/test-runner autonomous scorecards.
