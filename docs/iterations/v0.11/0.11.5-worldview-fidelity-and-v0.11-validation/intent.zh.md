# 意图

英文源文件：`intent.md`。

状态：文档已起草 / 等待评审

## 问题 / 目的

v0.11 需要诚实 closeout。一个 rule-bound world 可能有有效 rules 和 legal diffs，但仍然没有保持公开 premise。本包从 public evidence 验证 immediate 和 bounded-run worldview fidelity，并记录 v0.11 结果。

## 为什么现在做

`0.11.1` 到 `0.11.4` 已创建 provider/worldview preflight、session rules、direction boundary 和 rule-compliant event/diff path。最后一个 v0.11 child 现在必须评估这些 evidence 是否支持 rule-bound world evolution closeout。

## Roadmap 关系

本包只关闭 v0.11。Agent continuity 和外部自动化验证交给 v0.12。不声明 complete MVP readiness。

## 非目标

- 不声明 provider live PASS。
- 不声明外部 Validation Client PASS。
- 不声明 Agent autonomy PASS。
- 不实现 frontend。
- 不新增 rule/event/direction feature scope。
- 不修改 `backend/worldengine/`。

## 预期交接

如果 v0.11 以 PASS 或可接受 PARTIAL 关闭，v0.12 将从具备 fidelity evidence 和明确 exclusions 的 rule-bound running world 开始。
