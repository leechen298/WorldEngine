# Technical Design

英文版本：`technical-design.md`。

## Current State

Active backend path 是 `backend/app/`。当前 Event schema 位于
`backend/app/schemas/event.py`，并用 Pydantic `BaseModel` 和 `Field` 定义 Event、EventPage、
EventStep 和 EventStepPage。

Event 当前包含 `id`、`tick_id`、`world_time_seconds`、`type`、`source`、`payload` 和
`created_at`。EventPage、EventStep 和 EventStepPage 包装 Event values。目前 Event 没有
structured reference list。

## Contract Alignment and Invariants

- Implementation 必须是 additive。
- Existing Event construction without refs 必须保持有效。
- Existing Event payload behavior 必须保持不变。
- EventPage、EventStep 和 EventStepPage 必须兼容 old and new Event values。
- EventRef 必须保持 event-local and lightweight。
- EventRef 必须定义在 `backend/app/schemas/event.py`。
- 本 package 中，`backend/app/schemas/event.py` 不能 import EntityRef、WorldCell 或 WorldSpec。

## Proposed Implementation

Review approval 后，只通过以下方式更新 `backend/app/schemas/event.py`：

- 新增 `EventRef`。
- 给 Event 增加 `refs: List[EventRef] = Field(default_factory=list)`。
- 增加 validation，拒绝 empty `EventRef.id` 和 empty `EventRef.kind`。

新增 `backend/app/tests/test_event_schema_compat.py`，放 focused schema tests。Tests 应直接构造
models，避免 app factory、HTTP routes、runtime stepping、event log storage、fixtures、loaders
或 frontend behavior。

## Affected Surfaces

- Schemas：Event 增加 optional `refs`；新增 EventRef。
- Tests：新增 focused event schema compatibility test file。
- Event log storage：不受影响。
- Runtime engine：不受影响。
- Modules：不受影响。
- API routes：不受影响。
- Frontend：不受影响。
- `backend/worldengine/`：不受影响。

## Data Model / Schema Changes

`EventRef` fields：

```python
id: str
kind: str
role: Optional[str] = None
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`Event` 增加：

```python
refs: List[EventRef] = Field(default_factory=list)
```

`kind` 有意保持 string，而不是 `Literal`，因为未来 reference kinds 尚未定型。`role` 保持 optional，
让后续 event producers 可以区分 subject、target、actor、location、source_cell、affected_cell
或未来 roles，而不需要再做 schema migration。

## Runtime / Service Design

本包不包含 runtime 或 service design changes。Implementation 不能 resolve refs、enforce
referential integrity、把 EventRef 接入 WorldCell runtime、修改 event log storage 或改变 API
route behavior。

## Compatibility

兼容性通过 `refs` default empty list 保持：旧 Event dictionaries without refs 仍然有效。
`payload` 继续作为 event-specific data 的 flexible escape hatch，不会被删除、重命名、收窄或重新解释。

## Risks

- Risk：EventRef 意外 import recursive-world schemas。Detection：contract review 和
  implementation diff review 必须确认 `event.py` 没有 EntityRef、WorldCell 或 WorldSpec import。
- Risk：old events without refs validation 失败。Detection：focused schema compatibility tests。
- Risk：EventPage、EventStep 或 EventStepPage wrappers 拒绝 new Event refs。Detection：wrapper
  validation tests。
- Risk：添加 refs 时改变 payload semantics。Detection：测试 old event examples 并 review event
  schema diff。
- Risk：implementation 扩大到 runtime、API route、frontend、loader、village、migration、agent
  memory 或 pseudo-self work。Detection：changed-file scope checks。
