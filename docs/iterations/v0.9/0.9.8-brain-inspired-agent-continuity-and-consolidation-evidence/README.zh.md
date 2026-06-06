# 0.9.8 类脑 Agent 连续性与沉淀证据

英文原文：`README.md`。

Status：implementation complete / verification passed
Type：mixed implementation package

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no

## 目标

为 v0.9 定义第一版公开、类脑启发的 Agent continuity evidence surface，同时不声明意识，也不暴露私有内部信息。

本包要让 WorldEngine 能展示：Agent 可以感知公开 world events，保持有界 short-term continuity，暴露 public long-term summary references，报告稳定或 bounded-drift 的 personality/skill summary references，选择 intent/action/no-intent/rest states，响应事件，并记录可跨多个 ticks 的 sleep/rest/low-activity consolidation phases。

## 范围

本包允许在 `backend/app/` active backend path 中扩展：

- additive public Agent continuity schemas。
- additive public consolidation evidence schemas。
- 用于 continuity summaries 和 consolidation phase records 的 deterministic in-memory helpers。
- Agent public intent、autonomous action、no-intent、rest、event reaction 和 consolidation records 的 additive event payload evidence。
- focused backend/API tests，覆盖 redaction、multi-tick continuity、consolidation cadence、no-intent/rest states、event reaction evidence、与既有 Agent loop 和 v0.5 memory surfaces 的兼容，以及拒绝 client-scripted autonomy evidence。

本包不得执行 live providers、不得创建 generated results、不得执行 checkers、不得修改 checker fixtures、不得运行 external validation、不得添加 frontend 或 Validation Client 工作、不得实现 narrative projection 或 diagnostic dialogue、不得添加 durable scheduling，也不得修改 `backend/worldengine/`。

## 交付物

- Public Agent continuity artifact contract。
- Public consolidation artifact contract。
- Public autonomous action evidence contract，用于区分 WorldEngine-backed Agent action 和 client-scripted action。
- 在 active backend scope 内生成 public continuity 和 consolidation evidence 的 deterministic helper 或 API behavior。
- 排除 raw thought、chain-of-thought、private memory payloads、private goals、hidden context 和 private evaluator data 的 redaction behavior。
- Focused tests，证明 multi-tick continuity evidence、consolidation cadence、accepted autonomous action evidence、no-intent/rest states、event reactions、redaction，以及与 existing Agent loop、memory、event、runtime 和 public handoff surfaces 的兼容性。

Closeout 后交接到：
`0.9.9-external-narrative-and-diagnostic-dialogue-boundary`。

## 当前授权

Documentation/contract/design/test-plan review 已通过。本包记录的 scoped active-backend Agent continuity and consolidation evidence work 已完成 implementation。

## 最终评估状态

Scoped active-backend `0.9.8` work 已完成 implementation。Focused、related 和 backend regression verification 已在当前 session 通过，implementation re-review 报告无 code-level P0/P1/P2/P3 findings。

Provider live calls、generated-result creation、checker execution 或 fixture changes、external validation、frontend UI、Validation Client changes、narrative projection、diagnostic dialogue、durable scheduling 和 `backend/worldengine/` changes 仍未授权。
