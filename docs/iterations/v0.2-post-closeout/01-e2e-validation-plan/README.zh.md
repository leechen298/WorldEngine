# E2E / Integration / API Smoke Validation Plan

状态：`package complete / planning re-accepted`
类型：验证规划

## 目标

定义 v0.2 post-closeout 的 E2E、集成检查和 API smoke 验证范围，但本 package
不执行任何验证命令。

## 当前 Campaign 说明

本 package 之前已经达到 `review complete`。在当前
`v0.2-post-closeout` goal campaign 中，那次 review 只作为历史证据保留；
campaign 进入 `02-e2e-validation-execution` 前，必须重新复核本规划，或在
review 中写明理由后重新接受它。

## 范围

本 package 规划以下验证范围：

- 仓库状态和文档一致性检查。
- 后端确定性测试。
- schema smoke 检查。
- event 兼容性检查。
- runtime step 检查。
- world events 检查。
- event steps 检查。
- 可用时检查 params。
- 可用时检查 archive。
- API smoke 检查。
- E2E 框架可用性检查。
- release 声明核对。
- 具体 demo-world 内容回归检查。

## E2E 定义

WorldEngine v0.2 不声明已交付 product UI。对本 post-closeout package 来说，
E2E 的含义是：

- 如果仓库里有可运行的框架，就运行 browser E2E。
- 如果 browser E2E 不可用，则用后端集成检查、API smoke 和 release 声明核对
  作为替代验证线。

如果不存在 E2E 框架，或测试套件无法运行，必须把 E2E 记录为
`not configured` 或 `blocked`。不得把未执行的检查写成成功结果。

## 交付物

- `intent.md`
- `intent.zh.md`
- `contract.md`
- `contract.zh.md`
- `test-plan.md`
- `test-plan.zh.md`
- `plan.md`
- `plan.zh.md`
- `review.md`
- `review.zh.md`

## 最终评估状态

当前 campaign 中的本 package 已完成。本 package 仍然只负责规划，不执行验证；
下一个 checkpoint 由 `02-e2e-validation-execution` 承接。
