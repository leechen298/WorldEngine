# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Active Backend Placement

Implementation must stay in `backend/app/`. The preferred shape is:

```text
backend/app/schemas/agent_continuity.py
backend/app/core/agent_continuity.py
backend/app/api/routes/world_agent.py or backend/app/api/routes/world.py
backend/app/tests/test_agent_continuity_consolidation_evidence.py
```

The implementation may choose a narrow adjacent module name if local patterns
make that clearer. It must not add runtime features under
`backend/worldengine/`.

## Data Flow

1. Caller or Agent loop observes public runtime/event/memory context.
2. Deterministic helper receives public Agent id, runtime tick/world time,
   public event refs, public memory summary refs, and candidate public state.
3. Helper scans for private markers and rejects raw/private evidence.
4. Helper emits `AgentContinuityArtifact` for observe/intent/action/no-intent,
   wait, rest, sleep, consolidating, or reacting states.
5. Consolidation helper records phase windows and public source/emitted
   summary refs without per-tick mandatory personality, memory, or skill
   mutation.
6. If exposed through an apply-capable route, accepted artifacts append public
   event evidence. Rejected scripted-autonomy evidence returns diagnostics and
   no canonical accepted autonomy event.

## Schema Notes

`AgentContinuityArtifact`

- `schema_version`
- `world_id`
- `agent_id`
- `tick_id`
- `world_time_seconds`
- `state`
- `perception_summary_refs`
- `working_memory_summary`
- `long_term_memory_summary_refs`
- `personality_summary_refs`
- `skill_summary_refs`
- `intent_summary`
- `event_reaction_refs`
- `consolidation_phase_refs`
- `evidence_refs`
- `redaction_status`

`AgentConsolidationArtifact`

- `phase_id`
- `world_id`
- `agent_id`
- `status`
- `start_tick`
- `end_tick`
- `start_world_time_seconds`
- `end_world_time_seconds`
- `source_short_term_summary_refs`
- `emitted_long_term_summary_refs`
- `personality_summary_status`
- `skill_summary_status`
- `public_explanation`
- `redaction_status`

`AgentContinuityDiagnostic`

- `code`
- `message`
- `path`
- `severity`

## Deterministic Algorithm

The helper should:

1. Scan ids, refs, summaries, evidence, diagnostics, and optional route
   payloads for private markers.
2. Require public world id, Agent id, tick, world time, and allowed public
   state.
3. Require event reaction artifacts to reference public event ids.
4. Reject direct client-scripted autonomy claims unless they are explicitly
   represented as rejected diagnostics.
5. Require accepted action state evidence to reference public Agent action and
   action-result events with WorldEngine-owned provenance.
6. Reject automatic per-tick personality, long-term memory, or skill mutation
   flags.
7. Accept consolidation artifacts only when they record a bounded phase window
   or active phase tick evidence.
8. Return only public summaries and public refs.

## Event Integration

Accepted artifacts may append generic events such as:

```text
agent.continuity.recorded
agent.action.continuity.recorded
agent.consolidation.recorded
agent.autonomy.rejected
```

Accepted payloads must contain public artifact ids, Agent id, world id, state,
summary refs, redaction status, and evidence refs. They must not include raw
thought, private memory payloads, raw prompts, provider traces, or hidden
context.

## API Surface

An implementation may add an additive public endpoint such as:

```text
POST /worlds/{world_id}/agents/{agent_id}/continuity/evaluate
```

If no route is necessary, helper and tests are enough for this package. If a
route is added, it must be listed in the public handoff manifest and covered
by focused API tests.

## Compatibility

- Do not change existing Agent loop required request or response fields.
- Do not change existing memory store semantics except additive public
  summary/reference behavior.
- Do not change existing event or runtime response shapes.
- Do not change rule-linked event legality behavior from `0.9.7`.
- Preserve public manifest compatibility while adding any new surface.

## Redaction

The redaction marker vocabulary must include at least:

```text
api_key
authorization
chain-of-thought
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
self_state
sk-live-
sk-test-
```

## Stop Conditions

Stop implementation and return to documentation review if:

- continuity evidence requires raw reasoning or private memory payloads.
- implementation requires live provider interpretation.
- checker support or fixture changes become necessary.
- narrative projection or diagnostic dialogue is required.
- durable scheduling or background execution is required.
- Agent continuity cannot be explained through public summaries and refs.
