# Plan

## Objective

创建完整 `0.8.5-core-working-state-smoke-evidence` package，并在任何 evidence commands
运行前准备 documentation/contract review。

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
- `docs/iterations/v0.8/0.8.4-external-validation-handoff-contract/contract.md`
- `docs/testing/product-capability-validation-playbook.md`
- `docs/current-implementation.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`

## Documentation Type

Mixed validation package 的 documentation stage。本 package 在 review authorization 后可运行
evidence commands，但 drafting 阶段不运行 evidence，也不修改 implementation files。

## Files To Create Or Update

Create：

- `README.md` / `README.zh.md`
- `intent.md` / `intent.zh.md`
- `contract.md` / `contract.zh.md`
- `technical-design.md` / `technical-design.zh.md`
- `test-plan.md` / `test-plan.zh.md`
- `plan.md` / `plan.zh.md`
- `review.md` / `review.zh.md`

Package files 存在后，将 parent v0.8 status surfaces 更新为 `0.8.5 ready for review`。

## Files Explicitly Out Of Scope

- Documentation drafting 阶段不修改 runtime、schema、API、frontend、backend test、checker
  implementation、fixture、migration、generated result、external repository、external
  validator code、external application code 和 `backend/worldengine/` files。

## Required Package Status Values

Review 前：

- package `Status: planned / ready for review`。
- `implementation_authorized: no`。
- `evidence_execution_authorized: no`。
- parent status `in progress / 0.8.5 ready for review`。

Documentation/contract evaluator PASS 后：

- package 可变为 `ready for evidence execution`。
- `implementation_authorized: no`，除非 contract 已更新并 reviewed。
- `evidence_execution_authorized: yes`，仅限 exact `test-plan.md` commands。

## Allowed Changes

- 本 package 下的 documentation。
- Parent v0.8 route/status/review synchronization。
- Review 后才可运行 authorized evidence commands 并记录 evidence。

## Forbidden Changes

- Documentation drafting 阶段的 implementation changes。
- External validator 或 external application execution。
- Product-specific validation data。
- 未 review 的 result artifacts。
- 把 skipped、blocked、out-of-scope、historical 或 documentation evidence 过度声明为 PASS。

## Review Gates

1. 创建 full docs 和 mirrors。
2. 运行 documentation shape/status/scope/text guards。
3. 请求 read-only documentation/contract evaluator 检查 scope、command matrix、authorization、
   non-claims 和 handoff compatibility。
4. 修复 P1/blocking P2 findings。
5. 记录 review results；如果 approved，记录 bounded evidence execution authorization。

## Verification Commands

Documentation stage：

- `git diff --check`
- required child docs and mirrors check。
- parent/child status consistency check。
- changed-file scope guard。
- v0.8 Markdown whitespace check。
- command-matrix and overclaim scans。

Evidence stage after review：

- 仅运行 `test-plan.md` 中列出的 exact commands。

## Stop Conditions

Evidence execution 前遇到以下情况停止：

- documentation/contract evaluator 报告 P1 或 blocking P2。
- command matrix 未覆盖 required core surfaces 或未分类 gaps。
- evidence 需要 private external validation data。
- 必须修改 product code 才能让 validation pass。
- external validator 或 external application execution 变成必要。

## Handoff After Review

如果 documentation review 通过，hand off 给 exact authorized commands 的 evidence execution。
如果后续 evidence passed 或 blockers 已记录，hand off 给
`0.8.6-v0.8-evidence-and-boundary-audit`。
