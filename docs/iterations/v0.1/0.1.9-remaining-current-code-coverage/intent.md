# Intent

## Problem

After 0.1.8, v0.1 has a strong current-code test chain, but three current-code
coverage gaps remain:

- `dashboard-agent-autotune` has existing UI/backend behavior and selectors,
  but no Playwright E2E implementation.
- `dashboard-timeline-navigation` has existing UI controls and expanded-detail
  selectors, but no Playwright E2E implementation.
- `dashboard-invalid-param` is validator-supported, but no live Agent smoke
  run has been recorded.

The other known gaps in the test map are not v0.1 current-code coverage gaps:
full autonomous scorecards, persistence/restart behavior, WorldSpec/WorldCell,
and agent memory or pseudo-self belong to later roadmap work.

## Goal

After this package is implemented and reviewed:

- `dashboard-agent-autotune` is implemented as deterministic Playwright E2E
  coverage.
- `dashboard-timeline-navigation` is implemented as deterministic Playwright
  E2E coverage.
- `dashboard-invalid-param` has one real live Agent smoke run recorded and
  validated with helper-generated `api-summary.json`.
- The test map clearly separates closed v0.1 current-code coverage from
  v0.2+ or autonomous future work.

## Non-goals

- Do not add API curl smoke.
- Do not run full Codex/test-runner autonomous scenarios.
- Do not add or change autonomous scorecards or verdict sources.
- Do not modify backend runtime behavior or API contracts.
- Do not modify `backend/worldengine/`.
- Do not implement persistence/restart tests.
- Do not implement WorldSpec, WorldCell, recursive world, world generation,
  agent memory, or pseudo-self tests.
- Do not start v0.2 in this package.

## Why Now

0.1.6 mapped current-code scenarios, 0.1.7 made the validator and selectors
ready, and 0.1.8 recorded one live params smoke plus archive E2E. The remaining
three items are small, bounded, and tied to current v0.1 behavior. Closing
them now keeps v0.1 from carrying avoidable current-code test debt into v0.2.

## North Star Alignment

This package improves evidence for the current dashboard projection of runtime,
params-agent, timeline, and validation behavior. It does not change the engine
direction, add village-specific runtime logic, or pull recursive world and
agent-continuity work forward from later milestones.
