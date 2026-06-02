# Technical Design

## Design Summary

Implementation candidate 是 existing world-generation surface 中的 generic
core-readiness probe。它复用当前 generation、loader、runtime-context、runtime-engine 和
Agent-loop primitives。不得把 candidate `WorldSpec` 接入 `app.state.runtime_engine`。

## Candidate API

```text
POST /world/generation/core-readiness
```

Candidate request shape：

- `request_id`
- `worldspec` 或 `preview_request` 二选一
- optional `source_label`
- optional `event_limit`，边界与 `LoopStepRequest` 一致

Candidate response shape：

- `request_id`
- `validation_status`
- 提供 preview request 时返回 `preview`
- `runtime_readiness`
- `isolated_runtime_step`
- `agent_loop_probe`
- `does_not_mutate_app_runtime`
- `diagnostics`

具体命名可在 implementation 中细化，但上述 semantics 必须保持。

## Implementation Flow

1. Resolve candidate `WorldSpec`。
   - 如果提供 `worldspec`，直接使用。
   - 如果提供 `preview_request`，调用既有 `preview_generation()`。
   - 如果 preview failed，返回 failed diagnostics，不返回 runtime 或 Agent success evidence。
2. 调用既有 `check_runtime_readiness()`。
3. 如果 runtime readiness failed，返回 failed diagnostics。
4. 再通过既有 loader/runtime-context helpers 载入 candidate，创建 isolated runtime 所需的
   `RuntimeContext`。
5. 创建 isolated `InMemoryEventLog`、`WorldState` 和带 runtime context 的 `RuntimeEngine`。
6. 调用 `RuntimeEngine.step()` 一次。
7. 使用 default bounded perception 和 `ActionResultAdapter` 创建 isolated
   `AgentLoopService`。
8. 使用 default `LoopStepRequest(event_limit=...)` 调用 service，强制 default `noop`
   intent。
9. 返回 bounded evidence。

## Evidence Shape

Response 只应暴露：

- 既有 preview semantics 已允许的 generation metadata 和 preview payload。
- runtime-readiness result 和 context summary。
- 一次 isolated runtime step 后的 runtime state。
- isolated events 的 bounded event ids/types/ticks。
- Agent loop intent type/reason、result status/applied flag 和 perception summary。

不得暴露 raw prompts、provider traces、secrets、private transcript data、raw memory store
internals、app event log contents 或 external validation oracle details。

## Compatibility

- 不改变既有 `/world/generation/preview`、`/regenerate`、`/runtime-readiness` behavior。
- 不改变既有 `/runtime/state`、`/runtime/step`、`/world/agent/loop/step` behavior。
- API additions 必须使用既有 `ApiResponse` envelope 和 pydantic 422 error handling。
- Schema changes 必须 additive。

## Stop Rules

如果出现以下情况，停止 implementation：

- probe 需要 frontend changes。
- probe mutate `app.state.runtime_engine`、app event log、app world params、memory store、
  archive store 或 external state。
- probe 需要 persistence、migration、live provider behavior、external validator connection
  logic 或 product-app behavior。
- test evidence 无法区分 isolated runtime events 和 app runtime events。
