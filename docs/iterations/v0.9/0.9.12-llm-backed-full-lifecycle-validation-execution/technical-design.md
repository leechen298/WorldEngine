# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Execution Flow

The package uses the runbook sequence from
`docs/testing/agent-autonomous/llm-backed-suite-execution.md`:

1. preflight and budget check.
2. start required local services.
3. run provider live smoke.
4. run LLM-backed world creation.
5. run rule parameter evolution.
6. run rule-compliant event generation.
7. run Agent persistent autonomy evidence.
8. run full lifecycle.
9. export result directory.
10. run checker/scorecard.
11. run second-Agent review.
12. write durable result summary.

## Result Directories

Live artifacts should be written under:

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

Durable summaries should be written under:

```text
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.md
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.zh.md
```

## Result Classification

- `pass`: all critical score items pass, checker validates the result, and
  second-Agent review reports no blocking P1/P2.
- `fail`: execution runs but evidence proves a product, rule, redaction,
  client-evidence, checker, or autonomy violation.
- `blocked`: execution cannot produce valid evidence because of provider,
  environment, quota, service, or missing prerequisite constraints.
- `not_run`: execution is intentionally skipped and the reason is recorded.

## Evidence Integrity

The operating agent must not repair artifacts after the run to force PASS.
If artifacts are malformed or missing, classify the result or rerun the same
scenario from the beginning when allowed by budget and stop rules.

## Second-Agent Review

Second-Agent review must be read-only. It should inspect the result directory,
checker output, scorecard, redaction scan, operation log, API summary, evidence
bundle, and PASS claims. Any blocking P1/P2 blocks full lifecycle PASS.
