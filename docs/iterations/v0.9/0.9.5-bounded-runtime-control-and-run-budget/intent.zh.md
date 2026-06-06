# Intent

英文原文：`intent.md`。

## 问题 / 目的

WorldEngine 当前只暴露 single-step runtime advancement。v0.9 需要 finite run controls，
使 validation 和后续 user-facing flows 可以让世界按有限 tick 数或有限 world-time duration 前进，
而不会产生 infinite loops、unbounded provider usage 或证据不清。

## 为什么现在做

`0.9.4` 只有在 supplied public bounded-run evidence 存在时才能评估 bounded-run fidelity。
`0.9.5` 在后续 natural-language direction、rule-linked event legality、Agent continuity、
checker fixtures 和 full lifecycle validation 之前，提供这个 bounded execution foundation。

## 与路线图的关系

本包通过让 runtime execution 变得 finite、inspectable 且 guard-controlled，推进 v0.9
LLM-backed lifecycle foundation。它支撑 North Star：world evolution 必须由 event-backed、
reviewable 的过程支撑，而不是隐藏在 unbounded loops 后面。

## 非目标

- 不调用 live providers。
- 不实现 provider-backed world evolution。
- 不实现 rule-linked parameter evolution 或 event legality。
- 不实现 natural-language direction semantics。
- 不实现 Agent continuity 或 consolidation。
- 不实现 durable scheduling、background workers、queues 或 deployment infrastructure。
- 不实现 frontend UI 或 Validation Client behavior。
- 不运行 checker execution、generated-result creation、external validation、E2E 或 autonomous validation。
- 不修改 `backend/worldengine/`。

## 预期交接

`0.9.5` 应向 `0.9.6` 交接 bounded runtime controls 和 public run summaries，使
natural-language world direction 可以依赖 finite run windows，而不是 uncontrolled progression。

