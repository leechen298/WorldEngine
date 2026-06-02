# Full Autonomous Scenario: product-exploration-regression

Status: contract-only / full-runner-required
Scenario ID: AUTO-FULL-V07-006

## User Goal

As an ordinary test user, perform one bounded autonomous exploration that covers
runtime, params, Agent Loop API, generation preview/readiness, and v0.7
readiness evidence, then classify every selected layer with raw artifacts.

## Autonomous Operation Boundary

Allowed operations:

- Dashboard UI operations.
- Public API calls documented by WorldEngine contracts.
- Public checker CLI commands.
- Artifact creation for UI, API, CLI, transcript, and scorecard evidence.

Forbidden operations:

- hidden reset APIs, private fixtures, private oracle outputs, database
  inspection, external validation world internals, or private projection app
  state.
- changing code, docs, tests, scenarios, checkers, fixtures, or schemas during
  the run.
- suppressing failed, blocked, skipped, or out-of-scope classifications.
- reporting PASS from Codex narration alone.

## Preconditions

- Backend and frontend services are reachable.
- Checker commands are available.
- The runner can store full result artifacts.
- The run target, branch, commit, service URLs, and environment notes are
  recorded before the first action.

## Required Coverage

The autonomous agent may choose exact order and retries, but the final result
must classify these layers:

- dashboard runtime step and timeline evidence.
- dashboard params valid and invalid flows.
- public Agent Loop API accepted, rejected, and schema-error flows.
- generation preview/readiness valid and invalid diagnostics.
- v0.7 readiness manifest/report/projection checker surfaces.
- external suite and projection application readiness as passed, failed,
  blocked, skipped, or out of scope.

## Expected Assertions

- Every selected capability has at least one user-observable or public API/CLI
  evidence item.
- Every failed or blocked layer has a concrete reason.
- Raw artifacts are retained and linked by result summary.
- Known P1/P2 blockers are preserved in the classification.
- The run does not use private APIs or private validation details.

## Failure Or Blocked Conditions

- Any required layer is omitted without classification.
- A P1/P2 blocker is hidden or downgraded without evidence.
- Raw artifacts are missing.
- The agent reports product PASS without checker or command evidence.
- The agent uses private interfaces to produce evidence.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-log.jsonl`
- `api-summary.json`
- CLI logs for checker commands
- `transcript.md`
- `console.log` or explicit empty-console note
- `scorecard-summary.json`
- screenshots for UI paths
- final result summary with passed/failed/blocked/skipped/out-of-scope
  classification.

## PASS Source

Future full autonomous suite checker plus per-scenario scorecard results.
Current v0.7 does not have this full runner; this scenario is a future gate and
must be reported as `blocked`, `skipped`, or `out_of_scope` until implemented
and executed.
