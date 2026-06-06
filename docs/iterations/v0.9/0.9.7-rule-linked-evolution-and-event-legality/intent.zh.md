# 意图

英文原文：`intent.md`。

## 问题

v0.9 已经具备公开的生成规则/参数 schema、有界运行控制，以及有界的自然语言世界方向引导。缺失的是中间桥梁：证明某个事件或参数变化确实符合公开规则和当前公开状态。

如果没有这座桥，LLM-backed lifecycle 仍然可能表现得像任意插入故事事实。验证者需要看到公开证据：事件之所以被选择，是因为它匹配规则、约束、概率、因果、位置、时间，以及经过脱敏后的方向压力。

## 产品意图

本包建立第一版确定性的公开规则关联演化边界。WorldEngine 可以检查一个 `WorldEventCandidate`，用公开的 `GeneratedRuleParameterSet` 和公开状态快照来评估它，然后：

- 将合法候选接受为世界演化事件，并记录公开状态差异证据；或
- 用公开诊断拒绝该候选，且不产生 canonical state mutation。

本包不是故事引擎、checker、provider-backed adjudicator，也不是 Agent autonomy system。它是规则关联事件合法性的通用引擎边界。

## 用户价值

- 用户可以引导世界方向，但不能强制最终事实。
- 验证者可以看到事件为什么合法或非法。
- 后续 Agent continuity 工作可以依赖一个不是任意 hidden mutation 的事件流。
- 未来 LLM-backed checker support 可以消费公开合法性证据，而不需要私有 prompt 或 provider trace。

## North Star 对齐

WorldEngine 的 north star 要求世界能带着事件、规则、时间线、资源、历史、快照和恢复能力随时间运行。本包让事件合法性在后续 Agent continuity 和 checker package 依赖它之前变得可检查。

## 非目标

- 不做 live provider interpretation。
- 不创建 generated world 或 generated rules。
- 不执行 checker，也不修改 fixture。
- 不做 external validation。
- 不修改 frontend 或 Validation Client。
- 不修改 Agent private memory、goal、personality、skill、relationship、inventory、life/death 或 location，除非这是公开世界规则明确覆盖的公开状态差异。
- 不实现 narrative projection 或 diagnostic dialogue。
- 不添加 durable scheduler 或 background evolution loop。
- 不修改 `backend/worldengine/`。
