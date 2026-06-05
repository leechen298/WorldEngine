# World Rule Parameter Evolution

状态：planned / checker-extension-required

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目标

证明 generated world parameters 会跨 ticks 根据 WorldEngine rules 演化，而不是 static
counters 或 hard-coded mock behavior。

## 必要操作

- 从带 public parameters 和 rules 的 LLM-backed world 开始。
- 推进多个 ticks。
- 捕获 parameter diffs、events、snapshots 和 replay references。
- 验证 material parameter changes 有 public rule references 或 public legality
  explanations。

## 禁止操作

- static counter-only tick progression 被报告为 rule evolution。
- 没有 rule evidence 的 direct mutation 被报告为 valid。
- Validation Client 计算 authoritative world parameter changes。
- hidden implementation details 被导出为 proof。

## 必要 Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `rule-parameter-summary.json`
- `world-lifecycle-summary.json`
- `diff-replay-summary.json`
- event artifacts
- snapshot artifacts
- `redaction-scan.json`
- `scorecard-summary.json` 或 checker output

## PASS 来源

PASS 需要 checker 或 scorecard output 证明跨 ticks 存在 rule-linked parameter changes。

## FAIL Taxonomy

- `world_evolution`
- `world_creation`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

允许 public rule ids、public explanations、parameter names、values 和 diffs。禁止
private provider traces、raw prompt text、raw response text 和 hidden reasoning。
