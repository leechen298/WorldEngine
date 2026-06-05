# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Design Principle

The repair must be evidence-led. The implementation agent must first reproduce
or inspect the failure, then identify which layer is wrong. The fix must target
that layer without weakening the scenario's user-facing proof.

## Existing Scenario

The implemented E2E scenario:

```text
frontend/e2e/dashboard.spec.ts
dashboard-archive-summary creates and renders a newer archive summary
```

Expected flow:

1. record the latest summary before stepping.
2. open the dashboard and ensure MemoryPanel is visible.
3. step runtime four times.
4. wait for a newer summary through API.
5. assert tick range and event stats.
6. assert MemoryPanel renders the newer summary stats and text.

The scenario documentation lives at:

```text
docs/testing/e2e-scenarios/dashboard-archive-summary.md
```

## Diagnostic Matrix

| Bucket | Evidence to collect | Likely repair |
| --- | --- | --- |
| `archive_generation_gap` | no newer summary exists through API after enough steps | backend archive interval, event capture, or summary generation repair |
| `summary_api_visibility_gap` | summary exists internally but latest-summary API does not expose/order it | backend summary list/latest ordering or filtering repair |
| `memory_panel_refresh_gap` | API has newer summary but MemoryPanel renders old/empty state | frontend refresh or state update repair |
| `e2e_environment_gap` | Playwright server does not apply low summary/snapshot intervals | test server environment or setup repair |
| `e2e_wait_or_state_isolation_gap` | app behavior is correct but predicate compares the wrong baseline or races serial state | focused Playwright helper repair with assertion strength preserved |
| `other_blocked` | root cause requires broader archive redesign or unavailable dependency | stop and document blocker |

## Required Investigation Flow

1. Run the focused failing scenario.
2. Capture the latest summary before stepping.
3. Step runtime four times.
4. Query summaries and runtime state after stepping.
5. Compare:
   - `beforeSummary` identity and tick range.
   - latest API summary identity and tick range.
   - total events and `tick.advanced` count.
   - MemoryPanel rendered text and stats.
6. Record one root-cause bucket in `review.md`.

## Repair Strategy

Choose exactly one primary repair path unless evidence proves multiple layers
are broken:

### Backend Archive Path

Use only if the API does not produce a newer valid summary after expected
steps.

Possible work:

- ensure summary interval configuration is honored in the E2E environment.
- ensure runtime steps produce summary-eligible archived events.
- ensure summary tick ranges advance after new events.
- add or update focused backend tests for the repaired archive behavior.

### Frontend MemoryPanel Path

Use only if API evidence is correct but the UI does not render the newer
summary.

Possible work:

- refresh latest archive summary after runtime steps.
- update state handling so the latest summary replaces stale data.
- keep stable `data-testid` selectors unless a selector bug is the proven root
  cause.

### E2E Harness Path

Use only if backend and UI behavior are correct but the test predicate is
wrong, under-sized, or not isolated.

Possible work:

- make the baseline comparison use stable summary identity and tick coverage.
- poll the correct API endpoint.
- isolate serial state if a prior test creates a summary that confuses
  ordering.
- tune timeout only with evidence that application behavior is correct and the
  original timeout is insufficient.

## Claim Boundaries

This package may claim only:

- focused archive summary E2E repair.
- current `make test-e2e` clean pass if run and passed.
- latest basic full lifecycle saved-result checker still validates if run and
  passed.

This package may not claim:

- LLM-backed lifecycle capability.
- live provider capability.
- product readiness.
- external validation PASS.
- archive persistence or summary quality beyond the repaired scenario.
