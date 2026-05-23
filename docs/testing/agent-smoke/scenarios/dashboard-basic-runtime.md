# Scenario: dashboard-basic-runtime

## Purpose

Verify that an agent can operate the dashboard while the final verdict remains
deterministic and evidence-based.

## Steps

1. Start the backend and frontend dev services.
2. Open the dashboard.
3. Record `GET /health`.
4. Record `GET /runtime/state` as `before_tick`.
5. Click the dashboard `Step` button.
6. Record `GET /runtime/state` as `after_tick`.
7. Save at least one screenshot.
8. Save a transcript of actions and observations.
9. Save console output or an explicit empty-console note.
10. Save `api-summary.json`.
11. Save `result.json` with `verdict_source: "deterministic_checker"`.
12. Run `make validate-agent-smoke-result RESULT_DIR=<run-dir>`.

## Required Deterministic Check

`api-summary.json` must prove:

- `health_status` is `ok`.
- `after_tick === before_tick + 1`.

## Invalid Verdicts

The result is invalid if Codex writes `verdict_source: "agent"` or claims PASS
without the validation script exiting `0`.
