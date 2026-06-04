# Contract

英文镜像：`contract.md`。

## Public Concepts

本包只定义规划概念：

- `provider_class`：公开类别，例如 `kimi_code_subscription`、
  `kimi_platform_api`、`moonshot_api`、`deepseek_api`、`mock` 或
  `unconfigured`。
- `provider_readiness`：公开状态，例如 `ready`、`degraded`、`unavailable`、
  `blocked` 或 `not_configured`。
- `credential_source_class`：脱敏标签，例如 `environment`、`secret_manager`、
  `developer_local` 或 `none`。
- `handoff_manifest`：公开对象，列出 core-side validation surfaces、evidence
  references、provider readiness summary、redaction confirmation 和 blocker
  classification。
- `external_validation_consumer`：消费 WorldEngine public contracts 的外部客户端或
  Agent 系统。

## Allowed Changes

本文档包可以：

- 定义 provider boundary semantics。
- 定义 handoff manifest 字段预期。
- 定义 stop rules 和 evidence classification。
- 引用 provider 官方公开文档作为 planning inputs。
- 为后续 schemas、checkers 或 public endpoint docs 规划 package scope。

## Forbidden Changes

本包不得：

- 修改 runtime、schema、API、frontend、tests、fixtures、migrations 或 generated
  evidence。
- 实现 provider calls。
- 保存 provider keys 或 account details。
- 暴露 provider traces、raw prompts、raw responses、private evaluator oracle
  data、private validation scenarios、external repo paths、product UI selectors、
  concrete world content 或 hidden reset APIs。
- 声明 external validation PASS、product readiness、live provider PASS、Agent
  autonomous PASS、E2E PASS 或 human validation PASS。

## Compatibility Constraints

- WorldEngine 仍是 provider owner。
- 外部验证客户端只消费 public summaries。
- Schema/API changes 属于 future work，必须有 reviewed implementation package。
- 既有 v0.7 和 v0.8 closeout evidence 保持 historical and bounded。

## Stop Rules

- 如果字段需要暴露 secret、private prompt、provider raw trace 或 private validator
  detail，停止。
- 如果需要验证客户端定义 WorldEngine core readiness taxonomy，停止。
- 如果 provider integration 无法在不决定 runtime behavior 的情况下描述，停止并交
  给后续 code package。
