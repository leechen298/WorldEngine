# 0.9.1 Provider Live Smoke And Redaction Boundary

英文原文：`README.md`。

Status: implementation complete / non-live focused verification passed
Type: mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: yes, limited to non-live focused tests in `test-plan.md`
provider_live_call_authorized: no

## 目标

为 v0.9 添加第一条 WorldEngine-owned provider live smoke contract 和 implementation
path，并提供 redacted public evidence 与安全的 unconfigured 行为。

本包只证明 provider boundary。它不生成世界，不评估 worldview fidelity，不演化规则，
不创建 Agent continuity，也不声明 LLM-backed lifecycle PASS。

## 范围

documentation/contract review 后允许：

- 在 active `backend/app/` 路径中添加或细化 backend provider configuration helpers。
- 添加最小 WorldEngine-owned provider smoke call path，优先使用 `POST
  /provider/live-smoke`，operation id 为 `provider_live_smoke`。
- 添加 public redacted provider live summary schema。
- 添加 failure taxonomy：
  - `not_configured`
  - `network`
  - `quota`
  - `provider_error`
  - `redaction_failure`
  - `unsupported_provider`
  - `blocked`
- 保持 `/manifest` additive-compatible，同时明确 manifest readiness 不是 live-call proof。
- 添加 focused backend tests，覆盖 configured、not configured、safe mock、public response
  shape 和 redaction。
- 仅在本包需要时添加 checker 或 fixture support，用于验证 redacted provider summary。
- code work 后更新 package `review.md` 记录 implementation evidence。

禁止：

- 不暴露、存储、记录或导出 API keys、authorization headers、raw prompts、raw
  provider requests、raw provider responses、raw provider traces、account identifiers、
  private evaluator data、hidden context、raw thought 或 private Agent memory。
- 不让 Validation Client 拥有 provider calls、provider keys、prompts 或 evaluation
  authority。
- 除固定的最小 smoke prompt 外，不实现 LLM-backed world generation。
- 不添加 concrete demo-world names、maps、characters、resources、story rules、seed data
  或 application-specific backend behavior。
- 不修改 `backend/worldengine/`。
- 没有 current-session evidence 时，不声明 provider PASS、LLM-backed lifecycle PASS、
  external validation PASS、product readiness、API-wide PASS、E2E PASS、Agent smoke
  PASS 或 autonomous PASS。

## 交付物

- 完整 package document set 和中文镜像。
- 代码变更前的 reviewed implementation authorization。
- 最小 provider live smoke API 或 command。
- Public provider live summary schema。
- Redacted evidence contract 和 redaction tests。
- Focused backend tests 和 `/manifest` compatibility tests。
- 仅在 provider environment 已配置且本包明确授权时，执行 optional live smoke。

## 状态清单

- [x] Package documents drafted.
- [x] Chinese mirrors drafted.
- [x] Documentation/contract evaluator complete.
- [x] Implementation authorized.
- [x] Implementation complete.
- [x] Focused verification complete.
- [x] Review evidence updated.
- [x] Handoff to `0.9.2` recorded.

## 最终评估状态

当前值：`implementation complete / non-live focused verification passed`。

本包已实现 reviewed provider smoke and redaction boundary，且没有运行真实 provider call。Live
provider calls 仍保持关闭。下一条 route 是
`0.9.2-llm-worldview-ingestion-and-generation-contract` documentation package creation。
