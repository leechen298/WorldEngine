# 意图

状态：review complete

## 问题

`0.5.2` 已添加 working 和 episodic memory 的 generic in-memory substrate，但 Agent Loop
仍无法 perceive 这些 memory。v0.5 需要先建立一条从 substrate records 到 perception 的
bounded read-only bridge，后续 package 才能安全讨论 relationship、reflection、
self-summary 或 drift contracts。

这个 bridge 有风险，因为 perception 是 loop response 的一部分。本包必须让变化保持 additive，
并避免修改 action semantics。

## 目标

本包完成后，`PerceptionFrame` 可以包含由 working 和 episodic memory records 组装而成的
bounded memory context。Loop 可以在 response 的 perception 部分暴露该 context，同时 action
intent/result behavior 保持不变。

## 非目标

- 不添加 public memory APIs。
- 不添加用于 memory selection 的 loop request fields。
- 不在 loop step 中写 memory。
- 不修改 `ActionIntent`、`ActionResult`、action adapter semantics、accepted action types
  或 params patch validation。
- 不添加 persistence、migrations、vector retrieval、summarization、relationship behavior、
  reflection automation、self-summary generation、personality drift action modifiers、
  frontend behavior、fixtures 或 concrete world content。

## 为什么现在做

Memory substrate 已存在并通过 `0.5.2` review。v0.5 现在可以添加最小 read-only consumer path：
perception context。这样可以支撑后续 contract follow-up，同时不让 memory 改变 action behavior。

## Roadmap Relationship

本包是 v0.5 中把 memory substrate 连接到 Agent-in-World loop 的步骤。它不实现 v0.6 generation、
v0.7 external validation readiness、v0.8 projection readiness，也不实现更高风险的
self-continuity behaviors。

## North Star 对齐

North Star 要求 agents 能够基于 lived experience 形成连续性的 perceive 和 act。本包通过向
perception 暴露 bounded、inspectable memory context 支持该方向，同时保持 action behavior 明确且可测试。

## 预期交接

本包交接给 `0.5.4-reflection-relationship-and-drift-contract-followup`，届时 read-only
memory context 已集成并通过测试。
