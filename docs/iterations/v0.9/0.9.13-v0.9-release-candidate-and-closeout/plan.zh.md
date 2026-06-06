# Plan

英文镜像：`plan.md`。

## Objective

基于当前 evidence，将 v0.9 作为 reviewed BLOCKED release candidate close。

## Authoritative Inputs

- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/review.md`
- `docs/testing/results/2026-06-06-llm-backed-lifecycle-validation.md`
- `test-results/agent-autonomous/20260606T142210+0800-llm-backed-full-lifecycle/result.json`

## Steps

1. 创建 0.9.13 package document set。
2. Review 后将 parent route/status docs 更新为 `final / blocked`。
3. 重新验证 package completeness 和 saved-result evidence。
4. 运行 whitespace/status consistency checks。
5. final closeout 前请求 read-only evaluator review。

## Stop Conditions

- 任何 parent doc 声明 provider live PASS、external validation PASS、product readiness 或
  LLM-backed full lifecycle PASS。
- 缺少任何 required package file 或 mirror。
- saved BLOCKED result 不再通过验证。
- read-only evaluator 发现 blocking P1/P2。
