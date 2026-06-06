# LLM-backed World Creation

状态：saved-result-checker-supported / live evidence not run

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目标

证明基础 user premise 可以通过 WorldEngine 生成 public、system-digestible、
LLM-backed world state。

## 必要操作

- 通过 Validation Client 或其他 public external surface 输入基础 world premise。
- 通过 WorldEngine 创建世界。
- 捕获 public initial state、locations、entities、Agents、items、environment state、
  parameters、rule definitions、boundary conditions 和 visualization payload。
- 将结果与当前 deterministic generic world response 对比。

## 禁止操作

- Validation Client 生成或改写 world content。
- deterministic fallback 被标记为 LLM-backed。
- raw prompt 或 raw provider response 被导出。
- user premise 被直接复制成 final state，而没有 WorldEngine generated structures。
- concrete validation world seed data 被存入 WorldEngine repository。

## 必要 Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `world-creation-summary.json`
- `world-rule-summary.json`
- `initial-snapshot.json` 或等价 public snapshot artifact
- `redaction-scan.json`
- `scorecard-summary.json` 或 checker output

## PASS 来源

PASS 需要 checker 或 scorecard output 证明 generated world：

- premise-specific。
- 可被 WorldEngine system-digest。
- redacted。
- 不是 deterministic generic response。
- 当 LLM-backed lifecycle 在范围内时，有 provider-backed generation evidence。

## FAIL Taxonomy

- `world_creation`
- `provider`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

只保存 public generated state 和 public rule summaries。不得保存 raw prompts、raw
provider responses、private traces、hidden generation internals、private evaluator data
或 concrete external world seed data。
