# Compatibility Audit

Status: audit complete

Scope: v0.4 implementation through `0.4.4-minimal-agent-loop-orchestration-and-api`.

## Summary

v0.4 adds a minimal, request-driven Agent-in-World loop without background autonomy, memory, generation, external validation readiness, projection readiness, or concrete world content.

Compatibility status:

- Runtime tick/time behavior: preserved.
- Event API pagination and optional refs behavior: preserved.
- World params validation, dry-run, apply behavior: preserved and reused.
- Existing params-agent route: preserved.
- API envelope: preserved; action validation rejection stays inside HTTP 200 loop result, while request schema errors still use 422 envelope.
- Schema changes: additive.
- Frontend, fixture, migration, legacy `backend/worldengine/`: unchanged.

## Surface Audit

| Surface | v0.4 Change | Compatibility Assessment | Evidence |
| --- | --- | --- | --- |
| Runtime state and stepping | Read-only perception uses `RuntimeEngine.get_state()`; loop action adapter reads runtime state for event tick/time. | No tick/time semantic change. | `test_runtime_step.py` included in focused backend/API command; final full backend `139 passed`. |
| Runtime context bridge | Perception optionally summarizes runtime context without exposing full root object. | Additive read-only summary; no runtime context mutation. | `test_runtime_context_bridge.py` included in 0.4.2 focused command. |
| Event log and event APIs | `params.patch` from loop emits `params.applied` with `source="agent.loop"`; perception reads newest-first events through `list_page(limit=N)`. | Event schema remains compatible; existing event routes remain covered. | `test_event_schema_compat.py`, `test_event_api_compat.py`, `test_agent_loop_api.py`. |
| World params | Loop `params.patch` uses strict `ActionParamPatchItem` schemas that remain `ParamPatchItem` compatible, then reuses `ParamValidator`, `ParamDryRunValidator`, and `WorldState.apply_patch()`. | Existing validation/apply semantics preserved; loop patch-item extras now fail with the existing 422 envelope before mutation. | `test_agent_action_adapter.py`, `test_param_validator.py`, `test_dry_run_validation.py`, `test_world_params.py`, `test_agent_loop_api.py`. |
| Existing ParamsAgent route | `/world/agent/params/propose-and-apply` was retained. | Existing endpoint behavior preserved. | `test_params_agent.py`; 0.4.4 API smoke includes existing route. |
| New loop route | Adds `POST /world/agent/loop/step`. | Additive API route; no existing route replaced. | `test_agent_loop_api.py`. |
| API error model | Action rejections return HTTP 200 with `ActionResult(status="rejected")`; invalid request bodies return existing 422 envelope. | Compatible with existing API envelope rules. | `test_agent_loop_api.py`. |
| Archive service | App factory wiring leaves archive callback unchanged. | No archive behavior change. | Full backend regression. |
| Frontend / browser E2E | No frontend changes. | Not applicable. | `git status --short --branch`; commands recorded as not run. |
| Fixtures / migrations | No fixture or migration changes. | Not applicable. | Scope guard `out_of_scope=0`. |
| Legacy backend | No changes under `backend/worldengine/`. | Preserved. | Scope guard `out_of_scope=0`. |

## Additive Schema Inventory

Added or extended models in `backend/app/schemas/agent_loop.py`:

- `RuntimeStateSummary`
- `RuntimeContextSummary`
- `PerceptionFrame`
- `ActionParamPatchItem`
- `ActionIntent`
- `ActionResult`
- `LoopStepRequest`
- `LoopStepResponse`

These models do not replace existing response models. They are consumed by the new loop service/API route and focused tests.

## Event Semantics

The loop uses the existing `params.applied` event type for successful param patches and differentiates the route with `source="agent.loop"`.

Rejected actions and no-op actions emit no event.

## Scope Exclusions Confirmed

v0.4 does not implement:

- memory, episodic memory, relationship state, self-summary, reflection, or personality drift;
- world generation;
- external validation runner readiness or report automation;
- projection application readiness;
- concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle behavior;
- new runtime features under `backend/worldengine/`.

## Residual Risk

No unresolved P1/P2 risk is recorded at this audit boundary.

Residual non-blocking risk:

- v0.4 is request-driven and deterministic for missing intent; it is not an autonomous agent runtime.
- v0.4 exposes a minimal action vocabulary only: `noop` and `params.patch`.
- Frontend and browser E2E were not run because no frontend surface changed.

## Handoff

This audit supports preparing a release-candidate bundle in `0.4.6` from the reviewed 0.4.5 documentation-only scope, mirror, command-evidence, and finding record.
