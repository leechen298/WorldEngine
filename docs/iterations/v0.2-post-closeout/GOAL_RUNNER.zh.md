# GOAL_RUNNER.md

目的：为 WorldEngine `v0.2-post-closeout` validation chain 提供 Codex App
`/goal` 路由说明。

本文只是路由辅助文件，不重新打开 v0.2 implementation，也不改变 v0.2 release status。

## 权威输入

运行任何 validation goal 前，必须读取：

- `CURRENT_STATE.md`
- `validation-master-plan.md`
- `README.md`
- `findings.md`
- active package 的 `README.md`、`intent.md`、`contract.md`、`plan.md` 和
  `review.md`
- active package 存在 `test-plan.md` 时也读取它
- package 有 execution report 或 template 时，读取对应文件
- `docs/iterations/AGENTS.md`
- root `AGENTS.md`

如果这些文件与真实 git state 冲突，停止并记录为 `NEEDS_USER_INPUT`。

## 执行模式

默认模式：每次 `/goal` 只处理一个 validation package。

- 只处理一个 package。
- package 达到最终 route status 后立即停止。
- 除非用户明确要求 full campaign mode，否则不要继续下一个 package。

Full campaign mode：

- 仅当当前 package 达到 `PACKAGE_COMPLETE` 时继续。
- 遇到 `BLOCKED`、`FAILED`、`FOLLOW_UP_REQUIRED`、`NEEDS_USER_INPUT`、
  source conflict 或 evidence insufficiency 时停止。

## 路由类型

- `review-closeout-plan`
- `validation-execution`
- `autonomous-review-execution`
- `final-bundle-closeout`

## Runtime 授权

本 validation chain 不允许修改 implementation files。

所有 package 均禁止：

- runtime code changes
- schema changes
- API changes
- frontend changes
- backend test changes
- fixture changes
- migration changes
- external repository changes

只有当 active package 明确拥有 execution 时，validation execution 才可以运行命令并更新
validation documents。

## 最终状态词汇

使用以下精确 route status：

- `PACKAGE_COMPLETE`
- `REVIEW_READY`
- `NOT_EXECUTED`
- `BLOCKED`
- `FAILED`
- `PASSED_WITH_P3`
- `NEEDS_USER_INPUT`
- `FOLLOW_UP_REQUIRED`

不要用措辞把 `blocked`、`failed` 或 `not executed` 转写成 `passed`。状态由 evidence 决定。

## Package 路由

当前默认路由：

```text
03-codex-autonomous-validation-plan review-closeout-plan
```

不要在 `03` 执行 autonomous validation。

`03` 只审查 plan 是否足以交接给
`04-codex-autonomous-validation-execution`。

`04` 负责 independent Codex autonomous validation execution。

`05` 负责 final bundle synthesis 和 v0.4 proceed decision。

## 强制停止条件

出现以下情况时停止：

- required files 缺失；
- git state 与 package status 冲突；
- package 在没有 command evidence 的情况下声明 passed；
- command 无法运行且未记录 blocker；
- `findings.md` 仍有 unresolved P1/P2，而当前 package 试图声明 clean final pass；
- execution 需要修改 implementation files；
- final bundle 在缺少 E2E / API / backend 和 Codex autonomous validation evidence
  的情况下试图允许 v0.4 继续。

## 每个 Package 的必要 Closeout

结束 package goal 前，必须更新 package `review.md`，记录：

- changed files；
- files read；
- commands run；
- commands not run；
- test results；
- compatibility review；
- scope review；
- unresolved P1/P2/P3；
- final status。

保持 `CURRENT_STATE.md` 与最新 package status 一致。
