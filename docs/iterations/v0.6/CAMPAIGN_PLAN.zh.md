# Campaign 计划

状态：in progress / 0.6.0 review complete

## 目标

以 review-gated `/goal` campaign 运行 v0.6，定义并实现 World Generation v1，同时避免把
WorldEngine 变成 application-specific backend，或把 concrete world content 存进 core
repository。

## 0.6.0 已读取的权威输入

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/CURRENT_STATE.md`
- `docs/iterations/v0.5/GOAL_RUNNER.md`
- `docs/iterations/v0.5/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.5/v0.5-plan.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/review.md`
- `backend/app/schemas/world_cell.py`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`

## Campaign 规则

- Active child package 是唯一 implementation scope。
- `0.6.0` 是 documentation-only，且不得修改 implementation files。
- 每个 child 的 implementation authorization 初始都是 no。
- Mixed/code packages 必须先完成 documentation review，才能 implementation。
- 历史 v0.5 evidence 只作为 handoff context。
- 在声明 v0.6 generation、runtime、API、frontend、E2E、build、Agent smoke、
  autonomous validation、generation-quality 或 release claims 前，必须有
  current-session command evidence。
- 中文镜像必须保持 status、type、goal、scope、forbidden changes、compatibility
  requirements、findings 和 final assessment semantics 等价。

## 计划子包序列

1. `0.6.0-v0.6-planning-and-generation-boundary-baseline`
2. `0.6.1-world-generation-contracts-and-template-semantics`
3. `0.6.2-template-catalog-and-deterministic-generator-core`
4. `0.6.3-structured-generation-plan-compiler`
5. `0.6.4-ai-assisted-generation-boundary-and-plan-import`
6. `0.6.5-generation-validation-metadata-and-preview-api`
7. `0.6.6-regeneration-and-runtime-readiness-integration`
8. `0.6.7-dashboard-generation-preview-and-e2e-smoke`
9. `0.6.8-v0.6-evidence-and-compatibility-audit`
10. `0.6.9-v0.6-release-candidate-bundle`
11. `0.6.10-v0.6-final-closeout`

## 跨子包交接规则

- `0.6.0` 将已评审的 campaign structure 和 generation boundaries 交接给 `0.6.1`。
- `0.6.1` 将 public generation concepts、schema semantics 和 authorization
  criteria 交接给 `0.6.2`。
- `0.6.2` 将 deterministic template generation evidence 交接给 `0.6.3`。
- `0.6.3` 将 structured-plan compiler evidence 交接给 `0.6.4`。
- `0.6.4` 将 AI-assisted plan-import boundaries 交接给 `0.6.5`。
- `0.6.5` 将 backend/API validation、metadata 和 preview evidence 交接给 `0.6.6`。
- `0.6.6` 将 regeneration 和 runtime-readiness evidence 交接给 `0.6.7`。
- `0.6.7` 将 dashboard preview 与 E2E smoke evidence 交接给 audit。
- `0.6.8` 将 evidence 和 compatibility review 交接给 release candidate。
- `0.6.9` 将 release-candidate findings 交接给 final closeout。
- `0.6.10` 只有在 evidence consistency 和 review gates 通过后，才能标记 final
  status。

## Campaign 退出标准

只有在满足以下条件时，v0.6 才能标记为 `final / closeout complete`：

- 所有 active child packages 均 review complete，或已由 contract 明确 deferred。
- Implementation-bearing children 记录 current-session command evidence。
- Compatibility review 确认 v0.5 loop/memory surfaces 和 v0.3 `WorldSpec`
  loader/runtime-context bridge 保持兼容，或只被已评审 contract 以 additive 方式改变。
- Scope review 确认没有混入 concrete demo-world、external validation internal、
  application-specific backend behavior、migration、projection app、live external
  AI-provider dependency 或 `backend/worldengine/` work。
- Generated `WorldSpec` data 已通过已评审 loader 和 runtime-readiness checks 验证。
- Unresolved findings 已分类，且没有未被明确接受的 P1/P2。

## 停止条件

如果出现以下情况，必须在 implementation 或 closeout 前停止：

- active package docs 缺少必需文件或 mirrors。
- required evaluator checkpoint 不可用，或报告 blocking P1/P2。
- implementation 触及 active package contract 之外的文件。
- verification commands 失败，且 package 无法诚实记录 pass evidence。
- generated examples 需要把 concrete demo-world content 放进本 repo。
- README、current state、plan、review 和 closeout docs 之间出现 status drift。
