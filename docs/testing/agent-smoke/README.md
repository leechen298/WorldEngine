# Agent Smoke Protocol

Status: current protocol

Agent smoke is an agent-assisted exploratory check. Codex may operate the app,
observe UI state, record commands, and write transcript notes, but Codex may not
issue the final PASS verdict.

## First Scenario

The first supported scenario is `dashboard-basic-runtime`.

Scenario instructions:

- `docs/testing/agent-smoke/scenarios/dashboard-basic-runtime.md`

## Required Evidence

Each run writes local artifacts under:

```text
test-results/agent-smoke/<timestamp>/
```

Required files:

- `result.json`
- `transcript.md`
- `console.log`
- `api-summary.json`
- at least one file under `screenshots/`

`trace.zip` is optional for this first protocol.

## Verdict Rule

`result.json` must contain:

```json
{
  "status": "pass",
  "verdict_source": "deterministic_checker"
}
```

If `verdict_source` is `agent`, the run is invalid even when Codex observed the
UI successfully.

Validate a run with:

```bash
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/<timestamp>
```

Codex may summarize only the validation command result and evidence path.
