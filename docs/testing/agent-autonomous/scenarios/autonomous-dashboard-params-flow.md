# Autonomous Scenario: autonomous-dashboard-params-flow

Status: contract-only-do-not-execute

## Goal

Change `counter.increment` to `2` through the dashboard and confirm the change
affects a later world event.

## Allowed Operations

- CLI operations to start services.
- UI operations to inspect and change dashboard params.
- CLI operations to run a documented checker after one exists.

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
- scorecard result after a checker exists.

## Scorecard Items

- Modify params through UI.
- Find params update evidence.
- Trigger `Step` through UI.
- Find counter increment event evidence.
- Operation log contains no forbidden operation.
- Checker returns PASS.

## PASS Source

Future autonomous scorecard checker. This scenario has no executable PASS
source today.

## Unverified Items

- Autonomous scorecard schema is not implemented.
- Autonomous checker is not implemented.
- Agent smoke validator support for this scenario is also pending.
