# CURRENT_STATE.md

本文是 Codex App `/goal` 推进 `v0.2-post-closeout` campaign 时使用的当前路由快照。

本文刻意保持简短。历史证据仍保留在各 package report 中，但新的 `/goal` run 以本文
记录的 current campaign state 为准。

## 快照

current_mode: full_campaign_restart
parent_package: v0.2-post-closeout
parent_status: CAMPAIGN_READY
campaign_verification_status: unverified_restart
v0.2_release_status: final / closeout complete
reopens_v0.2_implementation: no
implementation_changes_allowed: child_contract_controlled
one_sentence_goal: 完成 v0.2-post-closeout

## 当前进度

| Package | Current route status | Next action |
|---|---|---|
| `01-e2e-validation-plan` | `RESTART_READY` | 作为 child campaign 第一个 checkpoint 重新执行 planning review |
| `02-e2e-validation-execution` | `NOT_EXECUTED_CURRENT_CAMPAIGN` | `01` 达到 `PACKAGE_COMPLETE` 后重新执行 |
| `03-codex-autonomous-validation-plan` | `NOT_EXECUTED_CURRENT_CAMPAIGN` | `02` 达到 `PACKAGE_COMPLETE` 或记录 accepted blocker 后再 review-closeout |
| `04-codex-autonomous-validation-execution` | `NOT_EXECUTED_CURRENT_CAMPAIGN` | 仅在 `03` 达到 `PACKAGE_COMPLETE` 后执行 |
| `05-final-validation-bundle` | `NOT_EXECUTED_CURRENT_CAMPAIGN` | 仅在 `04` 达到 `PACKAGE_COMPLETE`、`BLOCKED` 或 `FAILED` 后填写 |

## 当前活动包

active_package: 01-e2e-validation-plan
next_action: restart-child-campaign-from-01
goal_mode: full_campaign
handoff_target: 02-e2e-validation-execution

## 证据策略

evidence_package: 02-e2e-validation-execution
archived_status: passed
evidence_date: 2026-05-29
evidence_branch: v0.3-lcoal
evidence_commit: dbffa069a5e74b6b1e6b60719152922595c60df6
current_campaign_counts_this_as_passed: no

archived_results:

- backend deterministic: passed, 115 passed
- API smoke: passed
- Playwright availability: passed
- configured browser E2E: passed, 6 passed

historical_blockers:

- earlier localhost bind blocker resolved by host-capable rerun

重启规则：

- archived results 不能算作当前 campaign 的完成证据。
- archived evidence 必须保留，供审计和对比使用。
- 新的 `/goal` 工作必须根据 `GOAL_RUNNER.md` 和 `CAMPAIGN_PLAN.md` 重新执行，
  或明确重新接受每个 child package gate。

## 已知未关闭 findings

- `v0.2-post-closeout-P2-001`：中文镜像过于 English-heavy。
  clean final closeout 前必须解决、带理由降级，或在 final bundle 中明确承接。

## 冲突规则

如果本文与 package `review.md`、execution report、`findings.md` 或真实 git state
冲突，且冲突来自 reset 前的 archived evidence，则以本文的 current campaign state
为准。其他冲突一律停止并记录为 `NEEDS_USER_INPUT`。
