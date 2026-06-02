# Autonomous Scenario: autonomous-dashboard-agent-autotune

Status: saved-result-checker-supported

## Goal

Try `LLM Auto-Tune` through the dashboard and confirm whether it successfully
walks the params-agent path or fails with explicit evidence.

## Allowed Operations

- CLI operations to start services.
- UI operations to find the Auto-Tune control, enter a goal, and trigger it.
- CLI operations to run the documented saved-result checker.

## Forbidden Operations

- Direct API calls recorded as Agent operations.
- Direct POST to `/world/agent/params/propose-and-apply` as an Agent
  operation.
- Reporting a failed Auto-Tune attempt as PASS.
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

- Find Auto-Tune UI.
- Enter goal or intentionally use the default goal.
- Trigger Auto-Tune through UI.
- Find explicit success or error feedback.
- If successful, record patch evidence.
- If failed, record error evidence and do not report PASS.
- Operation log contains no forbidden operation.
- Saved-result checker validates the protocol, required UI targets, score_items
  with evidence, artifacts, and unresolved P1 boundary.
- Auto-Tune success/error and patch semantics remain recorded scorecard claims
  unless a future scenario-specific checker verifies them independently.

## PASS Source

Saved-result autonomous scorecard checker:
`make validate-agent-autonomous-result RESULT_DIR=<result-dir>`.

This is not a broad autonomous runner verdict; it validates recorded evidence.
The current checker verifies referenced artifact paths are loadable; strict
basename enforcement for the protocol filenames above is a future hardening
item unless implemented in the checker.

## Unverified Items

- Auto-Tune stable selectors exist, but autonomous selector-driven execution
  has not been implemented.
- The scenario has no PASS unless a concrete result directory validates.
