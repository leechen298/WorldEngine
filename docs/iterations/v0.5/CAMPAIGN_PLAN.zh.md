# 战役计划

状态：planned / ready for review

## 目标

以 review-gated `/goal` campaign 方式运行 v0.5，定义并实现 Memory and
Self-Continuity Substrate，同时避免把 WorldEngine 扩展成 application-specific
backend behavior。

## 0.5.0 已读取的权威输入

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.4/README.md`
- `docs/iterations/v0.4/CURRENT_STATE.md`
- `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/final-closeout.md`
- `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/review.md`
- `docs/iterations/v0.4/review.md`
- `docs/iterations/v0.4-post-closeout/README.md`
- `docs/iterations/v0.4-post-closeout/CURRENT_STATE.md`
- `docs/iterations/v0.4-post-closeout/review.md`
- `docs/testing/results/2026-05-31-v0.4-overall-product-capability-validation.md`
- `docs/testing/results/2026-05-31-v0.4-e2e-agent-test-expansion.md`

## 战役规则

- Active child package 是唯一 implementation scope。
- `0.5.0` 是 documentation-only，不得修改 implementation files。
- 每个 child 的 implementation authorization 初始都是 no。
- Mixed/code packages 必须先完成 documentation review，再 implementation。
- 历史 v0.4 evidence 只作为 handoff context。
- 任何 v0.5 runtime、API、E2E、build、Agent smoke、autonomous validation 或
  release claims 都需要 current-session command evidence。
- 中文镜像必须在 status、type、goal、scope、forbidden changes、compatibility
  requirements、findings 和 final assessment 语义上与英文一致。

## 计划子包序列

1. `0.5.0-v0.5-planning-and-continuity-boundary-baseline`
2. `0.5.1-memory-self-continuity-contracts`
3. `0.5.2-working-and-episodic-memory-substrate`
4. `0.5.3-memory-context-loop-integration`
5. `0.5.4-reflection-relationship-and-drift-contract-followup`
6. `0.5.5-v0.5-evidence-and-compatibility-audit`
7. `0.5.6-v0.5-release-candidate-bundle`
8. `0.5.7-v0.5-final-closeout`

## 子包间交接规则

- `0.5.0` 将已评审的 campaign structure 和 capability boundaries 交给 `0.5.1`。
- `0.5.1` 将 public concept 和 schema semantics 交给 `0.5.2`。
- `0.5.2` 只将 working 和 episodic memory substrate evidence 交给 `0.5.3`。
- `0.5.3` 将 bounded read-only memory context evidence 交给 `0.5.4`。
- `0.5.4` 将 relationship、self-summary、reflection 和 drift contract status 交给
  audit。
- `0.5.5` 将 evidence 和 compatibility review 交给 release candidate。
- `0.5.6` 将 release-candidate findings 交给 final closeout。
- `0.5.7` 只有在 evidence consistency 和 review gates 通过后，才能标记 final status。

## 战役退出标准

只有满足以下条件时，v0.5 才可标记为 `final / closeout complete`：

- 所有 active child packages 均 review complete，或按 contract 明确 deferred。
- Implementation-bearing children 记录 current-session command evidence。
- Compatibility review 确认 v0.4 loop/API surfaces 保持兼容，或只由已评审 contracts
  以 additive 方式改变。
- Scope review 确认没有 concrete demo-world、external validation internal、
  frontend product behavior、migration、projection app、generation 或
  `backend/worldengine/` work 混入。
- Unresolved findings 已分类，且没有未被明确接受并说明理由的 P1/P2。

## 停止条件

遇到以下情况时，必须在 implementation 或 closeout 前停止：

- Active package docs 缺少 required files 或 mirrors。
- 必需 subagent/evaluator checkpoint 不可用，或报告 blocking P1/P2。
- Implementation 触及 active package contract 外的文件。
- Verification commands 失败，且 package 无法诚实记录 pass evidence。
- README、current state、plan、review 和 closeout docs 之间出现 status drift。
