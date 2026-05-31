# 0.6.9 v0.6 发布候选包

状态：review complete

implementation_authorized: no

类型：documentation-only

## 目标

基于已评审的 implementation evidence 和 `0.6.8` evidence/compatibility audit，
准备 v0.6 release-candidate bundle。本 package 不声明 final release、product
readiness、external validation readiness、projection readiness、autonomous
validation 或 generation quality。

## 必读材料

- `docs/iterations/v0.6/0.6.8-v0.6-evidence-and-compatibility-audit/review.md`
- `docs/iterations/v0.6/0.6.8-v0.6-evidence-and-compatibility-audit/technical-design.md`
- `0.6.0` 到 `0.6.7` 的 child review 文件
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`

## 允许变更

- 本 package documentation 及中文 mirrors。
- 只反映 release-candidate routing 的 parent v0.6 status surfaces。
- Release-candidate evidence summaries、checklists、finding classification 和
  handoff text。

## 禁止变更

- Runtime、schema、API、frontend、backend test、fixture、migration、generated
  output、external repository 或 `backend/worldengine/` implementation files。
- 新 generation behavior 或新的 validation checkers。
- Final closeout status。
- 未运行的 validation、product readiness、external validation readiness、
  projection readiness、autonomous validation 或 generation quality claims。

## 发布候选范围

Release candidate 是一个 documentation bundle，用于在 final closeout 前让已评审的
v0.6 evidence 易于检查。它可以说明已评审的 v0.6 packages 提供 deterministic
generation、structured planning、plan-import boundaries、preview metadata/API、
regeneration/readiness API、dashboard generation preview、E2E smoke 和 audited
compatibility evidence。

它必须同时明确 exclusions：v0.6 不声明 external validation-world readiness、
projection app readiness、full autonomous runner coverage、concrete product
readiness 或 subjective generation quality。

## 退出标准

- 必需 package docs 和 `.zh.md` mirrors 存在。
- `0.6.8` 已 review complete，且没有 unresolved P1/P2 finding。
- Release-candidate checklist 完整且有 evidence 支撑。
- Read-only release-candidate evaluator 报告无 P1/P2 finding。
- Parent status surfaces 可以在不授权 implementation 的情况下交接给
  `0.6.10-v0.6-final-closeout`。
