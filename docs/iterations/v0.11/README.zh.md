# v0.11 MVP 规则约束下的世界演化

英文版本：`README.md`。

状态：`closeout complete / scoped PASS`
类型：Codex `/goal` development campaign 和 iteration package root
parent_implementation_authorized: no
active_child_implementation_authorized: no
active_child_evidence_execution_authorized: no

## 目标

v0.11 基于 v0.10 的 runnable session，让世界变化变得有原因、可检查。

通俗地说：创建出来的世界不能只是 tick counter 增加。它要有 public parameters 和
rules；用户的自然语言引导只能作为 world-level pressure；WorldEngine 要生成或选择符合规则的
events，应用 public diffs，并让验证者看得懂世界为什么变了。

## 来自 v0.10 的交接

v0.10 预期交接：

- public MVP manifest 和 checker handoff skeleton。
- world session identity 和 state store。
- worldview-to-session creation。
- bounded runtime controls。
- event/snapshot evidence。
- dashboard create/run/inspect flow。

v0.11 假设这条纵向链路已经存在。如果不存在，v0.11 必须记录 handoff blocker，不能绕过
session 或 evidence contracts。

## 范围

通过子包评审后，v0.11 允许做：

- WorldEngine-owned provider live preflight for world evolution inputs。
- provider-backed 或明确标记 fallback 的 worldview generation。
- public structured world parameters、rules、constraints 和 boundaries。
- natural-language direction queue，只影响 world-level pressure、environment trends、
  event candidates、probabilities 或 constraints。
- rule-compliant event candidate generation/evaluation/application。
- 与 rules 和 parameters 关联的 public diff/replay evidence。
- immediate 和 bounded-run worldview fidelity checks。
- 供 Validation Client 调试 rule/evolution 的 discoverability 和 evidence fields。

v0.11 禁止做：

- 用户 guidance 不得直接指定 final fact。
- 不做玩家投放物品、直接触发细节事件或 player-as-world-entity gameplay。
- 用户 guidance 不得直接修改 Agent private memory、goal、personality、skill、injury、
  death 或 inventory。
- 不得把“让这个 Agent 现在死亡”这类用户命令直接复制为最终世界事实；“这个 Agent 可能面临雷击风险”
  这类风险仍必须通过天气、位置、概率、生命状态和 rules 评估。
- 不做 hidden rule execution 或 private evaluator oracle。
- evidence 不得包含 raw prompts、raw provider responses、provider traces、secrets、
  raw thought、private Agent memory 或 hidden context。
- 不实现完整 Agent autonomy。
- 不在本仓库存 concrete demo-world seed data。
- 不在本仓库实现 Validation Client。

## 计划子包

`v0.11-plan.md` 是详细 planned-package specification。planned packages 只是路线规格。

计划顺序：

1. `0.11.0-rule-bound-evolution-planning-and-v0.10-handoff`
2. `0.11.1-provider-and-worldview-generation-preflight`
3. `0.11.2-structured-world-rules-and-parameters`
4. `0.11.3-natural-language-direction-queue-and-boundary`
5. `0.11.4-rule-compliant-event-generation-and-diffs`
6. `0.11.5-worldview-fidelity-and-v0.11-validation`

## 当前状态

当前 active child package：
none；v0.11 closeout complete。

当前 route：

```text
v0.11-closeout-complete-handoff-to-v0.12-parent
```

Implementation authorization: no.

Evidence execution authorization: no.

Closeout result：rule-bound world evolution scope 内 scoped `PASS`。Handoff route：
v0.12 parent `v0.12-parent-documentation-ready-for-review`，从
`0.12.0-agent-validation-planning-and-v0.11-handoff` 开始。

## 验证边界

v0.11 PASS 证明 rule-bound world evolution，不证明 living Agent autonomy 或完整 MVP close。
一个有效的 v0.11 result 应该展示：

```text
runnable session -> rules/params -> user direction -> legal event/diff -> bounded-run fidelity evidence
```

Direction boundary 是验证目标的一部分。PASS 需要证据证明：被接受的用户 guidance 仍是
world-level pressure，被拒绝的 guidance 没有修改 final facts 或 Agent private state。
