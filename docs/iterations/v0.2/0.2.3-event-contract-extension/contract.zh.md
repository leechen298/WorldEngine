# Contract

英文版本：`contract.md`。

## Public Concepts

- `EventRef`：轻量 event-local pointer。它不是 resolved runtime object，不是 storage state，
  也不是 WorldCell 或 EntityRef binding。
- `Event.refs`：Event 上 additive optional EventRef list。
- `payload`：既有 flexible event-specific data field。它保持不变并完全 backward compatible。

## Current Event Schema

当前 Event schema 包含：

```python
id: str
tick_id: int
world_time_seconds: int
type: str
source: str
payload: Dict[str, Any]
created_at: str
```

`EventPage`、`EventStep` 和 `EventStepPage` 包装 Event values。Existing event construction 和
API response compatibility 必须保持不变。

## Allowed Changes

这个 documentation gate 通过 review 和 approval 后，implementation 只允许：

- 在 `backend/app/schemas/event.py` 中新增 `EventRef`。
- 给 Event 增加 optional `refs: List[EventRef] = Field(default_factory=list)`。
- 在 `backend/app/tests/test_event_schema_compat.py` 中新增 focused compatibility tests。
- Closeout 时更新本 package 的 `review.md` 和 `review.zh.md`。

## Forbidden Changes

- 本 documentation stage 不实现代码。
- 不改变 Event `id`、`tick_id`、`world_time_seconds`、`type`、`source`、`payload` 或
  `created_at` semantics。
- 不删除或重命名 `payload`。
- 不要求 existing events 必须有 `refs`。
- 不修改 event log storage。
- 不修改 runtime engine behavior。
- 不修改 modules。
- 不修改 API routes。
- 不修改 frontend。
- 不修改 `backend/worldengine/`。
- 不把 EventRef 接入 WorldCell runtime。
- 不 resolve refs。
- 不 enforce referential integrity。
- 不实现 WorldSpec loader。
- 不实现 village runtime。
- 不实现 agent memory 或 pseudo-self。
- 不启动 0.2.4。

## Schema Contract

`EventRef` 必须定义在 `backend/app/schemas/event.py`，并且不能 import `EntityRef`、`WorldCell`
或 `WorldSpec`。

`EventRef` 必须使用当前 backend Pydantic 风格，并提供：

```python
id: str
kind: str
role: Optional[str] = None
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`Event` 必须增加：

```python
refs: List[EventRef] = Field(default_factory=list)
```

`kind` 保持 string，不使用 `Literal`，因为未来 reference kinds 尚未定型。`role` 保持 optional，
这样 event 可以区分 subject、target、actor、location、source_cell、affected_cell 或未来 roles，
而不需要 schema churn。

## Validation Contract

- `EventRef.id` 必须拒绝 empty strings。
- `EventRef.kind` 必须拒绝 empty strings。
- `EventRef.role` 是 optional。
- `EventRef.metadata` 默认是 empty dict。
- `Event.refs` 默认是 empty list。
- Existing Event instances without `refs` 必须仍然 validate。
- Existing Event payload 保持不变并完全 backward compatible。
- 带 refs 的 Event values 必须能在 `EventPage` 中 validate。
- 带 refs 的 Event values 必须能在 `EventStep` 中 validate。
- 嵌套 Event refs 的 EventStep values 必须能在 `EventStepPage` 中 validate。
- `model_dump()` / `model_validate()` round-trip 必须保留 refs。

## Compatibility Constraints

这个 extension 必须是 additive。Existing event construction、existing API response compatibility、
EventPage wrapping、EventStep wrapping、EventStepPage wrapping 和 old event examples 必须保持有效。

`payload` 继续作为 event-specific data 的 escape hatch。`refs` 只增加 structured pointer slot，
不替代 payload。

## North Star Check

EventRef 为未来 recursive worlds、projections、agent memory 和 pseudo-self work 创建 event
evidence hook，但不把这些后续系统强行接进 v0.2 runtime。它让 Event Contract 足够通用以服务
engine north star，同时足够窄以保留当前行为。

## Out-of-Scope Follow-ups

- 0.2.4 WorldSpec Reference Fixture。
- v0.3 WorldSpec loader and runtime bridge。
- Runtime ref resolution 和 referential integrity。
- Event-driven agent memory 或 pseudo-self continuity。
- Village runtime 和 game surface。
