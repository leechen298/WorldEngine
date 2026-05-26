# Plan

英文版本：`plan.md`

## Files

Documentation stage 创建：

- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/README.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/README.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/intent.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/intent.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/contract.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/contract.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/technical-design.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/test-plan.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/plan.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/plan.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/review.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/review.zh.md`

Documentation stage 修改：

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Review approval 后 potential implementation-stage files：

- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`
- `docs/iterations/v0.2/findings.md`
- 本包的 `README.md`、`README.zh.md`、`review.md` 和 `review.zh.md`。

不得触碰：

- runtime implementation files。
- schema implementation files。
- API route files。
- frontend implementation files。
- fixture files。
- migration files。
- test implementation files。
- `backend/worldengine/`。
- external repository paths 或 private validation internals。

## Steps

1. 阅读 repository guidance、iteration standards、v0.2 milestone index、v0.2
   detailed plan、0.2.11 release-candidate bundle 和 findings ledger。
2. Draft 0.2.12 package docs，并明确 approval gates、blocker rules、assumptions、
   risks 和 verification commands。
3. 创建 synchronized Chinese mirrors。
4. 在 package README、milestone index 和 detailed plan mirrors 中把 0.2.12 status
   设为 `ready for review`。
5. 运行 `test-plan.md` 中的 documentation-stage checks。
6. 在 `review.md` 和 `review.zh.md` 中记录 documentation-stage evidence。

## Verification

Documentation stage 必须运行：

- `git diff --check`
- package mirror presence check。
- status consistency grep。
- closeout gate wording grep。
- changed-file scope guard。
- trailing whitespace grep。
- package file listing。

不计划运行：

- backend tests。
- frontend tests。
- API smoke。
- E2E。
- Agent smoke。
- runtime 或 schema execution tests。

只有当 changed-file set 保持 documentation-only 时，这些 not-planned checks 才有效。

## Exit Criteria

- 0.2.12 package docs complete。
- Acceptance 和 verification requirements 可测试。
- Assumptions 和 open risks 明确。
- English 和 Chinese mirrors 同步。
- Package README 和 v0.2 milestone index 将 0.2.12 标记为 `ready for review`。
- 没有修改 runtime、schema、API、frontend、fixture、migration 或 test implementation files。
