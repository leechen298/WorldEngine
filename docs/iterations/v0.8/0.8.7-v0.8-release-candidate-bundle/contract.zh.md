# Contract

## Public Concepts

- `ReleaseCandidateBundle`：final closeout 前收集 reviewed v0.8 package evidence 的
  documentation artifact。
- `BoundedClaim`：由 named evidence 支撑、且受该 evidence boundary 限制的 claim。
- `Exclusion`：release-candidate bundle 有意不声明的 surface。
- `HandoffDecision`：取值为 `ready_for_final_closeout_review`、`blocked` 或
  `defer_pending_review`。

## Allowed Changes

Documentation stage：

- 创建或更新本 package docs 和中文 mirrors。
- 创建 `release-candidate-summary.md` 和 `release-candidate-summary.zh.md`。
- 记录 evidence references、bounded claims、exclusions、unresolved findings 和 review gates。
- 将 parent v0.8 status surfaces 更新为本 package ready-for-review。

Review stage after evaluator approval：

- 在本 package `review.md` 和 mirror 中记录 evaluator findings。
- 只有 review 通过时才更新 package status。
- 只有 package review 授权 handoff 时才更新 parent route。

## Forbidden Changes

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、
  migration、generated result、external repository、external validator、external application、
  deployment 或 `backend/worldengine/` files。
- 本 package 不运行新的 product validation 或 external validation。
- 不创建 final release claims。
- 不声明 external validation PASS、external consumer PASS、product readiness、frontend/E2E
  PASS、Agent smoke PASS、autonomous PASS、generation-quality PASS 或 final v0.8 readiness。
- 不把 historical v0.7 evidence 转换成 current v0.8 PASS evidence。
- 不包含 private external validator details、private repository paths、UI selectors、
  oracle internals、raw prompts、provider traces、secrets 或 concrete validation-world details。

## Required Bundle Surfaces

Release-candidate summary 必须包含：

- `0.8.0` through `0.8.6` package status matrix。
- evidence reference table。
- bounded claim table。
- compatibility table。
- exclusion list。
- unresolved finding table。
- handoff decision for `0.8.8-v0.8-final-closeout`。

## Closeout Rule

只有 documentation/contract review 没有 P1 或 blocking P2，且 release-candidate summary
没有暗示 final release 或 unsupported readiness claims，本 package 才能建议 handoff 到
`0.8.8-v0.8-final-closeout`。
