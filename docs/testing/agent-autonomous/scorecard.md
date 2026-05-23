# Agent Autonomous Scorecard

Status: contract-only-do-not-execute

## Required Fields

Every future Codex/test-runner autonomous result must include:

- `scenario`
- `goal`
- `mode`
- `allowed_operations`
- `forbidden_operations`
- `required_artifacts`
- `score_items`
- `verdict_source`
- `unverified_items`

## PASS Requirements

A future autonomous run can pass only when:

- the scorecard checker returns pass.
- no forbidden operations are present.
- required artifacts exist.
- no unverified P1 item remains.
- Codex did not self-report PASS.
- `verdict_source` is a deterministic checker or scorecard source accepted by
  the scenario contract.

## Operation Boundary

Allowed operation records may include UI and CLI operations. Direct API calls
must not be recorded as Codex/test-runner Agent operations.

Checker-generated API evidence may exist in dedicated checker artifacts, but it
must be separate from the Agent operation log.

## Current State

No executable autonomous scorecard checker exists in v0.1. All autonomous
scenarios remain contract-only until a later package defines and verifies the
checker.
