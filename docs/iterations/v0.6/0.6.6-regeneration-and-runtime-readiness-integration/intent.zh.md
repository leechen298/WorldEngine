# 意图

状态：review complete

## 问题

`0.6.5` 已暴露带 bounded metadata 的 generation preview API。v0.6 仍需要一种已评审的方式，
从 generation input 再生成，并在后续 dashboard 或 runtime-facing work 依赖前，检查
generated `WorldSpec` 是否能通过现有 loader 和 runtime-context bridge。

## 目标

- 添加带 deterministic lineage metadata 的 bounded regeneration semantics。
- 使用 `load_worldspec`、`build_runtime_context` 和 `summarize_runtime_context` 添加
  runtime-readiness checks。
- 保持 readiness checks inert：不得 mutate live runtime，也不得改变 `RuntimeEngine.step`。
- 通过现有 generation API envelope 暴露 regeneration/readiness。
- 保留现有 generation preview、loader、runtime-context、runtime-step、event、
  Agent/memory 和 frontend behavior。

## 非目标

- 不做 full runtime migration。
- 不默认 mutate live runtime。
- 不添加 durable regeneration history、persistence、repositories 或 migrations。
- 不添加 dashboard UI 或 E2E workflow。
- 不声明 external validation readiness、projection readiness、product readiness、release
  readiness、generation-quality claim 或 autonomous validation claim。
- 不添加 live AI provider behavior。

## 北极星对齐

本 package 通过证明 generated specs 可以被加载并摘要成 runtime context，推进 runnable world
generation。它保持该证明 bounded 和 inspectable，而不是静默把 generated worlds 推入 live
runtime。

## 交接

完成后，`0.6.7-dashboard-generation-preview-and-e2e-smoke` 接收稳定 backend/API surfaces，
用于 dashboard preview work。
