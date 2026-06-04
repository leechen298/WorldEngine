# Technical Design

英文源文件：`technical-design.md`。

## 设计摘要

在 active backend path `backend/app/` 暴露一个小型 public contract layer。该 layer 把现有 generation/readiness 能力适配为 Validation Client 可发现的 public surfaces，同时避免在 public responses 中暴露 provider、prompt、evaluator 和 Agent-private data。

不得添加 application-specific worlds，也不得把 external validation logic 移入 WorldEngine。

## 候选文件

预期实现文件：

```text
backend/app/schemas/world.py
backend/app/api/routes/world.py
backend/app/api/routes/__init__.py
backend/app/api/app_factory.py
backend/app/core/world_generation.py
backend/app/tests/test_world_generation_schema.py
backend/app/tests/test_generation_core_readiness_api.py
```

如果更符合现有 backend 约定，最终实现可选择单独的 schema 或 route 文件。

## Public Manifest

`GET /manifest` 应返回 top-level JSON object，不返回 private evidence。

Provider readiness 初期可报告 `not_configured` 或 `unknown`，不得伪造 ready。本包不要求 live provider calls。

## World Creation

`POST /worlds` 必须能被 Validation Client 从 OpenAPI 发现：

- path 以 `/worlds` 结尾。
- method 是 `POST`。
- operation id 是 `create_world`。
- tag 可包含 `worlds`。

Request:

```json
{
  "world_prompt": "a concise generic world request"
}
```

Response 应为 top-level JSON，包含：

```json
{
  "world_id": "public stable id",
  "status": "created",
  "public_initial_state": {},
  "visualization": {}
}
```

Route 可把 `world_prompt` 适配到现有 preview 或 deterministic generation helper，但不能引入 concrete demo-world fixtures，也不能返回 private generation prompts。

## Director Guidance

若实现 `POST /worlds/{world_id}/director-guidance`，只接受 public guidance。Response status 可为 `accepted`、`applied`、`blocked` 或 `unavailable`。禁止直接修改 private Agent memory、private goals、identity、relationships 或 `self_state`。

如果不在代码中实现，`/manifest` 必须记录 public unavailable reason，closeout 不得声明 full ready-for-human-validation。

## Redaction

Public responses 不得包含 secrets、credentials、authorization、private_prompt、raw_response、raw_request、private memory、private goal、`self_state` 或 `hidden_context`。

测试应序列化 public responses，并断言 forbidden private terms 和已知 secret-like inputs 不出现。
