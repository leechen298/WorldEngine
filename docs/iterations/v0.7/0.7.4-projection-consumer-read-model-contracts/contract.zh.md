# Contract

## Public Concepts

- `ProjectionReadModelContract`：public、read-only contract，描述后续 packages 中
  external consumers 可读取的 payload families。
- `ReadModelFamily`：`runtime_summary`、`event_timeline_summary`、
  `agent_loop_summary`、`memory_context_summary`、`generation_readiness_summary`、
  `readiness_manifest_summary` 或 `redacted_report_summary`。
- `BoundedSummary`：redacted summary，避免 raw memory、raw prompts、private traces、
  transcripts 和 non-redacted event payloads。
- `NoWriteCapability`：required marker，确认 read model 不暴露 mutation、reset、
  persistence、private runner hook 或 product-specific write behavior。

## Required Read Model Families

Schema/checker 必须要求这些 read-only families：

- `runtime_summary`
- `event_timeline_summary`
- `agent_loop_summary`
- `memory_context_summary`
- `generation_readiness_summary`
- `readiness_manifest_summary`
- `redacted_report_summary`

每个 family 必须定义：

- family id。
- version。
- read-only marker。
- allowed public fields。
- redaction notes。
- no-write guarantee。

## Allowed Changes

- 创建或更新
  `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/`。
- 创建或更新本 child package 中文镜像。
- 创建 `docs/contracts/projection-read-model-contract.md`。
- 创建 `docs/contracts/projection-read-model-schema.json`。
- 创建 `tools/testing/validate_projection_read_model_contract.py`。
- 创建 `tools/testing/test_validate_projection_read_model_contract.py`。
- Review 和 closeout 后更新 parent v0.7 status and route surfaces。

## Forbidden Changes

- 不添加 runtime、API route、frontend、persistence、migration、product dashboard、
  projection app、game UI、concrete world viewer、write API、reset API、private runner hook、
  external repository 或 `backend/worldengine/` implementation changes。
- 不暴露 private application state、concrete validation worlds、character names、
  location names、maps、story rules、seed data、UI selectors、raw memory records、
  provider secrets、prompts、private traces、transcripts 或 non-redacted event payloads。
- 不声明 projection application readiness、product readiness、external consumer PASS、
  runtime/API/frontend PASS 或 v0.8 readiness。

## Compatibility Requirements

- Read-model contracts 必须 additive、read-only、versioned。
- Existing runtime、event、Agent loop、memory、generation、API envelope 和 dashboard behavior
  保持不变。
- `0.7.3` manifest references 保持有效。
- 如果 future API-backed projection surfaces 需要 runtime/API implementation，必须由后续
  reviewed package 授权。

## Review Gates

Implementation 只有在以下条件满足后才能开始：

- package docs 与中文镜像存在。
- documentation/contract evaluator 报告无 P0/P1 且无 blocking P2。
- package `review.md` 记录 `implementation_authorized: yes`。

Closeout 只有在以下条件满足后才能进行：

- focused projection read-model checker tests 通过。
- 如果 manifest references 被触及，readiness manifest checker tests 通过。
- `git diff --check` 通过。
- changed-file scope guard 通过。
- implementation-scope、code-review、validation-evidence 和 closeout consistency
  evaluators 无 blocking findings。

## Out-of-Scope Follow-ups

- `0.7.5`：quality regression and compatibility evidence。
- `0.7.6`：evidence and compatibility audit。
- `0.7.7`：release-candidate bundle。
- `0.7.8`：final closeout。
