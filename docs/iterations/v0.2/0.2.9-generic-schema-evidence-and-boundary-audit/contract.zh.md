# Contract

英文版本：`contract.md`

## 公开概念

- Evidence index：milestone-level document，将 active v0.2 claims 映射到
  source documents、package reviews、verification commands 和 status。
- Boundary audit：milestone-level document，检查 external consumer、concrete
  fixture、legacy directory、runtime compatibility 和 future-scope boundaries。
- Evidence status：`implemented`、`documented`、`tested`、`reviewed`、
  `planned`、`not implemented`、`historical artifact` 或 `finding`。
- Finding：带 priority 和 target package 的 unresolved evidence、boundary、
  compatibility 或 status issue。

## 兼容性约束

- Runtime behavior 不得改变。
- Schema behavior 和 validation behavior 不得改变。
- API response shapes 不得改变。
- Frontend behavior 不得改变。
- Fixture、migration 和 test implementation files 不得改变。
- `backend/app/` 保持 active backend code path。
- 除非 later reviewed package 改变该 boundary，`backend/worldengine/` 保持
  legacy。
- Documentation 必须区分 implemented behavior 与 planned 或 future-scope
  claims。

## 允许变更

- 新增 `docs/iterations/v0.2/evidence-index.md`。
- 新增 `docs/iterations/v0.2/evidence-index.zh.md`。
- 新增 `docs/iterations/v0.2/boundary-audit.md`。
- 新增 `docs/iterations/v0.2/boundary-audit.zh.md`。
- 更新 `docs/iterations/v0.2/findings.md`，用于新增、关闭或 retarget audit
  findings。
- 用 audit evidence 更新本 package 的 `review.md` 和 `review.zh.md`。
- 更新 v0.2 milestone index 和 plan 中的 0.2.9 status fields。
- 运行 read-only repository searches、path checks 和 documentation sanity
  checks。

## 禁止变更

- 不修改 runtime services、world state、modules、event log behavior、archive
  behavior、agent behavior、persistence、API routes 或 app assembly。
- 不修改 schema implementation files。
- 不修改 frontend files。
- 不修改 tests 或 fixtures。
- 不增加 migrations。
- 不修改 `backend/worldengine/`。
- 不实现 WorldSpec loading、runtime bridge、generation、projection、agent
  loop、memory、self-continuity、resolver 或 causality behavior。
- 不增加 external repositories 或 external validation internals。
- 不增加 concrete external-world names、characters、locations、roles、
  resources、story rules、seed data、UI selectors、private runner state 或
  application-specific backend logic。
- 不把未在当前 session 运行的 tests 或 runtime behavior 声称为 passed。

## 验收要求

- `docs/iterations/v0.2/evidence-index.md` 和 `.zh.md` 存在，并把 active v0.2
  claims 映射到 evidence，或明确标记为 planned、not implemented、
  historical 或 finding。
- `docs/iterations/v0.2/boundary-audit.md` 和 `.zh.md` 存在，并覆盖 external
  consumer boundaries、concrete fixture boundaries、legacy directory
  boundaries、runtime/schema/event boundaries、future-scope boundaries 和
  status drift。
- Deferred 0.2.7 plan/index status mismatch 已用 evidence 关闭，或继续在
  `findings.md` 中 visible，并附清晰理由。
- Audit 对 implemented/tested claims 引用 completed package review files，
  且不把 unreviewed plans 提升为 evidence。
- Concrete demo anchor sweep results 已记录，且不把 concrete pattern lists
  存入 tracked docs。
- Documentation checks 通过。
- Changed files 仅限 approved documentation paths。

## North Star 检查

本 package 审计 v0.2 是否仍是 generic recursive-world foundation。它不引入
concrete worlds、product-specific backend logic、application-specific fixtures
或 future runtime behavior。

## 范围外后续

- 0.2.10 review v0.1 runtime scaffold compatibility 和 legacy boundaries。
- 0.2.11 准备 release-candidate bundle。
- v0.3 只能在 v0.2 closeout 后，通过单独 package 设计和实现 WorldSpec loader
  与 runtime bridge。
