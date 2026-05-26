# Plan

Status: ready for review

英文版本：`plan.md`。

## Files

Create during documentation stage:

- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/README.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/README.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/intent.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/intent.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/contract.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/contract.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/technical-design.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/test-plan.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/plan.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/plan.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/review.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/review.zh.md`

Modify during documentation stage:

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Planned implementation-stage creates:

- `docs/contracts/entity-ref-contract.md`
- `docs/contracts/worldcell-contract.md`
- `docs/contracts/worldspec-contract.md`

Planned implementation-stage may modify:

- `backend/app/tests/test_world_cell_schema.py`
- `backend/app/tests/test_worldspec_schema_smoke.py`
- `backend/app/schemas/entity.py` only for approved additive clarifications。
- `backend/app/schemas/world_cell.py` only for approved additive clarifications。
- this package's `review.md` and `review.zh.md`。

Do not touch:

- runtime services。
- API routes。
- frontend files。
- fixtures or fixture data。
- migrations。
- `backend/worldengine/`。
- external repositories。
- unrelated iteration packages。

## Documentation-Stage Steps

1. 阅读 required repository、milestone、template、schema、test 和 boundary documents。
2. 创建带 English 和 Chinese mirrors 的 0.2.7 package documents。
3. 让 acceptance 和 verification requirements concrete and testable。
4. 标记 assumptions 和 open risks。
5. 在本 README 和 v0.2 milestone index 中将 0.2.7 status 设为 `ready for review`。
6. 运行 documentation checks。
7. 在 `review.md` 和 `review.zh.md` 中记录 documentation-stage evidence。

## Implementation-Stage Steps After Approval

1. 按顺序重新阅读本 package：`intent.md`、`contract.md`、`technical-design.md`、`test-plan.md`、`plan.md`、`review.md`。
2. 添加 EntityRef、WorldCell 和 WorldSpec contract docs。
3. 将 current schema tests 映射到 acceptance criteria。
4. 只添加缺失的 domain-neutral tests。
5. 只有 approved contract 要求时才修改 schema code。
6. 运行 `test-plan.md` 中的 command matrix。
7. 对 touched docs and tests 运行 concrete demo anchor sweep。
8. 用 actual implementation evidence 更新 `review.md` 和 `review.zh.md`。

## Verification

Documentation-stage verification:

- `git status --short --branch`
- `git diff --check`

Implementation-stage verification:

- `test-plan.md` 中的 focused schema pytest commands。
- `make check-backend`。
- 如果 schema code changes，运行 full backend app tests。
- 对 touched docs and tests 运行 concrete demo anchor sweep。
