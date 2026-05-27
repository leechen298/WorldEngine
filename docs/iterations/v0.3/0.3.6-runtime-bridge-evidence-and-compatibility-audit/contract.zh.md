# 契约

## 公开概念

- 证据索引：把 v0.3 包证据映射到变更文件、命令、兼容性表面和发现的文档表格。
- 兼容性审计：对运行时、API、事件、归档、参数、前端可见、schema、样例和旧路径影响进行分类的文档评估。
- 交接准备度：关于 v0.3 证据是否可在发布候选和收口门禁后支撑 v0.4 规划的可评审说明。

## 兼容性约束

- 不改变运行时行为。
- 不改变 API 返回形状。
- 不改变 schema 行为。
- 不改变前端行为。
- 不改变样例、迁移和测试实现文件。
- 既有证据必须引用 package review，不能把未运行测试扩大成通过声明。

## 允许变更

- 添加 `docs/iterations/v0.3/evidence-index.md`。
- 添加 `docs/iterations/v0.3/evidence-index.zh.md`。
- 添加 `docs/iterations/v0.3/compatibility-audit.md`。
- 添加 `docs/iterations/v0.3/compatibility-audit.zh.md`。
- 创建本 0.3.6 英文和中文迭代包文档。
- 将 v0.3 milestone index 和 plan 中的 0.3.6 状态更新为 `ready for review`。

## 禁止变更

- 不修改 `backend/`、`frontend/`、schema 实现、样例、迁移或测试实现文件。
- 不添加新运行时功能。
- 不在本包修补加载器或桥接代码。
- 不隐藏 P1 或 P2 发现。
- 不声明 v0.3 最终发布状态。
- 不把本包标记为 `ready for implementation`。
- 不添加具体演示世界或外部验证世界细节。

## 验收要求

- 包 README 和 v0.3 milestone index 将 0.3.6 标记为 `ready for review`。
- 证据索引把 0.3.0 到 0.3.5 映射到证据来源、命令或结果、兼容性覆盖和发现。
- 兼容性审计对运行时、API、事件、归档、参数、前端可见、schema、样例和旧路径影响进行分类。
- P1/P2/P3 发现、假设和开放风险明确列出。
- 测试和验证要求表述为可运行命令或可检查的文档断言。
- 英文和中文镜像保持同步。

## 北极星检查

本审计强化通用引擎边界。它不引入应用特定世界内容、产品 UI、外部样例内部细节或
Agent 自我连续性实现。

## 范围外后续

- v0.3 发布候选包。
- v0.3 最终收口。
- v0.4 世界内 Agent 最小闭环规划和实现。
- 机器可读外部报告 schema。
- 更广的 UI 或 E2E smoke 覆盖。
