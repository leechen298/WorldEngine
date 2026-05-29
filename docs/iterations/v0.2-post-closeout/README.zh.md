# v0.2 Post-Closeout Goal Campaign

状态：`campaign ready / unverified restart`
类型：goal campaign package

## 目标

把 `v0.2-post-closeout` 改成可以用一句 Codex App `/goal` 目标启动的 campaign：
文档必须说明先读哪些文件、child package 如何路由、如何验证、何时停止，以及如何记录
closeout evidence。

v0.2 feature 和 documentation closeout 仍保持完成状态。本 campaign 是 closeout 之后
的验证与 goal-running package，不改变 v0.2 release status。

## Goal Entry

自然语言目标：

```text
完成 v0.2-post-closeout
```

含义：

按照 `GOAL_RUNNER.md`、`CURRENT_STATE.md` 和 `CAMPAIGN_PLAN.md`，以 full
campaign goal 运行本 package。

从 `CURRENT_STATE.md` 中记录的当前 active child package 开始。每个 child package
必须按 child type、contract 和 risk，从 `GOAL_RUNNER.md` 定义的 gates 中选择需要执行的
流程。典型 gates 包括 documentation work、read-only review、在 child contract 允许时
记录 implementation authorization、被授权后 implementation、focused verification、
evaluator 或 code review、repair loops、按需执行 broader regression / E2E、按需执行
Codex autonomous validation、closeout consistency，并更新 `review.md`。

遇到 `BLOCKED`、`FAILED`、`FOLLOW_UP_REQUIRED`、`NEEDS_USER_INPUT`、source
conflict、evidence insufficiency，或任何超出 active child package contract 的文件修改，
必须停止。

这让本 package 对齐 Codex `/goal` 的使用方式：一个 durable objective、可验证停止条件、
明确 first-read files、证明进度的命令或产物、checkpoint 进展记录，以及明确暂停条件。

参考：<https://developers.openai.com/codex/use-cases/follow-goals#introduction>

## 当前路由说明

本 package 最初是 documentation-only post-closeout validation chain。此前
`02-e2e-validation-execution` 曾用 2026-05-29 evidence 记录为 `passed`。

这些证据仍保留为 archived evidence，供审计使用。但本 package 现在已回退为
`campaign ready / unverified restart`，这样 `/goal 完成 v0.2-post-closeout` 会从
child sequence 开头重新推进，而不是继承早前的完成结论。

当前重启顺序是：

1. 重新执行或重新接受 `01-e2e-validation-plan`；
2. 重新执行 `02-e2e-validation-execution`；
3. review-closeout `03-codex-autonomous-validation-plan`；
4. 执行 `04-codex-autonomous-validation-execution`；
5. 填写 `05-final-validation-bundle`。

`CURRENT_STATE.md` 是当前路由来源，`GOAL_RUNNER.md` 是执行状态机，
`CAMPAIGN_PLAN.md` 是 campaign 层面的 child sequence 和 closeout contract。

## 治理规则

本 validation documentation 位于 `docs/iterations/v0.2-post-closeout/`，并遵循
`docs/iterations/AGENTS.md` 中关于 evidence、review 和 post-closeout validation
的规则。

## 验证链

0. Master validation planning。
1. E2E / integration / API smoke validation plan。
2. E2E / integration / API smoke execution report。
3. Codex autonomous validation plan。
4. Codex autonomous validation execution and review template。
5. Final validation bundle template。

## Package Index

| Package | Type | Status | Purpose |
|---|---|---|---|
| `01-e2e-validation-plan` | validation-planning | restart ready | 定义或重新接受 v0.2 post-closeout E2E、integration 和 API smoke validation 范围。 |
| `02-e2e-validation-execution` | validation-execution | not executed in current campaign | 执行 v0.2 post-closeout E2E、integration 和 API smoke validation。 |
| `03-codex-autonomous-validation-plan` | validation-planning | not executed in current campaign | 定义独立 Codex autonomous validation 范围。 |
| `04-codex-autonomous-validation-execution` | validation-execution | not executed in current campaign | 执行独立 Codex autonomous validation。 |
| `05-final-validation-bundle` | validation-bundle | not executed in current campaign | 汇总最终 v0.2 post-closeout validation result。 |

## 结果状态

validation documents 可以使用以下状态：

- `planned`
- `ready for execution`
- `executed`
- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`
- `not executed in current campaign`
- `archived evidence only`

execution report 初始状态为 `not executed`，validation run 必须用
current-session evidence 填写结果。历史结果可以继续保留在 package reports 中，但
restart 后只能作为 `archived evidence only`；除非当前 campaign 明确重新运行或重新接受，
不得算作当前完成状态。

## 范围

允许：

- 定义 post-closeout validation workflow。
- 定义 report templates 和 evidence requirements。
- 定义 E2E / integration / API smoke execution expectations。
- 定义 Codex autonomous validation expectations。
- 定义 final validation bundle requirements。
- 定义 full-campaign `/goal` 路由和 restart semantics。

禁止：

- 更新 planning 或 routing documents 时，不运行 backend、frontend、E2E、API smoke、
  runtime、schema execution、fixture、migration 或 autonomous validation commands。
- 不在明确拥有 validation execution 的 package 之外运行 validation commands。
- 除非 child package contract 明确授权 implementation 且 `GOAL_RUNNER.md` 的
  implementation gate 已通过，否则不修改 runtime、schema、API、frontend、backend
  tests、fixtures 或 external repositories。
- 不加入具体 demo-world 名称、地点、角色、资源、story rules、seed data、UI
  selectors 或 private oracle details。
- `04` 和 `05` 未以 evidence closeout 前，不声明 v0.2 final validation 已完成。
- 不改变 v0.2 final / complete status。

## 交付物

- `CURRENT_STATE.md`
- `CURRENT_STATE.zh.md`
- `GOAL_RUNNER.md`
- `GOAL_RUNNER.zh.md`
- `CAMPAIGN_PLAN.md`
- `CAMPAIGN_PLAN.zh.md`
- `validation-master-plan.md`
- `validation-master-plan.zh.md`
- `validation-report-template.md`
- `validation-report-template.zh.md`
- `review.md`
- `review.zh.md`
- `01-e2e-validation-plan/`
- `02-e2e-validation-execution/`
- `03-codex-autonomous-validation-plan/`
- `04-codex-autonomous-validation-execution/`
- `05-final-validation-bundle/`

## 最终评估状态

本 campaign 已可由 Codex App `/goal` 启动，但当前还没有完成验证。
`CURRENT_STATE.md` 已回退为从 `01-e2e-validation-plan` 开始。
