# Goal Runner

英文镜像：`GOAL_RUNNER.md`。

Status：reviewed / 0.9.9 implementation complete / verification passed

## Goal Entry

本 campaign 覆盖的自然语言 goal 包括：

```text
完成 v0.9
开发 v0.9
编写 v0.9 文档
生成 v0.9 文档
启动 WorldEngine v0.9：LLM-backed World Lifecycle Foundation
```

当前 route 记录在 `CURRENT_STATE.md`。Implementation authorization 默认关闭。

## Route Selection

1. 读取 `CURRENT_STATE.md`。
2. 读取 `README.md`、`CAMPAIGN_PLAN.md` 和 `v0.9-plan.md`。
3. 如果 route 指向 `*-documentation-package-needed` child，必须先创建或确认该 child
   package document set，之后才可 implementation 或 evidence execution。
4. 对任何 child package，按以下顺序读取：
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
5. Active child package review 记录 `implementation_authorized: yes` 之前，不得实现。

`v0.9-plan.md` 不是 execution-approved child contract。里面的 planned package sections
必须先转换成 concrete package docs，之后才可 code、schema、API、checker、fixture、
frontend、evidence 或 provider work。

## Documentation Stage Gate

Documentation-only work 可创建或更新 v0.9 iteration documents、parent package plans、
roadmap specs、review evidence、handoff baselines、validation boundaries、planned
package specs 和 Chinese mirrors。

除非 reviewed active child package 明确授权对应文件类型，否则 documentation-only work
不得修改 runtime、schema、API、frontend、backend tests、checker implementation、fixtures、
migrations、generated results、external repositories、Validation Client code 或
`backend/worldengine/` implementation files。

## Implementation Authorization Rule

Implementation authorization 默认关闭。

对 mixed 或 code children：

1. `contract.md`、`technical-design.md`、`test-plan.md` 和 `plan.md` 必须经过 review。
2. documentation/contract evaluator 必须报告无 P0/P1 且无 blocking P2。
3. `review.md` 必须记录 `implementation_authorized: yes`。
4. Implementation 必须保持在 active child package contract 内。

如果 implementation 暴露设计缺口，必须停止 implementation，更新相关文档，并且在 updated
contract、design、test plan 或 execution plan reviewed 后才可继续。

## Provider And Redaction Rules

- Live provider calls 需要 active child authorization。
- Provider keys 必须由 WorldEngine 环境变量管理。
- Validation Client 不得存储、展示、转发或调用 provider keys。
- Evidence 不得包含 API keys、authorization headers、raw prompts、raw provider
  requests、raw provider responses、raw provider traces、private Agent memory、raw
  thought、raw chain-of-thought、hidden context 或 private evaluator data。
- Public summaries 可以包含 provider class、model label、success/failure、latency、
  approximate token buckets 和 failure categories。

## Runtime Control Rules

会推进世界的 v0.9 implementation children 必须使用 bounded run controls。Evidence 或
provider-backed tests 不允许 infinite 或 unbounded default execution。

除非更早 package 明确拥有更小前置条件，否则 required control semantics 属于 `0.9.5`：

- run one tick。
- run N ticks。
- run for a world-time duration。
- pause。
- resume。
- continue for N ticks 或 duration。
- maximum tick、duration、provider-call 和 cost guards。

## User Direction Rules

Natural-language user direction 是 world-level guidance，不是 direct mutation。

允许的 direction effects：

- environment trends。
- external pressure。
- event candidate bias。
- probability shifts。
- rule constraints。
- future evaluation hints。

禁止的 direction effects：

- direct Agent private memory mutation。
- direct Agent goal mutation。
- direct final fact assignment。
- direct death、injury、relationship 或 inventory outcomes。
- 绕过 world rules、probability、causality、location、time 或 state。

## Agent Continuity And Consolidation Rules

v0.9 的 Agent continuity 可以参考 brain-inspired design，但不得声称 consciousness 或完整
human neuroscience。

允许的 public evidence：

- perception summaries。
- working 或 short-term memory summaries。
- long-term memory summary references。
- personality summaries。
- skill summaries。
- intent、no-intent、wait、rest 或 sleep states。
- action 和 event-reaction summaries。
- 可以跨多个 ticks 的 consolidation records。

禁止的 Agent evidence 或 behavior：

- raw thought 或 raw chain-of-thought。
- private memory payloads。
- hidden context。
- private goals。
- automatic per-tick personality mutation。
- automatic per-tick long-term memory mutation。
- automatic per-tick skill drift。
- client-scripted action represented as Agent autonomy。

Memory、personality 和 skill updates 应通过 explicit sleep/rest/low-activity consolidation
phases 沉淀，前提是 active child package 拥有该 behavior。不得假定它们每 tick 都更新。

## Narrative Projection And Diagnostic Dialogue Rules

WorldEngine 可以定义 external narrative projection 和 out-of-world player-to-Agent diagnostic
conversation 作为 inspection surfaces。

这些 surfaces 默认在 canonical world state 之外：

- narrative projection 必须读取 events、snapshots 和 public Agent summaries，不得修改
  canonical world state。
- diagnostic conversation 可以帮助 user 或 validator 检查 Agent，但默认不是 in-world dialogue。
- 除非未来 reviewed bridge 明确授权，diagnostic conversation 不得写入 world timeline 或 Agent memory。
- evidence 必须明确 projection provenance 和 redaction status。

## Evidence And Reporting Rules

- Historical v0.8 evidence 只能作为 handoff evidence。
- 没有 current-session checker 或 scorecard evidence 时，不得声明 provider live smoke、
  world creation、evolution、event legality、Agent autonomy、checker support、Validation
  Client evidence export 或 full LLM-backed lifecycle passed。
- 不得把 UI smoke 当成完整 WorldEngine validation PASS。
- 在 active package `review.md` 记录 exact commands、exit status、pass counts、skipped
  checks、blockers、artifact paths 和 rationale。
- 用 testing taxonomy 分类 FAIL/BLOCKED：`provider`、`world_creation`、
  `world_evolution`、`event_legality`、`agent_autonomy`、`agent_consolidation`、
  `narrative_projection`、`diagnostic_dialogue`、`redaction`、`client_evidence` 和
  `checker_gap`。

## Stop Conditions

出现以下情况必须停止并记录 blocker：

- active package authorization 前实现代码。
- active package authorization 前运行 live provider calls。
- 暴露 secrets、raw prompts、raw responses 或 private Agent internals。
- 让用户 direction 直接施加 final facts。
- 把 personality、long-term memory 或 skill updates 建模成 automatic per-tick mutation。
- 默认把 external diagnostic conversation 当成 in-world dialogue 或 Agent memory。
- 让 narrative projection 修改 canonical world state。
- 在 core repository 创建 concrete demo-world content。
- 用 deterministic generic output 声明 LLM-backed PASS。
- 没有 checker、scorecard 或 required second-Agent review 就声明 LLM-backed PASS。
- 从只定义 handoff contracts 的 WorldEngine package 修改 Validation Client code。
