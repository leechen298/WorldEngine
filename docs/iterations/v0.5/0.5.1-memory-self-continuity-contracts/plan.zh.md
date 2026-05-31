# 计划

状态：review complete

## 文件

创建：

- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/README.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/README.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/intent.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/intent.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/contract.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/contract.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/technical-design.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/technical-design.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/test-plan.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/test-plan.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/plan.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/plan.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/review.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/review.zh.md`

验证后按需修改：

- 仅为准确交接修改父级 v0.5 status files。

不要触碰：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- tests
- fixtures
- migrations
- generated result artifacts
- external repositories

## 步骤

1. 读取必需 project 和 v0.5 campaign documents。
2. 读取 `0.5.0` review evidence 和 handoff。
3. 起草英文 package documents。
4. 起草语义等价的中文镜像。
5. 运行 `test-plan.md` 中的 documentation 和 scope checks。
6. 运行只读 documentation/contract evaluator。
7. 在 documentation scope 内修复任何 P1/P2。
8. 用 exact evidence 更新 `review.md` 和 `review.zh.md`。
9. 只有 checks 和 evaluator evidence 都通过时，才把本包标记为 review complete。
10. 交接给 `0.5.2-working-and-episodic-memory-substrate`。

## 停止条件

遇到以下情况必须停止并记录 blocker：

- 缺少必需 package docs 或 mirrors。
- 需要修改 implementation files。
- 某个概念必须依赖 behavior 才能成立。
- required evaluator checkpoint 不可用。
- evaluator 报告 P1 或 blocking P2。
- 历史 v0.4 evidence 被当作当前 v0.5 pass evidence。

## 验证

运行 `test-plan.md` 中的 exact commands。

## Review 更新步骤

验证后更新 `review.md` 和 `review.zh.md`，记录：

- changed files。
- commands run 和 exit status。
- test results 和 not-run rationale。
- compatibility review。
- scope review。
- subagent/evaluator findings。
- unresolved P1/P2/P3。
- final assessment。
