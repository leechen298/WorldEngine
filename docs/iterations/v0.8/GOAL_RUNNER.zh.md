# Goal Runner

状态：planned / ready for review

## Goal Entry

本 campaign 覆盖的自然语言目标包括：

```text
完成 v0.8
启动 WorldEngine v0.8：Minimum Proved Working WorldEngine / External Validation Readiness
编写 v0.8 文档
生成 v0.8 文档
```

当前 v0.8 route 是 parent documentation review。没有 active child package。
Implementation authorization 关闭。

v0.7 post-closeout code review 在
`docs/testing/results/2026-06-02-v0.7-code-review.md` 记录了 blocking findings。
除非受影响 blockers 已用 current-session evidence 修复，或 active v0.8 package 明确把
它们记录为 blockers，否则 v0.8 不得报告 clean pass、minimum working-state PASS、
external validation readiness PASS、product PASS 或 external consumer PASS。

## Route Selection

1. 读取 `CURRENT_STATE.md`。
2. 如果 `CURRENT_STATE.md` 没有指向 child package，保持在 parent documentation
   review。`v0.8-plan.md` 只能作为 planned package specs 的 roadmap。
3. 如果 `CURRENT_STATE.md` 指向 child package，先创建或确认该 child 的 complete
   package document set，然后按顺序读取：
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
4. 用 `CAMPAIGN_PLAN.md` 和 `v0.8-plan.md` 确认 package sequence 与 handoff rules。
5. Active child package review 记录 `implementation_authorized: yes` 前，不得
   implement。

`v0.8-plan.md` 本身不是 execution-approved child contract。它的 `0.8.x` sections
只是 planned package specs，必须在 implementation 前转换或重写为真实 child package
docs 并完成 review。

## Documentation Stage Gate

Documentation-only work 可以创建或更新 v0.8 iteration documents、parent package
plans、roadmap specs、review evidence、minimum working-state contract
documentation、external-validation boundary documentation、readiness taxonomy 和 Chinese
mirrors。

除非 reviewed active child package 明确授权文件类型，documentation-only work 不得修改
runtime、schema、API、frontend、backend test、checker implementation、fixture、
migration、external repository、generated result、external validation implementation 或
`backend/worldengine/` implementation files。

## Implementation Authorization Rule

Implementation authorization 默认关闭。

对于 mixed 或 code children：

1. `contract.md`、`technical-design.md`、`test-plan.md` 和 `plan.md` 必须 reviewed。
2. Documentation/contract evaluator 必须报告无 P0/P1，且无 blocking P2。
3. `review.md` 必须记录 `implementation_authorized: yes`。
4. Implementation 必须保持在 active child package contract 内。

如果 implementation 暴露设计缺口，停止 implementation，更新相关 documents，并仅在
updated contract/design/test plan/execution plan reviewed 之后恢复。

## Subagent / Evaluator Requirements

因为 v0.8 是包含未来 implementation-bearing children 的 `/goal` campaign，在可用且
被授权时使用 subagent/evaluator checkpoints：

1. 记录 `implementation_authorized: yes` 前，运行 documentation/contract evaluator。
2. 文件修改后、broad verification 前，运行 implementation-scope evaluator。
3. Focused tests 后、broader regression、E2E、API smoke、Agent smoke、autonomous
   checks、core-side readiness evidence 或 readiness claims 前，运行 code-review
   evaluator。
4. 记录 tests、E2E、API smoke、Agent smoke、autonomous validation、core-side
   readiness checks、build 或 release claims passed 前，运行 validation-evidence
   evaluator。
5. 任何 child 或 parent final assessment 前，运行 closeout consistency evaluator。

Documentation-only children 如果改变 process rules、package sequencing、evidence
rules、automation-consumption contracts、release status、validation templates、report
schemas、projection contracts、readiness taxonomy 或 mirror obligations，需要
read-only documentation evaluator。若 subagent/evaluator tooling 不可用或未授权，
记录 missing checkpoint，并保持 `planned / ready for review`，不要声明 review
complete。

## Reporting Rules

- Historical v0.7 和 v0.6 evidence 只能作为 handoff evidence 引用。
- 没有 current-session command evidence 时，不得把 v0.8 runtime、API、frontend、
  E2E、build、Agent smoke、autonomous validation、minimum working-state readiness、
  external validation readiness、external consumer validation、product readiness、
  generation-quality 或 release behavior 标记为 passed。
- 除非后续 package 和外部流程明确提供 redacted public evidence，否则不得记录 external
  validation PASS；当前 parent docs 不定义该流程。
- 在 `review.md` 中记录 exact commands、exit status、pass counts、skipped checks、
  blockers、artifact paths 和 rationale。
- 区分 `core contract ready`、`core observable surface ready`、`minimum
  working-state evidence ready`、`external validation handoff ready`、`external
  validation pass`、`skipped`、`blocked` 和 `out of scope`。
- P1 阻断 implementation 或 closeout。
- Unresolved P2 阻断 final status，除非 active package contract 和 review 明确接受。
- P3 只能通过 explicit handoff 继续携带。

## Scope Stop Conditions

如果任务会导致以下情况，停止并记录 blocker：

- active child 授权前修改 runtime/schema/API/frontend/test/checker implementation。
- 在 core repository 内实现 external validation function、external projection
  application、product UI、application state、application routing、product packaging、
  deployment 或 application-specific backend logic。
- 定义 external validator 如何连接、认证、运行 private scenarios、评估 oracle outcomes 或
  存储 external application state。
- 添加 concrete app worlds、external validation worlds、seed data、characters、
  locations、resources、story rules、private transcripts、UI selectors、hidden reset
  APIs、private oracle details、private runner state、private external repository
  paths 或 non-redacted external event payloads。
- 未经 active child authorization 添加 durable persistence、migrations、live provider
  behavior、generated-world active runtime execution，或 `backend/worldengine/` 下的新
  runtime features。
- 把 historical v0.7/v0.6 evidence 当成 current v0.8 PASS evidence。
- 做受影响 readiness claim 时忽略 v0.7 post-closeout P1/P2 blockers。
- 绕过 required documentation、implementation authorization、evaluator 或 evidence
  gates。
- Active child plan 存在问题时，不更新并重新 review 就继续执行。
