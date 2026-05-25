# Plan

英文版本：`plan.md`。

## Files

Documentation stage 创建：

- `docs/iterations/v0.2/0.2.2-recursive-world-contract/README.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/README.zh.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/intent.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/intent.zh.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/contract.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/contract.zh.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/technical-design.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/test-plan.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/plan.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/plan.zh.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/review.md`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/review.zh.md`

Documentation stage 修改：

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Review 通过后允许的 implementation files：

- `backend/app/schemas/entity.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/tests/test_world_cell_schema.py`

Documentation stage 不触碰：

- `backend/`
- `frontend/`
- `backend/worldengine/`
- `docs/iterations/v0.2/0.2.1-project-north-star/`
- 0.2.3 package files。

## Steps

1. 创建完整 0.2.2 English package documents。
2. 创建同步 `.zh.md` mirrors。
3. 更新 v0.2 README 和 plan documents，使 0.2.2 状态为 `ready for implementation`。
4. 运行 `test-plan.md` 中的 documentation-stage verification commands。
5. 用 actual documentation-stage evidence 更新 `review.md` 和 `review.zh.md`。
6. 在 implementation 前停止。等 review approval 后再使用 `worldengine-iteration-dev`。

## Verification

Focused documentation-stage verification：

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.2-recursive-world-contract -maxdepth 1 -type f | sort
rg -n "0.2.2-recursive-world-contract|ready for implementation|WorldCell|EntityRef|WorldSpec" docs/iterations/v0.2/0.2.2-recursive-world-contract docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|concrete demo|migration|agent memory|pseudo-self" docs/iterations/v0.2/0.2.2-recursive-world-contract docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
```

Implementation verification 已在 `test-plan.md` 定义，但必须等 review approval 后添加代码时才运行。
