# Plan

英文版本：`plan.md`

## 文件

Documentation stage 创建：

- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/README.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/README.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/intent.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/intent.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/contract.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/contract.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/technical-design.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/test-plan.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/plan.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/plan.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/review.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/review.zh.md`

Documentation stage 修改：

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Review 后的 planned audit-stage creates：

- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/evidence-index.zh.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/boundary-audit.zh.md`

Review 后的 planned audit-stage may modify：

- `docs/iterations/v0.2/findings.md`
- 本 package 的 `review.md` 和 `review.zh.md`
- 如果 audit 关闭或更新 status findings，可修改 v0.2 status docs。

不得触碰：

- runtime implementation。
- schema implementation。
- API routes 或 response code。
- frontend files。
- tests 或 fixtures。
- migrations。
- `backend/worldengine/`。
- external repositories。
- unrelated iteration packages，但可以 read-only evidence inspection。

## Documentation-Stage Steps

1. 阅读 repository guidance、v0.2 plan/index docs、templates、boundary docs、
   current implementation docs、completed package reviews、contracts 和 findings。
2. 创建 0.2.9 package documents，并保持 English / Chinese mirrors 同步。
3. 让 acceptance 和 verification requirements 具体且可测试。
4. 标记 assumptions 和 open risks。
5. 在本 README 和 v0.2 milestone index 中把 0.2.9 status 设为
   `ready for review`。
6. 同步 detailed v0.2 plan 和 Chinese mirrors。
7. 运行 documentation checks。
8. 在 `review.md` 和 `review.zh.md` 记录 documentation-stage evidence。

## Approval 后的 Audit-Stage Steps

1. 按顺序重读本 package：`intent.md`、`contract.md`、`technical-design.md`、
   `test-plan.md`、`plan.md`、`review.md`。
2. 从 completed v0.2 packages 和 current milestone documents 构建 evidence
   index。
3. 从 scope、external fixture、current implementation、backend implementation
   和 package review evidence 构建 boundary audit。
4. 运行 English / Chinese mirrors 的 status consistency checks。
5. 使用 untracked temporary pattern file 运行 concrete demo anchor sweep。
6. 为 missing evidence、boundary concerns 和 status drift 更新 findings。
7. 用 exact commands 和 results 更新 review evidence。

## Verification

Documentation-stage verification：

- `git status --short --branch`
- `git diff --check`
- required package mirror file check。
- package README 和 v0.2 index/plan docs 的 status consistency grep。

Audit-stage verification：

- `test-plan.md` 中的 documentation checks。
- 使用 shell commands 的 link/path sanity checks。
- changed-file scope guard。
- concrete demo anchor sweep。
