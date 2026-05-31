# Test Plan

Status: review complete

## Verification Strategy

`0.5.5` is documentation-only, but it audits implementation evidence. It must
therefore run documentation checks and refresh the core backend regression
evidence for the implemented v0.5 surfaces.

## Required Commands

```bash
git diff --check
```

Expected: exit `0`, no output.

```bash
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.5-v0.5-evidence-and-compatibility-audit'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

Expected: `missing=0`.

```bash
python3 -c "import subprocess; allowed=('docs/iterations/v0.5/','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py','backend/app/schemas/agent_loop.py','backend/app/agent/perception.py','backend/app/api/app_factory.py','backend/app/tests/test_agent_perception.py','backend/app/tests/test_agent_loop_api.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

Expected: `out_of_scope=0`.

```bash
git status --short -- backend/worldengine frontend backend/app/alembic backend/migrations
```

Expected: no output.

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_memory_substrate.py app/tests/test_agent_perception.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_agent_action_adapter.py -q
```

Expected: exit `0`.

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

Expected: exit `0`.

## Skipped Checks

Frontend, browser E2E, Agent smoke, autonomous, migrations, fixture, and
external validation checks are not required for `0.5.5` because this package
does not change those surfaces. Their absence must be recorded in review.

## Evaluator Checkpoint

Run a read-only evidence/compatibility evaluator after local checks.
