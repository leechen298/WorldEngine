# E2E Scenario: dashboard-agent-autotune

Status: scenario-contract-only / not-implemented

## Current Implementation State

The dashboard exposes `LLM Auto-Tune`, and the backend has a
`ParamsAgent + MockLLMProvider` path through
`/world/agent/params/propose-and-apply`.

This scenario is not implemented as E2E coverage today. Stable selectors now
exist, but it must not be reported as passed until a later package implements
the Playwright test, adds deterministic assertions, and runs it.

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
4. Wait for success or deterministic error feedback.
5. If successful, inspect patch details.
6. Verify params or event evidence reflects the result.

## Assertions

Future implementation should assert:

- Auto-tune action produces explicit success or failure feedback.
- Successful result displays `Applied ... patch(es)`.
- Patch details are inspectable.
- Params JSON or deterministic `/world/params` test-script evidence reflects
  the applied patch.
- Timeline or event evidence includes params-agent related evidence when
  available.

## PASS Source

Playwright assertion after implementation.

## Remaining Prerequisites

Stable selectors exist:

- `world-agent-goal-input`
- `world-agent-autotune-button`
- `world-agent-success`
- `world-agent-patches`
- `world-agent-error`

Remaining blockers:

- Playwright scenario implementation.
- Deterministic success/error assertions and checker expectations.
