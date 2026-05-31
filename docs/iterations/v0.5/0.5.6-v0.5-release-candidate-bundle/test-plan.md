# Test Plan

Status: review complete

## Verification Strategy

`0.5.6` is documentation-only. It packages already audited evidence and must
prove that the bundle docs exist, status wording is bounded, and no
implementation surfaces changed.

## Required Commands

```bash
git diff --check
```

Expected: exit `0`, no output.

```bash
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.6-v0.5-release-candidate-bundle'); docs=['README','intent','contract','technical-design','test-plan','plan','release-candidate-bundle','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
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
rg -n "final / closeout complete|final release|released|Status: final|状态：final" docs/iterations/v0.5/0.5.6-v0.5-release-candidate-bundle
```

Expected: only forbidden-scope descriptions, not a status declaration.

## Backend Tests

Backend tests are not required for `0.5.6` because it only packages the
current `0.5.5` audit evidence. The review must reference `0.5.5` fresh
backend evidence and record why tests were not rerun here.

## Evaluator Checkpoint

Run a read-only release-candidate bundle evaluator.
