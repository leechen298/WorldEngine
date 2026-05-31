# 执行计划

## 有序执行步骤

1. 阅读父级 v0.4 docs 和本包 docs。
2. 在授权实现前确认 `CURRENT_STATE.md` 中的当前 route 与 `implementation-authorization-review` 匹配；记录授权后确认与 `loop-orchestration-implementation` 匹配；否则在 `review.md` 记录 route mismatch。
3. 从 `contract.md` 确认允许和禁止的文件类别。
4. 在 `GOAL_RUNNER.md` 要求时运行 documentation / contract evaluator。
5. 如果本包是 documentation-only，只更新获批文档并保持 implementation authorization 关闭。
6. 如果本包是 mixed 或 code，且 review 已授权实现，只做获批实现变更。
7. 运行 `test-plan.md` 中的精确验证命令。
8. 运行必需 subagent/evaluator checkpoints 并分类 findings。
9. 更新 `review.md`，记录 changed files、commands、test results、compatibility review、scope review、findings 和 final assessment。
10. 只有本包达到 reviewed route status 后，才更新父级 `CURRENT_STATE.md`。

## 阶段边界

- 文档阶段只在 package docs 评审后结束。
- mixed/code package 只有记录 `implementation_authorized: yes` 后才进入实现阶段。
- 验证阶段没有当前会话命令证据时不得产生 pass claim。
- closeout 阶段不能带未解决 P1 或未接受 P2 推进。

## 停止条件

- 未完成必需 evaluator checkpoint 时停止。
- 发现 P1 或未解决 P2 时停止。
- 如果需要 active contract 未授权的文件类别，停止并记录 blocker。
- 不得用历史证据冒充当前会话通过证据。

如果必需 evaluator checkpoint 不可用，或 git state 显示越界修改，也必须停止。

## Review 更新步骤

package handoff 前必须更新 `review.md`。只有 review evidence 支持新 child status 后，才允许更新父级状态。
