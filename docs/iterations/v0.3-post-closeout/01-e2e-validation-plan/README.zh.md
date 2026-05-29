# 01 E2E 验证计划

状态：`planned / ready for review`
类型：验证规划包

## 目标

定义 v0.3 收口后验证中，后续 E2E、集成、API smoke、WorldSpec loader、
runtime context bridge、Event.refs、release claim 和 concrete demo-world regression
应该如何检查。

本包不执行验证。

## 范围

本计划覆盖：

- 仓库和文档检查。
- 后端确定性检查。
- 聚焦 WorldSpec loader 测试。
- 聚焦 runtime context bridge 测试。
- event API compatibility 测试。
- API smoke 检查。
- E2E framework 可用性检查。
- 已配置时的浏览器 E2E 执行。
- E2E framework 不可用时的 fallback。
- v0.3 release claim 验证。
- concrete demo-world regression 检查。

如果没有可运行的 E2E setup，必须把 E2E 记录为 not configured 或 blocked，并用
API smoke 加后端集成测试作为 fallback。

## 交付物

- `README.md`
- `intent.md`
- `contract.md`
- `test-plan.md`
- `plan.md`
- `review.md`

每个文件都有 `.zh.md` 镜像。

## 边界

允许：只写规划文档。

禁止：运行 backend / frontend / E2E / API smoke / runtime / schema / fixture /
migration / build / Agent smoke / Codex autonomous 检查，编辑代码或测试，添加 fixture，
创建外部仓库，或改变 v0.3 发布状态。

## 最终评估状态

最终评估：`planned / ready for review`。
