# Test Plan

英文原文：`test-plan.md`。

## 要运行的精确命令

Focused 0.9.5 tests：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py -q
```

Related runtime regression：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py app/tests/test_runtime_step.py app/tests/test_archive_snapshot_summary.py app/tests/test_dry_run_validation.py app/tests/test_agent_loop_api.py -q
```

Backend regression：

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

Documentation and whitespace checks：

```bash
git diff --check
```

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget')
combined = '\n'.join(path.read_text() for path in root.glob('*.md'))
required = [
    'provider_live_call_authorized: no',
    'generated_result_creation_authorized: no',
    'external_validation_authorized: no',
    'RuntimeRunRequest',
    'RuntimeRunSummary',
    'pause',
    'resume',
    'bounded runtime',
]
missing = [term for term in required if term not in combined]
if missing:
    raise SystemExit(f'missing required terms: {missing}')
print('OK')
PY
```

## 预期结果

- Focused tests 通过，覆盖 bounded tick runs、duration runs、pause/resume、invalid
  unbounded requests、max guard rejection、public run summary fields、provider/cost counters
  和 single-step compatibility。
- Related runtime regression 通过。
- Backend regression 通过，或用证据记录 unrelated existing failures。
- `git diff --check` 通过。
- Documentation term check 通过。

## 不运行的命令及原因

- Live provider smoke：`0.9.5` 未授权。
- Generated result creation：`0.9.5` 未授权。
- Checker execution 或 external validation：`0.9.5` 未授权。
- Validation Client E2E：不在本包范围内。
- Autonomous validation：不在本包范围内。

## Blocker 记录规则

如果任何 required command 失败，在 `review.md` 记录 exact command、exit status、相关输出、
suspected scope，以及是否 blocks closeout。不得用更窄命令替代失败命令后声明 package pass。

## 禁止未验证声明

只有当前会话实际运行的命令可以记录为 passed。历史 v0.8 或更早 v0.9 evidence 只能作为 handoff context。
