# 完整产品验证证据合同

状态：计划中的证据合同

英文镜像：`evidence-contract.md`。

## 目的

本文定义完整 WorldEngine 产品验证的最低 artifacts 和 redaction expectations。后续 checker
可以实现这些要求，但本文已经是文档层合同。

## 标准 Result Directory

推荐 result directory：

```text
test-results/product-validation/<timestamp>-complete-product-validation/
```

推荐文件：

```text
result.json
coverage-matrix.json
command-matrix.md
operation-log.jsonl
api-summary.json
console.log
transcript.md
redaction-scan.json
second-agent-review.md
artifacts/
raw/
```

如果包含 LLM-backed autonomous run，它的专用 result directory 应为：

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

## `result.json`

最低字段：

- `scenario`。
- `goal`。
- `mode`。
- `status`。
- `verdict`。
- `verdict_source`。
- `scope`。
- `started_at`。
- `completed_at`。
- `required_artifacts`。
- `artifacts`。
- `coverage_summary`。
- `failures`。
- `unresolved_findings`。
- `redaction`。

`verdict_source` 必须是以下之一：

- `command_matrix`。
- `deterministic_checker`。
- `scorecard_checker`。
- `saved_result_checker`。
- `second_agent_review`。
- `mixed_current_session_evidence`。

## `coverage-matrix.json`

`coverage-map.md` 中每个 CPV row 都必须出现。

最低 row 字段：

- `id`。
- `capability_area`。
- `scope_status`：`in_scope`、`out_of_scope` 或 `future_scope`。
- `validation_status`：`pass`、`fail`、`blocked`、`skipped` 或 `not_run`。
- `evidence_source`。
- `commands_or_checkers`。
- `artifacts`。
- `unresolved_findings`。
- `notes`。

## `command-matrix.md`

记录每个作为 evidence 的 command 或 checker：

- command。
- working directory。
- environment assumptions。
- start/end time 或 approximate duration。
- exit code。
- runner 报告的 pass/fail count。
- artifact path。
- 该 command 是否可以支持 PASS，还是只能作为 supporting evidence。

## `operation-log.jsonl`

Agent-operated flows 必须有 operation logs。

允许的 Agent operation types：

- `ui`。
- `cli`。

Direct HTTP/API calls 不得记录为 Agent operations。Public API evidence 应放在
`api-summary.json`、`api-log.jsonl` 或 checker artifacts 中。

每行应包含：

- `timestamp`。
- `actor`。
- `operation_type`。
- `target`。
- `summary`。
- `status`。
- `artifact_refs`。

禁止：

- API keys。
- authorization headers。
- 包含 prompts 或 secrets 的 raw request bodies。
- raw provider responses。
- private Agent memory、goals、thought 或 hidden context。

## `api-summary.json`

API summaries 可以包含：

- public endpoint。
- method。
- status code。
- public request category。
- public response category。
- latency。
- artifact reference。
- redaction flags。

不得包含：

- raw authorization headers。
- API key values。
- raw prompts。
- raw provider responses。
- private state payloads。

## Redaction Scan

`redaction-scan.json` 应记录：

- `passed`。
- `scanner_version` 或 `scanner_source`。
- checked artifact list。
- forbidden marker classes。
- findings by severity。
- 是否有 finding 阻断 PASS。

Forbidden marker classes 包括：

- provider credentials。
- authorization headers。
- raw prompts。
- raw provider requests 或 responses。
- provider traces。
- local private paths。
- hidden reset APIs。
- 暴露 private validation logic 的 UI selector leakage。
- private evaluator 或 oracle data。
- private Agent memory、goals、identity、relationships、self-state、raw thought、
  raw chain-of-thought 或 hidden context。
- core evidence 中的 concrete external validation world seed data。

## LLM-backed Artifact Summaries

当 LLM-backed lifecycle 在范围内时，evidence bundle 应包含：

- `provider-live-summary.json`。
- `world-creation-summary.json`。
- `world-rule-summary.json`。
- `rule-parameter-summary.json`。
- `event-legality-summary.json`。
- `agent-autonomy-summary.json`。
- `diff-replay-summary.json`。
- `scorecard-summary.json`。

这些文件由
`docs/testing/agent-autonomous/llm-backed-artifact-contract.md` 进一步定义。

## Durable Result Summary

运行后，在以下路径写 durable summary：

```text
docs/testing/results/YYYY-MM-DD-complete-product-validation.md
docs/testing/results/YYYY-MM-DD-complete-product-validation.zh.md
```

使用 `result-template.md` 和 `result-template.zh.md`。
