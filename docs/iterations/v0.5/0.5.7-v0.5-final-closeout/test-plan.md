# Test Plan

Status: final / closeout complete

## Verification Strategy

Final closeout must refresh the core backend evidence and prove documentation
and status surfaces are consistent before final status can be applied.

## Required Commands

```bash
git diff --check
```

Expected: exit `0`, no output.

```bash
python3 -c "from pathlib import Path; parent=Path('docs/iterations/v0.5'); parent_docs=['README','v0.5-plan','GOAL_RUNNER','CURRENT_STATE','CAMPAIGN_PLAN','review']; child_docs=['README','intent','contract','technical-design','test-plan','plan','review']; child_extra={'0.5.6-v0.5-release-candidate-bundle':['release-candidate-bundle'],'0.5.7-v0.5-final-closeout':['final-closeout']}; missing=[]; missing += [str(parent/(name+suffix)) for name in parent_docs for suffix in ('.md','.zh.md') if not (parent/(name+suffix)).exists()];\nfor child in [p for p in parent.iterdir() if p.is_dir() and p.name.startswith('0.5.')]:\n    docs=child_docs + child_extra.get(child.name, [])\n    missing += [str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]\nprint('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

Expected: `missing=0`.

```bash
python3 -c "import subprocess; allowed=('docs/iterations/v0.5/','docs/roadmap.md','docs/roadmap.zh.md','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py','backend/app/schemas/agent_loop.py','backend/app/agent/perception.py','backend/app/api/app_factory.py','backend/app/tests/test_agent_perception.py','backend/app/tests/test_agent_loop_api.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
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
external validation checks are not required for final v0.5 because the final
implementation surface is backend memory/loop code. Their absence must be
recorded and must not be converted into pass claims.

## Evaluator Checkpoint

Run a closeout consistency evaluator after the final verification commands.
Final status may be applied only after evaluator PASS.
