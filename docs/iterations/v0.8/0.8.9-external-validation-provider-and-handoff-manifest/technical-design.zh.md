# Technical Design

英文镜像：`technical-design.md`。

## 设计摘要

本包提出未来 public handoff manifest，但不实现它。该 manifest 应是一个由
WorldEngine 拥有的脱敏 public 文档或 endpoint，供外部验证客户端在运行 Agent
自主验证前消费。

## 未来 Handoff Manifest 形状

后续实现可以定义 JSON schema，字段类似：

```json
{
  "schema_version": "0.8.x",
  "generated_at": "2026-06-04T00:00:00Z",
  "worldengine_version": "v0.8",
  "provider": {
    "provider_class": "kimi_platform_api",
    "provider_readiness": "ready",
    "credential_source_class": "environment",
    "model_label": "redacted-or-public-model-label",
    "quota_status": "unknown|ready|limited|blocked",
    "rate_limit_note": "public summary only"
  },
  "public_surfaces": [],
  "evidence_refs": [],
  "redaction": {
    "secrets_included": false,
    "private_prompts_included": false,
    "provider_raw_traces_included": false,
    "private_validator_details_included": false
  },
  "blockers": [],
  "warnings": []
}
```

最终形状必须由后续 reviewed package 定义。

## Validation Client Discovery Requirement

当前外部 Validation Client 会从 WorldEngine OpenAPI 自动发现 world creation。它
需要以下任一条件：

- POST path 以 `/worlds` 结尾。
- POST operation id 等于 `createWorld` 或 `create_world`。
- POST operation tag 包含 `worlds`，且 operation id 包含 `create`。

推荐未来 public surface：

```text
POST /worlds
```

完整自主验证还需要 public director guidance surface：

```text
POST /worlds/{world_id}/director-guidance
```

这些 surfaces 只能返回 public summaries，不得暴露 provider raw traces、private
prompts、private Agent state 或 credentials。

## Provider 评估说明

### Kimi Code Subscription

Kimi Code 文档描述的是包含在 Kimi membership 中的开发者编程服务，API key 可
用于第三方 coding agents，支持 OpenAI 和 Anthropic compatible endpoints，并使
用稳定 model id `kimi-for-coding`。

规划影响：Kimi Code 适合作为 coding-agent 工具或外部操作 Agent 的候选。若要
作为 WorldEngine runtime provider，必须先评审条款、quota、可靠性和产品集成约
束。

### Kimi Platform / Moonshot API

Kimi Platform / Moonshot API 更适合作为产品式程序化 runtime 集成候选。它应被
作为由 WorldEngine 环境配置控制的按量或平台 API provider 来评估。

### DeepSeek API

DeepSeek API 是按量付费备选项。DeepSeek public pricing page 会列出模型、
context、output 和 token price 信息，这些信息可能变化。任何 live validation 都
必须使用显式 budget、max tokens 和 stop rules。

## 外部验证客户端消费方式

外部验证客户端可以读取：

- provider class。
- provider readiness。
- public model label。
- quota / rate-limit public note。
- public surface ids。
- redaction confirmation。
- blocked / skipped / unavailable reasons。

不得读取：

- API keys。
- provider account details。
- private prompts。
- raw provider traces。
- private validation scenarios。
- private evaluator oracle internals。

## 后续实现选项

1. 在 `docs/contracts/` 下定义 documentation-only contract surface。
2. 在 `docs/contracts/` 下定义 JSON schema 和 static manifest。
3. 新增 public API endpoint 输出 live readiness summary。

选项 1 最安全，应先执行。选项 2 和 3 需要 reviewed implementation package 和当
前会话测试证据。
