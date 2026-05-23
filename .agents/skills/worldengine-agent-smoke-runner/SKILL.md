---
name: worldengine-agent-smoke-runner
description: Use when running, preparing, validating, or reporting WorldEngine basic Agent smoke tests, `operation-log.jsonl`, `result.json`, or `make validate-agent-smoke-result`.
---

# WorldEngine Agent Smoke Runner

Use this skill only inside the WorldEngine repository.

Agent smoke is agent-assisted exploratory validation. Codex may operate and
observe, but the PASS verdict must come from the deterministic checker.

This is basic smoke only. Do not describe it as full Agent autonomous testing or
as coverage for broader autonomous scenario suites.

## Required Reading

Before running Agent smoke, read:

- `docs/testing/agent-smoke/README.md`
- `docs/testing/agent-smoke/scenarios/dashboard-basic-runtime.md`

Use `README.zh.md` when answering the user in Chinese.

## Hard Rules

- Operate through UI or CLI only.
- Record every UI and CLI operation in `operation-log.jsonl`.
- Do not record direct API calls as Agent operations.
- Do not write `verdict_source: "agent"`.
- Do not claim PASS unless the validation command exits `0`.
- If only fixtures were run, report only protocol/checker verification.

## Required Evidence

Each live run must produce:

```text
result.json
operation-log.jsonl
transcript.md
console.log
api-summary.json
screenshots/
```

`operation-log.jsonl` is newline-delimited JSON.

UI example:

```json
{"seq":1,"type":"ui","target":"runtime-step-button","action":"click","summary":"Clicked Step."}
```

CLI example:

```json
{"seq":2,"type":"cli","command":"make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest","exit_code":0}
```

Invalid operation:

```json
{"seq":3,"type":"api","method":"GET","target":"/runtime/state"}
```

API state may appear in `api-summary.json` as checker or CLI evidence, not as a
Codex operation entry.

## Workflow

1. Create a timestamped result directory under `test-results/agent-smoke/`.
2. Start services through CLI and log the command in `operation-log.jsonl`.
3. Open and operate the dashboard through UI; log every page action.
4. Save transcript, console log, screenshot, API summary, and `result.json`.
5. Validate the run:

```bash
make validate-agent-smoke-result RESULT_DIR=<run-dir>
```

6. If the user wants the latest raw record retained for review, mirror the
   validated run into:

```text
test-results/agent-smoke/latest/
```

## Reporting

The final summary may cite:

- validation command and exit status.
- evidence directory.
- `operation-log.jsonl` path.

The final summary must not replace the evidence or self-declare PASS.
