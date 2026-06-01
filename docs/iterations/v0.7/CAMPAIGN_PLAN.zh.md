# Campaign Plan 文档

状态：planned / ready for review

## 目标

把 v0.7 作为 review-gated `/goal` campaign 运行，通过 public contracts、redacted reports、
readiness manifests 和 compatibility evidence，让 WorldEngine 准备好被 external validation suites
和 projection consumers 使用，同时避免把 core repository 变成 external validation app、projection
product 或 application-specific backend。

## 父级文档已读取的权威输入

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/external-fixture-boundary.md`
- `docs/contracts/external-fixture-runner-contract.md`
- `docs/validation-report-template.md`
- `docs/testing/product-capability-validation-playbook.md`
- `docs/testing/test-documentation-playbook.md`
- `docs/testing/code-review-playbook.md`
- `docs/current-implementation.md`
- `docs/glossary.md`
- `docs/releases/v0.6.md`
- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/GOAL_RUNNER.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.6/v0.6-plan.md`

## Campaign 规则

- v0.7 parent package 是当前唯一权威入口。
- 当前没有 active 或 execution-approved child package。
- `v0.7-plan.md` 中 planned `0.7.x` entries 只是 roadmap-level planned package specs，不授权
  implementation，也不是不可变 execution script。
- 未来 child package 开始前，必须创建或确认该 child 的完整 document set，并完成 review gate。
- 每个 child 的 implementation authorization 初始为 no。
- mixed/code packages 必须先完成 documentation review，再进入 implementation。
- 历史 v0.6 evidence 只能作为 handoff context。
- 声明 v0.7 runtime、API、frontend、E2E、build、Agent smoke、autonomous validation、external
  validation、projection readiness、product readiness、generation-quality 或 release claims 前，必须有
  current-session command evidence。
- 中文镜像必须保留 status、type、goal、scope、forbidden changes、compatibility requirements、
  findings 和 final assessment 的语义。
- Readiness claims 必须区分 contract readiness、report format readiness、core-side compatibility
  readiness、actual external suite PASS 和 out-of-scope checks。

## Planned Child 顺序

1. `0.7.0-v0.7-planning-and-external-validation-boundary-baseline`
2. `0.7.1-public-validation-and-projection-contracts`
3. `0.7.2-validation-report-schema-and-redaction-checker`
4. `0.7.3-contract-bundle-and-readiness-manifest`
5. `0.7.4-projection-consumer-read-model-contracts`
6. `0.7.5-quality-regression-and-compatibility-evidence`
7. `0.7.6-v0.7-evidence-and-compatibility-audit`
8. `0.7.7-v0.7-release-candidate-bundle`
9. `0.7.8-v0.7-final-closeout`

这个顺序只是 route proposal。它可以被 reviewed child package documents 调整。不得用它跳过 active
child package review；如果 implementation 或 evidence 发现 design problem，也不得机械继续原计划。

## 跨 Child Handoff 规则

- 未来 `0.7.0` child 可以把 reviewed campaign structure、v0.6 handoff 和 external-consumer boundaries 交给
  `0.7.1`。
- 未来 `0.7.1` child 可以把 public readiness concepts、report semantics、projection consumer boundaries 和
  authorization criteria 交给 `0.7.2`。
- 未来 `0.7.2` child 可以把 report schema/checker 与 redaction evidence 交给 `0.7.3`。
- 未来 `0.7.3` child 可以把 public contract bundle 和 readiness manifest semantics 交给 `0.7.4`。
- 未来 `0.7.4` child 可以把 projection consumer read-model contracts 和任何已授权 implementation evidence 交给
  `0.7.5`。
- 未来 `0.7.5` child 可以把 regression 与 compatibility evidence 交给 audit。
- 未来 `0.7.6` child 可以把 evidence 和 compatibility review 交给 release candidate。
- 未来 `0.7.7` child 可以把 release-candidate findings 交给 final closeout。
- 未来 `0.7.8` child 只有在 evidence consistency 和 review gates 通过后，才可以标记 final status。

## Campaign Exit Criteria 出口标准

只有满足以下条件，v0.7 才能标记为 `final / closeout complete`：

- 所有 active child packages 都 review complete，或被 contract 明确 deferred。
- implementation-bearing children 记录 current-session command evidence。
- compatibility review 确认 v0.6 generation、v0.5 memory、v0.4 Agent loop 和 v0.3 `WorldSpec`
  loader/runtime-context bridge 保持兼容，或仅被 reviewed contracts 以 additive 方式修改。
- scope review 确认没有 concrete validation world、external oracle internal、UI selector、hidden
  reset API、application-specific backend behavior、migration、first projection app、live provider
  dependency 或 `backend/worldengine/` work 混入。
- redacted report 和 projection consumer claims 均由 current-session schema/checker/API/test
  evidence 支撑，前提是这些 claims 属于当前 scope。
- unresolved findings 已分类，且没有未被明确接受的 P1/P2。

## Stop Conditions 停止条件

出现以下情况时，在 implementation 或 closeout 前停止：

- active package docs 缺少 required files 或 mirrors。
- planned package 尚未转换成 current child package docs。
- required evaluator checkpoint 不可用，或报告 blocking P1/P2。
- implementation 触碰 active package contract 外的文件。
- implementation 发现 design gap，但 active child contract、design、test plan、plan 和 review 尚未更新并重新
  review。
- verification commands 失败，且 package 无法诚实记录 pass evidence。
- external validation examples 需要把 concrete external world content 放入本 repo。
- projection readiness 文本变成 v0.8 external projection application implementation。
- README、current state、plan、review 和 closeout docs 之间的 status surfaces 发生漂移。
