# E2E Scenario: dashboard-timeline-navigation

Status: implemented

## Current Implementation State

Timeline pagination controls and expanded row detail content now expose stable
selectors suitable for robust E2E assertions.

This scenario is implemented as Playwright E2E coverage in
`frontend/e2e/dashboard.spec.ts`.

## Purpose

Verify that the timeline remains usable after multiple runtime steps: page size
changes work, pagination state is correct, and event details can be inspected.

## Preconditions

- Backend and frontend can start through the Playwright web server config.
- Dashboard is reachable.
- The test can generate enough events through repeated UI steps.
- Stable selectors exist for timeline rows and expanded event detail content.

## Steps

1. Open the dashboard.
2. Click `Step` multiple times to generate events.
3. Change timeline page size.
4. Navigate to the next page when available.
5. Navigate back to the previous page.
6. Expand or inspect a recent tick row.
7. Read event type, source, and payload/detail evidence.

## Assertions

The implementation asserts:

- Timeline shows multiple tick records.
- Page-size changes are applied through `timeline-page-size`.
- Previous and next controls enable or disable correctly.
- Expanded details show event type, source, and payload/detail evidence.
- The scenario generates enough runtime events inside the test and does not
  depend on previous test state.

## PASS Source

Playwright assertion.

## Remaining Prerequisites

Stable selectors exist:

- `timeline-page-size`
- `timeline-prev-page`
- `timeline-next-page`
- `timeline-row`
- `timeline-row-expand`
- `timeline-event-type`
- `timeline-event-payload`
- `timeline-event-source`

Remaining blockers: none for current v0.1 E2E coverage.
