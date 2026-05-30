# 意图

## 问题 / 目的

只实现只读感知和增量 schema。

本包目标：新增通用世界内 Agent schema model 和有界 perception builder，读取 runtime state、recent events、world params 和可选 runtime-context summary，不产生状态变更。

## 为什么现在做

v0.3 final closeout 已完成，post-closeout campaign 以 P3 handoffs 通过。该证据允许 v0.4 规划启动，但不授权实现。本包建立或消费 v0.4 sequence 中的下一个已评审门禁。

## 与 Roadmap 的关系

v0.4 是 Agent-in-World Minimal Loop 里程碑，位于 v0.3 WorldSpec loader/runtime-context bridge 之后、v0.5 memory 和 self-continuity 之前。本包必须把这些后续能力排除在范围外。

## 非目标

- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

## 预期交接

`CAMPAIGN_PLAN.md` 中的下一包只接收已评审证据和明确 handoff notes。
