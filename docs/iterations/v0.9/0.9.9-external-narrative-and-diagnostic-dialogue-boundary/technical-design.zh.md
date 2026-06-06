# Technical Design

英文原文：`technical-design.md`。

## Active Backend Placement

Implementation 必须保持在 `backend/app/`。推荐结构：

```text
backend/app/schemas/external_projection.py
backend/app/core/external_projection.py
backend/app/api/routes/world.py
backend/app/tests/test_external_narrative_diagnostic_boundary.py
```

如果 local patterns 更清晰，implementation 可以选择相邻的 narrow module name。不得在
`backend/worldengine/` 下新增 runtime features。

## Data Flow

1. Caller 提供 public source refs，例如 event ids、snapshot refs、Agent continuity artifact refs
   和 public summary text。
2. Deterministic helper 扫描所有 candidate payloads，查找 private markers。
3. Helper 将 artifact 分类为 external projection 或 out-of-world diagnostic。
4. Helper 默认 reject 任何声称 canonical mutation、in-world dialogue recording 或 Agent memory write 的 candidate。
5. Accepted artifacts 返回 public summaries、provenance、evidence refs，以及显式 false mutation flags。
6. 如果通过 route 暴露，accepted artifacts 可以返回给 public inspection，但默认不得追加 canonical world events。

## Schema Notes

`NarrativeProjectionArtifact`

- `schema_version`
- `projection_id`
- `world_id`
- `source_event_refs`
- `source_snapshot_refs`
- `source_agent_continuity_refs`
- `public_narrative_summary`
- `projection_provenance`
- `canonical_state_mutation_applied`
- `canonical_event_appended`
- `agent_memory_write_applied`
- `in_world_dialogue_recorded`
- `redaction_status`

`DiagnosticDialogueArtifact`

- `schema_version`
- `dialogue_id`
- `world_id`
- `agent_id`
- `question_summary`
- `response_summary`
- `source_event_refs`
- `source_agent_continuity_refs`
- `diagnostic_provenance`
- `canonical_state_mutation_applied`
- `canonical_event_appended`
- `agent_memory_write_applied`
- `in_world_dialogue_recorded`
- `redaction_status`

`ProjectionBoundaryDecision`

- `status`
- `classification`
- `reason`
- `path`
- `redaction_status`

## Deterministic Algorithm

Helper 应：

1. 扫描 ids、refs、summaries、provenance、diagnostics 和 optional route payloads 中的 private markers。
2. 要求 public world id、provenance、redaction status 和 evidence refs。
3. 当 canonical mutation、canonical event append、Agent memory write 或 in-world dialogue flags
   为 true 时 reject。
4. 只接受 external projection 或 out-of-world diagnostic classifications。
5. 只返回 public summaries 和 public refs。

## API Surface

Implementation 可以添加 additive public endpoints，例如：

```text
POST /worlds/{world_id}/narrative/project
POST /worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate
```

如果添加 route，必须列入 public handoff manifest，并由 focused API tests 覆盖。

## Compatibility

- 不改变 existing Agent loop required request 或 response fields。
- 不改变 existing Agent memory store semantics。
- 不改变 existing event 或 runtime response shapes。
- 不改变 rule-linked event legality 或 Agent continuity behavior。
- 添加任何新 surface 时保持 public manifest compatibility。

## Redaction

Redaction marker vocabulary 至少包括：

```text
api_key
api key
authorization
bearer
chain-of-thought
chain_of_thought
credential
hidden context
private evaluator data
private goal
private memory
private prompt
provider trace
provider_secret
raw prompt
raw provider request
raw provider response
raw request
raw response
raw thought
secret
self_state
sk-live-
sk-test-
token
```

## Stop Conditions

如果出现以下情况，停止 implementation 并回到 documentation review：

- projection 需要 raw prompts、provider traces 或 private Agent memory。
- diagnostic dialogue 需要默认写入 Agent memory 或 world timeline。
- 需要 live provider interpretation。
- 需要 checker support 或 fixture changes。
- 需要 frontend UI 或 Validation Client implementation。
