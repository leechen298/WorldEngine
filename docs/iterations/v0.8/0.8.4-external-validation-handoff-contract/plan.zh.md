# Plan

## Objective

创建完整 `0.8.4-external-validation-handoff-contract` documentation package，并准备
read-only documentation/contract review。

## Authoritative Inputs Read

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/0.8.1-minimum-working-state-contract/contract.md`
- `docs/iterations/v0.8/0.8.2-core-observable-surface-boundary/contract.md`
- `docs/iterations/v0.8/0.8.3-generation-runtime-agent-loop-readiness/review.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/contract.md`
- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/contract.md`
- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/contract.md`
- `docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair/review.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/current-implementation.md`
- `docs/glossary.md`

## Documentation Type

Documentation-only package。因为它定义 evidence rules、status taxonomy、compatibility
boundaries 和 future automation-consumption vocabulary，所以使用完整 mixed-package shape。

## Files To Create Or Update

Create：

- `README.md` / `README.zh.md`
- `intent.md` / `intent.zh.md`
- `contract.md` / `contract.zh.md`
- `technical-design.md` / `technical-design.zh.md`
- `test-plan.md` / `test-plan.zh.md`
- `plan.md` / `plan.zh.md`
- `review.md` / `review.zh.md`

只更新 parent v0.8 status surfaces：

- `docs/iterations/v0.8/README.md`
- `docs/iterations/v0.8/README.zh.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/v0.8-plan.zh.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/CURRENT_STATE.zh.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.8/review.md`
- `docs/iterations/v0.8/review.zh.md`

## Files Explicitly Out Of Scope

- runtime、schema、API、frontend、backend test、checker implementation、fixture、migration、
  generated result、external repository、external validator code、external application code 和
  `backend/worldengine/` files。
- `docs/contracts/`、`tools/testing/` 和 report/template files。

## Required Package Status Values

Review 前：

- package `Status: planned / ready for review`。
- `implementation_authorized: no`。
- `evidence_execution_authorized: no`。
- parent route `documentation-review-needed`。

Evaluator PASS 和 final docs checks 后：

- package `Status: review complete`。
- parent status `in progress / 0.8.5 child selected`。
- `0.8.5-core-working-state-smoke-evidence: selected / child docs not created`。
- implementation 和 evidence execution authorization 仍为 `no`。

## Allowed Changes

- 本 package 下的 documentation。
- Parent v0.8 route/status/review synchronization。

## Forbidden Changes

- 任何 implementation 或 test changes。
- 任何 external validator 或 external application content。
- 任何 private scenario、oracle、selector、transcript、screenshot、private path、provider
  trace、prompt、secret、concrete world、product data、reset/write API、persistence、
  migration 或 `backend/worldengine/` work。

## Review Gates

1. 运行 documentation shape、status、scope、text 和 formatting checks。
2. 请求 read-only documentation/contract evaluator review 0.8.4。
3. 修复任何 P1 或 blocking P2。
4. 在 `review.md` 记录 evaluator evidence 和 final commands。
5. 只有 checks 和 evaluator review 通过后，才推进 parent route。

## Verification Commands

- `git diff --check`
- required child docs and mirrors check。
- v0.8 parent/child status consistency check。
- changed-file scope guard。
- v0.8 Markdown whitespace check。
- forbidden old-status/pending-claim scan。
- 0.8.4 handoff private-detail and overclaim text scan。

## Open Questions Or Assumptions

- 本 package 是 documentation-only。Schema/checker/template implementation 如有需要，属于后续
  reviewed package。
- `external_validation` 可作为 future evidence class 被命名，但不是 current PASS evidence。

## Stop Conditions

遇到以下情况停止：

- handoff contract 需要 concrete external validation content。
- implementation files 变成必要。
- 需要 private validator details。
- PASS claim 需要 current-session evidence。
- parent 和 child status surfaces 无法保持一致。

## Handoff After Review

Review 后 hand off 给 `0.8.5-core-working-state-smoke-evidence`，用于创建 core-side
smoke/evidence package。本 package 不运行该 evidence。
