# LLM-backed Full Lifecycle Autonomous Validation

状态：saved-result-checker-supported / live evidence not run

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目标

证明完整 LLM-backed lifecycle：provider live smoke、LLM-backed world creation、
rule-driven evolution、rule-compliant events、persistent Agent autonomy evidence、
evidence export、checker PASS 和第二 Agent 只读复核。

## 必要操作

- 运行 `provider-live-smoke-deepseek`，或消费同 session 中已接受的 provider live smoke
  prerequisite。
- 从基础 user premise 创建 LLM-backed world。
- 推进 ticks，直到可见 rule-driven parameter evolution、events、snapshots 和 diffs。
- 提交至少一条 external environmental direction，并验证 legality。
- 观察 multi-round Agent autonomy evidence。
- 从 Validation Client 导出 evidence bundle。
- 对 result directory 运行 WorldEngine checker 或 scorecard。
- 运行第二 Agent 只读 evidence review。

## 禁止操作

- UI smoke 被当作 full lifecycle PASS。
- provider readiness 被当作 live call proof。
- deterministic generic world output 被当作 LLM-backed。
- direct API calls 被记录为 Agent operation-log operations。
- client scripts Agent actions。
- user direction 被直接写成 final state。
- evidence 中出现 raw prompt、raw response、API key、private memory、raw thought 或
  hidden context。

## 必要 Artifacts

- `result.json`
- `operation-log.jsonl`
- `transcript.md`
- `console.log`
- screenshots
- `api-summary.json`
- `provider-live-summary.json`
- `world-creation-summary.json`
- `world-rule-summary.json`
- `rule-parameter-summary.json`
- `event-legality-summary.json`
- `agent-autonomy-summary.json`
- `diff-replay-summary.json`
- `world-lifecycle-summary.json`
- `validation-client-evidence-bundle.json`
- `scorecard-summary.json`
- `second-agent-review.md`

## PASS 来源

PASS 需要 WorldEngine checker 或 scorecard 对所有 critical items 输出 PASS，并且第二 Agent
只读复核无 blocking P1 或 P2。

## FAIL Taxonomy

- `provider`
- `world_creation`
- `world_evolution`
- `event_legality`
- `agent_autonomy`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

所有 component scenario redaction requirements 都适用。任何 API key、authorization
header、raw prompt、raw response、provider trace、private memory、private goal、raw
thought、raw chain-of-thought 或 hidden context 泄露，都立即 FAIL。
