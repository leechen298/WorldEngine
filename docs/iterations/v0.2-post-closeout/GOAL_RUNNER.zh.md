# GOAL_RUNNER.md

目的：为 WorldEngine `v0.2-post-closeout` goal campaign 提供 Codex App
`/goal` 路由说明。

本文是 campaign state machine。它不改变 v0.2 release status。是否允许
implementation 由每个 child package contract 控制，不由父级 campaign 单独授权。

## 边界

这些说明是给 agents 使用的 Codex App `/goal` prompt 和 campaign guidance。它们不是
WorldEngine runtime behavior，本文也不实现 automation controller。

Scheduling、orchestration、retry infrastructure 和 Codex role assignment 属于 Codex
环境或其他外部工具。此仓库只记录这些工具可消费的 deterministic package routing、
evidence requirements、scope guardrails 和 closeout state。

## 权威输入

运行任何 campaign goal 前，必须读取：

- `CURRENT_STATE.md`
- `CAMPAIGN_PLAN.md`
- `validation-master-plan.md`
- `README.md`
- `findings.md`
- active package 的 `README.md`、`intent.md`、`contract.md`、`plan.md` 和
  `review.md`
- active package 存在 `technical-design.md` 和 `test-plan.md` 时也读取它们
- package 有 execution report 或 template 时，读取对应文件
- `docs/iterations/AGENTS.md`
- root `AGENTS.md`

如果这些文件与真实 git state 冲突，停止并记录为 `NEEDS_USER_INPUT`。唯一例外是：
冲突只来自 `CURRENT_STATE.md` 已明确标记为 non-current 的 reset 前 archived
evidence。

## 执行模式

默认模式：用户说 `完成 v0.2-post-closeout` 时运行 full campaign。

- 从 `CURRENT_STATE.md` 开始。
- 按 `CAMPAIGN_PLAN.md` 执行 active child package。
- 只有当前 child 达到 `PACKAGE_COMPLETE`，或达到 next child contract 明确接受的其他
  exit status 后，才继续下一个 child。
- 遇到 `BLOCKED`、`FAILED`、`FOLLOW_UP_REQUIRED`、`NEEDS_USER_INPUT`、source
  conflict、evidence insufficiency 或 out-of-scope changes 时停止。

Single child mode：

- 仅当用户点名某个 child package，或明确说不要运行 full campaign mode 时使用。
- 只处理一个 package。
- package 达到最终 route status 后立即停止。

Full child-package cycle mode：

- 用户可以为 child package goal 明确请求 `full child-package cycle`。
- 在该模式下，Codex 可以在同一个 goal 内执行 adaptive child package cycle
  选出的所有 gates：documentation work、read-only evaluator 或 subagent
  review、允许时记录 `implementation_authorized: yes`、implementation、
  verification、code review、repair loops 和 closeout。
- 这不允许跳过 gates。含义是把 gates 放在同一个 goal 内执行，而不是要求用户用多次
  prompt 分别驱动。
- 如果 package contract、current routing state 或 Implementation Authorization
  禁止 implementation，该 goal 必须在 implementation 前停止，或路由为
  `NEEDS_USER_INPUT`。

## 路由类型

- `campaign-restart`
- `goal-entry`
- `gate-selection`
- `documentation-review`
- `review-closeout-plan`
- `implementation-execution`
- `validation-execution`
- `code-review`
- `evaluator-review`
- `repair-loop`
- `verification-escalation`
- `autonomous-review-execution`
- `final-bundle-closeout`

## Adaptive Child Package Cycle

不要盲目运行固定 phase list。对每个 child package，先判断 package shape 和 risk，
再选择满足 child contract、evidence requirements 和 stop conditions 的最简单 gate
集合。

始终运行这些 baseline gates：

1. 读取父级 routing docs 和 active child package docs。
2. 确认 package type、allowed files、forbidden files、required commands 和 final
   status vocabulary。
3. 将用户请求与 child contract、当前 git state 对照。
4. 在 `review.md` 中真实记录 command evidence、blockers 和 final status。
5. 写入任何 final status 前，运行 Closeout Consistency Gate。

Gate selection：

| Package shape | Required gates |
|---|---|
| Documentation-only or planning | Documentation update；routing 或 contract quality 有实质风险时运行 read-only documentation review；修复 P0 / P1 documentation findings；记录 closeout evidence；不做 implementation。 |
| Validation-only | Environment 和 command readiness check；运行 required validation commands 或记录具体 blocker；findings classification；closeout evidence；除非单独的 child contract 明确授权 repair，否则不做 implementation。 |
| Code or mixed | Documentation / contract gate；implementation authorization；scoped implementation；focused tests；code review 或 evaluator review；P0 / P1 repair loop；只有 contract 或 blast radius 要求时才运行 broader regression 或 E2E；closeout evidence。 |
| Autonomous validation | Independent review execution；command evidence 或 blocker evidence；P0 / P1 classification；recommendation；closeout evidence；除非 child contract 授权 repair，否则不修 implementation。 |
| Final bundle | 汇总 current evidence 和 findings disposition；只有为解决 evidence conflict 或缺失 proof 时才 rerun commands；不创建新的 implementation scope。 |

Subagent 和 evaluator 使用：

- 本 campaign 明确授权 `/goal` development mode 使用 subagent / evaluator
  checkpoints。
