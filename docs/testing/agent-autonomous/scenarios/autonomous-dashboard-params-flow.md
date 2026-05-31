# Autonomous Scenario: autonomous-dashboard-params-flow

Status: saved-result-checker-supported

## Goal

Change `counter.increment` to `2` through the dashboard and confirm the change
affects a later world event.

## Allowed Operations

- CLI operations to start services.
- UI operations to inspect and change dashboard params.
- CLI operations to run the documented saved-result checker.

## Forbidden Operations

- Direct API calls recorded as Agent operations.
- Direct POST to `/world/params/apply` as an Agent operation.
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

- Modify params through UI.
- Find params update evidence.
- Trigger `Step` through UI.
- Find counter increment event evidence.
- Operation log contains no forbidden operation.
- Checker returns PASS.

## PASS Source

Saved-result autonomous scorecard checker:
`make validate-agent-autonomous-result RESULT_DIR=<result-dir>`.

This is not a broad autonomous runner verdict; it validates recorded evidence.

## Unverified Items

- A broad autonomous runner is not implemented.
- The scenario has no PASS unless a concrete result directory validates.
