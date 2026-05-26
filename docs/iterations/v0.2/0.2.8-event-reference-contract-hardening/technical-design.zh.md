# Technical Design

英文版本：`technical-design.md`

## 当前状态

`backend/app/schemas/event.py` 定义 EventRef 为 Pydantic model，包含 non-empty
`id`、non-empty `kind`、optional `role` 和 default empty metadata。

`Event` 包含 `refs: List[EventRef] = Field(default_factory=list)`，并保留现有的
event identity、tick、world time、type、source、payload 和 created-at fields。

`EventPage`、`EventStep` 和 `EventStepPage` 嵌套 Event objects，因此会通过
paginated 和 grouped event response schemas 携带 Event.refs。

`backend/app/tests/test_event_schema_compat.py` 已覆盖 imports、existing event
construction without refs、refs with role and metadata、empty EventRef identity
rejection、optional role、default metadata、model dump / validate round trips、
EventPage validation 和 EventStepPage validation。

## Contract 对齐与不变量

- 保持 EventRef generic 且 event-local。
- 保持 `id`、`kind` 和 `role` 为 strings，不在 v0.2 中赋予 runtime enum
  semantics。
- 保持 `metadata` free-form，v0.2 runtime code 不解释它。
- Preserve existing event dictionaries without refs。
- Preserve existing payload behavior、event log behavior、API response shapes、
  frontend behavior、fixtures、migrations 和 legacy code behavior。
- Examples 和 tests 必须 domain-neutral。

## 计划实现

Documentation review approval 后，执行最小 scoped hardening pass：

1. 新增 `docs/contracts/event-ref-contract.md`，描述 EventRef fields、
   Event.refs semantics、validation behavior、compatibility guarantees 和
   non-goals。
2. 将 existing event schema compatibility tests 与 `test-plan.md` 中的 accepted
   coverage list 对照。
3. 只把缺失的 domain-neutral tests 添加到
   `backend/app/tests/test_event_schema_compat.py`。
4. 只有当 reviewed acceptance requirement 无法由当前 additive schema 满足时，
   才修改 schema code。
5. 用 actual changed files、commands、results、compatibility review、scope
   review 和 unresolved findings 更新 `review.md` 与 `review.zh.md`。

## 影响面

Documentation：

- `docs/contracts/event-ref-contract.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/**`

Possible tests：

- `backend/app/tests/test_event_schema_compat.py`

Possible schema，仅当需要 additive clarification：

- `backend/app/schemas/event.py`

## Data Model / Schema Changes

默认不需要 schema change。预期 implementation 是 contract documentation 加上任何
缺失的 focused compatibility tests。

如果 implementation 发现真实 schema ambiguity，允许的 schema changes 仅限
`contract.md` 已批准的 additive validation clarifications。Breaking changes 必须
回到 documentation review。

## Runtime / Service Design

无。本 package 不得增加 resolver behavior、causality evaluation、runtime bridge
flow、persistence changes、service wiring、background tasks、API routes 或
frontend behavior。

## 兼容性

Existing v0.1 runtime behavior、event log behavior、payload behavior、API
response shapes、frontend behavior、fixtures、migrations 和 legacy
`backend/worldengine/` behavior 均保持不变。

Existing valid Event payloads without refs 必须继续 validate。Existing valid
Event payloads with refs 必须继续 validate。Existing invalid empty EventRef
identity fields 必须继续 fail validation。

## 假设

- Pydantic 仍是本 package 的 event schema validation layer。
- Contract docs 可以澄清 semantics，而无需 schema code changes。
- Current focused tests 可能已满足部分或全部 acceptance criteria。
- v0.2 中 `EventRef.kind` values 是 producer-provided generic categories。

## 风险

- 风险：tests 重复 existing coverage，而不是加固 meaningful gaps。缓解：
  implementation 必须先把 current tests 映射到 acceptance criteria，再只添加
  missing tests。
- 风险：contract docs 暗示 refs 已被 resolve 或 causally ordered。缓解：EventRef
  contract 必须明确 v0.2 non-goals。
- 风险：examples 漂移到 concrete external-world details。缓解：使用 neutral
  identifiers，并对 touched docs 和 tests 运行 concrete demo anchor sweep。
- 风险：schema clarifications 可能改变 API behavior。缓解：默认避免 schema
  changes；如果 schema 或 tests 变更，则运行 focused compatibility checks。