- 对 implementation-bearing 或 full child-package cycle work，必须运行
  `docs/iterations/AGENTS.md` 中定义的 mandatory checkpoints：documentation /
  contract evaluator、implementation-scope evaluator、code review、
  validation-evidence evaluator 和 closeout consistency review。
- 对 broad code changes、security / compatibility risk、mirror quality、release
  claims、autonomous validation，以及 dense concept-learning 或 research-synthesis
  work，使用 read-only subagents 或 evaluator passes。
- 只有 independent subtasks 能清晰拆分时，才使用 orchestrator-worker style。始终由
  一个 controlling goal 负责 synthesis、verification、conflict resolution 和 final
  status。
- 除非 package contract 要求 review record，不为 trivial docs-only changes 启动
  subagents。
- subagent findings 必须分类为 P0 / P1 / P2 / P3，并且必须 fix、带理由 downgrade、
  在允许时 carry，或记录为 blockers。
- 如果 required subagent / evaluator checkpoint 无法运行，停止为 `BLOCKED` 或
  `NEEDS_USER_INPUT`；不得静默降级为 optional。

Verification escalation：

- 先运行 child `test-plan.md`、execution plan 或 review template 指定的 focused
  checks。
- 只有 child contract、changed-file blast radius 或未解决的 evidence conflict 要求时，
  才升级到 broader backend、API smoke、E2E 或 autonomous validation。
- 不得声明未运行的检查已通过。如果 required check 无法运行，记录精确 blocker，并路由为
  `BLOCKED`、`FAILED` 或 `NEEDS_USER_INPUT`。

goal 可以多次循环 review、repair 和 verification。证据要求时可以调整所选 gates 的
顺序，但不得用措辞跳过 required gate。

## Implementation Authorization

父级 campaign 不全局授权 implementation changes。

只有以下条件全部满足时才允许 implementation：

- active child package contract 允许 implementation；
- required documentation gates 已通过；
- 对应 `review.md` 记录 `implementation_authorized: yes`；
- changed files 没有超出 child contract；
- closeout 前已记录 verification 和 review evidence。

除非 child contract 和 implementation gate 明确允许，否则禁止：

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

- `CAMPAIGN_READY`
- `RESTART_READY`
- `PACKAGE_COMPLETE`
- `REVIEW_READY`
- `NOT_EXECUTED_CURRENT_CAMPAIGN`
- `NOT_EXECUTED`
- `BLOCKED`
- `FAILED`
- `PASSED_WITH_P3`
- `NEEDS_USER_INPUT`
- `FOLLOW_UP_REQUIRED`
- `ARCHIVED_EVIDENCE_ONLY`

不要用措辞把 `blocked`、`failed`、`not executed` 或 archived evidence 转写成
`passed`。状态由 evidence 决定。

## Package 路由

当前默认路由：

```text
campaign-complete
```

campaign 已回退为 `unverified_restart`。历史结果继续作为 archived evidence 保留，但
除非当前 goal 重新运行或明确重新接受对应 gate，否则不得算作当前 campaign completion
evidence。当前 goal 已重新接受 `01-e2e-validation-plan`，并已用当前 campaign 的
backend、API smoke、Playwright availability 和 host-capable E2E evidence 重新执行
`02-e2e-validation-execution`。当前 goal 也已接受
`03-codex-autonomous-validation-plan`，且没有在 `03` 执行 autonomous validation。
`04-codex-autonomous-validation-execution` 中的 independent Codex autonomous
validation 已通过。`05-final-validation-bundle` 已记录 final assessment `passed`；
campaign 已完成。

重启顺序：

1. `01-e2e-validation-plan`
2. `02-e2e-validation-execution`
3. `03-codex-autonomous-validation-plan`
4. `04-codex-autonomous-validation-execution`
5. `05-final-validation-bundle`

不要在 `03` 执行 autonomous validation。

`03` 只审查 plan 是否足以交接给
`04-codex-autonomous-validation-execution`。

`04` 负责 independent Codex autonomous validation execution。

`05` 负责 final bundle synthesis 和 v0.4 proceed decision。

## 强制停止条件

出现以下情况时停止：

- required files 缺失；
- git state 与 package status 冲突，除非只是已明确 archived 的 reset 前 evidence；
- package 在没有 command evidence 或 explicit re-acceptance rationale 的情况下声明
  passed；
- command 无法运行且未记录 blocker；
- `findings.md` 仍有 unresolved P1/P2，而当前 package 试图声明 clean final pass；
- 需要 implementation，但 child contract 尚未授权；
- final bundle 在缺少 E2E / API / backend 和 Codex autonomous validation evidence
  的情况下试图允许 v0.4 继续。

## Closeout Consistency Gate

任何 child goal 写入 final status 之前，必须把实际 changed files 与对应
`review.md` 的 changed-files list 做对照。

必跑检查：

- `git status --short`
- `git diff --name-only`
- `git diff --check`

规则：

- 每个 created、modified 或 deleted 的 in-scope file，都必须列入对应
  `review.md` 的 changed-files section。
- 如果缺失的是 in-scope docs-only support file，在同一个 goal 内更新
  `review.md` 后继续。
- 如果出现未列出的 runtime、test、eval、external result、fixture、schema、
  API、worker、frontend 或 out-of-scope file，停止并记录为
  `NEEDS_USER_INPUT`。
- 不要要求用户手动修复 docs-only changed-file omissions。

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
- implementation authorization state；
- final status。

保持 `CURRENT_STATE.md` 与最新 package status 一致。
