# LLM-backed Lifecycle Scorecard

状态：saved-result-checker-supported / live evidence not run

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目的

本 scorecard 定义未来 checker 对 `llm-backed-full-lifecycle-autonomous` 必须评估的
critical items。它是文档合同，不是已实现 checker。

## Score Items

| Item | Critical | PASS 条件 | FAIL 条件 | Artifact source |
| --- | --- | --- | --- | --- |
| `provider_live_smoke` | yes | WorldEngine-owned live DeepSeek call 成功，并有 redacted evidence。 | 没有 live call、provider failure，或把 `/manifest` readiness 当 proof。 | `provider-live-summary.json` |
| `world_creation_llm_backed` | yes | World 是 premise-specific、system-digestible，且不是 deterministic generic output。 | Generic fallback、client-generated content 或 non-digestible output。 | `world-creation-summary.json` |
| `world_rules_generated` | yes | parameters、meanings、initial values、evolution rules、boundaries 和 event legality rules 存在。 | 缺 rules/parameters，或只有 flavor text。 | `world-rule-summary.json` |
| `parameter_evolution_rule_linked` | yes | Tick changes 能关联 public rules，并产生 diffs/snapshots。 | 只有 fixed counter、无 rule linkage、无 state evidence。 | `rule-parameter-summary.json`, `diff-replay-summary.json` |
| `event_legality_enforced` | yes | random 和 user-guided external events 由 world rules adjudicate。 | 用户方向直接强制 outcome，或 impossible event 没有 legality status 却通过。 | `event-legality-summary.json` |
| `agent_persistent_autonomy` | yes | multi-round public Agent evidence 展示 observation、memory summary、thought/reflection summary、intent/no-intent、action 和 reaction。 | 单个 `params.applied`、无 continuity，或 client-scripted action。 | `agent-autonomy-summary.json` |
| `diff_replay_available` | yes | events、diffs 和 snapshots 支持 replay 或 state inspection。 | 缺 snapshots、缺 diffs，或无 replay reference。 | `diff-replay-summary.json`, snapshots |
| `redaction_clean` | yes | Redaction scan 无 blocking leak。 | 出现 API key、auth header、raw prompt/response、provider trace、private memory/goal/thought、hidden context 或 oracle data。 | `redaction-scan.json` |
| `client_evidence_complete` | yes | operation log、API summary、screenshots、transcript 和 evidence bundle 存在。 | required artifact 缺失或 malformed。 | result directory |
| `second_agent_review_clean` | yes | 第二 Agent 只读复核没有 blocking P1/P2。 | 任一 blocking P1/P2 或 unsupported PASS claim。 | `second-agent-review.md` |

## Verdict Rule

`llm-backed-full-lifecycle-autonomous` 只有在每个 critical item 都是 `pass` 时才能 PASS。
任何 critical `fail`、`blocked` 或 `not_run` 都会阻断 PASS。

## Allowed Item Statuses

- `pass`
- `fail`
- `blocked`
- `not_run`
- `out_of_scope`

对 full lifecycle scenario，critical items 不应是 `out_of_scope`。如果 critical item 仍是
future scope，则该 full lifecycle scenario 还不能作为 PASS-capable 场景运行。
