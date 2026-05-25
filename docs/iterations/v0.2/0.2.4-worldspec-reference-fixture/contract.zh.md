# Contract

英文版本：`contract.md`。

## Public Concepts

- Reference WorldSpec fixture：一个小型、确定性的 JSON document，用来展示 valid
  `WorldSpec` shape。
- historical concrete fixture：recursive world schema language 的第一份具名 reference fixture。
- Fixture validation test：聚焦测试，读取 JSON fixture 并通过 `WorldSpec.model_validate(...)`
  validate。

该 fixture 是 reference data fixture，不是 runtime world，不是 generated world，也不是
application-specific backend。

## Allowed Changes

通过 documentation gate review approval 后，implementation 只允许：

- 新增 `backend/data/world_specs/historical concrete fixture path`。
- 新增 `backend/app/tests/test_worldspec_fixture.py`。
- 在 closeout 阶段更新本 package 的 `review.md` 和 `review.zh.md`。

## Forbidden Changes

- 本 documentation stage 不实现代码。
- 暂不创建 `backend/data/world_specs/historical concrete fixture path`。
- 暂不创建 `backend/app/tests/test_worldspec_fixture.py`。
- 不修改 `backend/app/schemas/entity.py`。
- 不修改 `backend/app/schemas/world_cell.py`。
- 不修改 `backend/app/schemas/event.py`。
- 不修改 runtime engine behavior 或 `RuntimeEngine`。
- 不修改 event log storage。
- 不修改 modules。
- 不修改 API routes。
- 不修改 frontend。
- 不修改 `backend/worldengine/`。
- 不实现 WorldSpec loader。
- 不实现 runtime bridge。
- 不实现 concrete demo runtime。
- 不实现 application-specific backend logic。
- 不实现 world generation。
- 不实现 agent memory、pseudo-self 或 agent behavior loops。
- 不增加 persistence/restart logic。
- 不启动 0.2.5。

## Fixture Contract

该 fixture 必须使用 0.2.2 `WorldSpec` schema。

推荐形状：

```json
{
  "schema_version": "0.2",
  "id": "historical-concrete-fixture",
  "label": "historical concrete fixture",
  "metadata": {
    "purpose": "reference-fixture",
    "version": "0.2"
  },
  "root": {
    "id": "root",
    "label": "historical concrete fixture root",
    "kind": "world",
    "entity_refs": [
      {
        "id": "historical child cell",
        "kind": "location",
        "label": "Historical Child Cell"
      }
    ],
    "child_cells": [
      {
        "id": "historical child cell",
        "label": "Historical Child Cell",
        "kind": "world",
        "entity_refs": [
          {
            "id": "historical-nested-entity",
            "kind": "resource",
            "label": "Historical Entity"
          }
        ],
        "child_cells": [],
        "metadata": {
          "fixture_role": "public-location"
        }
      },
      {
        "id": "historical-child-cell",
        "label": "Historical Child Cell",
        "kind": "world",
        "entity_refs": [],
        "child_cells": [],
        "metadata": {
          "fixture_role": "work-location"
        }
      }
    ],
    "metadata": {
      "fixture_role": "root"
    }
  }
}
```

实际实现可以调整 label 或 metadata，但必须保留这些约束：

- `schema_version` 是 `"0.2"`。
- `id` 是 `"historical-concrete-fixture"`。
- `label` 是 `"historical concrete fixture"`。
- `metadata.purpose` 是 `"reference-fixture"`。
- `metadata.version` 是 `"0.2"`。
- `root.id` 是 `"root"`。
- `root.label` 是 `"historical concrete fixture root"`。
- `root.kind` 是 `"world"`。
- `root.entity_refs` 至少有一个 `EntityRef`-like entry。
- `root.child_cells` 至少有两个 nested `WorldCell` examples，例如 `historical child cell` 和
  `historical-child-cell`。
- 至少一个 child cell 可以包含一个 `entity_ref`。
- Metadata 只用于 fixture-specific metadata。

## EntityRef Usage

`entity_refs` 中的 fixture entries 必须使用 `EntityRef`-like dictionaries：

```json
{
  "id": "historical-nested-entity",
  "kind": "resource",
  "label": "Historical Entity",
  "metadata": {
    "fixture_role": "example-resource"
  }
}
```

Entity kinds 保持为 string，例如 `location`、`agent`、`resource`、`rule` 或 `building`。
该 fixture 不能定义 runtime entity state、memory、inventory、behavior、schedules、agent self
data 或任何 reference resolution semantics。

## Test Contract

Implementation-stage test 必须使用 Python standard library `json` 和 `pathlib` 直接读取 JSON
fixture，然后用 `WorldSpec.model_validate(...)` validate parsed dictionary。

允许 test-only JSON reading。本包禁止 production WorldSpec loader。

Implementation-stage tests 必须验证：

- fixture file 存在于 `backend/data/world_specs/historical concrete fixture path`。
- JSON 可以成功 parse。
- `WorldSpec.model_validate(fixture_dict)` 成功。
- `schema_version` 是 `"0.2"`。
- `root` 是 `kind == "world"` 的 `WorldCell`。
- `root` 至少有一个 child cell。
- `root` 至少有一个 entity ref。
- nested `child_cells` 可以 recursive validate。
- `entity_refs` 通过 `WorldCell` / `WorldSpec` validation 作为 `EntityRef` validate。
- `model_dump()` / `model_validate()` round-trip 对 fixture 有效。
- fixture 不依赖 runtime engine、app factory、API route 或 frontend。

## Compatibility Constraints

本包不能改变现有 schema behavior。它使用现有 0.2.2 models 作为 validation targets，不扩展
`EntityRef`、`WorldCell`、`WorldSpec` 或 `Event`。

JSON file 是 additive fixture data。它不能改变 runtime behavior、event log storage、module
behavior、API response shape、frontend behavior 或 legacy `backend/worldengine/` behavior。

## North Star Check

该 fixture 为 recursive world work 提供一个具体 schema example，同时保持 WorldEngine 对齐 engine
north star。它支持未来 generation、loading、runtime bridge、projection 和 agent work，但不在
0.2.4 实现这些系统。

## Out-of-Scope Follow-ups

- v0.3 WorldSpec loader and runtime bridge。
- Runtime reference resolution and referential integrity。
- Concrete demo runtime and product surface。
- Full world generation。
- Agent memory、pseudo-self 或 agent behavior loops。
- 0.2.5 legacy boundary cleanup。
