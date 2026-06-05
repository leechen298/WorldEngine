# Provider Live Smoke DeepSeek

Status: planned / checker-extension-required

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Goal

Prove WorldEngine can perform a minimal live DeepSeek provider call through
WorldEngine-owned configuration and return only redacted public evidence.

## Required Operations

- Start WorldEngine with DeepSeek environment variables configured by the
  WorldEngine environment.
- Read public provider readiness from WorldEngine.
- Trigger the smallest WorldEngine-owned provider live smoke call.
- Save redacted provider call evidence.
- Run the documented checker or scorecard once support exists.

## Forbidden Operations

- Validation Client calls DeepSeek directly.
- Agent reads, prints, stores, or forwards provider API keys.
- `/manifest` readiness is treated as live-call proof.
- Raw prompt, raw response, raw request, authorization header, or provider
  trace is stored in operation logs or evidence.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `provider-live-summary.json`
- `redaction-scan.json`
- `scorecard-summary.json` or checker output

## PASS Source

PASS requires checker or scorecard output confirming:

- WorldEngine attempted the live provider call.
- DeepSeek call succeeded.
- Evidence contains only provider class, redacted/public model label,
  success/failure, latency, approximate token statistics, and public failure
  category when applicable.
- Redaction scan passed.

## FAIL Taxonomy

- `provider`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

Evidence must not include API keys, authorization headers, raw prompts, raw
provider requests, raw provider responses, provider traces, account ids, private
paths, hidden context, or private evaluator data.
