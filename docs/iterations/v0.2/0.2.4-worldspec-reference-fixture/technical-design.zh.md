# Technical Design

英文版本：`technical-design.md`。

## Current State

Active backend path 是 `backend/app/`。0.2.2 已新增：

- `backend/app/schemas/entity.py` 中的 `EntityRef`。
- `backend/app/schemas/world_cell.py` 中的 `WorldCell` 和 `WorldSpec`。
- `backend/app/tests/test_world_cell_schema.py` 中的聚焦 schema tests。

`WorldSpec` 当前 validate top-level `schema_version`、`id`、optional `label`、
`root: WorldCell` 和 `metadata`。`WorldCell` validate recursive `child_cells` 和
`entity_refs`。当前还没有 checked-in reference WorldSpec fixture。

## Contract Alignment and Invariants

- 0.2.4 只在 review approval 后新增 data 和 tests。
- Fixture 必须通过现有 0.2.2 schema models validate。
- 允许 test-only JSON reading。
- 不允许 production loading behavior。
- Existing schema files 必须保持不变。
- Runtime、event log、modules、API routes、frontend 和 `backend/worldengine/` 必须保持不变。
- Fixture 不是 runtime world，也不是 application-specific backend feature。

## Proposed Implementation

通过 review approval 后，新增：

- `backend/data/world_specs/historical concrete fixture path`
- `backend/app/tests/test_worldspec_fixture.py`

JSON fixture 应该小型、确定性，并包含：

- `schema_version: "0.2"`
- `id: "historical-concrete-fixture"`
- `label: "historical concrete fixture"`
- top-level metadata，包含 `purpose: "reference-fixture"` 和 `version: "0.2"`
- root `WorldCell`，包含 `id: "root"`、`label: "historical concrete fixture root"` 和 `kind: "world"`
- 至少一个 root `entity_ref`
- 至少两个 nested child cells，例如 `historical child cell` 和 `historical-child-cell`
- 至少一个 nested child cell 包含 `entity_ref`
- 仅 fixture-specific metadata

Test file 应直接 load JSON：

```python
import json
from pathlib import Path

from app.schemas.world_cell import WorldCell, WorldSpec


FIXTURE_PATH = Path(__file__).resolve().parents[2] / "data" / "world_specs" / "historical concrete fixture path"


def load_fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text())
```

如果仍然局限在 test 内且不变成 production loader logic，implementation 可以选择等价路径表达式。

## Affected Surfaces

- Fixture data：`backend/data/world_specs/` 下的一个 JSON file。
- Tests：`backend/app/tests/` 下的一个 focused test file。
- Schemas：不受影响。
- Runtime engine / `RuntimeEngine`：不受影响。
- Event log storage：不受影响。
- Modules：不受影响。
- API routes：不受影响。
- Frontend：不受影响。
- `backend/worldengine/`：不受影响。

## Runtime / Service Design

本包不包含 runtime 或 service design changes。不得新增 WorldSpec loader、runtime bridge、API route、
app factory dependency、projection integration、persistence/restart behavior 或 concrete demo runtime。

## Compatibility

Compatibility 通过 additive data 和 existing schema validation 保持。Existing runtime behavior、
event contract、API behavior、frontend behavior 和 legacy backend behavior 保持不变。

## Risks

- Risk：fixture 开始编码 runtime state，而不是 schema shape。Detection：review fixture fields，
  确认没有 memory、inventory、behavior、schedules、self data、persistence 或 runtime-only state。
- Risk：test 变成 production loader。Detection：changed-file review 必须确认没有新增 loader module、
  service API、CLI loader、runtime bridge 或 dashboard integration。
- Risk：implementation 为了适配 fixture 修改 schemas。Detection：changed-file scope checks 必须确认
  `entity.py`、`world_cell.py` 和 `event.py` 未修改。
- Risk：historical concrete fixture 变成 application-specific backend logic。Detection：scope review 必须确认没有新增
  runtime、API、frontend、generator 或 application-specific behavior。
