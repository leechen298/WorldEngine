# Autonomous Scenario: autonomous-dashboard-timeline-investigation

Status: contract-only-do-not-execute

## Goal

Advance runtime several times and find details for the most recent tick event
through the dashboard timeline.

## Allowed Operations

- CLI operations to start services.
- UI operations to step runtime, navigate the timeline, and inspect event
  details.
- CLI operations to run a documented checker after one exists.

## Forbidden Operations

- Direct API calls recorded as Agent operations.
- Codex self-defined PASS.
- Code changes.
- Test scenario changes.
- Validator or checker changes during the run.

## Required Artifacts

- operation log.
- transcript.
- screenshots.
- console log or explicit empty-console note.
- scorecard result after a checker exists.

## Scorecard Items

- Step runtime multiple times through UI.
- Find the latest timeline tick.
- Expand or inspect event details through UI.
- Record event type, tick id, and visible evidence.
- Operation log contains no forbidden operation.
- Checker returns PASS.

## PASS Source

Future autonomous scorecard checker. This scenario has no executable PASS
source today.

## Unverified Items

- Timeline detail selectors are incomplete.
- Autonomous scorecard schema is not implemented.
- Autonomous checker is not implemented.
