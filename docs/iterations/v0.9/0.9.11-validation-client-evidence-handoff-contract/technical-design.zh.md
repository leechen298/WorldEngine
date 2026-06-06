# Technical Design

英文镜像：`technical-design.md`。

## Design Shape

Handoff 是 future evidence bundle 的 documentation contract。本 package 不新增 API、checker、
fixture 或 runtime path。

预期 bundle shape：

```text
evidence-bundle/
  manifest.json
  result.json
  operation-log.jsonl
  provider-live-summary.json
  world-creation-summary.json
  world-rule-summary.json
  rule-parameter-summary.json
  event-legality-summary.json
  agent-autonomy-summary.json
  diff-replay-summary.json
  world-lifecycle-summary.json
  narrative-projection-summary.json
  diagnostic-conversation-summary.json
  redaction-scan.json
  scorecard-summary.json
  second-agent-review.md
  screenshots/
  transcript.md
```

只有 scenario-required artifacts 必须存在。Manifest 必须说明每个 artifact 是否 required、
displayable、exportable 和 checker-consumable。

## Artifact Producer Roles

- `worldengine`：产生 canonical public evidence summaries。
- `validation_client`：展示或打包 public artifacts，不改变 evaluator meaning。
- `worldengine_checker`：根据 structured artifacts 验证 result status。
- `second_agent_review`：在需要时记录 read-only review findings。

## Manifest Validation Rules

未来 compatibility probe 应检查：

1. manifest 存在且是 valid JSON。
2. `client_role` 是 `display_export_only`。
3. `provider_owner` 是 `worldengine`。
4. `evaluator_role` 不是 client-owned evaluator。
5. 所有 artifact paths 都是 relative，且留在 bundle 内。
6. required artifact names 匹配 0.9.10 checker contract。
7. 每个 displayable/exportable artifact 都有 clean redaction status。
8. unsupported items 显式记录，且绝不转换成 PASS。

## Display Guidance

Client 可以展示：

- scenario 和 status。
- provider class/model label 以及 redacted call status。
- world creation summary 和 public model metadata。
- rule 与 event legality summaries。
- public Agent autonomy 和 continuity summaries。
- narrative projection 和 diagnostic conversation summaries，作为 external inspection surfaces。
- scorecard status 和 second-Agent review summary。

Client 不得展示 raw prompts、raw provider payloads、private memory、hidden context、private
evaluator data、seed/oracle data 或 provider secrets。

## Export Guidance

Client 可以按 autonomous saved-result checker 兼容的 relative files 导出 bundle。它必须保留
artifact names 和 status values。如果 artifact missing、malformed、blocked 或 not run，export
必须保留该事实。

## Risk Controls

- 通过禁止 client-owned PASS decisions 避免 client-side evaluator drift。
- 通过要求 bundle redaction status 并保留 `redaction-scan.json` 避免 redaction drift。
- 通过要求 bundle-relative paths 避免 path leakage。
- 通过保持 generic artifact-based contract 避免 application-specific narrowing。
