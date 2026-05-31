# 意图

Status: review complete

## 存在原因

`0.6.3` 已让 structured plans 可以编译。`0.6.4` 创建安全边界，让可能由 AI-assisted tools
产生的 plans 以 structured data 和 redacted provenance 进入，而不是以 prompts、provider
sessions 或可信 executable behavior 进入。

## 预期结果

Implementation 和 review 后：

- imported plans 使用 provider-independent schemas。
- provenance 可检查但 redacted，不包含 secrets、private prompts 或 external application
  data。
- invalid imported plans 在 compilation 前被拒绝。
- tests 使用 static/mock data，不需要 network 或 provider access。

## 非目标

- 不做 live LLM/provider integration。
- 不添加 API route、dashboard UI、preview API、regeneration、persistence 或 background
  execution。
- 不添加 prompt library、prompt execution、hidden retry loop 或 provider-specific
  orchestration。
- 不添加 concrete world content 或 private validation oracle details。

## 交接

`0.6.5-generation-validation-metadata-and-preview-api` 接收已评审的 generation
result/provenance semantics，用于后续 API exposure。
