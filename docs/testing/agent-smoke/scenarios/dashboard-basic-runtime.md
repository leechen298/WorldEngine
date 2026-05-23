# Scenario: dashboard-basic-runtime

Status: executable

## Purpose

Verify that an agent can operate the dashboard while the final verdict remains
deterministic and evidence-based.

## Steps

1. Start the backend and frontend dev services.
2. Open the dashboard.
3. Record the current health and tick evidence through UI or CLI-observable
   output.
4. Record `before_tick` from the dashboard UI.
5. Click the dashboard `Step` button.
6. Record `after_tick` from the dashboard UI.
7. Save `operation-log.jsonl` with every UI and CLI operation.
8. Save at least one screenshot.
9. Save a transcript of actions and observations.
10. Save console output or an explicit empty-console note.
11. Save `api-summary.json`.
12. Save `result.json` with `verdict_source: "deterministic_checker"`.
13. Run `make validate-agent-smoke-result RESULT_DIR=<run-dir>`.

## Required Deterministic Check

`api-summary.json` must prove:

- `health_status` is `ok`.
- `after_tick === before_tick + 1`.

`operation-log.jsonl` must prove the agent operated through UI or CLI. Direct
API operation entries are invalid; API state may appear only as deterministic
checker evidence in `api-summary.json`.

## PASS Source

```bash
make validate-agent-smoke-result RESULT_DIR=<run-dir>
```

## Invalid Verdicts

The result is invalid if Codex writes `verdict_source: "agent"` or claims PASS
without the validation script exiting `0`.
