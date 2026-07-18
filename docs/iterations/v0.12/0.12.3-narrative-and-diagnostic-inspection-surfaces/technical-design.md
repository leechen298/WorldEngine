# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Existing Inputs

- `backend/app/schemas/external_projection.py` defines redacted narrative and
  diagnostic projection request/response artifacts.
- `backend/app/core/external_projection.py` validates private markers,
  canonical mutation flags, public refs, and read-only boundaries.
- `backend/app/api/routes/world.py` exposes world-level projection and
  diagnostic evaluation endpoints.
- `0.12.1` adds session Agent state and runtime step evidence.
- `0.12.2` adds session Agent memory and rest consolidation evidence.
- The public event log, snapshot store, session store, direction queue, and
  memory store are available in app state.

## Proposed Schemas

Add small public inspection schemas in `backend/app/schemas/session.py` or an
adjacent module:

- `SessionNarrativeProjectionRequest`: tick range, optional branch ID, optional
  Agent ID, optional summary hint, and public source refs.
- `SessionNarrativeProjectionResponse`: accepted/rejected status, filters,
  public narrative summary, provenance refs, diagnostic list, read-only flags,
  and redaction status.
- `SessionDiagnosticInspectionRequest`: question summary, optional Agent ID,
  tick range, branch ID, and public source refs.
- `SessionDiagnosticInspectionResponse`: public answer summary, out-of-world
  classification, provenance refs, diagnostic list, read-only flags, and
  redaction status.

The schemas should forbid extra fields and reject private markers. Existing
`ExternalProjectionEvidenceRef` may be reused for public source refs.

## API Design

Add endpoints under the existing session route boundary:

```text
POST /sessions/{session_id}/narrative/project
POST /sessions/{session_id}/diagnostics/inspect
```

The endpoints are read-only. They may compute summaries from:

- public session runtime state.
- public event log entries filtered by tick range, branch ID, and Agent ID.
- public session Agent state.
- public working/episodic memory summaries.
- public snapshot refs.

## Projection Flow

Minimum deterministic behavior:

1. load the session and reject unknown sessions.
2. collect public event refs matching tick range, branch, and Agent filters.
3. include bounded public Agent state and memory summary refs when an Agent is
   focused.
4. validate private markers, forbidden mutation flags, and evidence refs.
5. return an accepted public summary if at least one public evidence source is
   available, otherwise return a rejected response with a public diagnostic.
6. do not append events, write memory, mutate session/world state, or write the
   direction queue.

## Public Artifact Fields

Responses may include:

- `session_id`
- `world_id`
- `agent_id`
- `tick_range`
- `branch_id`
- `public_narrative_summary` or `public_answer_summary`
- `source_event_refs`
- `source_snapshot_refs`
- `source_agent_refs`
- `source_memory_refs` using existing public summary-style evidence refs
  (`ref_type: "summary"`) unless implementation proves an additive memory ref
  type is necessary and reviewed.
- `inspection_provenance`
- `canonical_state_mutation_applied: false`
- `canonical_event_appended: false`
- `agent_memory_write_applied: false`
- `in_world_dialogue_recorded: false`
- `redaction_status`

## Stop Points

Stop implementation if:

- inspection requires raw private memory, raw thought, provider output, or raw
  diagnostic conversation.
- inspection writes canonical state, event log, direction queue, or Agent
  memory.
- implementation needs frontend, persistence, external Validation Client,
  checker automation, provider live calls, concrete demo content, or
  `backend/worldengine/`.
- the API would let clients steer world evolution outside the direction queue.
