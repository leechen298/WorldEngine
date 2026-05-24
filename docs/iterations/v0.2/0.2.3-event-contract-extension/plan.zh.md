# Plan

英文版本：`plan.md`。

## Files

Documentation stage 创建：

- `docs/iterations/v0.2/0.2.3-event-contract-extension/README.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/README.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/intent.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/intent.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/contract.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/contract.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/technical-design.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/test-plan.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/plan.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/plan.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/review.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/review.zh.md`

Documentation stage 修改：

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Review approval 后允许的 implementation files：

- `backend/app/schemas/event.py`
- `backend/app/tests/test_event_schema_compat.py`
- closeout 时本 package 的 `review.md` 和 `review.zh.md`

Documentation stage 不要触碰：

- `backend/`
- `frontend/`
- `backend/worldengine/`
- `docs/iterations/v0.2/0.2.1-project-north-star/`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/`
- 0.2.4 package files。

## Steps

1. 创建完整 0.2.3 English package documents。
2. 创建同步的 `.zh.md` mirrors。
3. 更新 v0.2 README 和 plan documents，让 0.2.3 变为 `ready for implementation`。
4. 运行 `test-plan.md` 中的 documentation-stage verification commands。
5. 用实际 documentation-stage evidence 更新 `review.md` 和 `review.zh.md`。
6. 在 implementation 前停止。只有当 implementation 被明确请求时，才使用
   `worldengine-iteration-dev`。

## Verification

Focused documentation-stage verification：

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.3-event-contract-extension -maxdepth 1 -type f | sort
rg -n "0.2.3-event-contract-extension|ready for implementation|EventRef|refs|Event Contract|backward compatible|payload|EventPage|EventStep|EventStepPage" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|village|migration|agent memory|pseudo-self|referential integrity|resolve refs|frontend|API route" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
git status --porcelain=v1 -uall | awk '{print $2}' | rg -v '^docs/iterations/v0.2/'
```

Implementation verification 定义在 `test-plan.md`，但必须等 review approval 后新增代码时才运行。
