# Technical Design

英文源文件：`technical-design.md`。

## Existing Inputs

- `backend/app/agent/loop_service.py` 提供 request-scoped perception 和 action adapter
  path。它保持兼容，但当 client supply intent 时，不能作为充分 autonomy evidence。
- `backend/app/agent/perception.py` 可以从 runtime state、event log、world params、runtime
  context 和 memory context 构建 bounded public perception。
- `backend/app/core/world_session.py` 存储 process-local public sessions、rules 和 direction
  queues。
- `backend/app/api/routes/session.py` 拥有 session-scoped public runtime、rules、direction、
  evolution、snapshot 和 evidence APIs。

## Proposed Public Schemas

在 `backend/app/schemas/session.py` 或小型 `backend/app/schemas/session_agent.py` module
中新增 redaction-safe session Agent schemas：

- `SessionAgentRuntimeRef`：tick、world time、step seconds。
- `SessionAgentEvidenceRef`：event IDs 和 event count before/after。
- `SessionAgentPublicState`：agent ID、session ID、world ID、state、public status、last
  observation summary、current intent label、visible action、runtime ref、evidence refs、
  redaction status。
- `SessionAgentStepRequest`：bounded event limit 和 optional mode hints only。不得接受
  concrete action patches/intents。
- `SessionAgentStepResponse`：previous state、updated state、public intent、
  action/rest/wait result label、evidence refs、redaction status。

允许的 state labels：

```text
observing
no_intent
acting
waiting
resting
blocked
```

## Store / Loop Design

扩展 `InMemoryWorldSessionStore`，或新增相邻 helper：

- first list/read 时为 session 创建 default Agent。
- `list_agents(session_id)`。
- `get_agent(session_id, agent_id)`。
- `step_agent(session_id, agent_id, runtime_state, recent_events)`。

Deterministic MVP policy 应保持简单：

1. 从 current runtime ref 和 latest public event types 构建 public observation summary。
2. 如果没有 actionable public event，记录 `no_intent` 或 `waiting`。
3. 如果存在 rule/evolution public event，记录 bounded public `action` label，例如
   `acknowledge_public_event`；不修改 world params。
4. 当 allowed public mode hint 请求时，可以记录 `resting`。

## API Design

在现有 session router 下新增 endpoints：

```text
GET  /sessions/{session_id}/agents
GET  /sessions/{session_id}/agents/{agent_id}
POST /sessions/{session_id}/agents/{agent_id}/step
```

Step endpoint 必须通过 Pydantic `extra="forbid"` reject unknown fields，且不得接受
`intent`、`patches` 或 direct action payloads。

## Event Evidence

Agent step append public events，例如：

```text
world.agent.observed
world.agent.intent.recorded
world.agent.action.recorded
world.agent.wait.recorded
world.agent.rest.recorded
```

Event payloads 只包含 public fields：

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

为三个 session Agent endpoints 和 `session_agent_runtime_loop` capability 添加 public manifest
discovery items。保持 additive。

## Stop Points

如果出现以下情况，停止 implementation：

- action selection 需要 private goals、raw thought、provider output 或 client-supplied patches。
- tests 需要 concrete demo content。
- implementation 会绕过 rule/event legality 修改 world state。
- changes 需要 persistence、frontend、external Validation Client 或 `backend/worldengine/`。
