# 0.2.10 Legacy Boundary and Compatibility Review

状态：`review complete`

类型：`documentation-only`

英文版本：`README.md`

## 目标

准备一个可评审的 documentation-only package，用于在 v0.3 bridge work
之前明确 v0.1 runtime scaffold 与 v0.2 recursive schema foundation 之间的
兼容边界。

## 范围

本 package 在文档评审通过后会创建 legacy boundary 和 compatibility review
文档。它可以检查 current implementation docs、architecture docs、API docs、
active backend paths、frontend-facing behavior descriptions、legacy paths 和
已完成的 v0.2 reviews，但不能修改 runtime、schema、API、frontend、fixture、
migration 或 test implementation 文件。

兼容性缺口必须记录为 findings 或 v0.3 handoff constraints，不能通过未评审的
implementation work 修复。

## 文档

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## 状态清单

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation-stage evidence complete
- [x] Legacy boundary docs complete
- [x] Compatibility review docs complete
- [x] Review complete

## 评审后计划交付物

- `docs/legacy-boundary.md`
- `docs/legacy-boundary.zh.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/compatibility-review.zh.md`
- 更新 `docs/iterations/v0.2/findings.md`，记录 compatibility gaps、status
  drift 或 v0.3 handoff risks。
- 本 package 在 `review.md` 和 `review.zh.md` 中记录 implementation evidence。

## 假设

- `backend/app/` 仍是 active backend code path。
- `frontend/` 仍是 active dashboard code path。
- `backend/worldengine/` 仍是 legacy 且未接入 active app，除非后续 reviewed
  iteration contract 改变该边界。
- v0.2 schema 和 event contracts 是 additive foundations，本 package 不会把它们
  加载到 v0.1 runtime scaffold 中。
- 本 package 保持 documentation-only；mixed scope 需要后续 reviewed contract
  update。

## 开放风险

- Current implementation docs 可能描述历史 v0.1 行为，其精确命令证据不一定是
  current-session evidence；compatibility review 必须把它标为 documented
  baseline，除非重新验证。
- v0.2 schema/event contracts 可能让人误以为 runtime bridge 已存在；本 package
  必须把这些期望保留为 v0.3 handoff constraints。
- Legacy path inspection 可能发现看似可用的 dormant code；本 package 必须区分
  active app wiring 和 legacy files。
