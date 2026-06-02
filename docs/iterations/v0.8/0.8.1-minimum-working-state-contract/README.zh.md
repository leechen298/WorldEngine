# 0.8.1 Minimum Working State Contract

状态：review complete
类型：documentation-only
implementation_authorized: no
evidence_execution_authorized: no

## 目标

定义 v0.8 何时可以称为 minimum normally working WorldEngine state，包括 required core
slices、claim taxonomy、evidence classes，以及被排除的 product 或 external validation
claims。

本 package 只定义 contract。不实现 schemas、checkers、APIs、frontend behavior、runtime
behavior、tests、external validators 或 external applications。

## 最小工作状态合同

只有后续已评审 package 为所有范围内必需切片提供当前会话证据后，v0.8 才可提出
minimum working-state claim：

- generation readiness：生成或导入的 generic world material 必须结构化、已验证、可检查，
  并明确标记为 runtime-ready 或 blocked。
- runtime readiness：已加载的 generic world 必须能暴露 state，按已批准 runtime steps
  推进，并记录 events，且没有隐藏副作用。
- event evidence：state changes 和 Agent actions 必须能通过 public、redacted event 或
  evidence surfaces 被观察。
- Agent loop readiness：Agent 必须能读取有边界的 world context，产出 validated intent，
  并在已批准 runtime boundaries 内收到可 review 的 action result。
- memory-context readiness：在已授权范围内可以包含 bounded read-only memory context，但不得暴露
  raw memory、private transcripts、provider traces，或超出当前 contracts 的 pseudo-self internals。
- projection/read-model observability：public read-only surfaces 可以总结当前 working-state
  evidence，但不得包含 product-specific behavior。
- evidence and blocker classification：pass、blocked、skipped 和 out of scope 必须清楚区分并可
  review。

## 声明分类

- `core contract ready`：documentation contracts 已 reviewed；不暗示 runtime pass。
- `core observable surface ready`：public observable surfaces 已由 reviewed package 定义或实现；
  不暗示 external validation PASS。
- `minimum working-state evidence ready`：current-session core evidence 已证明范围内必需切片；
  不暗示 product 或 external-suite PASS。
- `external validation handoff ready`：存在可供 external validator 消费的 public redacted handoff
  evidence；不暗示 external validation PASS。
- `external validation pass`：除非后续 reviewed external workflow 提供 redacted public evidence，
  否则不属于当前 v0.8 core packages 范围。
- `blocked`：required evidence 或 contract conditions 未满足。
- `skipped`：有理由地未运行。
- `out of scope`：被 active package contract 排除。

## 范围

允许范围：

- 创建本 package document set 和中文镜像。
- 定义 minimum working-state concepts、claim taxonomy、evidence classes、exclusions，以及后续
  packages 的 authorization criteria。
- Review 后同步 parent v0.8 route/status surfaces。
- 记录 documentation checks 和 evaluator findings。

禁止范围：

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、
  migration、generated result、external repository 或 `backend/worldengine/` implementation files。
- 不实现 minimum working-state schemas、observable surfaces、services、APIs、UI、persistence、
  checkers、tests 或 evidence artifacts。
- 不定义 external validator connection details、private scenarios、oracle logic、product app UI、
  application state、private repository paths、concrete world content、UI selectors、hidden reset
  APIs、provider traces 或 secrets。
- 不声明 minimum working-state PASS、runtime/API/frontend/E2E PASS、Agent smoke PASS、
  autonomous PASS、external validation PASS、projection readiness PASS、product readiness PASS 或
  release readiness。

## 最终评估状态

当前值：`review complete`。

本 package 定义 minimum working-state contract，并把 authorization criteria 交给
`0.8.2-core-observable-surface-boundary`。
