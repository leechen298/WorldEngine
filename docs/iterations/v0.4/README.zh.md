# v0.4 世界内 Agent 最小闭环

状态：ready for review（待评审）
类型：Codex `/goal` 开发活动与迭代包根目录

## 目标

v0.4 建立最小世界内 Agent 闭环。这个版本让 Agent 能感知世界事件、产生
action intent、接收 action result，并通过一个小而经过校验的边界影响世界状态。

本轮文档创建不实现 runtime、schema、API、frontend、test、fixture、migration 或
legacy 代码变更。它创建后续带实现子包必须遵守的已评审文档门禁。

## 目标 入口

自然语言 goal：

```text
完成 v0.4
```

解释：

- 从 `CURRENT_STATE.md` 开始。
- 按 `GOAL_RUNNER.md` 选择路线、执行 subagent/evaluator 检查点、判断实现授权、运行验证并处理停止条件。
- 按 `CAMPAIGN_PLAN.md` 和 `v0.4-plan.md` 推进子包顺序、交付物、兼容性约束和交接规则。
- 在处理任何子包前，先读 active child package docs。

这不是 automation-controller 实现。调度、编排、重试基础设施和 Codex 角色分配属于 Codex 环境或外部工具。

## 范围

v0.4 允许范围：

- 从 runtime state、recent events、current world params 和可选 runtime context summary 构建最小 perception frame。
- 最小 action intent 和 action result 契约。
- 经过校验的 `noop` 和 `params.patch` action effects。
- 请求驱动的闭环编排。
- 增量后端 schema、内部服务、只有 child package contract 明确授权时才新增的 API route，以及聚焦测试。

v0.4 禁止范围：

- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

## 交付物

- 父级 goal-campaign 文档：`README.md`、`v0.4-plan.md`、`GOAL_RUNNER.md`、`CURRENT_STATE.md`、`CAMPAIGN_PLAN.md`、`review.md` 及中文镜像。
- 八个子包文档集，每个包含 README、intent、contract、technical design、test plan、plan、review 及中文镜像。
- `/goal` 执行所需的 subagent/evaluator checkpoint 规则。
- 证明本轮仅修改文档的 documentation-stage review evidence。

## 包索引

### `0.4.0-v0.4-planning-and-compatibility-baseline`

- 类型：documentation-only
- 状态：ready for review
- 目的：创建 v0.4 文档根目录、goal campaign 控制文件、版本计划、兼容性基线和 v0.3 交接映射，不修改实现文件。

### `0.4.1-agent-in-world-loop-contract`

- 类型：documentation-only
- 状态：planned
- 目的：在代码变更前定义 v0.4 世界内 Agent 闭环的公开概念、事件语义、API 边界、错误模型和实现授权条件。

### `0.4.2-agent-perception-and-schemas`

- 类型：mixed or code
- 状态：planned
- 目的：新增通用世界内 Agent schema model 和有界 perception builder，读取 runtime state、recent events、world params 和可选 runtime-context summary，不产生状态变更。

### `0.4.3-action-intent-validation-and-result-adapter`

- 类型：mixed or code
- 状态：planned
- 目的：实现最小通用 action intent validator 和 result adapter，支持 noop 与经过校验的 params.patch，复用既有参数校验和 dry-run 防护。

### `0.4.4-minimal-agent-loop-orchestration-and-api`

- 类型：mixed or code
- 状态：planned
- 目的：接入请求驱动的最小世界内 Agent 闭环：构建 perception，获得或接受 intent，校验并应用 intent，发出可审查 result evidence，并返回稳定 API response。

### `0.4.5-agent-loop-evidence-and-compatibility-audit`

- 类型：documentation-only
- 状态：planned
- 目的：审计 v0.4 实现证据、变更文件、兼容性 surface、未解决 findings 和 release-candidate review 交接就绪度。

### `0.4.6-v0.4-release-candidate-bundle`

- 类型：documentation-only
- 状态：planned
- 目的：从已评审实现和审计证据准备 v0.4 release-candidate bundle，不声明最终发布，也不添加实现变更。

### `0.4.7-v0.4-final-closeout`

- 类型：documentation-only
- 状态：planned
- 目的：仅在 release-candidate review approval、证据一致性检查和未解决 finding 分类完成后，才把 v0.4 标记为 final / closeout complete。

## 当前状态

Active child package：`0.4.0-v0.4-planning-and-compatibility-baseline`。

当前路线：documentation planning and review。任何带实现子包都必须先完成 package docs 评审，并由必需 evaluator checkpoint 记录无阻塞 finding 后，才能获得实现授权。

## 最终评估状态

当前值：`ready for review`。

v0.4 尚未 implementation complete、release-candidate complete 或 final closeout complete。后续包必须记录自己的证据，才能声明 runtime、API、test、E2E 或 release claims。
