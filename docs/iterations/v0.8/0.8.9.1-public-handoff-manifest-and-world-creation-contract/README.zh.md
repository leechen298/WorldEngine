# 0.8.9.1 Public Handoff Manifest And World Creation Contract

状态：implementation complete / WORLDENGINE_CONTRACT_READY
类型：mixed implementation package
implementation_authorized: campaign-authorized by user request on 2026-06-04
evidence_execution_authorized: yes, bounded to WorldEngine Gate 1

英文源文件：`README.md`。

## 包

名称：`0.8.9.1-public-handoff-manifest-and-world-creation-contract`

本包是 `0.8.9-external-validation-provider-and-handoff-manifest` 的具体实现子包。

0.8.9 父包是 documentation-only。本包已实现外部 Validation Client 消费所需的
WorldEngine public contract surfaces。

## 目标

实现外部 Validation Client handoff 所需的 WorldEngine 侧 public contract：

- `GET /manifest` 返回脱敏 public handoff manifest。
- `POST /worlds` 能被 Validation Client 通过 OpenAPI 发现。
- world creation 返回 public world id、status、initial state、visualization payload。
- provider readiness 只通过脱敏 public labels 暴露。
- director guidance 作为 public endpoint 暴露，或在 manifest 中记录 unavailable。

## 范围摘要

已实现：

- 在 `backend/app/schemas/` 增加 public schema。
- 在 `backend/app/api/routes/` 增加 public route。
- 在 active FastAPI app factory 注册 route。
- 生成 generic public world creation response。
- 增加 focused backend tests，证明 OpenAPI discoverability、response shape、redaction。
- 更新本包 `review.md` 和 `review.zh.md` 的实现证据。

禁止：

- 修改 Validation Client 仓库。
- 添加具体 demo-world 内容。
- provider API 调用或 credential 存储。
- 在 public output 暴露 raw provider traces、private prompts、raw responses、private evaluator data、product UI selectors、private Agent memory、private goals、`self_state` 或 hidden context。
- 修改 `backend/worldengine/`。
- 声明 external validation PASS、Codex autonomous PASS 或 human validation PASS。

## Handoff

本包已用 `WORLDENGINE_CONTRACT_READY` 关闭 WorldEngine Gate 1。Validation Client
v0.7 可以进入 readiness implementation。本包不授权也不声明 Codex autonomous
validation PASS、second-Agent review PASS、human validation PASS、live provider PASS
或 product readiness。
