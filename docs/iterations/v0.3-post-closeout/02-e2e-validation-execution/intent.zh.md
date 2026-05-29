# 意图

## 问题 / 目的

本 campaign 需要一个单独的执行包，避免把验证证据混进规划文档。后续本包会记录实际运行了什么、
什么被阻塞，以及 findings 如何分类。

## 为什么现在需要

v0.3 收口中的 runtime 和 compatibility claims 依赖历史包证据。后续执行包必须把 fresh
validation evidence 明确、可 review 地记录下来。

## 与路线图的关系

本包可以为 v0.4 规划是否具备当前验证信心提供输入，但它本身不启动 v0.4。

## 非目标

- 在本轮文档创建中执行验证。
- 修复代码。
- 添加 E2E 测试。
- 修改 API routes。
- 改变 schema 或 runtime behavior。
- 添加 fixture data 或外部仓库。
- 改变 v0.3 发布状态。

## 预期交接

后续执行完成后，`03-codex-autonomous-validation-plan` 可以把本报告作为独立 Codex review
规划的输入之一。
