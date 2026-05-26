# Contract

英文版本：`contract.md`

## 公开概念

- EventRef：event-local structured reference，包含 required non-empty `id`、
  required non-empty `kind`、optional `role` 和 free-form `metadata`。
- Event.refs：Event 上 optional 的 EventRef list。省略 refs 时 validate 为
  empty list。
- Event-local reference semantics：refs 使用 structured references 标注 event
  payload。v0.2 中它们不证明 referential integrity、causality、runtime
  existence、memory linkage、projection visibility 或 action consequences。
- EventRef contract doc：human-readable contract document，解释 field
  semantics、compatibility expectations、validation boundaries 和 explicit
  non-goals。

## 兼容性约束

- `Event.refs` 保持 optional，默认 `[]`。
- Existing Event dictionaries without refs 必须继续 validate。
- Existing Event dictionaries with valid refs 必须继续 validate。
- EventRef 必须继续 reject empty `id` 和 empty `kind`。
- Existing payload behavior、event storage shape、runtime behavior、API
  response shapes、frontend behavior、fixtures、migrations 和 legacy
  `backend/worldengine/` behavior 必须保持不变。
- Schema changes 必须是 additive；除非本 package 先回到 documentation review，
  并获得 explicitly approved breaking-change contract。

## 允许变更

- 新增 `docs/contracts/event-ref-contract.md`。
- 如果阅读 existing tests 后仍有 coverage gaps，可以用 domain-neutral
  compatibility tests 更新 `backend/app/tests/test_event_schema_compat.py`。
- 仅在 approved contract 要求且有 tests 覆盖时，对
  `backend/app/schemas/event.py` 做 additive validation clarifications。
- 用实际 implementation evidence 更新本 package 的 `review.md` 和 `review.zh.md`。

## 禁止变更

- 不实现 referential integrity resolver。
- 不实现 timeline causality engine。
- 不把 EventRef 或 Event.refs 绑定到 live WorldCell runtime state。
- 不实现 Agent action consequence logic。
- 不实现 memory、self-continuity、projection、generation 或 WorldSpec loading
  behavior。
- 不修改 runtime services、runtime state flow、event log persistence、tick
  behavior、API routes、API response shapes 或 frontend files。
- 不修改 fixtures 或增加 fixture data。
- 不增加 migrations。
- 不修改 `backend/worldengine/`。
- 不增加 concrete external-world names、characters、locations、resources、
  roles、story rules、seed data、UI concepts 或 product-specific backend
  logic。
- 不创建 external repositories。

## 验收要求

- `docs/contracts/event-ref-contract.md` 存在，并描述 field semantics、
  compatibility behavior、validation boundaries、event-local semantics 和
  explicit non-goals。
- Focused event schema tests 要么经 documented assessment 证明已足够，要么更新
  以覆盖 optional refs、refs with role and metadata、empty `id` / `kind`
  rejection、default metadata、model dump / validate round trips，以及 nested
  EventPage / EventStepPage validation。
- Existing Event dictionaries without refs 继续 validate。
- 如果 schema 或 test files changed，`make check-backend` 必须通过。
- 如果 schema 或 test files changed，focused event schema pytest commands 必须通过。
- Package docs 和 contract docs 的 documentation checks 必须通过。
- Review evidence 记录每个 command run，不得把未运行的 tests 声称为 passed。
- Changed-file set 不包含 runtime、API、frontend、fixture、migration 或
  external-repository implementation files。

## North Star 检查

本 package 加固未来 runtime、agent、memory 和 projection systems 可消费的 event
contract。它不引入 concrete world、product-specific backend、application surface、
resolver 或 causality runtime。

## 范围外后续

- 0.2.9 审计 schema、event、external boundary 和 legacy boundary evidence。
- v0.3 可以把 validated generic WorldSpec data 加载到 runtime context。
- 后续里程碑可以增加 event causality、action consequences、projection、memory、
  agent loop 和 self-continuity。
