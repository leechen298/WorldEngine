# Plan

## Ordered Execution Steps

1. 读取治理文档：
   - `AGENTS.md`
   - `docs/project-plan.md`
   - `docs/project-north-star.md`
   - `docs/product-model.md`
   - `docs/scope-boundaries.md`
   - `docs/roadmap.md`
   - `docs/iterations/README.md`
   - `docs/iterations/AGENTS.md`
   - `docs/iterations/v0.10/README.md`
   - `docs/iterations/v0.10/GOAL_RUNNER.md`
   - `docs/iterations/v0.10/CURRENT_STATE.md`
   - `docs/iterations/v0.10/CAMPAIGN_PLAN.md`
   - `docs/iterations/v0.10/v0.10-plan.md`
   - `docs/iterations/v0.10/review.md`
2. 确认 active route 指向 `v0.10-parent-documentation-ready-for-review`。
3. 派出 read-only subagents/evaluators 做 v0.10 route 和 MVP campaign gate review。
4. 创建 `0.10.0` package document set 和中文镜像。
5. 同步 parent v0.10 status surfaces：
   - 将 `0.10.0` 标为 `review complete`。
   - 将 `0.10.1-mvp-public-manifest-and-debug-handoff` 选为
     documentation-package-needed。
   - 保持 implementation、evidence execution、provider live-call 和 external validation
     authorization 关闭。
6. 运行 `test-plan.md` 中的 documentation checks。
7. 将 subagent/evaluator findings 与 source files 和 command evidence 对齐。
8. 更新 `review.md`，记录 changed files、commands、test results、compatibility review、
   scope review、findings 和 final assessment。
9. 在 implementation 前停止。交接给 `0.10.1` documentation-package creation。

## Phase Boundaries

Documentation phase：

- 可以创建或更新 package documents 和 parent v0.10 status surfaces。
- 可以运行 documentation consistency checks。
- 可以使用 read-only subagents/evaluators。

Implementation phase：

- 本包不授权。
- 必须等未来 implementation-bearing child package 拥有 reviewed contract、technical
  design、test plan、plan 和 `review.md` authorization 后才能开始。

Evidence execution phase：

- 本包不授权。
- Provider live calls、checker saved-result generation、external validation 和 Validation
  Client flows 等待未来 package authorization。

## Stop Conditions

遇到以下情况停止：

- 缺少必需的 `0.10.0` package docs 或 mirrors。
- parent status surfaces 在 active child、route 或 authorization 上互相冲突。
- 任何 runtime、schema、API、frontend、backend test、checker、fixture、migration、
  generated result、external repository、Validation Client、provider configuration 或
  `backend/worldengine/` implementation file 需要被修改。
- 需要 live provider call、API smoke、E2E、autonomous validation、checker result 或
  external validation flow。
- subagent/evaluator 报告无法在 documentation-only scope 内修复的 P0/P1 或 blocking P2。
- v0.9 BLOCKED evidence 被描述成 v0.10 PASS evidence。
- secrets、raw prompts、raw responses、raw traces、private Agent memory、raw thought、
  hidden context 或 private evaluator data 会被暴露。

## Review Update Step

closeout 前，更新本 package `review.md` 和 mirrors，记录：

- changed files。
- commands run。
- test results。
- subagent/evaluator evidence。
- compatibility review。
- scope review。
- unresolved findings。
- final assessment and handoff route。
