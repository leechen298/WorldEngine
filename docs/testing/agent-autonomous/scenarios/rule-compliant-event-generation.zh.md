# Rule-compliant Event Generation

状态：saved-result-checker-supported / live evidence not run

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目标

证明 random events 和 user-directed external guidance 受 world rules 约束，不能直接强制
非法最终结果。

## 必要操作

- 运行带 public event legality rules 的世界。
- 捕获至少一个 WorldEngine-generated 或 selected random event。
- 提交至少一条 natural-language external direction，它描述 risk、pressure 或
  environmental tendency，而不是 final outcome。
- 验证 WorldEngine 根据 public rules 接受、拒绝、延迟、转换或解析该 direction。
- 捕获 legality summaries 以及 resulting diffs 或 snapshots。

## 禁止操作

- user direction 不经 rule adjudication 直接杀死、治愈、传送、改写或强制 Agent final state。
- Validation Client 创建 authoritative events。
- impossible events 没有 legality status 却通过。
- raw prompt 或 raw provider response 被用作 public proof。

## 必要 Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `event-legality-summary.json`
- event artifacts
- snapshot artifacts
- diff artifacts
- `redaction-scan.json`
- `scorecard-summary.json` 或 checker output

## PASS 来源

PASS 需要 checker 或 scorecard output 证明 external direction 只影响 external events 或
environment，并且 WorldEngine 通过 public rules 决定 final outcomes。

## FAIL Taxonomy

- `event_legality`
- `world_evolution`
- `agent_autonomy`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

允许 public legality summaries、event ids、rule references 和 public outcomes。禁止
private Agent memory、private goals、hidden context、raw thought、raw prompt 和 raw response。
