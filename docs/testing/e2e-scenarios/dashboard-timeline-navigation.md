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
- The current spec does not read `/world/events` or prove the expanded UI row is
  identical to a specific API event.

## PASS Source

Playwright assertion.

## Failure-Path Assertions

- Page-size selection not taking effect is a pagination failure.
- Prev/next enabled-state mismatch is a pagination state failure.
- Expanded row missing type, source, or non-empty payload/detail evidence is a
  detail visibility failure.
- API/UI event identity mismatch remains untested by this scenario and must not
  be reported as PASS evidence unless the spec is extended.

## Artifact Expectations

- HTML report: `test-results/e2e/html-report/index.html`
- Playwright artifacts: `test-results/e2e/artifacts/`
- Failure screenshot and trace are retained under the artifact directory when
  Playwright keeps them.

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

Remaining blockers: none for current dashboard E2E coverage; API row identity
matching is a planned gap unless added to the spec.
