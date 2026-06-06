# Contract

英文原文：`contract.md`。

## Public Concepts

- `provider readiness`：来自 `/manifest` 的 public environment-derived state。它可以报告
  configured 或 not configured，但不是 live call proof。
- `provider live smoke`：用于证明 live connectivity 的最小 WorldEngine-owned provider
  call，不生成世界。
- `redacted provider live summary`：smoke attempt 的 public evidence，不包含 raw prompts、
  raw requests、raw responses、raw traces、secrets 或 account details。
- `provider blocked`：environment、quota、network、provider availability 或 redaction 阻止
  live proof 时的分类状态。
- `worldengine_owned_call`：evidence 中的 boolean，用于证明调用由 WorldEngine 发起，而不是
  Validation Client。

## Public Provider Live Summary

provider smoke response 或 artifact 只能包含 public/redacted fields：

```text
schema_version
provider_class
model_label
call_attempted
call_status
latency_ms
token_usage_bucket
public_failure_category
worldengine_owned_call
redaction
```

允许的 `call_status`：

```text
success
failure
blocked
not_configured
not_run
```

允许的 `public_failure_category`：

```text
none
not_configured
network
quota
provider_error
redaction_failure
unsupported_provider
blocked
unknown
```

success 时所有 redaction flags 必须为 false：

```text
api_keys_included
authorization_headers_included
raw_prompts_included
raw_provider_requests_included
raw_provider_responses_included
provider_traces_included
private_agent_memory_included
raw_thought_included
hidden_context_included
```

## 允许变更

review authorization 后，本包可以修改：

- `backend/app/agent/llm_provider.py`
- `backend/app/api/routes/`
- `backend/app/api/app_factory.py`
- `backend/app/schemas/`
- `backend/app/tests/`
- 仅当本包需要 provider summary checker support 时，修改
  `tools/testing/validate_agent_autonomous_result.py` 和 focused tests。
- package `review.md` 和 `review.zh.md`。

如果更符合现有 backend structure，implementation 可以引入小型 helper module，例如
`backend/app/agent/provider_config.py` 或 `backend/app/schemas/provider.py`。

## 禁止变更

本包不得：

- 修改 `backend/worldengine/`。
- 修改 Validation Client repository。
- 添加 concrete worlds、maps、characters、resources、story rules、seed data 或
  application-specific backend behavior。
- 实现 LLM-backed world generation 或 prompt-driven world creation。
- 暴露或持久化 provider keys、authorization headers、raw prompts、raw provider
  requests、raw provider responses、provider traces、account ids、hidden context、
  private evaluator data、private Agent memory、raw thought 或 chain-of-thought。
- 让 Validation Client 调 provider 或管理 provider keys。
- 把 `/manifest` 当成 live-call proof。
- 用 deterministic mock output 声称 provider live PASS。
- 除非当前会话中 live call 成功且 redaction checks 通过，否则不声明 provider live PASS。

## 兼容性要求

- 既有 `/manifest` fields 保持 additive-compatible。
- 既有 unconfigured provider state 保持安全且可测试。
- 既有 `POST /worlds` deterministic generic world creation 不变。
- 既有 mock provider tests 保持 deterministic。
- Schema changes 保持 additive，除非本 contract 更新并重新 review。
- Provider errors 必须返回 public failure categories，不返回 private request 或 response details。

## Stop Rules

如出现以下情况，停止 implementation：

- live smoke call 无法在不存储或暴露 raw provider data 的情况下完成。
- provider configuration 需要 environment-owned runtime configuration 之外的 secrets。
- 需要 Validation Client changes。
- implementation 需要 concrete world generation content。
- tests 无法证明 not-configured behavior 和 redaction。
- implementation 发现本包需要超出 contract 的更宽 provider SDK 或 prompt architecture。
