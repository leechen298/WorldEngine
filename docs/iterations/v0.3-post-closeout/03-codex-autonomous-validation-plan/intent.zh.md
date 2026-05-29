# 意图

## 问题 / 目的

E2E 和 API smoke 验证执行行为。本包定义另一条独立 Codex review 线，用来检查 v0.3
release claims 是否被 docs、code、tests 和 command evidence 支撑。

## 为什么现在需要

v0.3 loader 和 bridge claims 比较细。Reviewer 必须直接验证契约边界，而不是相信实现者总结。

## 与路线图的关系

本 review 防止 v0.4 规划继承 unsupported v0.3 claims。它不授权 v0.4 实现。

## 非目标

- 在本包执行自主 review。
- 修改代码。
- 修改测试。
- 添加 fixtures 或 E2E coverage。
- 改变发布状态。
- 创建外部仓库。

## 预期交接

`04-codex-autonomous-validation-execution` 使用本计划和 review template 执行独立 review。
