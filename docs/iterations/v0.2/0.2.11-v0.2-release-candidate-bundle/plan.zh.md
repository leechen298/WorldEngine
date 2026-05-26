# Plan

英文版本：`plan.md`

## 文件

Review 后创建：

- `docs/iterations/v0.2/v0.2-release-candidate-bundle.md`
- `docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md`
- `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md`
- `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md`

Review 后修改：

- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- 如发现 new 或 changed findings，修改 `docs/iterations/v0.2/findings.md`。
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`
- 本包的 `README.md`、`README.zh.md`、`review.md` 和 `review.zh.md`。

不要触碰：

- runtime implementation files。
- schema implementation files。
- API route files。
- frontend implementation files。
- fixture files。
- migration files。
- test implementation files。
- `backend/worldengine/`。
- external repository paths 或 private validation internals。

## 步骤

1. 阅读 approved package documents。
2. 阅读 v0.2 package reviews、evidence index、boundary audit、compatibility
   review、findings、release docs、roadmap 和 scope boundaries。
3. 构建 release-candidate claim-to-evidence matrix。
4. 创建 release-candidate bundle 和中文 mirror。
5. 使用现有 template structure 创建 final review bundle 和中文 mirror。
6. 用 release-candidate evidence 更新 v0.2 release draft，同时保留 not-final status。
7. 如果发现 evidence gaps，记录 new 或 changed findings。
8. 运行 `test-plan.md` 中的 documentation verification checks。
9. 如实更新本包 review evidence 和 status docs。

## 验证

必需：

- `git diff --check`
- required file presence checks。
- package mirror presence checks。
- status consistency grep。
- release-status wording check。
- evidence traceability check。
- concrete demo anchor sweep with abstract classification only。
- changed-file scope guard。

不计划：

- backend tests。
- frontend tests。
- API smoke。
- E2E。
- Agent smoke。
- runtime 或 schema execution tests。

只有 changed-file set 保持 documentation-only 时，上述 not-planned tests 才有效。

## 退出条件

- Release-candidate bundle ready for human / ChatGPT review。
- Final review bundle complete，并且 mirrors template。
- Release docs 说明 candidate evidence，但不声明 final release。
- P1/P2 findings 清楚列出，并在 resolved 或 explicitly accepted 前阻塞 final closeout。
- Changed files 保持在 approved documentation scope 内。
