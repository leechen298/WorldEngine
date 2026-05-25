# 计划

英文版本：`plan.md`

## 文件

创建：

- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/README.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/README.zh.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/intent.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/intent.zh.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/contract.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/contract.zh.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/technical-design.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/test-plan.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/plan.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/plan.zh.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/review.md`
- `docs/iterations/v0.2/0.2.6-iteration-workflow-and-plan-reset/review.zh.md`
- `docs/iterations/v0.2/00-chatgpt-plan.md`
- `docs/iterations/v0.2/00-chatgpt-plan.zh.md`
- `docs/iterations/v0.2/development-workflow.md`
- `docs/iterations/v0.2/development-workflow.zh.md`
- `docs/iterations/v0.2/final-review-bundle-template.md`
- `docs/iterations/v0.2/final-review-bundle-template.zh.md`

修改：

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`
- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- historical `docs/iterations/v0.2/**` files，仅用于抽象化 concrete demo details。

不要触碰：

- runtime code。
- schema code。
- API code。
- frontend code。
- backend tests。
- fixtures。
- external repositories。
- 0.2.7 到 0.2.12 package directories。

## 步骤

1. 读取 required active docs 和 0.2.5 review evidence。
2. 创建 0.2.6 package documents，并补齐中文镜像。
3. 增加 automation workflow、ChatGPT seed plan 和 review bundle template。
4. 重写 v0.2 index 和 plan，让 0.2.6 成为 workflow/reset，让 0.2.7 到
   0.2.12 成为 planned quasi-package specifications。
5. 只更新 roadmap 的 v0.2 entries。
6. 将 release docs 更新为 draft / planned / not released。
7. 抽象化 v0.2 iteration docs 和 v0.2 release docs 中的 historical concrete
   demo details。
8. 运行 documentation verification commands。
9. 把 evidence 记录到本 package 的 `review.md` 和 `review.zh.md`。

## 验证

- `git status --short --branch`
- `git diff --check`
- 0.2.7 到 0.2.12 的 Detailed Plan Acceptance Gate。
- 使用 temporary untracked pattern file 做 concrete demo anchor sweep。
- release-status wording check。
