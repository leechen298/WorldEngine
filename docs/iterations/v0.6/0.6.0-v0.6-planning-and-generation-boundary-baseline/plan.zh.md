# 计划

状态：planned / ready for review

## 文件

创建：

- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `docs/iterations/v0.6/v0.6-plan.zh.md`
- `docs/iterations/v0.6/GOAL_RUNNER.md`
- `docs/iterations/v0.6/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/CURRENT_STATE.zh.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/review.zh.md`
- `docs/iterations/v0.6/0.6.0-v0.6-planning-and-generation-boundary-baseline/`
  下的全部英文和中文文件。

修改：

- `docs/iterations/v0.6/**` 之外不修改任何文件。

不要触碰：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- migrations 或 alembic files
- fixtures 或 generated results
- external repositories
- `docs/iterations/v0.6/**` 之外的任何现有文件

## 有序执行步骤

1. 读取 repository guidance、project direction、roadmap、iteration standards、
   v0.5 final closeout 和当前 WorldSpec/runtime-context code。
2. 起草 v0.6 parent campaign docs 和 package sequence。
3. 起草 `0.6.0` package docs 和中文镜像。
4. 保持所有 status values 为 `planned / ready for review`，并保持
   `implementation_authorized: no`。
5. 运行 `test-plan.md` 中的 documentation checks。
6. 用实际 command evidence 更新 parent 和 child `review.md` / `review.zh.md`。
7. 保持 implementation authorization closed，并交接给 documentation review。

## 阶段边界

- Documentation drafting 只能创建 `docs/iterations/v0.6/**`。
- Documentation review 只有在 checks 和 evaluator evidence 支撑时，才能更新 review
  evidence 和 status。
- Implementation 只能在后续 child package 完成评审并记录
  `implementation_authorized: yes` 后开始。

## 停止条件

出现以下情况时停止并记录 blocker：

- 缺少任何 required file 或 mirror。
- v0.6 planning 需要 concrete world content、private validation internals 或
  application-specific backend behavior。
- 命令失败且无法在 documentation scope 内修复。
- `0.6.0` 期间需要修改 implementation files。
- 需要 evaluator evidence 才能做更强 status claim，但 evidence 不可用。

## Review 更新步骤

验证后更新 `review.md` 和 `review.zh.md`，记录：

- changed files。
- exact commands run。
- exact results。
- compatibility review。
- scope review。
- evaluator status。
- unresolved P1/P2/P3 findings。
- final assessment。

## 验证

使用 `test-plan.md` 中的 exact documentation checks 和 scope guard。
