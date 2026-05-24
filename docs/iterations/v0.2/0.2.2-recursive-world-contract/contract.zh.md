# Contract

英文版本：`contract.md`。

## Public Concepts

- `EntityRef`：entities、agents、resources、rules、locations 和 future memory links 的轻量
  reference 或 declaration。它不是 runtime entity state。
- `WorldCell`：最小 recursive world unit。一个 cell 可以包含 entity references 和 child cells。
- `WorldSpec`：generated 或 loadable recursive world 的最小顶层容器。它是 schema container，
  不是 loader 或 runtime bridge。

## Compatibility Constraints

- Existing runtime behavior 不能改变。
- Existing API response shapes 不能改变。
- Existing event schema behavior 不能改变。
- Existing frontend behavior 不能改变。
- Existing v0.1 tests 必须保持兼容。
- Schema additions 必须是 additive，并且隔离在 allowed schema files 内。

## Allowed Changes

这个 documentation gate 通过 review 后，implementation 只允许：

- 新增 `backend/app/schemas/entity.py`。
- 新增 `backend/app/schemas/world_cell.py`。
- 新增 `backend/app/tests/test_world_cell_schema.py`。

## Forbidden Changes

- 本 documentation stage 不实现代码。
- 不修改 runtime services、modules、event storage、API routes 或 app factory behavior。
- 不修改 `backend/app/schemas/event.py`。
- 不修改 `frontend/`。
- 不修改 `backend/worldengine/`。
- 不添加 `backend/data/world_specs/tiny_village.world.json`。
- 不实现 WorldSpec loader。
- 不迁移 `RuntimeEngine` 到 `WorldCell`。
- 不实现 village runtime。
- 不实现 world generation。
- 不实现 agent memory、agent inner-world 或 pseudo-self continuity。
- 不启动 0.2.3。
- 不修改 0.2.1 package wording。

## Schema Contract

`EntityRef` 必须使用当前 backend Pydantic 风格，并提供：

```python
id: str
kind: str
label: Optional[str] = None
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`WorldCell` 必须提供：

```python
id: str
label: Optional[str] = None
kind: Literal["world"] = "world"
entity_refs: List[EntityRef] = Field(default_factory=list)
child_cells: List["WorldCell"] = Field(default_factory=list)
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`WorldSpec` 必须提供：

```python
schema_version: Literal["0.2"] = "0.2"
id: str
label: Optional[str] = None
root: WorldCell
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`label` fields 是 optional display labels，不是 stable identifiers。`id` 是 refs、cells 和
specs 的 stable identifier field。

## Validation Contract

- Required id-like fields 必须拒绝 empty strings。
- `WorldCell.kind` 只能接受 `"world"`。
- `WorldSpec.schema_version` 只能接受 `"0.2"`。
- Nested `child_cells` 必须递归验证为 `WorldCell`。
- `entity_refs` 必须验证为 `EntityRef`。
- Serialization 必须支持 `model_dump()`。
- Round-trip reconstruction 必须支持从 dumped nested `WorldSpec` dictionary 调用
  `model_validate()`。

本包不验证 unique ids、不检测 graph cycles、不解析 references、不加载文件，也不把 schemas 接入
runtime execution。

## North Star Check

本 contract 为 recursive worlds 定义第一根结构骨架，但不把 engine 写成 village-specific。它为
future generation、loading、runtime bridge 和 projection work 创建 schema language，同时把这些
follow-ups 保持在本包之外。

## Out-of-Scope Follow-ups

- 0.2.3 Event Contract Extension。
- 0.2.4 WorldSpec Reference Fixture。
- v0.3 WorldSpec loader and runtime bridge。
- Agent memory and pseudo-self continuity。
- Reference village runtime and game surface。
