# Plan

英文版本：`plan.md`

## 文件

Documentation stage 创建：

- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/README.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/README.zh.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/intent.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/intent.zh.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/contract.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/contract.zh.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/technical-design.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/test-plan.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/plan.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/plan.zh.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.zh.md`

Documentation stage 修改：

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Planned implementation-stage creates：

- `docs/contracts/event-ref-contract.md`

Planned implementation-stage may modify：

- `backend/app/tests/test_event_schema_compat.py`
- `backend/app/schemas/event.py`，仅用于 approved additive clarifications。
- 本 package 的 `review.md` 和 `review.zh.md`。

不得触碰：

- runtime services。
- API routes。
- frontend files。
- fixtures 或 fixture data。
- migrations。
- `backend/worldengine/`。
- external repositories。
- unrelated iteration packages。

## Documentation-Stage Steps

1. 阅读 required repository、milestone、template、schema、test 和 boundary
   documents。
2. 创建 0.2.8 package documents，并保持 English / Chinese mirrors 同步。
3. 让 acceptance 和 verification requirements 具体且可测试。
4. 标记 assumptions 和 open risks。
5. 在本 README 和 v0.2 milestone index 中把 0.2.8 status 设为
   `ready for review`。
6. 运行 documentation checks。
7. 在 `review.md` 和 `review.zh.md` 记录 documentation-stage evidence。

## Approval 后的 Implementation-Stage Steps

1. 按顺序重读本 package：`intent.md`、`contract.md`、`technical-design.md`、
   `test-plan.md`、`plan.md`、`review.md`。
2. 新增 EventRef contract doc。
3. 将 current event schema compatibility tests 映射到 acceptance criteria。
4. 只添加缺失的 domain-neutral tests。
5. 只有 approved contract 要求时才修改 event schema code。
6. 运行 `test-plan.md` 中的 command matrix。
7. 对 touched docs 和 tests 运行 concrete demo anchor sweep。
8. 用 actual implementation evidence 更新 `review.md` 和 `review.zh.md`。

## Verification

Documentation-stage verification：

- `git status --short --branch`
- `git diff --check`

Implementation-stage verification：

- `test-plan.md` 中的 focused event schema pytest commands。
- `make check-backend`。
- 如果 schema code changes，运行 full backend app tests。
- 对 touched docs 和 tests 运行 concrete demo anchor sweep。
