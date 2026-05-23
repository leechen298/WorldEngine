# Autonomous Scenario: autonomous-dashboard-invalid-param

Status: contract-only-do-not-execute

## Goal

Attempt an invalid param update through the dashboard and confirm the system
rejects it without changing world params.

## Allowed Operations

- CLI operations to start services.
- UI operations to inspect the dashboard and submit the invalid param.
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

- Enter invalid param path through UI.
- Find UI error evidence.
- Prove params are unchanged through checker evidence.
- Operation log contains no forbidden operation.
- Checker returns PASS.

## PASS Source

Future autonomous scorecard checker. This scenario has no executable PASS
source today.

## Unverified Items

- Autonomous scorecard schema is not implemented.
- Autonomous checker is not implemented.
- Agent smoke validator support for this scenario is also pending.
