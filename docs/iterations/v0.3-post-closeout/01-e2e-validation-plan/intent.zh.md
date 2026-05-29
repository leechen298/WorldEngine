# 意图

## 问题 / 目的

v0.3 final closeout 已经说明，0.3.8 阶段没有重新执行 fresh runtime、API、frontend、
schema、fixture、migration、build、E2E、Agent smoke 或 backend regression。
本包定义后续执行包生成独立证据前必须遵守的验证计划。

## 为什么现在需要

v0.3 已经交付 loader 和 bridge 基础设施。剩余验证风险不是文档是否声明 v0.3 已收口，
而是后续 fresh validation 能否重新检查 loader、bridge、runtime / API 兼容性、
Event.refs 响应形状和 E2E 可用性，而不是只依赖历史包证据。

## 与路线图的关系

本包保护 v0.3 到 v0.4 的交接。v0.4 仍只能通过自己的已评审迭代包启动。

## 非目标

- 执行测试。
- 修复实现。
- 改变运行时行为。
- 新增或修改 API routes。
- 添加 fixtures 或 demo-world 内容。
- 创建外部仓库。
- 改变 v0.3 发布状态。

## 预期交接

通过 review 后，`02-e2e-validation-execution` 可以按本计划运行或阻塞验证命令，并填写报告。
