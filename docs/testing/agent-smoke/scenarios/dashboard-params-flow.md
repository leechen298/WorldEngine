# Scenario: dashboard-params-flow

Status: live-smoke-recorded

## Purpose

Verify that a Codex/test-runner agent can change `counter.increment` through
the dashboard UI and prove the next runtime event reflects the new increment,
while PASS remains deterministic.

## Current Executability

This scenario now has validator support for deterministic checker evidence.
One live smoke run is recorded under `test-results/agent-smoke/latest/`.

Do not report refreshed evidence for this scenario without a fresh result
directory that passes `make validate-agent-smoke-result RESULT_DIR=<run-dir>`.

## Result Directory

New runs write artifacts under `test-results/agent-smoke/<timestamp>/`. The
validator command's `<run-dir>` must point to that directory or to an explicitly
recorded `test-results/agent-smoke/latest/` alias for the same run.

## Allowed Operations

- CLI operations to start services and run the validator.
- UI operations to open the dashboard, edit params, click `Apply`, and click
  `Step`.

## Forbidden Operations

- Do not record direct API calls in `operation-log.jsonl`.
- Do not directly `curl /world/params`.
- Do not directly POST `/world/params/apply`.
- Do not use Codex natural-language observation as PASS.
- Do not write `verdict_source: "agent"`.

## Steps

1. Start backend and frontend services through CLI.
2. Open the dashboard through UI.
3. Fill path `counter.increment`.
4. Select type `number`.
5. Fill value `2`.
6. Click `Apply`.
7. Observe params JSON update through UI.
8. Click `Step`.
9. Observe timeline or event evidence through UI.
10. Write required artifacts.
11. Run the Agent smoke validator.

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
  "scenario": "dashboard-params-flow",
  "param_path": "counter.increment",
  "expected_value": 2,
  "observed_value": 2,
  "counter_event_increment": 2
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

0.1.8 recorded live Agent smoke evidence under
`test-results/agent-smoke/latest/`. The recorded run uses helper-generated
`api-summary.json` and passed
`make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest`.
