# Provider Live Smoke DeepSeek

状态：saved-result-checker-supported / live evidence not run

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目标

证明 WorldEngine 可以通过 WorldEngine 自己管理的配置发起最小 live DeepSeek provider
call，并且只返回 redacted public evidence。

## 必要操作

- 用 WorldEngine environment 中配置的 DeepSeek environment variables 启动 WorldEngine。
- 从 WorldEngine 读取 public provider readiness。
- 触发最小 WorldEngine-owned provider live smoke call。
- 保存 redacted provider call evidence。
- 支持实现后运行 documented checker 或 scorecard。

## 禁止操作

- Validation Client 直接调用 DeepSeek。
- Agent 读取、打印、保存或转发 provider API keys。
- 把 `/manifest` readiness 当作 live-call proof。
- operation logs 或 evidence 中保存 raw prompt、raw response、raw request、
  authorization header 或 provider trace。

## 必要 Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `provider-live-summary.json`
- `redaction-scan.json`
- `scorecard-summary.json` 或 checker output

## PASS 来源

PASS 需要 checker 或 scorecard output 确认：

- live provider call 由 WorldEngine 发起。
- DeepSeek call 成功。
- evidence 只包含 provider class、redacted/public model label、success/failure、
  latency、approximate token statistics，以及适用时的 public failure category。
- redaction scan 通过。

## FAIL Taxonomy

- `provider`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

Evidence 不得包含 API keys、authorization headers、raw prompts、raw provider
requests、raw provider responses、provider traces、account ids、private paths、
hidden context 或 private evaluator data。
