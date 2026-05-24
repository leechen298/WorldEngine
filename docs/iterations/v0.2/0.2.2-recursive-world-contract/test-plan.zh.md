# Test Plan

英文版本：`test-plan.md`。

## Unit Tests

新增 `backend/app/tests/test_world_cell_schema.py`，覆盖：

- `EntityRef` construction：required `id` 和 `kind`、optional `label`、默认 empty
  `metadata`。
- `WorldCell` construction：默认 `kind="world"`、默认 empty `entity_refs`、默认 empty
  `child_cells`、optional `label`。
- 通过 `child_cells` 构造 nested `WorldCell`。
- 使用 `schema_version="0.2"` 和 `root` `WorldCell` 构造 `WorldSpec`。
- `EntityRef`、`WorldCell` 和 `WorldSpec` 的 invalid empty id-like fields。
- Invalid `WorldCell(kind="village")`。
- Invalid `WorldSpec(schema_version="0.3")`。
- Invalid child cell input，不能 validate as `WorldCell`。
- Invalid entity ref input，不能 validate as `EntityRef`。
- Nested `WorldSpec` 的 `model_dump()` serialization。
- 从 dumped nested `WorldSpec` dictionary 调用 `model_validate()` reconstruction。
- `EntityRef`、`WorldCell` 和 `WorldSpec` import smoke。

## Regression Tests

Existing backend tests 必须继续通过，因为本包不能改变 runtime behavior、API route behavior、event
behavior 或 frontend behavior。

## Commands

本 package documentation-stage commands：

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.2-recursive-world-contract -maxdepth 1 -type f | sort
rg -n "0.2.2-recursive-world-contract|ready for implementation|WorldCell|EntityRef|WorldSpec" docs/iterations/v0.2/0.2.2-recursive-world-contract docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|village|migration|agent memory|pseudo-self" docs/iterations/v0.2/0.2.2-recursive-world-contract docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
```

这个 documentation gate 通过 review 且 code added 之后，implementation-stage commands：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
cd backend && .venv/bin/python - <<'PY'
from app.schemas.entity import EntityRef
from app.schemas.world_cell import WorldCell, WorldSpec
print(EntityRef, WorldCell, WorldSpec)
PY
```

## Acceptance Criteria

- Documentation gate 只修改 `docs/iterations/v0.2/`。
- Package directory 包含完整 English seven-file set 和完整 `.zh.md` mirrors。
- v0.2 README 和 plan documents 显示 0.2.2 为 `ready for implementation`。
- `review.md` 和 `review.zh.md` 记录 documentation-stage evidence，并说明 implementation
  has not started。
- Documentation stage 不修改 backend、frontend、runtime、test implementation、fixture 或
  legacy backend files。
- Implementation 只能在本 package review approved 后开始。

## Not Run

Documentation stage 不运行 backend、frontend、runtime、E2E、UI smoke、Agent smoke 或
implementation tests，因为没有修改 code、runtime、schema implementation、API、UI、fixture 或
test implementation files。
