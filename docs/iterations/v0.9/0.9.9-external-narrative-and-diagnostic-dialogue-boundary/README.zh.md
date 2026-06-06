# 0.9.9 External Narrative And Diagnostic Dialogue Boundary

英文原文：`README.md`。

Status：implementation complete / verification passed
Type：mixed implementation package

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no

## 目标

定义第一版 external narrative projection 和 out-of-world diagnostic Agent dialogue 的公开边界，
且默认不把这两类 surface 当成 canonical world events、in-world dialogue 或 Agent memory。

本包要让 WorldEngine 能从 canonical public evidence 生成可检查的 narrative 或 diagnostic
outputs，同时保护 canonical world state、event timeline、Agent private memory 和 Agent
continuity artifacts，避免 projection-side mutation。

## 范围

Documentation review 之后，本包可以在 `backend/app/` 中扩展：

- additive public narrative projection schemas。
- additive public diagnostic dialogue schemas。
- 从 public events、snapshots 和 Agent continuity summaries 构造 redacted projection 或
  diagnostic artifacts 的 deterministic helpers。
- 可选 additive public API/manifest surfaces，用于 projection 和 diagnostic evaluation。
- focused backend/API tests，证明 projection 和 diagnostics 不修改 canonical world state、
  默认不追加 in-world dialogue events，并且默认不写入 Agent memory。

本包不得执行 live providers、不得创建 generated results、不得执行 checkers、不得修改
checker fixtures、不得运行 external validation、不得实现 frontend 或 Validation Client features、
不得创建 player-in-world chat system、不得把 diagnostic conversations 写入 Agent memory，
也不得修改 `backend/worldengine/`。

## 交付物

- Public narrative projection artifact contract。
- Public diagnostic dialogue artifact contract。
- 区分 external projection/diagnostic evidence 与 canonical world state、canonical events、
  Agent memory、in-world dialogue 的 decision table。
- Projection 和 diagnostics 的 provenance 与 redaction rules。
- 面向 additive active-backend work 的 focused implementation plan 和 test plan。

Closeout 后交接到：
`0.9.10-llm-backed-autonomous-checker-and-fixtures`。

## 当前授权

Documentation/contract/design/test-plan review 已通过。Implementation 仅授权本包记录的
scoped active-backend narrative projection and diagnostic dialogue boundary work，且已完成。

## 最终评估状态

Scoped active-backend `0.9.9` work 已完成 implementation。Focused、related 和 backend
regression verification 已在当前 session 通过，implementation re-review 在修复后报告无
P0/P1/P2/P3 findings。

Provider calls、generated-result creation、checker execution、external validation、frontend UI、
Validation Client work、durable scheduling 和 `backend/worldengine/` changes 仍未授权。
