# Campaign Plan

状态：planned / ready for review

## Objective

以 review-gated `/goal` campaign 运行 v0.8：准备 WorldEngine 达到 minimum normally
working state，并暴露足够 public、generic 的 core-side surfaces，让独立的 external
validation function 可以判断 engine 是否正常工作。

本 campaign 不得把 core repository 变成 external validator、external projection
application、product-specific backend，或 concrete validation worlds 的存放位置。

## Authoritative Inputs Read For Parent Drafting

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.7/README.md`
- `docs/iterations/v0.7/CURRENT_STATE.md`
- `docs/iterations/v0.7/GOAL_RUNNER.md`
- `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.7/v0.7-plan.md`
- `docs/testing/results/2026-06-02-v0.7-code-review.md`
- `docs/current-implementation.md`
- `docs/glossary.md`

## Campaign Rules

- Parent v0.8 package 保持 authoritative campaign entrypoint。
- 当前没有 active v0.8 child package。
- `v0.8-plan.md` 中的 planned `0.8.x` entries 是 roadmap-level planned package
  specs，不授权 implementation，也不是 immutable execution scripts。
- 每个 child 的 implementation authorization 初始为 no。
- Mixed/code packages 必须先完成 documentation review，才能 implementation。
- Historical v0.7 和 v0.6 evidence 只能作为 handoff context。
- v0.7 post-closeout P1/P2 blockers 必须被 repaired、route 到 narrow repair，或在
  affected v0.8 readiness claim 前记录为 blockers。
- 声明 v0.8 runtime、API、frontend、E2E、build、Agent smoke、autonomous validation、
  minimum working-state PASS、external validation readiness、product readiness、
  generation-quality 或 release claims 前，必须有 current-session command evidence。
- Chinese mirrors 必须保持 status、type、goal、scope、forbidden changes、
  compatibility requirements、findings 和 final assessment semantics。
- Readiness claims 必须区分 core contract readiness、core observable surface
  readiness、minimum working-state evidence、external validation handoff readiness、
  external validation PASS、blocked、skipped 和 out of scope。

## Planned Child Sequence

1. `0.8.0-v0.8-planning-and-v0.7-handoff-baseline`
2. `0.8.1-minimum-working-state-contract`
3. `0.8.2-core-observable-surface-boundary`
4. `0.8.3-generation-runtime-agent-loop-readiness`
5. `0.8.4-external-validation-handoff-contract`
6. `0.8.5-core-working-state-smoke-evidence`
7. `0.8.6-v0.8-evidence-and-boundary-audit`
8. `0.8.7-v0.8-release-candidate-bundle`
9. `0.8.8-v0.8-final-closeout`

该 sequence 是 route proposal，可由 reviewed child package documents 修订。不得用它跳过
active child package review；若 implementation 或 evidence 暴露 design problem，不得机械继续。

## Cross-Child Handoff Rules

- `0.8.0` hand off reviewed campaign structure、v0.7 handoff-risk handling、
  minimum working-state boundaries 和 external-validation boundaries 给 `0.8.1`。
- `0.8.1` hand off readiness claim taxonomy 和 authorization criteria 给 `0.8.2`。
- `0.8.2` hand off generic core observable surface semantics 给 `0.8.3`。
- `0.8.3` hand off core generation/runtime/Agent-loop readiness boundaries 和 evidence
  needs 给 `0.8.4`。
- `0.8.4` hand off external-validation handoff semantics，但不定义 external validator
  implementation。
- `0.8.5` hand off core-side smoke 和 compatibility evidence 给 audit。
- `0.8.6` hand off evidence 和 boundary review 给 release candidate。
- `0.8.7` hand off release-candidate findings 给 final closeout。
- `0.8.8` 只能在 evidence consistency 和 review gates 通过后标记 final status。

## Campaign Exit Criteria

v0.8 只有在以下条件满足时，才可标记 `final / closeout complete`：

- 所有 active child packages 都 review complete，或被 contract 明确 deferred。
- implementation-bearing children 记录 current-session command evidence。
- compatibility review 确认 v0.7 projection contracts、v0.6 generation、v0.5 memory、
  v0.4 Agent loop 和 v0.3 loader/runtime-context bridge 仍兼容，或只通过 reviewed
  contracts 做 additive changes。
- v0.7 post-closeout P1/P2 blockers 已用 current-session evidence 修复，或在 active
  v0.8 evidence 中记录为 blockers。
- scope review 确认没有 external validation implementation、external application
  implementation、product UI、concrete app data、private external repo path、UI
  selector、hidden reset API、private transcript、validation oracle internal、
  app-specific backend behavior、migration 或 `backend/worldengine/` work slip in。
- minimum working-state 与 external-validation handoff claims 在 in scope 时，有
  current-session schema/checker/API/test evidence 支撑。
- unresolved findings 已分类，且没有 P1/P2 在缺少 explicit accepted rationale 的情况下遗留。

## Stop Conditions

以下情况出现时，在 implementation 或 closeout 前停止：

- active package docs 缺 required files 或 mirrors。
- planned package 尚未转换成 current child package docs。
- required evaluator checkpoint 不可用，或报告 blocking P1/P2。
- implementation 触及 active package contract 外的文件。
- implementation 发现 design gap，但 active child contract、design、test plan、plan 和
  review 尚未更新并重新 review。
- verification commands fail，且 package 无法诚实记录 pass evidence。
- minimum working-state readiness text 变成 product readiness。
- external validation boundary text 变成 external validator implementation 或 external app
  implementation。
- concrete application data、private app internals、UI selectors、hidden reset APIs、
  external validator connection details、oracle internals 或 external repository details
  变成 required。
- 做 affected readiness claims 时忽略 v0.7 post-closeout blockers。
- README、current state、plan、review 和 closeout docs 之间 status surfaces drift。
