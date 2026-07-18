# Technical Design

英文源文件：`technical-design.md`。

## Existing Inputs

- `backend/app/agent/memory.py` 提供 process-local working 和 episodic memory storage，
  并有 scoped list methods。
- `backend/app/schemas/agent_memory.py` 已定义 generic working 和 episodic memory records。
- `0.12.1` 新增 session-scoped public Agent state 和 step evidence。
- `backend/app/api/app_factory.py` 已创建 `app.state.agent_memory_store`。

## Proposed Schemas

在 `backend/app/schemas/session.py` 或相邻小型 schema module 中新增 response/request schemas：

- `SessionAgentMemorySummaryResponse`：session ID、world ID、Agent ID、working memory
  summaries、episodic summaries、consolidation status、redaction status。
- `SessionAgentConsolidationResponse`：previous/updated Agent state、working memory
  record、rest 发生时的 episodic memory record、event evidence 和 redaction status。

如果 public fields 足够，现有 `WorkingMemoryRecord`、`EpisodicMemoryRecord` 和
`MemoryEvidenceRef` 可复用。

## API Design

在现有 session route 边界下新增 endpoints：

```text
GET  /sessions/{session_id}/agents/{agent_id}/memory
POST /sessions/{session_id}/agents/{agent_id}/memory/consolidate
```

Consolidate endpoint 只应接受 bounded public hints，例如 `mode: "rest"` 和
`event_limit`。它必须 reject raw memory payloads、raw thought、private goal 和 direct
private memory fields。

## Rest / Consolidation Flow

最小 deterministic behavior：

1. 读取当前 session Agent state 和 recent public `session.agent` events。
2. 从 recent public observation/intent/action/rest labels 创建 public working memory summary。
3. 当请求 consolidation 或当前 Agent step mode 为 `rest` 时，创建带 event/runtime refs 的
   public episodic memory summary。
4. append public events：
   - `world.agent.memory.recorded`
   - rest consolidation 时记录 `world.agent.consolidation.recorded`。
5. 返回 public memory summaries 和 evidence refs。

## Public Event Payloads

Payloads 可以包含：

- `session_id`
- `world_id`
- `agent_id`
- `memory_id`
- `memory_kind`
- `public_summary`
- `runtime_tick`
- `runtime_world_time_seconds`
- `evidence_refs`
- `redaction_status`
- `personality_mutation_applied: false`
- `skill_mutation_applied: false`
- `private_memory_payload_included: false`

## Stop Points

如果出现以下情况，停止 implementation：

- memory summaries 需要 raw private memory、raw thought、provider output 或 diagnostic
  conversation text。
- tests 需要 concrete demo content。
- implementation 需要 persistence、frontend、external Validation Client、checker automation、
  narrative/diagnostic 或 `backend/worldengine/`。
- evidence 无法区分 working memory、episodic memory 和 consolidation records。
