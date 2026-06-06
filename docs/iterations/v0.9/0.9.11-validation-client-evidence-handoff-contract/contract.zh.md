# Contract

英文镜像：`contract.md`。

## Public Concepts

- `validation_client_evidence_bundle`：client export 的目录，只包含 public、redacted evidence
  artifacts。
- `evidence_bundle_manifest`：描述 artifact names、relative paths、producer identity、
  schema versions、scenario、status 和 checker compatibility 的 JSON manifest。
- `display_artifact`：可向 human 展示的 public artifact，不得暴露 provider secrets、raw
  prompts、raw provider responses、private Agent memory、hidden context、raw thought、private
  evaluator data 或 external seed/oracle content。
- `export_artifact`：可写入 saved-result directory 供 checker consumption 的 public artifact。
- `client_role`：`display_export_only`。
- `evaluator_role`：`worldengine_checker_or_second_agent_review`。
- `provider_owner`：`worldengine`。

## Required Artifact Set

完整 LLM-backed lifecycle handoff 应能在 scenario 需要时引用这些 named artifacts：

- `result.json`
- `operation-log.jsonl`
- `provider-live-summary.json`
- `world-creation-summary.json`
- `world-rule-summary.json`
- `rule-parameter-summary.json`
- `event-legality-summary.json`
- `agent-autonomy-summary.json`
- `diff-replay-summary.json`
- `world-lifecycle-summary.json`
- `narrative-projection-summary.json`
- `diagnostic-conversation-summary.json`
- `redaction-scan.json`
- `scorecard-summary.json`
- `second-agent-review.md`
- optional screenshots 或 public transcript files。

Client 可以省略 active scenario 不需要的 artifacts，但不得把 missing required artifacts 重新标成
PASS。

## Manifest Requirements

`evidence_bundle_manifest` 必须包含：

- `schema_version`
- `bundle_id`
- `scenario`
- `result_status`
- `client_role`
- `provider_owner`
- `evaluator_role`
- `created_at`
- `artifact_index`
- `redaction_status`
- `checker_contract`
- `unsupported_items`

`artifact_index` entries 必须包含：

- `name`
- `path`
- `required`
- `displayable`
- `exportable`
- `producer`
- `schema_version`
- `redaction_status`

所有 paths 必须是 relative paths，且必须留在 evidence bundle 内。

## Compatibility Constraints

- Handoff contract 必须保持 additive 和 redacted。
- Existing 0.9.10 checker artifact names 仍是 saved-result validation 的权威来源。
- Client export 可以复制或打包 public artifacts，但不得把 redacted PASS-critical fields 转换成新含义。
- Client 必须保留 `pass`、`fail`、`blocked` 和 `not_run` status values，不得映射成只在 UI
  内部存在的 labels。

## Allowed Changes

- 本 package directory。
- Parent v0.9 route/status/review docs。
- 必要时，本仓库 documentation-only public handoff specs。

## Forbidden Changes

- 不实现 Validation Client repository。
- 不修改 WorldEngine backend runtime behavior。
- 不修改 checker implementation 或 fixtures。
- 不运行 provider live calls，不处理 provider credentials。
- 不实现 frontend。
- 不创建或重写 generated results。
- 不执行 external validation。
- 不在 `backend/worldengine/` 下新增 runtime features。

## Boundary Rules

- Client 不拥有 LLM calls、provider keys、provider readiness truth 或 generated world content。
- Client 不决定 PASS。它可以展示 checker status 和 reviewer findings。
- Client 不得暴露 raw prompts、raw provider requests/responses、provider traces、
  authorization headers、API keys、private Agent memory、private Agent goals、raw thought、
  hidden context、private evaluator data 或 external seed/oracle content。
- Client 不得把 narrative projection 或 diagnostic conversation 转换成 canonical world events 或
  Agent memory。

## North Star Check

本 package 帮助 external validation 消费 WorldEngine evidence，同时不把 engine 收窄成
application-specific backend，也不把 core LLM behavior 移入 client。

## Out-of-Scope Follow-ups

- `0.9.12` 拥有 live 或 explicitly blocked LLM-backed full lifecycle validation execution evidence。
- Validation Client implementation 属于 separate repository 或未来明确授权的 milestone。
