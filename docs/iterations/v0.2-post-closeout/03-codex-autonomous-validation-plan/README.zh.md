# Codex Autonomous Validation Plan

状态：`not executed in current campaign`
类型：autonomous validation planning

## 目标

定义 independent Codex reviewer 如何验证 v0.2 post-closeout claims，且不依赖
implementer summaries。

## 当前 Campaign 说明

campaign reset 后，本 planning package 不是当前 active child。它必须等待当前
campaign 的 `02-e2e-validation-execution` evidence，或等待 accepted blocker 后，
才能进入 review-closeout。

## 命名规则

使用 `Codex autonomous validation`，不要使用 Agent autonomous testing。这样可以避免与
WorldEngine Agent-in-World concepts 混淆。

## 范围

independent reviewer 必须读取 release docs、evidence docs、code、schemas 和 tests。
reviewer 必须运行可用 validation commands，或记录 blocker。reviewer 不得修改 code。

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

当前 campaign 尚未执行。autonomous validation 也尚未执行。
