# 0.9.0 v0.9 规划与 v0.8 交接基线

英文原文：`README.md`。

状态：review complete
类型：documentation-only
implementation_authorized: no
evidence_execution_authorized: no
provider_live_call_authorized: no

## 目标

把 v0.9 父级路线图转换为第一个具体子包，并在 provider、runtime、
checker 或证据执行工作开始前记录 v0.8 交接基线。

本包保持实现关闭。它确认 v0.9 起点位于已证明的基础生命周期之后，
但尚未授权任何 LLM-backed provider smoke、LLM-backed world generation、
rule-linked evolution、Agent continuity consolidation、narrative projection、
diagnostic dialogue、checker、fixture 或 Validation Client handoff 实现。

## 范围

允许范围：

- 创建本子包文档集和中文镜像。
- 在父级 review 后同步 v0.9 父级 route/status 表面。
- 将 v0.8 交接事实记录为历史基线。
- 确认 basic full-lifecycle evidence 只能作为 handoff context 引用。
- 保持 LLM-backed lifecycle validation 为 `BLOCKED`，直到当前会话的包级证据
  证明其他状态。
- 定义 `0.9.0` 文档基线工作与后续
  `0.9.1-provider-live-smoke-and-redaction-boundary` 工作之间的边界。
- 记录文档检查、subagent/evaluator 证据、兼容性 review、范围 review 和
  unresolved findings。

禁止范围：

- 不修改 runtime、schema、API、frontend、backend test、checker
  implementation、fixture、migration、generated result、external repository、
  Validation Client、provider configuration 或 `backend/worldengine/`
  implementation 文件。
- 不运行 live provider calls 或 evidence execution。
- 不实现 provider smoke、LLM-backed world creation、world rules、runtime run
  controls、user direction、event legality、Agent continuity、consolidation、
  narrative projection、diagnostic dialogue、checker support、fixtures、
  scorecards 或 Validation Client handoff behavior。
- 不存储、展示或导出 API keys、authorization headers、raw prompts、raw
  provider responses、raw provider traces、private Agent memory、raw thought、
  chain-of-thought、hidden context 或 private evaluator data。
- 不声称 LLM-backed lifecycle PASS、product readiness、external validation
  PASS、provider readiness PASS、runtime PASS、API PASS、frontend PASS、E2E
  PASS、Agent smoke PASS、autonomous PASS、generation-quality PASS 或
  human-quality simulation。

## 交付物

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`
- 每个包文档的中文镜像。
- 面向下一个子包选择的父级 route/status 同步。

## 状态清单

- [x] Package documents drafted.
- [x] Chinese mirrors drafted.
- [x] Documentation checks complete.
- [x] Subagent/evaluator review complete.
- [x] Review evidence updated.
- [x] Handoff to `0.9.1` recorded.

## 最终评估状态

当前值：`review complete`。

本包 review complete，并把已 review 的 v0.9 campaign structure、v0.8 basic
lifecycle handoff context、LLM-backed blocker taxonomy、provider/redaction stop
rules，以及 implementation-closed status 交接给
`0.9.1-provider-live-smoke-and-redaction-boundary`。
