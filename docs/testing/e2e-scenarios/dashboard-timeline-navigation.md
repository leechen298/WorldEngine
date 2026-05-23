# E2E Scenario: dashboard-timeline-navigation

Status: scenario-contract-only / partially-blocked-by-selector

## Current Implementation State

Timeline pagination controls currently expose selectors for page size,
previous page, and next page. Expanded row detail content is visible in the UI,
but does not yet have stable selectors suitable for robust E2E assertions.

This scenario is not implemented as E2E coverage today.

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

Future implementation should assert:

- Timeline shows multiple tick records.
- Page-size changes alter the displayed set or pagination behavior.
- Previous and next controls enable or disable correctly.
- Expanded details show event type, source, and payload/detail evidence.

## PASS Source

Playwright assertion after implementation.

## Selector / Checker Prerequisites

Existing selectors:

- `timeline-page-size`
- `timeline-prev-page`
- `timeline-next-page`

Missing selectors:

- `timeline-row`
- `timeline-row-expand`
- `timeline-event-type`
- `timeline-event-payload`
- `timeline-event-source`
