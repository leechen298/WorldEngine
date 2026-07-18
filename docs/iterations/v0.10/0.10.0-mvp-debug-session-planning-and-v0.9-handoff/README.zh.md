# 0.10.0 MVP 调试会话规划与 v0.9 交接

英文版本：`README.md`。

状态：`review complete`
类型：documentation-only
implementation_authorized: no
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

创建第一个具体 v0.10 child package，并记录 v0.9 blocked LLM-backed lifecycle
foundation 如何成为 MVP session 输入，而不是 release blocker。

本包保持 implementation 关闭。它确认 v0.10 从已评审的 MVP parent plan
开始，把产品路径收窄到一条可调试 session slice，并交接给
`0.10.1-mvp-public-manifest-and-debug-handoff`，由该 mixed package 先创建完整
文档集，再开始任何 manifest 或 API 工作。

## 范围

允许范围：

- 创建本 `0.10.0` child package 文档集和中文镜像。
- 将 v0.9 final BLOCKED closeout 记录为历史交接上下文。
- 在 parent review 后同步 v0.10 parent route/status surfaces。
- 只把 `0.10.1` 选为 documentation-package-needed。
- 保持 v0.10 implementation、evidence execution、provider live call 和
  external validation 未授权。
- 记录 documentation checks、subagent/evaluator findings、compatibility
  review、scope review 和 unresolved findings。

禁止范围：

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、
  fixture、migration、generated result、external repository、Validation Client、
  provider configuration 或 `backend/worldengine/` implementation files。
- 不运行 live provider call、API smoke、E2E、autonomous validation、
  generated-result rewrite、checker result generation 或 external Validation Client
  flow。
- 不实现 manifest changes、session storage、worldview session creation、bounded
  runtime controls、dashboard session flow、validation repair、Agent autonomy 或
  MVP closeout behavior。
- 不存储、展示、记录或导出 API keys、authorization headers、raw prompts、raw
  provider requests/responses、raw provider traces、raw thought、private Agent memory、
  hidden context 或 private evaluator data。
- 不声明 v0.10 runnable session PASS、MVP PASS、provider readiness PASS、
  dashboard PASS、external validation PASS 或 product readiness。

## Deliverables

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`
- 每个 package document 的中文镜像。
- Parent v0.10 status synchronization，将 `0.10.1` 选为下一个 documentation
  package。

## 状态清单

- [x] Package documents drafted。
- [x] Chinese mirrors drafted。
- [x] Documentation checks complete。
- [x] Subagent/evaluator review complete。
- [x] Review evidence updated。
- [x] Handoff to `0.10.1` recorded。

## Final Assessment State

当前值：`review complete`。

本包 review complete，并把已评审的 v0.10 campaign structure、v0.9 BLOCKED handoff
context、MVP debug-session stop rules 和 implementation-closed status 交接给
`0.10.1-mvp-public-manifest-and-debug-handoff`。该 child docs 已被选中，但尚未创建。
