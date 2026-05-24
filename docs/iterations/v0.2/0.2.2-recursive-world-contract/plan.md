# Plan

## Files

Create during documentation stage:

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

Modify during documentation stage:

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Allowed implementation files after review:

- `backend/app/schemas/entity.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/tests/test_world_cell_schema.py`

Do not touch during documentation stage:

- `backend/`
- `frontend/`
- `backend/worldengine/`
- `docs/iterations/v0.2/0.2.1-project-north-star/`
- 0.2.3 package files.

## Steps

1. Create the complete 0.2.2 English package documents.
2. Create synchronized `.zh.md` mirrors.
3. Update v0.2 README and plan documents so 0.2.2 is `ready for review`.
4. Run documentation-stage verification commands from `test-plan.md`.
5. Update `review.md` and `review.zh.md` with actual documentation-stage
   evidence.
6. Stop before implementation. Wait for review approval before using
   `worldengine-iteration-dev`.

## Verification

Focused documentation-stage verification:

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.2-recursive-world-contract -maxdepth 1 -type f | sort
rg -n "0.2.2-recursive-world-contract|ready for review|WorldCell|EntityRef|WorldSpec" docs/iterations/v0.2/0.2.2-recursive-world-contract docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|village|migration|agent memory|pseudo-self" docs/iterations/v0.2/0.2.2-recursive-world-contract docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
```

Implementation verification is defined in `test-plan.md` but must not run
until code is added after review approval.
