# 计划

Status: review complete

## 文件

创建：

- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/README.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/README.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/intent.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/intent.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/contract.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/contract.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/technical-design.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/technical-design.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/test-plan.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/test-plan.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/plan.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/plan.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/review.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/review.zh.md`

当 review evidence 支持完成后，更新：

- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `docs/iterations/v0.6/v0.6-plan.zh.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/CURRENT_STATE.zh.md`
- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/review.zh.md`

不触碰：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- migration 或 alembic 文件
- fixture 或 generated result
- external repository
- active v0.6 package 之外的 release document

## 执行步骤

1. 读取 repository guidance、project direction docs、iteration standards、v0.6
   parent docs、`0.6.0` review evidence，以及当前 WorldSpec / loader /
   runtime-context / API envelope code。
2. 起草完整 `0.6.1` package docs 和中文镜像，状态保持
   `planned / ready for review`，并保持 `implementation_authorized: no`。
3. 运行 `test-plan.md` 中的 documentation check、mirror check、required-term
   check 和 scope guard。
4. 派发或记录 read-only documentation evaluator，对已起草 package 做评审。
5. 在 documentation scope 内修复 P1/P2 finding；如果无法修复，则记录 blocker。
6. 当检查和 evaluator evidence 表明没有未解决 P1/P2 时，更新本 package 的
   `review.md` 与 `review.zh.md`，记录准确 evidence。
7. 更新 parent v0.6 status surfaces 和 mirrors，将 `0.6.1` 标记为 review
   complete，并把 active child 设置为
   `0.6.2-template-catalog-and-deterministic-generator-core`。
8. 在 parent status update 后重新运行 status 与 scope checks。

## 阶段边界

- 文档起草阶段只能创建本 package 的 docs 和 mirrors。
- 只有在 checks 与 evaluator evidence 支持 completion 后，review synchronization
  才能更新 parent v0.6 status surfaces。
- Implementation 保持 closed。`0.6.1` 不得启动 schema、service、API、frontend、
  fixture、migration、generated result 或 test implementation。

## 停止条件

如果出现以下情况，停止并记录 blocker：

- 任一必需 package file 或 mirror 缺失。
- contract 要求 concrete world content、private validation internals、
  application-specific backend behavior、live AI-provider behavior、external
  validation readiness 或 projection readiness。
- documentation command 失败，且无法在 documentation scope 内修复。
- subagent/evaluator 报告无法在 documentation scope 内修复的阻塞性 P1/P2。
- 本 package 需要修改 implementation files。
- package 与 parent docs 之间 status surface drift。

## Review 更新步骤

验证后，更新 `review.md` 和 `review.zh.md`，记录：

- changed files。
- exact commands run。
- exact results。
- compatibility review。
- scope review。
- subagent/evaluator status。
- unresolved P1/P2/P3 findings。
- final assessment。

## 验证

使用 `test-plan.md` 中准确的 documentation checks、mirror checks、status checks 和
scope guards。
