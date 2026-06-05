# Intent

英文镜像：`intent.md`。

## 问题

最新一次 current WorldEngine product surface validation 得到了混合结果：

- basic full lifecycle saved-result checker：PASS。
- Validation Client UI smoke：只证明 smoke evidence PASS，不是权威 full validation。
- WorldEngine E2E：FAIL，其中一个 dashboard archive summary scenario 失败。

这个失败用例重要，因为 archive summaries 属于可观察的 memory/history surface。如果
dashboard 不能稳定证明 runtime steps 后创建并渲染了 newer archive summary，那么当前
validation baseline 不够干净，不适合继续报告更强的 LLM-backed lifecycle evidence。

## 为什么需要这个 Package

这是一个小修复迭代，不是新的产品能力 milestone。它的目的只是通过修复验证中发现的
精确回归，恢复干净的 basic E2E baseline。

这个 repair 需要放进 concrete package，因为批准后它可能修改 frontend、backend 或
E2E implementation files。代码开始前，documentation gate 必须先定义 allowed files、
forbidden shortcuts、diagnostics、verification 和 claim boundaries。

## 已捕获的用户意图

用户希望失败状态保持可见，并且当验证问题需要修复时，通过小的、可 review 的迭代来处理。
用户不希望自己成为每个子步骤的人工调度员，也不希望为了通过验证而把大量无关实现藏进去。

因此本 package 提供一个完整 approval target：复现、诊断、修复最小已证明根因、验证、
review、close。

## 非目标

- 不实现 LLM-backed world creation 或 evolution。
- 不测试 DeepSeek live provider calls。
- 不修改 Validation Client behavior。
- 不超出失败 E2E contract 去提升 archive summary quality。
- 不实现 durable archive persistence。
- 不声明 product readiness 或 LLM-backed lifecycle readiness。
- 不把这个 regression 扩成 broad dashboard refactor。

## 期望结果

Closeout 时必须记录以下结果之一：

- `PASS`：focused E2E 通过，`make test-e2e` 通过，必要 adjacent regressions 通过，
  且 latest basic full lifecycle autonomous result 的 saved-result checker 仍通过。
- `BLOCKED`：根因需要超出本 package 的更大设计或外部依赖。
- `FAIL`：尝试修复但 verification 未通过。
