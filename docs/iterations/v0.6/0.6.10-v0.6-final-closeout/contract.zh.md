# 合同

状态：final / closeout complete

implementation_authorized: no

## 范围

本 package 是 documentation-only final closeout。只有 current-session final evidence
和 closeout consistency review 通过后，它才可以更新 final v0.6 status surfaces 和
roadmap status。

## 允许文件

- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/` 下的文件
- Parent v0.6 status/review documents：
  - `docs/iterations/v0.6/README.md`
  - `docs/iterations/v0.6/README.zh.md`
  - `docs/iterations/v0.6/CURRENT_STATE.md`
  - `docs/iterations/v0.6/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.6/GOAL_RUNNER.md`
  - `docs/iterations/v0.6/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.6/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.6/v0.6-plan.md`
  - `docs/iterations/v0.6/v0.6-plan.zh.md`
  - `docs/iterations/v0.6/review.md`
  - `docs/iterations/v0.6/review.zh.md`
- `docs/roadmap.md` 和 `docs/roadmap.zh.md`，仅在 final evidence 通过后做 status
  synchronization。
- root `README.md` 和 `README.zh.md`，仅在 final evidence 通过后同步 final status、
  capability 和 evidence。

## 禁止文件

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- migrations、fixtures、generated output、external repositories、concrete world
  content 和 product demo files。

## 允许的最终声明

如果所有 final checks 通过，v0.6 可以声明：

- 已评审的 World Generation v1 contracts、schema/core、deterministic template
  generation、structured plan compilation、plan import boundaries、
  preview/regeneration/readiness API、dashboard preview 和 E2E smoke 对 v0.6 完成；
- current-session final backend regression、frontend unit/build 和 E2E smoke
  commands passed；
- v0.6 final closeout complete。

## 禁止的声明

Final closeout 不得声明：

- v0.7 external validation readiness；
- v0.8 projection readiness；
- 覆盖所有 WorldEngine surfaces 的 product readiness；
- Agent smoke 或 autonomous runner pass；
- subjective generation quality approval；
- live provider integration；
- concrete world/story/map/character content readiness。

## 评审门禁

只有满足以下条件后，本 package 才能标记 final：

- `0.6.9` 已 review complete；
- final verification commands 通过；
- final closeout records 已写入 exact results；
- status consistency checks 通过；
- closeout consistency evaluator 报告无 P1/P2 finding。
