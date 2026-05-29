# 02 E2E 验证执行

状态：`not started / template`
类型：验证执行包

## 目标

为后续 v0.3 收口后 E2E、集成、API smoke、后端确定性检查、WorldSpec loader、
runtime context bridge、Event.refs、release claim 和 concrete demo-world regression
验证提供执行包。

本轮只创建模板，不执行验证。

## 交付物

- `README.md`
- `intent.md`
- `contract.md`
- `execution-plan.md`
- `e2e-validation-report.md`
- `review.md`

每个文件都有 `.zh.md` 镜像。

## 初始报告状态

`e2e-validation-report.md` 初始为 `not executed`。

后续真正执行本包前，不要替换这个状态。

## 边界

后续执行可以运行验证命令并更新本包报告。但仍不得修改 runtime、schema、API、
frontend、backend tests、fixtures、migrations、外部仓库或 v0.3 发布状态。
