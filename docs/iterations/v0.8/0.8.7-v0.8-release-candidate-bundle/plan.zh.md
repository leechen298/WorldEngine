# Plan

状态：documentation-stage plan

## Objective

创建完整的 `0.8.7-v0.8-release-candidate-bundle` document package，并准备 read-only
review。

## Authoritative Inputs Read

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/0.8.6-v0.8-evidence-and-boundary-audit/audit-report.md`
- `docs/iterations/v0.8/0.8.6-v0.8-evidence-and-boundary-audit/review.md`

## Documentation Type

Documentation-only release-candidate package。因为它改变 release status、evidence rules、
package sequencing 和 automation-consumption contracts，所以 package 包含
`technical-design.md` 和 `test-plan.md`。

## Files To Create Or Update

Create：

- `README.md` and `README.zh.md`
- `intent.md` and `intent.zh.md`
- `contract.md` and `contract.zh.md`
- `technical-design.md` and `technical-design.zh.md`
- `test-plan.md` and `test-plan.zh.md`
- `plan.md` and `plan.zh.md`
- `review.md` and `review.zh.md`
- `release-candidate-summary.md` and `release-candidate-summary.zh.md`

只更新 parent v0.8 status surfaces 来记录本 package ready for review。

## Out Of Scope

- Runtime、schema、API、frontend、backend tests、checker implementation、fixtures、
  migrations、generated results、external repositories、external validator implementation、
  external app implementation、deployment 和 `backend/worldengine/`。
- New validation execution。
- Final v0.8 closeout。

## Execution Steps

1. 创建 package directory 和所有 required docs。
2. 起草带 bounded evidence references 的 release-candidate summary。
3. 将 parent status surfaces 更新为 `0.8.7 ready for review`。
4. 运行 `test-plan.md` 中的 documentation checks。
5. 在任何 review-complete status 前请求/读取 documentation evaluator feedback。
6. 如果 review 通过，按 evaluator recommendation 更新本 package review 和 parent route。

## Stop Conditions

如果 evidence references missing、status surfaces drift、private details appear、任何 summary
claim 暗示 final release，或任何 P1/P2 finding 阻断 release-candidate review，则停止。
