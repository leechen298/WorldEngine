# Technical Design

英文原文：`technical-design.md`。

## Design Summary

在 active backend path `backend/app/` 中添加一个小型 provider smoke layer。该 layer 应尽量
复用当前 provider readiness environment mapping，但必须区分 environment readiness 和 live
call evidence。

smoke path 即使在 provider 未配置时也应返回 public structured evidence。这样本包可以在没有
secrets 的情况下测试，并保持 live execution optional and bounded。

## Candidate Backend Shape

预期 implementation surfaces：

```text
backend/app/agent/llm_provider.py
backend/app/api/routes/provider.py
backend/app/api/routes/__init__.py
backend/app/api/app_factory.py
backend/app/schemas/provider.py
backend/app/tests/test_provider_live_smoke_api.py
backend/app/tests/test_public_handoff_contract_api.py
```

如果符合本地 conventions 且仍在 allowed paths 内，可以使用其他文件名。

## Endpoint Contract

首选 endpoint：

```text
POST /provider/live-smoke
operation_id: provider_live_smoke
```

Request body 应为空，或只包含 public control fields，例如：

```json
{
  "mode": "safe"
}
```

Request 不得接受 raw prompt text、API keys、provider headers、provider account ids 或
private evaluator data。

Response shape：

```json
{
  "schema_version": "0.9.1",
  "provider_class": "deepseek_api",
  "model_label": "deepseek-chat",
  "call_attempted": true,
  "call_status": "success",
  "latency_ms": 123,
  "token_usage_bucket": "1-100",
  "public_failure_category": "none",
  "worldengine_owned_call": true,
  "redaction": {
    "api_keys_included": false,
    "authorization_headers_included": false,
    "raw_prompts_included": false,
    "raw_provider_requests_included": false,
    "raw_provider_responses_included": false,
    "provider_traces_included": false,
    "private_agent_memory_included": false,
    "raw_thought_included": false,
    "hidden_context_included": false
  }
}
```

provider 未配置时：

```json
{
  "call_attempted": false,
  "call_status": "not_configured",
  "public_failure_category": "not_configured",
  "worldengine_owned_call": true
}
```

## Provider Call Strategy

Implementation 应支持两个可测试路径：

- unconfigured path：没有 key 或 unsupported provider 时返回 public `not_configured` 或
  `blocked` evidence，不尝试 live call。
- safe mock path：tests 可以注入 provider implementation，返回 redacted public outcome，不需要
  network access。

Live DeepSeek execution 是 optional，必须由 environment configuration 加 explicit package
authorization gate 控制。Live call 应使用固定 internal smoke intent，不使用 user-supplied prompt
content，且不能在 public evidence 中包含该固定 prompt。

## Redaction Strategy

Response serialization tests 必须扫描 secret-like values 和 forbidden markers，包括：

```text
api_key
apikey
authorization
bearer
credential
provider_secret
raw prompt
raw_prompt
raw request
raw_request
raw response
raw_response
provider_trace
hidden_context
private memory
private goal
self_state
```

Redaction status 本身不够；tests 必须证明 serialized public responses 不包含注入的
secret-like env values。

## Compatibility Strategy

- 保持 `/manifest` response compatible and additive。
- 如果 `/manifest` 列出 smoke endpoint，仍必须警告 provider readiness 不是 live-call proof，
  直到产生 smoke response。
- 保持 existing public handoff tests passing。
- 不改变 `POST /worlds`。

## Anti-Drift Rules

- 不让 smoke prompt design 扩展成 world generation。
- 不让 Validation Client 成为 provider ownership 的一部分。
- 不添加 persistent provider traces。
- 不在 operation logs 中记录 raw provider request/response。
- 不添加 concrete world content 来证明 provider behavior。
- 不用 mock-only evidence 标记 provider PASS。
