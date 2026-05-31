# Autonomous Scenario: autonomous-dashboard-basic-runtime

Status: saved-result-checker-supported

## Goal

Confirm that the dashboard can advance the runtime once and find timeline
evidence for the new tick.

## Allowed Operations

- CLI operations to start services.
- UI operations to inspect the dashboard and click controls.
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

- Find the current runtime tick.
- Click `Step` through UI.
- Find timeline evidence for the advanced tick.
- Save a screenshot.
- Operation log contains no forbidden operation.
- Checker returns PASS.

## PASS Source

Saved-result autonomous scorecard checker:
`make validate-agent-autonomous-result RESULT_DIR=<result-dir>`.

This is not a broad autonomous runner verdict; it validates recorded evidence.

## Unverified Items

- A broad autonomous runner is not implemented.
- The scenario has no PASS unless a concrete result directory validates.
