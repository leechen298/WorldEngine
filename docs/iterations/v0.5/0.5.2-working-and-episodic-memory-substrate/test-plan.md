# Test Plan

Status: review complete

## TDD Requirement

Before production code changes, add focused failing backend tests for the
memory substrate and run them to observe the expected failure.

## Unit Tests

Add:

- `backend/app/tests/test_agent_memory_substrate.py`

Required coverage:

- working-memory records validate required semantics.
- working-memory store scopes by `agent_id` and `world_id`.
- bounded working-memory listing is deterministic and priority-aware.
- episodic records preserve event references, tick, and world time.
- episodic listing is scoped and deterministic.
- store read results do not expose mutable backing state.

## Regression Tests

Run adjacent compatibility tests:

- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_service.py`
- `backend/app/tests/test_agent_loop_api.py`
- `backend/app/tests/test_agent_action_adapter.py`

Run full backend regression only if implementation touches existing shared
schemas, app factory state, loop/API behavior, runtime, event, params, archive,
or other shared surfaces beyond the approved new modules.

## Commands

Documentation and scope checks:

```bash
git diff --check
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.2-working-and-episodic-memory-substrate'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed=('docs/iterations/v0.5/0.5.0-v0.5-planning-and-continuity-boundary-baseline/','docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/','docs/iterations/v0.5/0.5.2-working-and-episodic-memory-substrate/','docs/iterations/v0.5/README.md','docs/iterations/v0.5/README.zh.md','docs/iterations/v0.5/CURRENT_STATE.md','docs/iterations/v0.5/CURRENT_STATE.zh.md','docs/iterations/v0.5/v0.5-plan.md','docs/iterations/v0.5/v0.5-plan.zh.md','docs/iterations/v0.5/review.md','docs/iterations/v0.5/review.zh.md','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

Expected results:

- `git diff --check` exits 0 with no output.
- package docs and mirrors check prints `missing=0`.
- changed-file scope guard prints `out_of_scope=0`.
- TDD red run fails before production code because the memory substrate module
  does not exist yet.
- focused memory tests pass after implementation.
- adjacent compatibility tests pass with existing loop/action behavior
  unchanged.

TDD red command:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_memory_substrate.py -q
```

Focused and adjacent green commands:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_memory_substrate.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_agent_perception.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_agent_action_adapter.py -q
```

Optional broader backend regression if required by touched surfaces:

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

## Acceptance Criteria

- TDD red failure is recorded before production code.
- Focused memory tests pass.
- Adjacent loop/perception/API/action tests pass.
- Documentation checks and changed-file scope guard pass.
- Required evaluators report no unresolved P1/P2 before closeout.

## Blocker Recording Rule

If any documentation, TDD, focused, adjacent compatibility, or scope check
fails, record the exact command, exit status, and failure summary in
`review.md`. Fix only inside the approved package scope, then rerun the failed
command before claiming progress.

If a required evaluator is unavailable or returns P1/blocking P2, record
`BLOCKED` or `NEEDS_USER_INPUT` and do not start or close implementation.

## No Unverified Claims Rule

Do not mark backend tests, compatibility tests, runtime/API behavior, E2E,
Agent smoke, autonomous validation, build, migration, or release evidence as
passed unless the exact command or flow was run in the current session and the
result is recorded in `review.md`.

## Not Run

Frontend, E2E, Agent smoke, autonomous validation, fixture validation,
migrations, external validation runners, and builds are not required unless the
implementation unexpectedly touches those surfaces. Any skipped check must be
recorded in `review.md`.
