# Plan

状态：planned / ready for review

## Objective

在 release-candidate packaging 前，为 reviewed v0.8 evidence 和 boundaries 准备
documentation-only audit package。

## Authoritative Inputs

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/review.md`
- `docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/review.md`
- `docs/iterations/v0.8/0.8.1-minimum-working-state-contract/review.md`
- `docs/iterations/v0.8/0.8.2-core-observable-surface-boundary/review.md`
- `docs/iterations/v0.8/0.8.3-generation-runtime-agent-loop-readiness/review.md`
- `docs/iterations/v0.8/0.8.4-external-validation-handoff-contract/review.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/review.md`
- `docs/testing/results/2026-06-02-v0.7-code-review.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.md`

## Steps

1. 创建完整 `0.8.6` package document set 和 Chinese mirrors。
2. 创建 `audit-report.md` 和 `audit-report.zh.md` templates。
3. 同步 parent v0.8 status 到 ready-for-review。
4. 运行 documentation checks 与 scope/status guards。
5. 请求 read-only documentation/contract review。
6. 若 review 通过，授权 documentation-only audit execution。
7. 根据 authorized audit checks 填写 audit report 和 package review。
8. Hand off 给 `0.8.7` 前，请求 validation/closeout review。

## Stop Conditions

- required input reviews 缺失时停止。
- audit execution 时任何 evidence reference 无法定位则停止。
- audit 需要 runtime、API、frontend、test、checker、fixture、migration、generated-result、
  external repo、external validator/app 或 `backend/worldengine/` changes 时停止。
- 任意 P1 或 blocking P2 会被隐藏或转换为 PASS 时停止。
- audit language 暗示 final v0.8 readiness、product readiness 或 external validation PASS
  时停止。

## Current Stage

仅 documentation stage。Review 前 audit execution、implementation 和 evidence execution 都未授权。
