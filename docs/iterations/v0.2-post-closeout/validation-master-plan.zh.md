# Validation Master Plan

状态：`campaign complete / passed`
类型：post-closeout goal campaign control plan

## 目的

本文控制 v0.2 post-closeout validation。它存在的原因是：v0.2 closeout 已完成，但剩余
validation 必须由 evidence 支撑，不能只从 release status 推断。

本 campaign 不改变 v0.2 release status。它建立并路由 validation runs 和 Codex
`/goal` child-package cycles 所需的 evidence channels。

本文是 Codex App `/goal` campaign guidance。它不定义 WorldEngine runtime behavior，
不实现 automation controller，也不会把 scheduling、orchestration、retry
infrastructure 或 Codex role assignment 放进此仓库。这些职责仍属于 Codex 环境或消费这些
deterministic specs 的外部工具。

## 当前路由快照

当前简短路由来源是 `CURRENT_STATE.md`；Codex App `/goal` 路由说明位于
`GOAL_RUNNER.md`；child sequence 和 campaign exit criteria 位于
`CAMPAIGN_PLAN.md`。

截至 2026-05-29：

- campaign 正从 `unverified_restart` reset 状态继续推进。
- `01-e2e-validation-plan` 在当前 campaign 中已完成。
- `02-e2e-validation-execution` 已用当前 campaign 的 backend deterministic、API
  smoke、Playwright availability 和 host-capable browser E2E evidence 完成。
- `03-codex-autonomous-validation-plan` 在当前 campaign 中已完成。
- `04-codex-autonomous-validation-execution` 在当前 campaign 中已完成。
- `05-final-validation-bundle` 在当前 campaign 中已完成，final assessment 为 `passed`。
- `findings.md` 中 `v0.2-post-closeout-P2-001` 已解决。

## 必读文件

validation planning 和后续 execution 必须读取：

- `docs/iterations/AGENTS.md`
- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/v0.2-release-candidate-bundle.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/review.md`
- `docs/scope-boundaries.md`
- `docs/external-fixture-boundary.md`
- `docs/validation-report-template.md`
- `README.md`

如果 execution 时必读文件不存在，必须记录到对应 review 中，不得凭空假设内容。

## 流程

0. Master campaign planning：定义 status taxonomy、stop conditions、severity
   rules 和 handoff order。
1. E2E / integration / API smoke plan：定义应检查内容，不执行检查。
2. E2E / integration / API smoke execution：记录 branch、commit、commands、
   results、blockers 和 P1/P2/P3 findings。
3. Codex autonomous validation plan：定义独立 reviewer instructions。
4. Codex autonomous validation execution and review：收集 independent review，
   并验证它是否具备 evidence。
5. Final validation bundle：汇总两条 validation line，并判断 unresolved findings
   是否阻塞后续 v0.4 work。

## Codex App Goal 路由规则

当用户说：

```text
完成 v0.2-post-closeout
```

Codex 应根据 `GOAL_RUNNER.md`、`CURRENT_STATE.md` 和 `CAMPAIGN_PLAN.md` 运行
full campaign mode。

默认下一条路由是：

```text
campaign-complete
```

用户点名某个 child package，或明确说不要运行 full campaign mode 时，仍可使用
single child mode。

`03` 不得执行 autonomous validation。`04` 负责 autonomous validation execution，
`05` 负责 final bundle synthesis。

## 结果状态

- `planned`：docs 已存在，execution 尚未开始。
- `ready for execution`：execution instructions 已完整且可 review。
- `executed`：execution 已运行，report fields 已填写。
- `passed`：validation evidence 支撑被检查 claims，且没有 unresolved P1/P2/P3。
- `passed with P3`：validation evidence 支撑被检查 claims，仅有已接受的
  non-blocking P3 findings。
- `blocked`：validation 无法完成，且 blocker 已记录。
- `failed`：validation 已完成，并发现 P1/P2 failure 或 claim conflict。
- `not executed`：没有执行 validation。
- `not executed in current campaign`：package 可能有历史 evidence，但 reset 后的当前
  campaign 尚未执行或重新接受它。
- `archived evidence only`：历史 evidence 仅供审计，不是当前 completion evidence。

## 严重级别规则

- P1：使 v0.2 release claim 失效、暴露 concrete demo-world regression、破坏
  compatibility，或证明 required validation report 不受 evidence 支撑。
- P2：缺少 required evidence、execution 不完整、blocker 不清楚，或存在会影响可靠
  validation 的 unsupported claim。
- P3：不阻塞的 documentation gap、polish issue，或不会改变 final assessment 的 future
  handoff。

P1 和 unresolved P2 会阻塞 clean validation result。P3 只有在明确列出并分配 follow-up
owner 或 version 后才可接受。

## 停止条件

出现以下情况时，停止 validation 并记录 `blocked` 或 `failed`：

- backend deterministic tests fail。
- API smoke fails。
- release claim 与 actual behavior 冲突。
- Codex autonomous reviewer reports P1。
- 出现 concrete demo-world regression。
- commands 无法运行且未记录 blocker。
- execution package 无法识别 branch 和 commit。
- report 在没有 current-session command evidence 的情况下声明成功。

## Branch 和 Commit 规则

不要硬编码 branch name。execution package 必须用以下命令记录真实 branch 和 commit：

```bash
git status --short --branch
git rev-parse HEAD
```

## E2E 可用性规则

Playwright configuration 的存在只能作为 E2E availability hint，不能证明 E2E suite
可运行。

execution 必须发现实际 install、start 和 test commands；如果 dependencies、
browser binaries、ports、services 或 environment variables 阻止 suite 运行，必须记录
blockers。

如果没有 runnable E2E framework，记录 E2E 为 not configured 或 blocked，然后使用
API smoke 加 backend integration tests 作为 fallback validation line。

## v0.4 继续规则

v0.4 可以继续，因为 final validation bundle 记录：

- `passed`
- `passed with P3`

如果 final validation bundle 记录 `blocked`、`failed` 或 `not executed`，bundle 必须
说明 v0.4 是被阻塞、可有条件继续，还是需要单独 approval。
