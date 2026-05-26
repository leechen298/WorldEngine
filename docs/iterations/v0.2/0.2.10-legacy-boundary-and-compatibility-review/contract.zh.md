# Contract

英文版本：`contract.md`

## 公开概念

- Legacy boundary：`backend/app/` active code 与 `backend/worldengine/`
  legacy code 之间的文档化分界。
- Compatibility baseline：v0.2 必须保留的 v0.1 runtime、API envelope、
  dashboard-facing behavior、params flow、event timeline、archive behavior 和
  params-agent scaffold。
- v0.2 foundation boundary：EntityRef、WorldCell、WorldSpec、EventRef 和
  Event.refs 是 additive schema/event contracts，不是 active runtime loading
  behavior。
- v0.3 handoff constraint：未来 bridge work 改变 runtime behavior 前必须满足的
  文档化要求或风险。
- Compatibility finding：带有优先级和目标 package 的 unresolved documentation、
  evidence 或 behavior ambiguity。

## 兼容性约束

- Runtime behavior 不得改变。
- Schema behavior 和 validation behavior 不得改变。
- Event storage、event pagination 和当前 event response behavior 不得改变。
- API response envelopes 和 endpoint shapes 不得改变。
- Frontend behavior 不得改变。
- Fixture、migration 和 test implementation files 不得改变。
- `backend/app/` 仍是 active backend code path。
- `frontend/` 仍是 active dashboard code path。
- `backend/worldengine/` 仍是 legacy 且未接入，除非后续 reviewed package
  明确改变该边界。
- 文档必须区分已实现的 v0.1 behavior、additive v0.2 contracts 和未来 v0.3
  bridge work。

## 允许变更

- 新增 `docs/legacy-boundary.md`。
- 新增 `docs/legacy-boundary.zh.md`。
- 新增 `docs/iterations/v0.2/compatibility-review.md`。
- 新增 `docs/iterations/v0.2/compatibility-review.zh.md`。
- 更新 `docs/iterations/v0.2/findings.md`，新增、关闭或重定向 compatibility
  findings。
- 更新本 package 的 `review.md` 和 `review.zh.md` 记录 evidence。
- 更新 v0.2 milestone index 和 plan 中 0.2.10 的状态字段。
- 运行只读 repository searches、path checks 和 documentation sanity checks。

## 禁止变更

- 不修改 runtime services、world state、modules、event log behavior、archive
  behavior、agent behavior、persistence、API routes 或 app assembly。
- 不修改 schema implementation files。
- 不修改 frontend files。
- 不修改 tests 或 fixtures。
- 不增加 migrations。
- 不修改 `backend/worldengine/`。
- 不实现 WorldSpec loading、RuntimeEngine-to-WorldCell migration、runtime
  bridge、generation、projection、agent loop、memory、self-continuity、resolver
  或 causality behavior。
- 不增加 external repositories 或 external validation internals。
- 不增加 concrete external-world names、characters、locations、roles、
  resources、story rules、seed data、UI selectors、private runner state 或
  application-specific backend logic。
- 除非在当前 session 运行了命令或流程，否则不得声称 tests、builds、runtime
  behavior、API behavior 或 frontend behavior 通过。

## 验收要求

- `docs/legacy-boundary.md` 和 `.zh.md` 存在，并记录 active backend、active
  dashboard、legacy backend、placeholder infrastructure、documentation 和 future
  bridge boundaries。
- `docs/iterations/v0.2/compatibility-review.md` 和 `.zh.md` 存在，并覆盖
  runtime state、runtime step behavior、event timeline behavior、world params、
  params-agent scaffold、archive summaries/snapshots、API envelope、frontend
  expectations、schema/event additive contracts 和 v0.3 handoff constraints。
- Compatibility review 将每个 claim 标记为 documented、reviewed、
  current-session verified、planned、not implemented、legacy 或 finding。
- 任何 missing evidence、ambiguous active path 或 v0.3 bridge risk 都记录到
  `docs/iterations/v0.2/findings.md`，而不是用代码修复。
- Documentation checks 通过。
- Changed files 限于允许的 documentation paths。
- Package docs 和新增 boundary/review docs 的英文与中文镜像保持同步。

## North Star 检查

本 package 通过区分当前 runtime compatibility 与未来 bridge work，保护
WorldEngine 作为通用 recursive world engine 的方向。它不引入 concrete worlds、
product-specific backend logic、application-specific fixtures 或 runtime
behavior。

## 范围外后续工作

- 0.2.11 准备 v0.2 release-candidate bundle。
- v0.3 只能在 v0.2 closeout 后设计和实现 WorldSpec loader 与 runtime bridge。
- 任何 compatibility-preserving regression tests 都需要后续 reviewed mixed 或
  code package。
