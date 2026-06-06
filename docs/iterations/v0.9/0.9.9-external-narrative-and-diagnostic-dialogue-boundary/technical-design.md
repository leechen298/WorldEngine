# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Active Backend Placement

Implementation must stay in `backend/app/`. The preferred shape is:

```text
backend/app/schemas/external_projection.py
backend/app/core/external_projection.py
backend/app/api/routes/world.py
backend/app/tests/test_external_narrative_diagnostic_boundary.py
```

The implementation may choose a narrow adjacent module name if local patterns
make that clearer. It must not add runtime features under
`backend/worldengine/`.

## Data Flow

1. Caller provides public source refs such as event ids, snapshot refs, Agent
   continuity artifact refs, and public summary text.
2. Deterministic helper scans all candidate payloads for private markers.
3. Helper classifies the artifact as external projection or out-of-world
   diagnostic.
4. Helper rejects any candidate that claims canonical mutation, in-world
   dialogue recording, or Agent memory write by default.
5. Accepted artifacts return public summaries, provenance, evidence refs, and
   explicit mutation flags set to false.
6. If exposed through a route, accepted artifacts may be returned for public
   inspection but must not append canonical world events by default.

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

The helper should:

1. Scan ids, refs, summaries, provenance, diagnostics, and optional route
   payloads for private markers.
2. Require public world id, provenance, redaction status, and evidence refs.
3. Reject canonical mutation, canonical event append, Agent memory write, or
   in-world dialogue flags when set to true.
4. Accept only external projection or out-of-world diagnostic classifications.
5. Return only public summaries and public refs.

## API Surface

An implementation may add additive public endpoints such as:

```text
POST /worlds/{world_id}/narrative/project
POST /worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate
```

If a route is added, it must be listed in the public handoff manifest and
covered by focused API tests.

## Compatibility

- Do not change existing Agent loop required request or response fields.
- Do not change existing Agent memory store semantics.
- Do not change existing event or runtime response shapes.
- Do not change rule-linked event legality or Agent continuity behavior.
- Preserve public manifest compatibility while adding any new surface.

## Redaction

The redaction marker vocabulary must include at least:

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

Stop implementation and return to documentation review if:

- projection requires raw prompts, provider traces, or private Agent memory.
- diagnostic dialogue needs to write Agent memory or world timeline by
  default.
- live provider interpretation becomes necessary.
- checker support or fixture changes become necessary.
- frontend UI or Validation Client implementation becomes necessary.
