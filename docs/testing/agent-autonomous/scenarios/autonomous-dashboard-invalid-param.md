# Autonomous Scenario: autonomous-dashboard-invalid-param

Status: saved-result-checker-supported

## Goal

Attempt an invalid param update through the dashboard and confirm the system
rejects it without changing world params.

## Allowed Operations

- CLI operations to start services.
- UI operations to inspect the dashboard and submit the invalid param.
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

- Enter invalid param path through UI.
- Find UI error evidence.
- Prove params are unchanged through checker evidence.
- Operation log contains no forbidden operation.
- Saved-result checker validates the protocol, required UI targets, score_items
  with evidence, artifacts, and unresolved P1 boundary.
- Invalid-param no-mutation semantics remain recorded scorecard claims unless a
  future scenario-specific checker verifies them independently.

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
