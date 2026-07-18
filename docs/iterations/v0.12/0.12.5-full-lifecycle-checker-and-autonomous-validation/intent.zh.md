# Intent

英文原文：`intent.md`。

## 问题

v0.12 现在已有 public Agent continuity surfaces 和 Validation Client evidence handoff contract。MVP 仍需要 evidence-backed lifecycle classification。本仓库包含 deterministic autonomous checker fixtures，但当前 fresh external Validation Client export 可能不存在。

## 用户价值

用户会得到诚实分类：哪些 checker evidence 通过了，哪些 fresh validation 没有运行，以及剩余 MVP 路径是 PASS、PARTIAL、BLOCKED 还是 FAIL。

## 工程价值

本包防止历史 saved results 或 UI smoke 被误表述成当前 v0.12 full lifecycle PASS。同时它定义 `0.12.6` final closeout 的输入。

## 非目标

- 不实现 external Validation Client。
- 不改 product code。
- 除非后续明确授权，不做 provider live calls。
- 不做 final MVP closeout。
