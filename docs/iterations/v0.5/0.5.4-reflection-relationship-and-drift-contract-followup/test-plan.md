# Test Plan

Status: review complete

## Verification Strategy

`0.5.4` is documentation-only. Verification proves that the package docs and
mirrors exist, that the worktree stayed inside documentation scope, and that no
runtime/code surfaces were touched.

## Required Commands

```bash
git diff --check
```

Expected: exit `0`, no output.

```bash
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.4-reflection-relationship-and-drift-contract-followup'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

Expected: `missing=0`.

```bash
python3 -c "import subprocess; allowed=('docs/iterations/v0.5/','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py','backend/app/schemas/agent_loop.py','backend/app/agent/perception.py','backend/app/api/app_factory.py','backend/app/tests/test_agent_perception.py','backend/app/tests/test_agent_loop_api.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

Expected: `out_of_scope=0`. The baseline allows inherited reviewed `0.5.2` and
`0.5.3` implementation files because this `/goal` campaign is accumulating one
final commit.

```bash
git status --short -- backend/worldengine frontend backend/app/alembic backend/migrations
```

Expected: no output.

## Backend Tests

Backend tests are not required for `0.5.4` because it is documentation-only and
does not change runtime, schemas, APIs, services, tests, migrations, or
frontend behavior.

The review must explicitly record that backend/frontend/API/E2E/build/Agent
smoke/autonomous checks were not run and why.

## Evaluator Checkpoint

Run a read-only documentation/contract evaluator after docs and local checks.
The evaluator must report no P1 and no blocking P2 before closeout.
