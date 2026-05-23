# Agent Smoke Protocol

Status: current protocol

Chinese mirror: `README.zh.md`.

Agent smoke is an agent-assisted exploratory check. Codex may operate the app
through UI or CLI, observe UI state, record the raw operation log, and write
transcript notes, but Codex may not issue the final PASS verdict.

## Scenario Index

| Scenario | Status | Instructions |
|---|---|---|
| `dashboard-basic-runtime` | `executable` | `docs/testing/agent-smoke/scenarios/dashboard-basic-runtime.md` |
| `dashboard-params-flow` | `validator-supported-no-live-run-recorded` | `docs/testing/agent-smoke/scenarios/dashboard-params-flow.md` |
| `dashboard-invalid-param` | `validator-supported-no-live-run-recorded` | `docs/testing/agent-smoke/scenarios/dashboard-invalid-param.md` |

`dashboard-params-flow` and `dashboard-invalid-param` now have deterministic
validator support, but this repository has no live smoke result for them yet.
Do not report either scenario as passed without a fresh validated result
directory.

## Required Evidence

Each run writes local artifacts under:

```text
test-results/agent-smoke/<timestamp>/
```

The latest raw evidence that should be committed and pushed is mirrored under:

```text
test-results/agent-smoke/latest/
```

Do not commit every timestamped run. Commit only the latest reviewed raw run
when it is needed for audit, plus durable summaries under `docs/testing/results/`.

Required files:

- `result.json`
- `transcript.md`
- `console.log`
- `api-summary.json`
- `operation-log.jsonl`
- at least one file under `screenshots/`

`trace.zip` is optional for this first protocol.

## Operation Log Rule

`operation-log.jsonl` is the raw record of what the agent did. Each non-empty
line must be a JSON object.

Allowed operation types:

- `ui`: requires `seq`, `target`, and `action`.
- `cli`: requires `seq`, `command`, and `exit_code`.

Direct API operations are not valid agent operations. If deterministic evidence
needs API state, it belongs in `api-summary.json` as checker/CLI output, not as
a Codex operation entry.

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

Codex may summarize only the validation command result, evidence path, and raw
operation log path.
