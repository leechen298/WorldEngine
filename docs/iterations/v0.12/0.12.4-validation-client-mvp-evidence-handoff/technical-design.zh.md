# Technical Design

英文原文：`technical-design.md`。

## Artifact Directory Shape

后续 Validation Client export 应写入一个 result directory：

```text
worldengine-mvp-result/
  manifest.json
  operation-log.jsonl
  api-log.jsonl
  session-summary.json
  agent-evidence.json
  inspection-evidence.json
  scorecard-input.json
  redaction-report.json
  reviewer-notes.md
```

`reviewer-notes.md` 是可选项。如存在，只能包含 public review notes。

## Status Taxonomy

- `PASS`：所有 required public evidence 都存在，checker/scorecard/review 同意没有 blocking P1/P2。
- `PARTIAL`：WorldEngine 产出部分 MVP evidence，但 required capability 或 artifact 不完整。
- `BLOCKED`：provider credentials、external client capability、checker assets、permissions 或 environment 阻止 required validation。
- `FAIL`：evidence 存在，且 checker/scorecard/review 发现 blocking product 或 contract failure。

## Operation Log Rows

每条 `operation-log.jsonl` row 必须包含：

- `operation_id`
- `timestamp`
- `actor_class: "external_validation_agent"`
- `worldengine_surface`
- `public_action_summary`
- `result_status`
- `public_artifact_refs`
- `redaction_status`

Rows 不得包含 raw prompts、hidden reasoning、secrets、raw provider payloads 或 private evaluator notes。

## API Log Rows

每条 `api-log.jsonl` row 必须包含：

- `request_id`
- `timestamp`
- `method`
- `path`
- `status_code`
- `operation_id`
- `public_request_summary`
- `public_response_summary`
- `artifact_refs`
- `redaction_status`

Raw request/response bodies 禁止出现，除非它们已经是 public 且通过 redaction-scan。

## Scorecard Input

`scorecard-input.json` 必须 normalize：

- manifest readiness。
- session creation and bounded runtime。
- rule-linked event/diff evidence。
- Agent observe/intent/action-or-wait/rest evidence。
- Agent memory/consolidation evidence。
- narrative/diagnostic read-only inspection evidence。
- redaction report status。
- 世界内 Agent 与 external validation agent 的 terminology checks。

## Redaction Scan

Redaction report 必须扫描所有 public artifacts 是否包含：

```text
api_key
authorization
bearer
chain-of-thought
hidden context
private memory
private prompt
provider trace
raw prompt
raw provider response
raw response
raw thought
secret
sk-live-
token
```

Scan 可以包含更多 markers，但必须至少包含这些。

## Integration Boundary

WorldEngine 定义这些 artifact semantics 和 public API expectations。WorldEngine-Validation-Client 在自己的仓库中实现 export 和 client automation。Client 可以报告 evidence completeness，但 PASS 仍是 checker/scorecard/review classification。
