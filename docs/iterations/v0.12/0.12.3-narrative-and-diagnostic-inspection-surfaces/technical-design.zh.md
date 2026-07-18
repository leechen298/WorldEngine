# Technical Design

英文原文：`technical-design.md`。

## 现有输入

- `backend/app/schemas/external_projection.py` 定义 redacted narrative 和 diagnostic projection request/response artifacts。
- `backend/app/core/external_projection.py` 验证 private markers、canonical mutation flags、public refs 和 read-only boundaries。
- `backend/app/api/routes/world.py` 暴露 world-level projection 和 diagnostic evaluation endpoints。
- `0.12.1` 增加 session Agent state 和 runtime step evidence。
- `0.12.2` 增加 session Agent memory 和 rest consolidation evidence。
- app state 中已有 public event log、snapshot store、session store、direction queue 和 memory store。

## 拟议 Schema

在 `backend/app/schemas/session.py` 或邻近模块中增加小型 public inspection schema：

- `SessionNarrativeProjectionRequest`：tick range、optional branch ID、optional Agent ID、optional summary hint 和 public source refs。
- `SessionNarrativeProjectionResponse`：accepted/rejected status、filters、public narrative summary、provenance refs、diagnostic list、read-only flags 和 redaction status。
- `SessionDiagnosticInspectionRequest`：question summary、optional Agent ID、tick range、branch ID 和 public source refs。
- `SessionDiagnosticInspectionResponse`：public answer summary、out-of-world classification、provenance refs、diagnostic list、read-only flags 和 redaction status。

这些 schema 必须 forbid extra fields 并拒绝 private markers。可以复用现有 `ExternalProjectionEvidenceRef` 作为 public source refs。

## API 设计

在现有 session route boundary 下增加 endpoint：

```text
POST /sessions/{session_id}/narrative/project
POST /sessions/{session_id}/diagnostics/inspect
```

这些 endpoint 是只读的。它们可从以下公开信息计算 summary：

- public session runtime state。
- 按 tick range、branch ID 和 Agent ID 过滤的 public event log entries。
- public session Agent state。
- public working/episodic memory summaries。
- public snapshot refs。

## Projection Flow

最小确定性行为：

1. 读取 session，未知 session 则拒绝。
2. 收集符合 tick range、branch 和 Agent filters 的 public event refs。
3. Agent-focused 时包含 bounded public Agent state 和 memory summary refs。
4. 验证 private markers、forbidden mutation flags 和 evidence refs。
5. 至少有一个 public evidence source 时返回 accepted public summary，否则返回带 public diagnostic 的 rejected response。
6. 不 append events，不写 memory，不改 session/world state，不写 direction queue。

## 公开 Artifact 字段

响应可以包含：

- `session_id`
- `world_id`
- `agent_id`
- `tick_range`
- `branch_id`
- `public_narrative_summary` 或 `public_answer_summary`
- `source_event_refs`
- `source_snapshot_refs`
- `source_agent_refs`
- `source_memory_refs` 使用现有 public summary-style evidence refs（`ref_type:
  "summary"`），除非实现证明需要 additive memory ref type 并完成评审。
- `inspection_provenance`
- `canonical_state_mutation_applied: false`
- `canonical_event_appended: false`
- `agent_memory_write_applied: false`
- `in_world_dialogue_recorded: false`
- `redaction_status`

## 停止点

遇到以下情况停止实现：

- inspection 需要 raw private memory、raw thought、provider output 或 raw diagnostic conversation。
- inspection 写 canonical state、event log、direction queue 或 Agent memory。
- 实现需要 frontend、persistence、外部 Validation Client、checker automation、provider live call、具体 demo content 或 `backend/worldengine/`。
- API 会让 client 绕过 direction queue 来 steering world evolution。
