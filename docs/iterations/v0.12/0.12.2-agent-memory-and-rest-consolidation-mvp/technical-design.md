# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Existing Inputs

- `backend/app/agent/memory.py` provides process-local working and episodic
  memory storage with scoped list methods.
- `backend/app/schemas/agent_memory.py` already defines generic working and
  episodic memory records.
- `0.12.1` adds session-scoped public Agent state and step evidence.
- `backend/app/api/app_factory.py` already creates `app.state.agent_memory_store`.

## Proposed Schemas

Add response/request schemas in `backend/app/schemas/session.py` or a small
adjacent schema module:

- `SessionAgentMemorySummaryResponse`: session ID, world ID, Agent ID, working
  memory summaries, episodic summaries, consolidation status, redaction status.
- `SessionAgentConsolidationResponse`: previous/updated Agent state, working
  memory record, episodic memory record when rest occurs, event evidence, and
  redaction status.

Existing `WorkingMemoryRecord`, `EpisodicMemoryRecord`, and `MemoryEvidenceRef`
may be reused if their public fields remain sufficient.

## API Design

Add endpoints under the existing session route boundary:

```text
GET  /sessions/{session_id}/agents/{agent_id}/memory
POST /sessions/{session_id}/agents/{agent_id}/memory/consolidate
```

The consolidate endpoint should accept only bounded public hints such as
`mode: "rest"` and `event_limit`. It must reject raw memory payloads, raw
thought, private goal, and direct private memory fields.

## Rest / Consolidation Flow

Minimum deterministic behavior:

1. read current session Agent state and recent public `session.agent` events.
2. create a public working memory summary from recent public observation/
   intent/action/rest labels.
3. if consolidation is requested or current Agent step mode is `rest`, create
   a public episodic memory summary with event/runtime refs.
4. append public events:
   - `world.agent.memory.recorded`
   - `world.agent.consolidation.recorded` for rest consolidation.
5. return public memory summaries and evidence refs.

## Public Event Payloads

Payloads may include:

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

Stop implementation if:

- memory summaries require raw private memory, raw thought, provider output, or
  diagnostic conversation text.
- tests need concrete demo content.
- implementation needs persistence, frontend, external Validation Client,
  checker automation, narrative/diagnostic, or `backend/worldengine/`.
- evidence cannot distinguish working memory, episodic memory, and
  consolidation records.
