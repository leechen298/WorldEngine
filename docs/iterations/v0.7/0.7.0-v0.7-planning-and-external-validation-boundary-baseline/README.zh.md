# 0.7.0 Planning And External Validation Boundary Baseline

状态：review complete
Type: documentation-only
implementation_authorized: no

## Goal

将 v0.7 parent roadmap 中的 `0.7.0` 转换为具体、可 review 的 documentation-only child
package，并把已 review 的 campaign structure、v0.6 handoff context、external-validation boundary
和 projection-consumer boundary 安全交接给 `0.7.1`。

本 package 必须保持 implementation closed。它只准备 goal campaign route；不实现 contracts、schemas、
APIs、checkers、frontend behavior、fixtures、migrations、external validation suites 或 projection
applications。

## Scope

Allowed scope:

- 创建本 child package document set 及中文镜像。
- 在 parent review 后同步 parent v0.7 route/status surfaces。
- 仅把 v0.6 handoff 记录为 historical context。
- 定义 `0.7.0` documentation baseline work 与后续 `0.7.1` public contract work 的边界。
- 记录 documentation checks、subagent/evaluator evidence、compatibility review、scope review 和
  unresolved findings。

Forbidden scope:

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、migration、
  external repository、generated result 或 `backend/worldengine/` implementation files。
- 不实现 report schemas、redaction checkers、contract bundles、readiness manifests、projection
  endpoints 或 quality regression tooling。
- 不加入 concrete external validation world data、private oracle details、UI selectors、hidden reset
  APIs、private fixture paths、live provider behavior 或 application-specific backend logic。
- 不声明当前 v0.7 runtime、API、frontend、E2E、Agent smoke、autonomous、external validation、
  projection readiness、product readiness 或 final release behavior passed。

## Deliverables

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`
- 每个 package document 的中文镜像。
- active child selection 对应的 parent route/status synchronization。

## Status Checklist

- [x] Package documents drafted.
- [x] Chinese mirrors drafted.
- [x] Documentation checks complete.
- [x] Subagent/evaluator review complete.
- [x] Review evidence updated.
- [x] Handoff to `0.7.1` recorded.

## Final Assessment State

Current value: `review complete`.

This package is review complete and hands off to
`0.7.1-public-validation-and-projection-contracts`. Implementation remains closed.
