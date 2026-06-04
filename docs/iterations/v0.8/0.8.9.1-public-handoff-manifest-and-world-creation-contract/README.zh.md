# 0.8.9.1 Public Handoff Manifest And World Creation Contract

状态：drafted / ready for user review
类型：mixed implementation package
implementation_authorized: no
evidence_execution_authorized: no

英文源文件：`README.md`。

## 包

名称：`0.8.9.1-public-handoff-manifest-and-world-creation-contract`

本包是 `0.8.9-external-validation-provider-and-handoff-manifest` 的具体实现子包。

0.8.9 父包是 documentation-only，不授权 runtime、API、schema、test 或 evidence 变更。本包用于定义进入实现前必须 review 的实现门禁。

## 目标

实现外部 Validation Client handoff 所需的 WorldEngine 侧 public contract：

- `GET /manifest` 返回脱敏 public handoff manifest。
- `POST /worlds` 能被 Validation Client 通过 OpenAPI 发现。
- world creation 返回 public world id、status、initial state、visualization payload。
- provider readiness 只通过脱敏 public labels 暴露。
- director guidance 作为 public endpoint 暴露，或在 manifest 中记录 unavailable。

## 范围摘要

本包 review 并显式授权实现后，允许：

- 在 `backend/app/schemas/` 增加 public schema。
- 在 `backend/app/api/routes/` 增加 public route。
- 在 active FastAPI app factory 注册 route。
- 复用现有 generation/readiness helper 生成 generic public world summary。
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

本包当前只 ready for user review。只有用户批准本实现包，或明确记录本包 contract、technical design、test plan、plan 已获准实现后，才能开始实现。
