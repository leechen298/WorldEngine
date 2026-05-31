# 0.6.7 Dashboard Generation Preview 与 E2E Smoke

状态：review complete
类型：mixed
implementation_authorized: yes

## 目标

定义并且仅在 review authorization 后实现 dashboard-facing generation preview
workflow。该 workflow 基于现有 v0.6 generation API，让 operator 提交 generic
template preview request、检查 validation metadata、查看 bounded runtime-readiness
output，并通过 focused frontend 与 browser E2E smoke tests 验证。

## 范围

Documentation stage：

- 创建本 package 和中文镜像。
- 定义 dashboard generation preview UI、API-client 和 E2E-smoke boundaries。
- 为 active child state 更新 parent v0.6 status surfaces。

Implementation stage，仅在 authorization 后：

- 为现有 generation preview、regeneration 和 runtime-readiness routes 添加 frontend
  API client types/functions。
- 添加 focused dashboard generation preview component，并挂载到现有 dashboard page。
- 添加 focused component/API-client tests 和 dashboard generation flow browser E2E
  smoke。
- 更新本 package review evidence 和 parent status surfaces。

Forbidden：

- 不修改 backend schema/API/runtime implementation，除非重新打开 documentation review。
- 不改变 runtime tick/time/event semantics。
- 不自动 mutation、activation、persistence、migration 或 repository storage generated specs。
- 不添加 concrete demo-world、story、private validation oracle、external validation
  runner、projection app、live provider/network/prompt execution、credential 或
  `backend/worldengine/**` work。
- 不声明 dashboard preview、E2E smoke、generation quality、product readiness、
  projection readiness、external validation readiness、autonomous validation、release
  readiness 或 full runtime migration 已完成。

## 交付物

- 完整 package docs 和中文镜像。
- 已评审 dashboard generation preview contract。
- Authorization 后的 frontend API-client/component tests、browser E2E smoke、
  focused backend generation API compatibility evidence、build evidence、static checks、
  scope checks 和 evaluator checkpoints。
- Review evidence 需要区分 dashboard preview smoke 与 product、generation-quality、
  external validation、projection、autonomous 和 release readiness。

## 文档

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## 当前评估

本 package 已 review complete。修复 readiness-diagnostics P2 后，
documentation/contract、implementation-scope、code-review、validation、E2E、build、
backend compatibility、browser smoke 和 scope checks 均已通过。它将 dashboard
preview 与 E2E smoke evidence 交接给
`0.6.8-v0.6-evidence-and-compatibility-audit`。
