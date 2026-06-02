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

- `result.json`
- `operation-log.jsonl`
- `transcript.md`
- `console.log` or explicit empty-console note referenced by `result.json`
- `scorecard-summary.json`
- `screenshots/`

## Scorecard Items

- Modify params through UI.
- Find params update evidence.
- Trigger `Step` through UI.
- Find counter increment event evidence.
- Operation log contains no forbidden operation.
- Saved-result checker validates the protocol, required UI targets, score_items
  with evidence, artifacts, and unresolved P1 boundary.
- Params-application semantics remain recorded scorecard claims unless a future
  scenario-specific checker verifies them independently.

## PASS Source

Saved-result autonomous scorecard checker:
`make validate-agent-autonomous-result RESULT_DIR=<result-dir>`.

This is not a broad autonomous runner verdict; it validates recorded evidence.
The current checker verifies referenced artifact paths are loadable; strict
basename enforcement for the protocol filenames above is a future hardening
item unless implemented in the checker.

## Unverified Items

- A broad autonomous runner is not implemented.
- The scenario has no PASS unless a concrete result directory validates.
