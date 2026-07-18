# v0.12 MVP Agent 连续性与验证自动化

英文版本：`README.md`。

状态：`closeout complete / PARTIAL`
类型：Codex `/goal` development campaign 和 iteration package root
implementation_authorized: no
evidence_execution_authorized: no

## 目标

v0.12 通过最小 living-Agent loop 和 WorldEngine-Validation-Client 外部验证路径，完成
MVP 闭环。

通俗地说：当世界已经能运行并按规则演化后，至少一个 Agent 应该能明显地观察、决定行动
或不行动、对事件反应、保留公开记忆摘要、跨 tick 休息或睡眠，并产出 external validation
client 可以导出、checker 可以分类的证据。

## 来自 v0.11 的交接

v0.11 预期交接：

- 带 public manifest/debug contract 的 runnable session。
- bounded runtime、events、diffs 和 snapshots。
- structured rules 和 parameters。
- natural-language direction 作为 world-level guidance。
- rule-compliant event generation 和 bounded-run fidelity evidence。

v0.12 假设世界已经能通过 public rules 变化。如果没有这个 handoff，v0.12 必须记录
blocker，而不是在 client 里脚本化 Agent 行为。

## 面向用户的检查模型

小说式 narrative projection 允许用户请求某个 session、tick range、worldline branch，或以
Agent 为焦点的 public history 的可读摘要。Projection 必须来自 public events、diffs、
snapshots、Agent summaries 和 provenance。

Diagnostic conversation 允许用户在世界外询问，例如“这个事件为什么发生”、“这个 Agent 公开看起来
记得什么”或“当前运行是否仍符合 worldview”。Transcript 只是 inspection evidence。它不是世界内
对话，不是玩家参与，不是 Agent memory，也不是引导未来事件的通道。任何希望影响世界的请求都必须走
direction queue。

## 范围

通过子包评审后，v0.12 允许做：

- public Agent state、needs、intent state、behavior 和 event reactions。
- 与 session runtime 集成的 minimal Agent loop。
- 合法的 no-intent、wait、rest 和 sleep states。
- short-term memory summaries 和 long-term memory/consolidation summaries。
- 可跨多个 tick 的 sleep/rest/low-activity consolidation。
- 小说式 narrative projection 和 out-of-world diagnostic conversation，作为 read-only inspection
  surfaces。
- WorldEngine-owned public evidence artifacts for Agent autonomy and validation。
- MVP full lifecycle 的 checker scenarios、scorecards、result schema 和只读外部评估者复核
  protocol。
- WorldEngine-to-Validation-Client handoff prompt 和 required artifact list。
- 明确区分世界内 Agent 与 Codex、OpenClaw 等外部验证 Agent 的 terminology。

v0.12 禁止做：

- 不声明真实意识。
- evidence 不得包含 raw thought、raw chain-of-thought、private memory、private goals、
  hidden context、secrets、raw prompts、raw provider responses 或 provider traces。
- 不把 client-scripted action 表述为 Agent autonomy。
- 不做 automatic per-tick personality、skill 或 long-term memory mutation。
- diagnostic conversation 默认不进入 world timeline 或 Agent memory。
- narrative projection 不得修改 canonical world state。
- out-of-world diagnostic conversation 默认不得被表述成世界内玩家对话。
- external validation agent 不得被表述成世界内 Agent。
- 不在本仓库加入 concrete game content 或 product-specific backend behavior。
- 不在本仓库实现 Validation Client。

## 计划子包

`v0.12-plan.md` 是详细 planned-package specification。planned packages 只是路线规格。

计划顺序：

1. `0.12.0-agent-validation-planning-and-v0.11-handoff`
2. `0.12.1-agent-public-state-and-runtime-loop`
3. `0.12.2-agent-memory-and-rest-consolidation-mvp`
4. `0.12.3-narrative-and-diagnostic-inspection-surfaces`
5. `0.12.4-validation-client-mvp-evidence-handoff`
6. `0.12.5-full-lifecycle-checker-and-autonomous-validation`
7. `0.12.6-mvp-release-candidate-and-closeout`

## 当前状态

当前 active child package：none。

当前 route：

```text
v0.12-closeout-complete-partial
```

Implementation authorization: no.

Evidence execution authorization: no.

Final classification：PARTIAL。WorldEngine-side Agent continuity、memory、inspection、handoff
和 deterministic checker evidence 已存在。Complete MVP PASS 仍被缺失的 current v0.12
external Validation Client export/result directory 阻断。

## 验证边界

v0.12 PASS 是第一次完整 MVP validation claim。它必须来自 checker、scorecard 和 read-only
review evidence，不能来自 UI smoke 或人的主观感觉。

必需 MVP lifecycle：

```text
client discovery -> create world -> run bounded ticks -> rule-linked events/diffs -> Agent observe/intent/action-or-rest/memory -> evidence export -> checker/scorecard/review
```

在这条 lifecycle 中，“Agent”指世界内 Agent。操作客户端并 review evidence 的外部验证 Agent
留在世界外，不得记录为 world participant。
