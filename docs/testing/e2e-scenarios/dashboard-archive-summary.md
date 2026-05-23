# E2E Scenario: dashboard-archive-summary

Status: scenario-contract-only / not-implemented

## Current Implementation State

The backend has archive snapshot and summary behavior, and the dashboard
MemoryPanel displays the latest archive summary. Stable MemoryPanel selectors
now exist for E2E assertions.

This scenario is not implemented as E2E coverage today.

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

Future implementation should assert:

- Latest summary becomes visible.
- Summary includes a tick range or equivalent interval evidence.
- Summary stats include total event count.
- Summary stats include event type counts such as `tick.advanced`.

## PASS Source

Playwright assertion after implementation.

## Remaining Prerequisites

Stable selectors exist:

- `memory-panel`
- `memory-summary-text`
- `memory-summary-stats`
- `memory-summary-empty`

Remaining blockers:

- Playwright scenario implementation.
- E2E test environment must define low archive intervals without changing
  runtime logic.
