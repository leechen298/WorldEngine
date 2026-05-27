# Test Plan

## Unit Tests

Add `backend/app/tests/test_runtime_context_bridge.py` with focused tests for:

- deriving context from a successful `LoadedWorldSpec`.
- context fields matching the reviewed shape.
- unsupported input returning `unsupported_input`.
- unsuccessful loader results returning `unsupported_input` or
  `invalid_loaded_worldspec`, according to the implemented input wrapper.
- incomplete loaded output returning `invalid_loaded_worldspec`.
- derivation failures returning `context_derivation_error`.
- context summary containing only bounded diagnostic fields.
- no raw `WorldSpec` object or raw `WorldSpec` dictionary in context summary.
- default `RuntimeEngine()` construction and `step()` with no context.
- optional context storage, if added, leaving `RuntimeEngine.step()` output
  unchanged.
- no raw `WorldSpec` event payloads when stepping runtime with context.

## Regression Tests

Run existing focused tests for touched compatibility surfaces:

- `backend/app/tests/test_runtime_step.py`
- `backend/app/tests/test_event_api_compat.py`
- `backend/app/tests/test_event_schema_compat.py`
- `backend/app/tests/test_world_params.py`
- `backend/app/tests/test_params_agent.py`
- `backend/app/tests/test_archive_snapshot_summary.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_worldspec_schema_smoke.py`

Run broader backend tests if implementation touches shared runtime helpers
beyond `runtime_context.py`, `runtime_engine.py`, or focused tests.

## Commands

Documentation-stage checks:

```bash
git status --short --branch
git diff --check
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/README.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/intent.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/contract.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/technical-design.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/plan.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/README.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/intent.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/contract.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/plan.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.zh.md
rg -n 'Status: ready for review|状态：`待评审`|状态：待评审|0\.3\.4-runtime-context-bridge-implementation' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation
rg -n 'RuntimeContextBridge|RuntimeContextInput|RuntimeContext|RuntimeContextSummary|RuntimeContextBridgeError|unsupported_input|invalid_loaded_worldspec|context_derivation_error|RuntimeEngine|world_time_seconds|/runtime/state|/runtime/step|/world/events|/world/event-steps|params|archive|frontend|backend/worldengine' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

Implementation-stage checks:

```bash
git status --short --branch
git diff --check
pytest backend/app/tests/test_runtime_context_bridge.py
pytest backend/app/tests/test_runtime_step.py
pytest backend/app/tests/test_event_api_compat.py
pytest backend/app/tests/test_event_schema_compat.py
pytest backend/app/tests/test_world_params.py backend/app/tests/test_params_agent.py
pytest backend/app/tests/test_archive_snapshot_summary.py
pytest backend/app/tests/test_worldspec_loader.py backend/app/tests/test_worldspec_schema_smoke.py
! rg -n 'APIRouter|FastAPI|archive|params_apply|migration|frontend|backend/worldengine' backend/app/core/runtime_context.py
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' backend/app/core/runtime_context.py backend/app/tests/test_runtime_context_bridge.py
```

The `rg` commands prefixed with `!` are no-match checks. If a reviewed
implementation needs a matching term only in a negative test or explanatory
comment, run the matching command without `!`, inspect every match, and record
the rationale in `review.md`.

## Acceptance Criteria

- Required package docs and Chinese mirrors exist.
- Package README and milestone index mark 0.3.4 as `ready for review` /
  `待评审`.
- Documentation states assumptions, open risks, allowed changes, forbidden
  changes, acceptance requirements, and implementation-stage verification.
- Implementation adds only approved bridge code, optional inert runtime
  storage, and focused tests.
- Focused runtime context bridge tests pass in the implementation session.
- Required compatibility tests pass in the implementation session.
- Scope checks show no schema, API, frontend, fixture, migration,
  persistence, params, archive, event, or legacy implementation changes
  outside the reviewed contract.
- Concrete anchor sweep shows no introduced concrete demo-world or external
  validation-world content.

## Not Run

During documentation stage, backend, frontend, API, E2E, Agent smoke, and
runtime behavior tests are not planned because implementation files are not
modified.

During implementation stage, any skipped verification must be recorded in
`review.md` with the reason and residual risk.
