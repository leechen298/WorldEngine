# Scenario: dashboard-invalid-param

Status: validator-supported-no-live-run-recorded

## Purpose

Verify that a Codex/test-runner agent can attempt an invalid param update
through the dashboard UI and prove that the system rejects it without polluting
world params.

## Current Executability

This scenario now has validator support for deterministic checker evidence.
No live smoke run has been recorded for it yet.

Do not report this scenario as passed without a fresh result directory that
passes `make validate-agent-smoke-result RESULT_DIR=<run-dir>`.

## Allowed Operations

- CLI operations to start services and run the validator.
- UI operations to open the dashboard, enter an invalid param, click `Apply`,
  and inspect UI feedback.

## Forbidden Operations

- Do not record direct API calls in `operation-log.jsonl`.
- Do not directly `curl /world/params`.
- Do not directly POST `/world/params/apply`.
- Do not use Codex natural-language observation as PASS.
- Do not write `verdict_source: "agent"`.

## Steps

1. Start backend and frontend services through CLI.
2. Open the dashboard through UI.
3. Fill path `system.secret`.
4. Fill value `blocked`.
5. Click `Apply`.
6. Observe validation error through UI.
7. Write required artifacts.
8. Run the Agent smoke validator.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `transcript.md`
- `console.log`
- `api-summary.json`
- at least one screenshot under `screenshots/`

## Required Deterministic Check

`api-summary.json` must include checker evidence such as:

```json
{
  "scenario": "dashboard-invalid-param",
  "invalid_path": "system.secret",
  "ui_error_seen": true,
  "params_unchanged": true
}
```

This API evidence is checker evidence only. It is not an Agent operation.

## PASS Source

PASS must come from:

```bash
make validate-agent-smoke-result RESULT_DIR=<run-dir>
```

with `verdict_source: "deterministic_checker"`.

## Live Evidence Status

No live Agent smoke result has been recorded for this scenario in 0.1.7.
