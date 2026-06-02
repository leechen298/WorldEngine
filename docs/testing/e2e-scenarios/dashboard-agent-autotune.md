# E2E Scenario: dashboard-agent-autotune

Status: implemented

## Current Implementation State

The dashboard exposes `LLM Auto-Tune`, and the backend has a
`ParamsAgent + MockLLMProvider` path through
`/world/agent/params/propose-and-apply`.

This scenario is implemented as Playwright E2E coverage in
`frontend/e2e/dashboard.spec.ts`.

## Purpose

Verify that the dashboard can trigger the current params-agent auto-tune path
and display deterministic patch evidence.

## Preconditions

- Backend and frontend can start through the Playwright web server config.
- Dashboard is reachable.
- Stable selectors exist for the auto-tune input, button, result, and patch
  details.

## Steps

1. Open the dashboard.
2. Enter a goal such as `keep counter stable`.
3. Click `LLM Auto-Tune`.
4. Wait for deterministic success feedback.
5. Inspect patch details from `world-agent-patches`.
6. Verify the observed params reflect the actual patch value.

## Assertions

The implementation asserts:

- Auto-tune action produces explicit success feedback.
- Successful result displays `Applied ... patch(es)`.
- Patch details include a `counter.increment` `set` patch.
- The test reads the actual patch value and verifies `/world/params` and
  dashboard params JSON reflect that value.
- The test checks a new `params.applied` event with `source="agent.params"` and
  a patch path for `counter.increment`; it does not currently assert `reason`.
- The test does not hardcode the previous params-flow value as the Auto-Tune
  expected result.

## PASS Source

Playwright assertion.

## Failure-Path Assertions

- UI success without params/API evidence is a failure.
- A `params.applied` event missing `source="agent.params"` or a
  `counter.increment` patch path is a failure.
- A test or result claiming `reason` was asserted is an overclaim unless the
  spec is extended first.

## Artifact Expectations

- HTML report: `test-results/e2e/html-report/index.html`
- Playwright artifacts: `test-results/e2e/artifacts/`
- Failure screenshot and trace are retained under the artifact directory when
  Playwright keeps them.

## Remaining Prerequisites

Stable selectors exist:

- `world-agent-goal-input`
- `world-agent-autotune-button`
- `world-agent-success`
- `world-agent-patches`
- `world-agent-error`

Remaining blockers: none for current dashboard E2E coverage.
