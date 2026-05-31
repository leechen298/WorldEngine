# 合同

状态：review complete

implementation_authorized: no

## 范围

本 package 是 documentation-only。它可以创建 v0.6 release-candidate bundle，并为
release-candidate routing 更新 v0.6 parent status surfaces。它不能修改
implementation files，也不能扩展 v0.6 product claims。

## 允许的发布候选声明

Bundle 可以说明 v0.6 对以下内容已有 reviewed current-session evidence：

- generation concept、template 和 schema semantics；
- deterministic template catalog generation；
- structured generation plan compilation；
- AI-assisted plan import boundaries，不包含 provider/runtime AI integration；
- validation metadata 和 preview API behavior；
- bounded regeneration 与 loader/runtime-context readiness checks；
- dashboard generation preview 和 focused E2E smoke；
- `0.6.8` 前的 compatibility audit，且无 unresolved P1/P2 finding。

## 禁止的声明

Bundle 不得声明或暗示：

- final release 或 closeout completion；
- 覆盖所有 WorldEngine surfaces 的 product readiness；
- external validation-world readiness；
- projection application readiness；
- Agent smoke 或 full autonomous runner coverage；
- generation-quality approval；
- live provider integration、prompt quality 或 network-backed AI behavior；
- concrete world、story、map、character、seed、fixture 或 demo application
  readiness。

## 允许文件

- `docs/iterations/v0.6/0.6.9-v0.6-release-candidate-bundle/` 下的文件
- Parent v0.6 docs：
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

## 禁止文件

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- fixture、migration、generated output、external repository 和 product demo files。

## 评审门禁

只有满足以下条件后，本 package 才能标记为 review complete：

- required English docs 和 Chinese mirrors 存在；
- `0.6.8` 已 review complete，且无 unresolved P1/P2 finding；
- release-candidate claims 和 exclusions 明确；
- documentation 与 status consistency checks 通过；
- read-only release-candidate evaluator 报告无 P1/P2 finding。

## 交接

如果 review complete，则交接给 `0.6.10-v0.6-final-closeout`，implementation
authorization 仍保持关闭。
