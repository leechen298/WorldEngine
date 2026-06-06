# Plan

## 有序执行步骤

1. 阅读治理文档：
   - `AGENTS.md`
   - `docs/iterations/AGENTS.md`
   - `docs/project-north-star.md`
   - `docs/product-model.md`
   - `docs/scope-boundaries.md`
   - `docs/roadmap.md`
   - `docs/iterations/v0.9/README.md`
   - `docs/iterations/v0.9/GOAL_RUNNER.md`
   - `docs/iterations/v0.9/CURRENT_STATE.md`
   - `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
   - `docs/iterations/v0.9/v0.9-plan.md`
   - `docs/iterations/v0.9/review.md`
2. 确认 active route 指向
   `0.9.0-v0.9-planning-and-v0.8-handoff-baseline-documentation-package-needed`。
3. 派发 read-only subagents/evaluators 执行 v0.9 gate 和 scope review。
4. 创建 `0.9.0` package document set 和中文镜像。
5. 同步父级 v0.9 status surfaces：
   - 将 `0.9.0` 标记为 `review complete`。
   - 选择 `0.9.1-provider-live-smoke-and-redaction-boundary` 为
     documentation-package-needed。
   - 保持 implementation、evidence execution、provider live-call、audit 和
     external validation authorization 关闭。
6. 运行 `test-plan.md` 中的 documentation checks。
7. 将 subagent/evaluator findings 与 source files 和 command evidence 对齐。
8. 更新 `review.md`，记录 changed files、commands、test results、compatibility
   review、scope review、findings 和 final assessment。
9. 在 implementation 前停止。交接给 `0.9.1` documentation-package creation。

## 阶段边界

Documentation phase：

- 可以创建或更新 package documents 和 parent v0.9 status surfaces。
- 可以运行 documentation consistency checks。
- 可以使用 read-only subagents/evaluators。

Implementation phase：

- 本包未授权。
- 必须等未来 implementation-bearing child package 拥有已 review 的 contract、
  technical design、test plan、plan 和 `review.md` authorization 后才能开始。

Evidence execution phase：

- 本包未授权。
- Provider live calls 和 checker-backed LLM-backed evidence 等待未来 package
  authorization。

## Stop Conditions

如出现以下情况则停止：

- 必需的 `0.9.0` package docs 或 mirrors 缺失。
- 父级 status surfaces 对 active child、route 或 authorization 存在冲突。
- 任何 runtime、schema、API、frontend、backend test、checker、fixture、
  migration、generated result、external repository、Validation Client、provider
  configuration 或 `backend/worldengine/` implementation file 需要被修改。
- 需要 live provider call 或 evidence execution。
- subagent/evaluator 报告无法在本 documentation-only scope 内修复的 P0/P1 或
  blocking P2。
- v0.8 handoff evidence 被描述为 v0.9 PASS evidence。
- LLM-backed testing docs 被描述为当前 PASS-capable coverage。
- provider secrets、raw prompts、raw responses、raw traces、private Agent memory、
  raw thought、chain-of-thought 或 hidden context 会被暴露。

## Review Update Step

closeout 前，更新本包 `review.md` 和 mirrors，记录：

- changed files。
- commands run。
- test results。
- subagent/evaluator evidence。
- compatibility review。
- scope review。
- unresolved findings。
- final assessment 和 handoff route。
