# Test Plan

Status: review complete

## TDD Requirement

Before production code changes, add a focused failing test for memory context
in perception or loop API and run it to observe the expected failure.

## Unit Tests

Update or add focused tests for:

- `PerceptionBuilder` includes bounded working and episodic memory context.
- memory context is copied and cannot mutate store backing state.
- old `PerceptionBuilder` callers still work when no memory store is provided.
- loop API includes memory context only additively and preserves old request
  compatibility.
- action result behavior remains unchanged.

## Regression Tests

Run:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_memory_substrate.py app/tests/test_agent_perception.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_agent_action_adapter.py -q
```

Run broader adjacent compatibility if app factory wiring touches shared
state:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_params.py app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py app/tests/test_runtime_step.py -q
```

Run full backend regression only if implementation touches behavior beyond
approved loop/perception/app-factory memory wiring.

## Commands

Documentation and scope checks:

```bash
git diff --check
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.3-memory-context-loop-integration'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed=('docs/iterations/v0.5/','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py','backend/app/schemas/agent_loop.py','backend/app/agent/perception.py','backend/app/api/app_factory.py','backend/app/tests/test_agent_perception.py','backend/app/tests/test_agent_loop_api.py','backend/app/tests/test_agent_loop_service.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

## Expected Results

- Documentation checks print `missing=0` and `out_of_scope=0`.
- Scope guard accepts already reviewed `0.5.2` memory substrate files as the
  inherited baseline for this single-commit `/goal` campaign.
- TDD red fails before production code because `PerceptionFrame` lacks memory
  context.
- Focused/adjacent backend tests pass after implementation.
- Existing strict request validation and action behavior tests continue to
  pass.

## Blocker Recording Rule

Record any failed command, exit status, and failure summary in `review.md`.
Fix only inside approved scope and rerun the failed command before claiming
progress.

## No Unverified Claims Rule

Do not claim API, loop, runtime, frontend, E2E, Agent smoke, autonomous,
fixture, migration, build, or release behavior passed unless the exact current
session command or flow is recorded.

## Not Run

Frontend, E2E, Agent smoke, autonomous validation, fixture validation,
migrations, external validation runners, and builds are not required unless
implementation touches those surfaces.
