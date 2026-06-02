# 0.8.0 Planning And v0.7 Handoff Baseline

状态：review complete
类型：documentation-only
implementation_authorized: no
evidence_execution_authorized: no

## 目标

把 v0.8 parent roadmap 中的 `0.8.0` 条目转换成具体的 documentation-only child
package，安全地把已评审的 campaign structure、当前 v0.7 交接状态、minimum
working-state boundaries 和 external-validation boundaries 交给
`0.8.1-minimum-working-state-contract`。

本 package 保持 implementation 和 evidence execution 关闭。它只准备 goal campaign
route；不实现 contracts、schemas、APIs、checkers、frontend behavior、fixtures、
migrations、external validation functions 或 external applications。

## 范围

允许范围：

- 创建本 child package document set 及中文镜像。
- Parent review 后同步 v0.8 route/status surfaces。
- 把当前 v0.7 handoff 记录为 historical context only。
- 用当前 `0.7.9` checker/docs repair 状态替换过时的 v0.7 post-closeout blocker
  表述，同时保留 v0.8 non-claims。
- 定义 `0.8.0` documentation baseline work 与后续 `0.8.1` minimum working-state
  contract work 的边界。
- 记录 documentation checks、subagent/evaluator evidence、compatibility review、
  scope review 和 unresolved findings。

禁止范围：

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、
  fixture、migration、external repository、generated result 或 `backend/worldengine/`
  implementation files。
- 不实现 minimum working-state contracts、observable surfaces、schemas、checkers、
  services、APIs、UI、persistence、external validation behavior、projection
  application behavior 或 tests。
- 不添加 concrete external validation world data、concrete world names、maps、
  characters、locations、resources、story rules、seed data、private transcripts、UI
  selectors、private repository paths、hidden reset APIs、live provider behavior 或
  application-specific backend logic。
- 不声明当前 v0.8 runtime、API、frontend、E2E、Agent smoke、autonomous、external
  validation、external consumer、product readiness、minimum working-state readiness
  或 final release behavior passed。

## 交付物

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`
- 每个 package document 的中文镜像。
- Active child selection 所需的 parent route/status synchronization。

## 状态清单

- [x] Package documents 已起草。
- [x] Chinese mirrors 已起草。
- [x] Documentation checks 已完成。
- [x] Subagent/evaluator review 已完成。
- [x] Review evidence 已更新。
- [x] Handoff to `0.8.1` 已记录。

## 最终评估状态

当前值：`review complete`。

本 package 已 review complete，并把已评审的 campaign structure、当前 v0.7
checker/docs clean-pass handoff context、minimum working-state boundaries、
external-validation boundaries 和 implementation-closed status 交给
`0.8.1-minimum-working-state-contract`。
