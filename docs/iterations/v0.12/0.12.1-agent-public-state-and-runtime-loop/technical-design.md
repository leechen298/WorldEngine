# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Existing Inputs

- `backend/app/agent/loop_service.py` provides a request-scoped perception and
  action adapter path. It remains compatible but is not sufficient autonomy
  evidence when a client supplies intent.
- `backend/app/agent/perception.py` can build bounded public perception from
  runtime state, event log, world params, runtime context, and memory context.
- `backend/app/core/world_session.py` stores process-local public sessions,
  rules, and direction queues.
- `backend/app/api/routes/session.py` owns session-scoped public runtime,
  rules, direction, evolution, snapshot, and evidence APIs.

## Proposed Public Schemas

Add redaction-safe session Agent schemas, likely in `backend/app/schemas/session.py`
or a small `backend/app/schemas/session_agent.py` module:

- `SessionAgentRuntimeRef`: tick, world time, step seconds.
- `SessionAgentEvidenceRef`: event IDs and event count before/after.
- `SessionAgentPublicState`: agent ID, session ID, world ID, state, public
  status, last observation summary, current intent label, visible action,
  runtime ref, evidence refs, redaction status.
- `SessionAgentStepRequest`: bounded event limit and optional mode hints only.
  It must not accept concrete action patches/intents.
- `SessionAgentStepResponse`: previous state, updated state, public intent,
  action/rest/wait result label, evidence refs, redaction status.

Allowed state labels:

```text
observing
no_intent
acting
waiting
resting
blocked
```

## Store / Loop Design

Extend `InMemoryWorldSessionStore` or add an adjacent helper with:

- default Agent creation for a session when first listed/read.
- `list_agents(session_id)`.
- `get_agent(session_id, agent_id)`.
- `step_agent(session_id, agent_id, runtime_state, recent_events)`.

The deterministic MVP policy should be simple:

1. build public observation summary from current runtime ref and latest public
   event types.
2. if no actionable public event exists, record `no_intent` or `waiting`.
3. if a rule/evolution public event exists, record a bounded public `action`
   label such as `acknowledge_public_event`; do not mutate world params.
4. optionally record `resting` when requested by an allowed public mode hint.

## API Design

Add endpoints under the existing session router:

```text
GET  /sessions/{session_id}/agents
GET  /sessions/{session_id}/agents/{agent_id}
POST /sessions/{session_id}/agents/{agent_id}/step
```

The step endpoint must reject unknown fields through Pydantic `extra="forbid"`
and must not accept `intent`, `patches`, or direct action payloads.

## Event Evidence

Agent step appends public events such as:

```text
world.agent.observed
world.agent.intent.recorded
world.agent.action.recorded
world.agent.wait.recorded
world.agent.rest.recorded
```

Event payloads include only public fields:

- `session_id`
- `world_id`
- `agent_id`
- `agent_state`
- `public_observation_summary`
- `public_intent`
- `visible_action`
- `runtime_tick`
- `runtime_world_time_seconds`
- `redaction_status`
- `client_scripted_action: false`

## Manifest Updates

Add public manifest discovery items for the three session Agent endpoints and
for the `session_agent_runtime_loop` capability. Keep additions additive.

## Stop Points

Stop implementation if:

- action selection requires private goals, raw thought, provider output, or
  client-supplied patches.
- tests need concrete demo content.
- implementation would mutate world state without rule/event legality.
- changes require persistence, frontend, external Validation Client, or
  `backend/worldengine/`.
