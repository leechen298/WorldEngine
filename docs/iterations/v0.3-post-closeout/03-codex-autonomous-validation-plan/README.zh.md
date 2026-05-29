# 03 Codex 自主验证计划

状态：`review complete`
类型：自主验证规划包

## 目标

定义 v0.3 收口后的独立 Codex 自主验证计划。本包告诉后续 reviewer 应读什么、检查哪些
claims、运行哪些命令或记录哪些 blocker，以及不能修改什么。

本包不执行自主验证。已批准的 campaign 执行把本计划推进到
`04-codex-autonomous-validation-execution`。

## 交付物

- `README.md`
- `intent.md`
- `contract.md`
- `test-plan.md`
- `plan.md`
- `review.md`

每个文件都有 `.zh.md` 镜像。

## Reviewer 必须做到

Reviewer 必须：

- 不依赖实现者总结。
- 直接读取 docs 和 code。
- 运行可用验证命令，或记录 blocker。
- 不修改代码。
- 不声明未验证检查成功。
- 输出 independent review。
- 检查 WorldSpec loader claims。
- 检查 runtime context bridge claims。
- 检查 RuntimeEngine compatibility。
- 检查 Event.refs response compatibility。
- 检查没有 concrete demo-world regression。
