# 意图

状态：review complete

## 问题

v0.5 已评审 memory 和 self-continuity semantics，但 engine 还没有 generic substrate
来记录 working memory 或 event-linked episodes。没有这个最小 substrate，`0.5.3`
无法安全地向 Agent Loop 提供 bounded read-only memory context。

实现必须保持小范围，因为周边 self-continuity features 仍是 contract-only。本包只证明记录可以创建、
bounded、隔离和检查，而不改变 runtime 或 action semantics。

## 目标

本包完成后，backend code 拥有：

- working memory 和 episodic memory 的 additive schema models。
- generic agent/world-scoped memory records 的 in-memory store。
- 证明 bounded working-memory retrieval、episodic event linkage、provenance semantics
  和 copy isolation 的测试。
- v0.4 Agent Loop behavior 未改变的 compatibility evidence。

## 非目标

- 不添加 API routes 或 public runtime endpoints。
- 不把 memory 接入 `PerceptionBuilder` 或 `AgentLoopService`。
- 不修改 `LoopStepRequest`、`ActionIntent`、`ActionResult`、action result adapter behavior、
  accepted action types 或 params patch semantics。
- 不添加 durable persistence、migrations、vector search、summarization、
  relationship state behavior、reflection automation、self-summary generation、
  personality drift action modifiers、frontend behavior、fixtures 或 concrete world content。

## 为什么现在做

`0.5.1` 已定义 public concept 和 schema semantics。最小安全代码切片是只做 working 和
episodic memory，不接入 loop。这样可以为 `0.5.3` 提供一个已测试、只读可消费的 substrate。

## Roadmap Relationship

本包是 v0.5 Memory and Self-Continuity Substrate roadmap goal 中第一个带实现的切片。
它只实现 `v0.5-plan.md` 标为首个安全 implementation candidates 的 working-memory 和
episodic-memory 部分。

它不实现 v0.6 world generation、v0.7 external validation readiness、v0.8 projection
application readiness，也不实现 relationship updates、self-summary generation、
reflection automation 或 personality drift action modifiers 等后续 memory behavior。

## North Star 对齐

本包用可检查记录支持 agent memory 和 lived experience，同时让 pseudo-self behavior 保持明确、
有边界且可评审。它不声称意识，也不把 WorldEngine 收窄成 game-specific 或 application-specific backend。

## 预期交接

本包交接给 `0.5.3-memory-context-loop-integration`，提供 generic in-memory substrate，
供 perception code 只读消费，并保持 action semantics 不变。
