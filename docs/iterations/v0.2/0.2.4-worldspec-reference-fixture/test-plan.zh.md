# Test Plan

英文版本：`test-plan.md`。

## Unit Tests

通过 documentation gate review approval 后，新增 `backend/app/tests/test_worldspec_fixture.py`，
测试内容包括：

- fixture file 存在于 `backend/data/world_specs/tiny_village.world.json`。
- 使用 Python standard library `json` 和 `pathlib` 可以成功 parse JSON。
- `WorldSpec.model_validate(fixture_dict)` 成功。
- `spec.schema_version == "0.2"`。
- `spec.root` 是 `WorldCell`。
- `spec.root.kind == "world"`。
- `spec.root.child_cells` 至少有一个 child cell。
- `spec.root.entity_refs` 至少有一个 entity ref。
- nested `child_cells` 可以 recursive validate。
- `entity_refs` 通过 `WorldCell` / `WorldSpec` validation 作为 `EntityRef` validate。
- `model_dump()` / `model_validate()` round-trip 对 fixture 有效。
- `WorldSpec`、`WorldCell` 和 `EntityRef` import smoke。

## Regression Tests

Existing backend tests 必须继续通过，因为本包不能改变 runtime behavior、schema implementation
behavior、event log storage、modules、API routes、frontend behavior 或 `backend/worldengine/`。

## Commands

本包 documentation-stage commands：

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.4-worldspec-reference-fixture -maxdepth 1 -type f | sort
rg -n "0.2.4-worldspec-reference-fixture|ready for review|WorldSpec|tiny_village|reference fixture|model_validate|WorldCell|EntityRef|schema_version" docs/iterations/v0.2/0.2.4-worldspec-reference-fixture docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "WorldSpec loader|runtime bridge|RuntimeEngine|backend/worldengine|village runtime|game-specific|world generation|agent memory|pseudo-self|frontend|API route|event log" docs/iterations/v0.2/0.2.4-worldspec-reference-fixture docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
git status --porcelain=v1 -uall | awk '{print $2}' | rg -v '^docs/iterations/v0.2/'
```

Implementation-stage commands 只记录，不在 code added 和 review approval 前运行：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_fixture.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
cd backend && .venv/bin/python - <<'PY'
import json
from pathlib import Path
from app.schemas.world_cell import WorldSpec

path = Path("data/world_specs/tiny_village.world.json")
spec = WorldSpec.model_validate(json.loads(path.read_text()))
print(spec.id, spec.schema_version, spec.root.id)
PY
```

## Acceptance Criteria

- Documentation gate 只改变 `docs/iterations/v0.2/`。
- Package directory 包含完整 English seven-file set 和完整 `.zh.md` mirrors。
- v0.2 README 和 plan documents 显示 0.2.4 为 `ready for review`。
- 0.2.4 不标记为 ready for implementation、implementation complete 或 review complete。
- `review.md` 和 `review.zh.md` 记录 documentation-stage evidence，并说明 implementation has
  not started。
- Documentation stage 不改变 backend、frontend、runtime、schema implementation、API、UI、
  fixture、loader、generator 或 test implementation file。
- Implementation 只能在 package 被 review and approved 后开始。

## Not Run

Backend、frontend、runtime、E2E、UI smoke、Agent smoke 和 implementation tests 在 documentation
stage 不运行，因为本阶段不改变 code、runtime、schema implementation、API、UI、fixture、loader、
generator 或 test implementation files。
