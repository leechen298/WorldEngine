# Scenario: dashboard-agent-autotune

Status: executable

## Purpose

Verify that a Codex/test-runner agent can operate the dashboard Auto-Tune flow
through UI and CLI only, while a deterministic checker proves the params-agent
patch result.

This scenario covers the existing dashboard params-agent route. It is not the
v0.4 Agent Loop API and must not expect `source="agent.loop"`.

## Result Directory

New runs write artifacts under `test-results/agent-smoke/<timestamp>/`. The
validator command's `<run-dir>` must point to that directory or to an explicitly
recorded `test-results/agent-smoke/latest/` alias for the same run.

## Allowed Operations

- CLI operations to start services, collect baseline/checker evidence, and run
  the validator.
- UI operations to open the dashboard, set `counter.increment` to `2`, enter
  an Auto-Tune goal, click Auto-Tune, and inspect success/patch/params
  evidence.

## Forbidden Operations

- Do not record direct API calls in `operation-log.jsonl`.
- Do not directly POST `/world/agent/params/propose-and-apply` as an Agent
  operation.
- Do not directly POST `/world/agent/loop/step`.
- Do not use Codex natural-language observation as PASS.
- Do not write `verdict_source: "agent"`.
- Do not call this full scorecard-based autonomous validation.

## Steps

1. Start backend and frontend services through CLI.
2. Open the dashboard through UI.
3. Set `counter.increment` to `2` through the params form.
4. Confirm the dashboard params JSON shows the baseline value.
5. Collect baseline checker evidence with
   `tools/testing/agent_smoke_evidence.py baseline`.
6. Enter an Auto-Tune goal through `world-agent-goal-input`.
7. Click `world-agent-autotune-button`.
8. Observe `world-agent-success`.
9. Observe `world-agent-patches`.
10. Observe the updated params JSON.
11. Collect checker evidence with
    `tools/testing/agent_smoke_evidence.py collect --scenario dashboard-agent-autotune`.
12. Write required artifacts.
13. Run the Agent smoke validator.

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
  "scenario": "dashboard-agent-autotune",
  "baseline_counter_increment": 2,
  "observed_counter_increment": 1,
  "counter_changed": true,
  "patches_count": 1,
  "patch_paths": ["counter.increment"],
  "params_applied_event_seen": true,
  "params_applied_event_source": "agent.params",
  "ui_success_seen": true,
  "ui_patches_seen": true
}
```

This API evidence is checker evidence only. It is not an Agent operation.

## PASS Source

PASS must come from:

```bash
make validate-agent-smoke-result RESULT_DIR=<run-dir>
```

with `verdict_source: "deterministic_checker"`.
