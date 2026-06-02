# Goal Runner 执行器

状态：final / closeout complete；已记录 post-closeout code-review blockers

## Goal 入口

本 campaign 覆盖的自然语言 goals：

```text
完成 v0.7
启动 WorldEngine v0.7：External Validation Readiness / Projection Consumer Readiness
编写 v0.7 文档
```

当前 v0.7 route 对历史 `0.7.8` closeout 已完成。Closeout 后的新工作必须从新的 reviewed
package 或下一版本自己的 reviewed iteration package 开始。

Post-closeout code review 已在
`docs/testing/results/2026-06-02-v0.7-code-review.md` 记录 blocking findings。在这些 P1/P2
被修复，或被 active validation result 明确记录为 blockers 之前，不得把 complete route
报告为 clean pass、product PASS、external suite PASS 或 projection readiness PASS。

已知 post-closeout code-review blockers 应先路由到窄范围 v0.7 repair package，再尝试新的
clean-pass validation。

## Route Selection 路由选择

1. 读取 `CURRENT_STATE.md`。
2. 如果 `CURRENT_STATE.md` 不指向 child package，则停留在 parent documentation review。`v0.7-plan.md`
   只作为 planned package specs 的 roadmap 使用。
3. 如果 `CURRENT_STATE.md` 指向某个 child package，必须先创建或确认该 child 的完整 package document set，
   再按以下顺序读取：
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
4. 用 `CAMPAIGN_PLAN.md` 和 `v0.7-plan.md` 确认 package sequence 与 handoff rules。
5. 只有 active child package 的 `review.md` 记录 `implementation_authorized: yes` 后，才允许
   implementation。

`v0.7-plan.md` 本身不是 execution-approved child contract。它的 `0.7.x` sections 是 planned package
specs，必须在 implementation 前重新确认或改写为真实 child package docs。

## Documentation Stage Gate 文档阶段门禁

Documentation-only work 可以创建或更新 v0.7 iteration documents、parent package plans、roadmap specs、
review evidence、validation documentation、report templates、projection contract documentation 和中文镜像。

除非 reviewed active child package 明确授权对应文件类别，documentation-only work 不得修改 runtime、
schema、API、frontend、backend test、checker implementation、fixture、migration、external repository、
generated result 或 `backend/worldengine/` implementation files。

## Implementation Authorization Rule 实现授权规则

Implementation authorization 默认关闭。

对于 mixed 或 code children：

1. `contract.md`、`technical-design.md`、`test-plan.md` 和 `plan.md` 必须完成 review。
2. documentation/contract evaluator 必须报告没有 P0/P1，也没有 blocking P2。
3. `review.md` 必须记录 `implementation_authorized: yes`。
4. implementation 必须保持在 active child package contract 内。

如果 implementation 暴露设计缺口，停止 implementation，更新相关 documents，并且只有 updated
contract/design/test plan/execution plan reviewed 后才能恢复。

## Subagent / Evaluator Requirements 要求

v0.7 是带有未来 implementation-bearing children 的 `/goal` campaign，因此在可用并授权时必须使用
subagent/evaluator checkpoints：

1. 记录 `implementation_authorized: yes` 前进行 documentation/contract evaluator。
2. files changed 后、broad verification 前进行 implementation-scope evaluator。
3. focused tests 后、broader regression、E2E、API smoke、Agent smoke、autonomous checks、
   external validation 或 readiness claims 前进行 code-review evaluator。
4. 记录 tests、E2E、API smoke、Agent smoke、autonomous validation、external suite checks、build
   或 release claims passed 前进行 validation-evidence evaluator。
5. 任一 child 或 parent final assessment 前进行 closeout consistency evaluator。

documentation-only children 如果改变 process rules、package sequencing、evidence rules、
automation-consumption contracts、release status、validation templates、report schemas、projection
contracts、readiness taxonomy 或 mirror obligations，必须使用 read-only documentation evaluator。如果
subagent/evaluator tooling 不可用或未授权，记录缺失 checkpoint，并保持 `planned / ready for review`，
不能静默宣称 review complete。

如果 implementation 发现 active child 已批准的计划错误、不完整或不安全，必须停止 implementation。按需要更新
active child 的 `contract.md`、`technical-design.md`、`test-plan.md`、`plan.md` 和 `review.md`，并且只有
updated package reviewed 后才能继续。不得因为 parent roadmap 已列出顺序，就继续执行过期计划。

## Reporting Rules 报告规则

- 历史 v0.6 evidence 只能作为 handoff evidence。
- 没有 current-session command evidence 时，不得标记 v0.7 runtime、API、frontend、E2E、build、
  Agent smoke、autonomous validation、external validation、projection readiness、product readiness、
  generation quality 或 release behavior 已通过。
- 在 `review.md` 记录 exact commands、exit status、pass counts、skipped checks、blockers、artifact
  paths 和 rationale。
- 区分 `contract ready`、`report format ready`、`core-side compatibility ready`、`external suite
  pass`、`projection consumer contract ready`、`skipped`、`blocked` 和 `out of scope`。
- P1 阻塞 implementation 或 closeout。
- unresolved P2 阻塞 final status，除非 active package contract 和 review 明确接受。
- P3 只能带明确 handoff 保留。

## Scope Stop Conditions 范围停止条件

遇到以下情况必须停止并记录 blocker：

- active child 授权前修改 runtime/schema/API/frontend/test/checker implementation。
- 添加 concrete external validation world data、seed data、characters、locations、resources、story
  rules、private transcripts、UI selectors、hidden reset APIs、private oracle details 或
  application-specific backend logic。
- 实现 first external projection application 或 product packaging behavior；该范围属于 v0.8。
- 在 reviewed v0.7 contract 外添加 durable persistence、migrations、live provider behavior 或 generated
  world execution。
- 在 `backend/worldengine/` 下新增 runtime features。
- 把 v0.6 historical evidence 当成当前 v0.7 PASS evidence。
- 绕过 required documentation、implementation authorization、evaluator 或 evidence gates。
- 不更新和 review active child package 就继续执行有问题的 child plan。
