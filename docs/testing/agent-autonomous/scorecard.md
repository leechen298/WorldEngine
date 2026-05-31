# Agent Autonomous Scorecard

Status: minimal saved-result checker available

## Result Required Fields

Every Codex/test-runner autonomous `result.json` validated by the minimal
saved-result checker must include:

- `scenario`
- `goal`
- `mode`
- `status`
- `verdict_source`
- `score_items`
- `required_artifacts`
- `artifacts`
- `operation_log`
- `unverified_items`
- `failures`

`allowed_operations` and `forbidden_operations` belong in the scenario
documentation. The checker enforces their result-level effects through
`operation-log.jsonl`, including the rule that Agent operations may be only
`ui` or `cli`.

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

`make validate-agent-autonomous-result RESULT_DIR=<dir>` validates saved
autonomous scorecard result artifacts. `make validate-agent-autonomous-fixtures`
validates positive and negative checker fixtures. This is minimal checker
support, not a broad autonomous runner or full-suite live execution.
