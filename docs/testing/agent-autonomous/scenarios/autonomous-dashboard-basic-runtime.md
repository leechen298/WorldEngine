# Autonomous Scenario: autonomous-dashboard-basic-runtime

Status: contract-only-do-not-execute

## Goal

Confirm that the dashboard can advance the runtime once and find timeline
evidence for the new tick.

## Allowed Operations

- CLI operations to start services.
- UI operations to inspect the dashboard and click controls.
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

- Find the current runtime tick.
- Click `Step` through UI.
- Find timeline evidence for the advanced tick.
- Save a screenshot.
- Operation log contains no forbidden operation.
- Checker returns PASS.

## PASS Source

Future autonomous scorecard checker. This scenario has no executable PASS
source today.

## Unverified Items

- Autonomous scorecard schema is not implemented.
- Autonomous checker is not implemented.
