# Technical Design

英文版本：`technical-design.md`。

## Current State

Active backend path 是 `backend/app/`。现有 `backend/app/schemas/` 共享 schemas 使用
Pydantic `BaseModel` 和 `Field`，模型保持小而聚焦。`backend/worldengine/` 是 legacy path，
不是本包 active runtime path。

当前没有 `EntityRef`、`WorldCell` 或 `WorldSpec` schema。v0.1 runtime services、modules、
event storage 和 API routes 不消费 recursive world schema data。

## Contract Alignment and Invariants

- Implementation 必须只添加 schemas，不接入 runtime。
- Implementation 不能改变 existing API response shapes。
- Implementation 不能改变 current event behavior。
- Implementation 不能添加 loaders、fixtures、generators 或 dashboard changes。
- `EntityRef`、`WorldCell` 和 `WorldSpec` 必须保持 schema-level concepts。

## Proposed Implementation

新增 `backend/app/schemas/entity.py`，定义 `EntityRef`。

新增 `backend/app/schemas/world_cell.py`，定义 `WorldCell` 和 `WorldSpec`。使用 Pydantic
v2-compatible models 和 local imports。递归 child cells 如有需要可使用 forward references。

新增 `backend/app/tests/test_world_cell_schema.py`，写 focused schema tests。测试应直接构造
models，不使用 app factory、HTTP routes、runtime stepping、fixtures 或 external services。

## Affected Surfaces

- Schemas：新增 `EntityRef`、`WorldCell` 和 `WorldSpec`。
- Tests：新增 focused schema test file。
- Runtime services：不受影响。
- API routes：不受影响。
- Events：不受影响。
- Frontend：不受影响。
- Fixtures：不受影响。
- Legacy backend：不受影响。

## Data Model / Schema Changes

`EntityRef` fields：

```python
id: str
kind: str
label: Optional[str] = None
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`WorldCell` fields：

```python
id: str
label: Optional[str] = None
kind: Literal["world"] = "world"
entity_refs: List[EntityRef] = Field(default_factory=list)
child_cells: List["WorldCell"] = Field(default_factory=list)
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`WorldSpec` fields：

```python
schema_version: Literal["0.2"] = "0.2"
id: str
label: Optional[str] = None
root: WorldCell
metadata: Dict[str, Any] = Field(default_factory=dict)
```

所有三个 schema concepts 的 `label` 都是 optional。`id` 是 required stable identifier。
`WorldCell.kind` 和 `WorldSpec.schema_version` 使用 Literal，让 tests 可以验证 contract。

## Runtime / Service Design

本包不包含 runtime 或 service design changes。这些 schemas 在后续 packages 把 WorldSpec data
接入 fixtures、loaders、event contracts 或 runtime bridges 之前保持 inert。

## Compatibility

Existing data 仍然有效，因为当前 persistence format 不改变。Existing API clients 仍然兼容，因为
route responses 不改变。v0.1 runtime behavior 仍然兼容，因为新 schemas 不导入 runtime flow。

## Risks

- Risk：schema additions 意外变成 runtime migration。Detection：changed-file scope check 和
  regression test command。
- Risk：literals 被文档化但 implementation 未 enforcement。Detection：invalid `kind` 和 invalid
  `schema_version` tests。
- Risk：recursive child cells 无法 validate 或 serialize。Detection：nested construction 和
  `model_dump()` / `model_validate()` round-trip tests。
- Risk：future 0.2.4 fixture 缺少顶层容器。Detection：本包 contract 包含 `WorldSpec`。
