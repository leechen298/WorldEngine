# E2E Scenario: dashboard-archive-summary

Status: implemented

## Current Implementation State

The backend has archive snapshot and summary behavior, and the dashboard
MemoryPanel displays the latest archive summary. Stable MemoryPanel selectors
exist for E2E assertions.

This scenario is implemented in `frontend/e2e/dashboard.spec.ts`.

## Purpose

Verify that after enough runtime steps, an archive summary is generated and
displayed in the dashboard MemoryPanel.

## Preconditions

- Backend and frontend can start through the Playwright web server config.
- Dashboard is reachable.
- Test environment can lower summary/snapshot intervals, for example:
  `WORLD_SUMMARY_INTERVAL_TICKS=2` and
  `WORLD_SNAPSHOT_INTERVAL_TICKS=2`.
- Stable MemoryPanel selectors exist.

## Steps

1. Start E2E services with a low summary interval.
2. Open the dashboard.
3. Click `Step` enough times to trigger summary creation.
4. Wait for MemoryPanel to refresh.
5. Inspect the latest summary text and stats.

## Assertions

The implementation asserts:

- The latest summary before stepping is recorded.
- A newer summary is created after stepping.
- Latest summary becomes visible.
- Summary includes tick range evidence.
- Summary stats include total event count.
- Summary stats include event type counts such as `tick.advanced`.

## PASS Source

Playwright assertion through `make test-e2e`.

## Failure-Path Assertions

- No newer summary within the timeout is an archive interval/setup failure.
- Summary exists through API but MemoryPanel does not render it is a UI refresh
  failure.
- Summary stats lacking event counts or `tick.advanced` evidence is a summary
  evidence failure.

## Artifact Expectations

- HTML report: `test-results/e2e/html-report/index.html`
- Playwright artifacts: `test-results/e2e/artifacts/`
- Failure screenshot and trace are retained under the artifact directory when
  Playwright keeps them.

## Remaining Prerequisites

Stable selectors exist:

- `memory-panel`
- `memory-summary-text`
- `memory-summary-stats`
- `memory-summary-empty`

The Playwright backend web server defines low archive intervals for this E2E
environment without changing backend runtime defaults or API behavior.
