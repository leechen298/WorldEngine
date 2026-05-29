# Codex Autonomous Validation Plan

状态：package complete / plan accepted current campaign
类型：autonomous validation planning

## 目标

定义独立 Codex reviewer 如何直接验证 v0.2 post-closeout claims，并避免只复述
implementer summaries。

## 当前 Campaign 说明

当前 campaign 的 `02-e2e-validation-execution` evidence 已通过后，本 planning package
成为 active child。当前 `/goal` run 已 review 并接受本计划，下一步交接给
`04-codex-autonomous-validation-execution`。

## 命名规则

使用 `Codex autonomous validation`，不要写成 Agent autonomous testing。这样可以避免与
WorldEngine 的 Agent-in-World 概念混淆。

## 范围

独立 reviewer 必须读取 release docs、evidence docs、code、schemas 和 tests。reviewer
必须运行可用的 validation commands；如果命令无法运行，必须记录 blocker。reviewer 不得
修改 code。

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

本计划已在当前 campaign 中接受。本 package 没有执行 autonomous validation；
`04-codex-autonomous-validation-execution` 负责该执行步骤。
