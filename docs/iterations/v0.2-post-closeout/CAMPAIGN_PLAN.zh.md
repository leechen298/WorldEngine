# Campaign Plan

状态：`campaign complete / passed`
类型：Codex `/goal` campaign plan

## 目的

`CAMPAIGN_PLAN.md` 定义以下 durable goal 的 child-package 顺序：

```text
完成 v0.2-post-closeout
```

本 campaign 遵循 Codex `/goal` 的使用方式：一个目标、权威输入、可重复的验证循环、
checkpoint 证据，以及明确停止条件。`GOAL_RUNNER.md` 是 goal runner，
`CURRENT_STATE.md` 是当前路由来源。

## 边界

本文是 Codex App `/goal` campaign guidance。它不定义、也不实现 WorldEngine runtime
behavior，并且不是 automation-controller implementation。

Scheduling、orchestration、retry infrastructure 和 Codex role assignment 不属于
WorldEngine，由 Codex 环境或其他外部工具负责；这些外部工具可以消费本文中的 package
specs、evidence rules 和 closeout records。

## 当前重启位置

本 campaign 正从 `unverified_restart` 的 reset 状态继续推进。

历史 validation evidence 仍保留在 package reports 中。当前 `/goal` run 已重新执行
`02-e2e-validation-execution`，并已接受
`03-codex-autonomous-validation-plan`。`04-codex-autonomous-validation-execution`
中的 independent Codex autonomous validation 已通过；campaign 现在路由到
`05-final-validation-bundle` 并已关闭。

## Campaign Objective

从当前 active child package 开始，完成 `v0.2-post-closeout` validation campaign，
直到 final bundle closeout。

本 campaign 必须：

- 保持 v0.2 release status 为 final / closeout complete；
- 避免 application-specific 或 demo-world implementation drift；
- 保留历史 evidence；
- 任何当前 pass claim 都必须有 current-session command evidence；
- active child 要求 review，或 risk 需要 independent evaluation 时，使用 read-only
  subagent 或 evaluator review；
- 前进前修复 P0 / P1 findings；
- unresolved P2/P3 必须 fix、带理由降级，或明确承接；
- evidence 缺失时停止，不得编造成功状态。

## Child Sequence

| Order | Child package | Current status | Required exit before next child |
|---|---|---|---|
| 1 | `01-e2e-validation-plan` | `PACKAGE_COMPLETE` | current-campaign planning review 已重新接受 |
| 2 | `02-e2e-validation-execution` | `PACKAGE_COMPLETE` | 当前 campaign 的 backend、API smoke、Playwright availability 和 host-capable E2E evidence 已通过 |
| 3 | `03-codex-autonomous-validation-plan` | `PACKAGE_COMPLETE` | autonomous validation plan 已接受；本 package 未执行 autonomous validation |
| 4 | `04-codex-autonomous-validation-execution` | `PACKAGE_COMPLETE` | independent Codex autonomous validation 已通过 |
| 5 | `05-final-validation-bundle` | `PACKAGE_COMPLETE` | final campaign status 已记录为 `passed` |

默认 campaign progression 只有在 active child 达到 `PACKAGE_COMPLETE`，或达到 next
child contract 明确接受的状态后，才继续前进。遇到 `BLOCKED`、`FAILED`、
`FOLLOW_UP_REQUIRED`、`NEEDS_USER_INPUT`、evidence insufficiency 或 source
conflict 时停止。

## Adaptive Child Cycle

对每个 child package，Codex 必须按 package type、contract 和 risk 选择 gates，
而不是机械执行固定 phase list。目标是在保持 campaign autonomous 的同时，避免增加不必要的
agent 复杂度。

每个 child 都必须运行的 baseline gates：

1. 读取父级 `CURRENT_STATE.md`、`GOAL_RUNNER.md`、本文、父级 `README.md`、
   `findings.md`，以及 active child package documents。
2. 确认 child contract、package type、allowed files、forbidden files、required
   commands 和 exit criteria。
3. 将请求的工作与当前 git state 对照。
4. 运行 `GOAL_RUNNER.md` 中的 Closeout Consistency Gate。
5. 按需更新 child `review.md`、父级 `CURRENT_STATE.md` 和 `findings.md`。

Workflow selection：

| Child type | Selected workflow |
|---|---|
| Planning or documentation-only | Draft / update docs；contract 或 routing evidence 有实质影响时运行 read-only documentation review；修复 P0 / P1 documentation findings；close out。 |
| Validation execution | 运行 required commands 或记录 concrete blockers；classify findings；除非单独授权，否则避免 implementation；close out。 |
| Code or mixed implementation | 通过 documentation / contract gate；记录 `implementation_authorized: yes`；在范围内 implementation；运行 focused verification；运行 evaluator 或 code review；修复 P0 / P1；按需升级到 broader tests 或 E2E；close out。 |
| Autonomous validation | 运行 independent Codex review 和 required commands；记录 findings 和 recommendation；除非 contract 授权，否则不 repair implementation；close out。 |
| Final validation bundle | 汇总 current evidence 和 findings disposition；只有解决 evidence conflict 或缺失 proof 时才 rerun；决定 final campaign result。 |

对于 implementation-bearing 或 full child-package cycle 的 `/goal` development-mode
child work，subagents 是 mandatory checkpoints。必须使用 `docs/iterations/AGENTS.md`
中的 documentation / contract、implementation-scope、code-review、
validation-evidence 和 closeout consistency checkpoints。

Subagents 仍然不是形式主义仪式：不得用 subagents 绕过 contract gates、在无 evidence
情况下写 final status，或把 scope 扩到 active child package 之外。只有 trivial
docs-only edits 不影响任何 gate、contract、status、claim、automation route 或 mirror
obligation 时，才可以跳过 subagents。

campaign 可以多次循环 review、repair 和 verification。证据需要时可以调整所选 gates 的
顺序，但不得用措辞跳过 required gate。

## Implementation Authorization

父级 campaign 不全局授权 implementation changes。

只有以下条件全部满足时才允许 implementation：

- active child package contract 允许 implementation；
- required documentation gates 已通过；
- `review.md` 记录 `implementation_authorized: yes`；
- changed files 没有超出 child contract；
- closeout 前已记录 verification 和 review evidence。

任一条件不满足时，child 必须保持 documentation-only，或停止为
`NEEDS_USER_INPUT`。

## Current Campaign Exit Criteria

本 campaign 已完成，`05-final-validation-bundle` 记录：

- `passed`

final bundle 必须汇总：

- current `02` validation evidence 或 accepted blocker；
- current `04` Codex autonomous validation evidence 或 accepted blocker；
- `findings.md` 中 open rows 的最终处置；
- v0.4 是否可以继续；
- commands run 和 commands not run；
- changed-file consistency check results；
- compatibility 和 scope review。

## Required Proof Commands

每个 child closeout 都必须运行：

```bash
git status --short
git diff --name-only
git diff --check
```

execution-bearing child packages 还必须运行自身 `test-plan.md`、execution plan 或
review template 指定的命令，除非 package 记录了具体 blocker。

## Hard Stops

出现以下情况时停止 campaign：

- required child package file 缺失；
- active child contract 与请求动作冲突；
- command 无法运行且未记录 blocker；
- package 在没有 current-session command evidence 或明确 re-acceptance rationale
  的情况下声明 passed；
- 出现未列出的 runtime、test、eval、external result、fixture、schema、API、worker、
  frontend 或 out-of-scope files；
- 需要 implementation，但 child package 尚未授权；
- final bundle 阶段仍有 unresolved P0 / P1 或未接受的 P2。
