# 意图

## 问题 / 目的

v0.9 父包定义了版本级 LLM-backed lifecycle foundation，但计划中的
`0.9.x` 章节不是可执行的子包 contract。`0.9.0` 创建第一个具体子包，并记录当前
v0.8 交接状态，避免后续 agent 从父级路线图文字直接跳到 provider、runtime、
checker、fixture 或 Validation Client work。

关键漂移风险是过度声明：v0.8 已通过官方 checker 证明 basic lifecycle，而
LLM-backed lifecycle validation 仍被缺失的 provider live smoke、LLM-backed
world creation、rule-linked evolution、event legality、persistent Agent
autonomy and consolidation evidence，以及 checker/schema support 阻塞。本包保留
这个拆分。

## 为什么现在

用户启动了 v0.9 的 `/goal` development，并明确授权使用 subagents。v0.9
`CURRENT_STATE.md` route 要求在 implementation 或 evidence execution 之前创建或
确认具体 `0.9.0` child package。

如果没有本包，后续工作可能把 `v0.9-plan.md` 当作直接实现授权，在 redaction
rules review 前运行 live provider calls，或把计划中的 LLM-backed testing assets
标记为 pass-capable evidence。

## 与路线图的关系

v0.9 将 WorldEngine 从已证明的 basic lifecycle 推向第一个 LLM-backed lifecycle
foundation。本包是交接给
`0.9.1-provider-live-smoke-and-redaction-boundary` 的文档基线；`0.9.1` 必须先定义
provider live smoke 和 provider evidence redaction，之后才能开始 LLM-backed world
generation。

## 非目标

- 不实现 provider configuration 或 provider smoke。
- 不运行 live provider calls。
- 不实现 LLM-backed world creation。
- 不实现 rule/parameter schemas。
- 不实现 runtime run controls。
- 不实现 user direction、event legality、Agent continuity、consolidation、
  narrative projection、diagnostic dialogue、checker support、fixtures、
  scorecards 或 Validation Client handoff behavior。
- 不修改 runtime、API、schema、frontend、backend tests、checker、fixture、
  migration、generated result、external repository、Validation Client、provider
  configuration 或 `backend/worldengine/` 文件。
- 不声称 v0.9 runtime/API/frontend/E2E/Agent/autonomous/product、provider、
  LLM-backed、external validation 或 generation-quality PASS。

## 预期交接

`0.9.1-provider-live-smoke-and-redaction-boundary` 接收：

- 父级 v0.9 route/status 已同步到下一个子包选择。
- v0.8 basic full-lifecycle PASS 仅作为 handoff context。
- LLM-backed lifecycle blocker taxonomy 保持为当前 v0.9 起点。
- 明确的 provider live-call 和 redaction stop rules。
- implementation 与 evidence execution 仍关闭，直到 `0.9.1` package documents
  被创建、review 并授权。
