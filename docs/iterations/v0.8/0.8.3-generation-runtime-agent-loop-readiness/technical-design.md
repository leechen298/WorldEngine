# Technical Design

## Design Summary

The implementation candidate is a generic core-readiness probe in the existing
world-generation surface. It reuses current generation, loader,
runtime-context, runtime-engine, and Agent-loop primitives. It must not wire a
candidate `WorldSpec` into `app.state.runtime_engine`.

## Candidate API

```text
POST /world/generation/core-readiness
```

Candidate request shape:

- `request_id`
- either `worldspec` or `preview_request`
- optional `source_label`
- optional `event_limit`, bounded like `LoopStepRequest`

Candidate response shape:

- `request_id`
- `validation_status`
- `preview` when a preview request is supplied.
- `runtime_readiness`
- `isolated_runtime_step`
- `agent_loop_probe`
- `does_not_mutate_app_runtime`
- `diagnostics`

Names may be refined during implementation, but the semantics above must stay
stable.

## Implementation Flow

1. Resolve the candidate `WorldSpec`.
   - If `worldspec` is provided, use it directly.
   - If `preview_request` is provided, call existing `preview_generation()`.
   - If preview fails, return failed diagnostics without runtime or Agent
     success evidence.
2. Call existing `check_runtime_readiness()`.
3. If runtime readiness fails, return failed diagnostics.
4. Load the candidate again through existing loader/runtime-context helpers to
   create a `RuntimeContext` for the isolated runtime.
5. Create isolated `InMemoryEventLog`, `WorldState`, and `RuntimeEngine` with
   the derived runtime context.
6. Call `RuntimeEngine.step()` once.
7. Create an isolated `AgentLoopService` with default bounded perception and
   `ActionResultAdapter`.
8. Call the service with default `LoopStepRequest(event_limit=...)`, forcing
   the default `noop` intent.
9. Return bounded evidence.

## Evidence Shape

The response should expose only:

- generation metadata and preview payload already allowed by existing preview
  semantics.
- runtime-readiness result and context summary.
- isolated runtime state after one step.
- bounded event ids/types/ticks from isolated events.
- Agent loop intent type/reason, result status/applied flag, and perception
  summary.

It must not expose raw prompts, provider traces, secrets, private transcript
data, raw memory store internals, app event log contents, or external
validation oracle details.

## Compatibility

- Existing `/world/generation/preview`, `/regenerate`, and `/runtime-readiness`
  behavior must not change.
- Existing `/runtime/state`, `/runtime/step`, and `/world/agent/loop/step`
  behavior must not change.
- API additions must use the existing `ApiResponse` envelope and pydantic 422
  error handling.
- Schema changes must be additive.

## Stop Rules

Stop implementation if:

- the probe needs frontend changes.
- the probe mutates `app.state.runtime_engine`, app event log, app world params,
  memory store, archive store, or external state.
- the probe needs persistence, migration, live provider behavior, external
  validator connection logic, or product-app behavior.
- test evidence cannot distinguish isolated runtime events from app runtime
  events.
