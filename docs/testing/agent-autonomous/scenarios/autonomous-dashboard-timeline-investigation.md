# Autonomous Scenario: autonomous-dashboard-timeline-investigation

Status: saved-result-checker-supported

## Goal

Advance runtime several times and find details for the most recent tick event
through the dashboard timeline.

## Allowed Operations

- CLI operations to start services.
- UI operations to step runtime, navigate the timeline, and inspect event
  details.
- CLI operations to run the documented saved-result checker.

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
- scorecard result.

## Scorecard Items

- Step runtime multiple times through UI.
- Find the latest timeline tick.
- Expand or inspect event details through UI.
- Record event type, tick id, and visible evidence.
- Operation log contains no forbidden operation.
- Checker returns PASS.

## PASS Source

Saved-result autonomous scorecard checker:
`make validate-agent-autonomous-result RESULT_DIR=<result-dir>`.

This is not a broad autonomous runner verdict; it validates recorded evidence.

## Unverified Items

- Timeline detail selectors are incomplete.
- A broad autonomous runner is not implemented.
- The scenario has no PASS unless a concrete result directory validates.
