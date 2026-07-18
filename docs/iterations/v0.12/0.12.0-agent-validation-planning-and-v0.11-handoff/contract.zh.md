# Contract

英文源文件：`contract.md`。

## Public Concepts

- `v0.11 handoff`：已评审的 rule-bound world evolution slice 以 scoped `PASS`
  关闭。
- `v0.12 input`：Agent continuity 经 child authorization 后可依赖的 session、rule、
  direction、event、diff、snapshot 和 fidelity public evidence。
- `Agent continuity`：后续 v0.12 行为，其中 in-world Agent 可见地 observe、选择 action 或
  no-action、react、通过 public summaries 记忆，并跨 tick rest 或 sleep。
- `handoff caveat`：未证明的区域，必须保持显式，不能转换成 MVP PASS claim。

## Allowed Changes

- 创建并评审本 package document set。
- review 后更新 v0.12 parent docs，把 `0.12.1` 选为下一 route。
- 记录当前 session 的文档检查和 no-code-test rationale。

## Forbidden Changes

- 不修改 runtime、API、schema、frontend、checker、fixture、provider、generated
  result、Validation Client、migration、persistence 或 `backend/worldengine/`
  implementation。
- 不执行 live provider。
- 不执行外部 Validation Client。
- 不实现 Agent runtime loop、memory、rest/sleep、narrative、diagnostic、checker 或
  MVP closeout。
- 不声明 v0.11 已证明 Agent autonomy、external automation、frontend E2E、durable
  persistence、product readiness 或 complete MVP PASS。

## Compatibility Requirements

- 保留 v0.11 closeout 只在 reviewed rule-bound world evolution scope 内为 PASS。
- 在后续 package 有证据前，provider live-call 和 external Validation Client automation 仍是
  unproven。
- 区分 in-world Agents 和 external validation agents。
- 在 reviewed package 授权 implementation 前，narrative 和 diagnostic inspection 保持
  read-only。

## Out-of-Scope Follow-Ups

- Agent public state and runtime loop 属于 `0.12.1`。
- Agent memory and rest consolidation 属于 `0.12.2`。
- Narrative and diagnostic inspection 属于 `0.12.3`。
- Validation Client evidence handoff 属于 `0.12.4`。
- Full lifecycle checker/autonomous validation 属于 `0.12.5`。
- MVP release candidate closeout 属于 `0.12.6`。
