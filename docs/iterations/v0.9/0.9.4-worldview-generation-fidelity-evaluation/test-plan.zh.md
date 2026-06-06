# Test Plan

英文原文：`test-plan.md`。

## 要运行的精确命令

Focused 0.9.4 tests：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_worldview_fidelity_evaluation.py -q
```

Related v0.9 regression set：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_worldview_fidelity_evaluation.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_generation_schema.py app/tests/test_llm_worldview_generation_api.py app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py -q
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
paths = list(Path('docs/iterations/v0.9/0.9.4-worldview-generation-fidelity-evaluation').glob('*.md'))
required = [
    'implementation_authorized: no',
    'provider_live_call_authorized: no',
    'generated_result_creation_authorized: no',
    'external_validation_authorized: no',
    'Validation Client',
    'bounded runtime',
    'WorldviewFidelityScorecard',
    'ImmediateWorldviewFidelityArtifact',
    'BoundedRunWorldviewFidelityArtifact',
]
missing = []
combined = '\n'.join(path.read_text() for path in paths)
for term in required:
    if term not in combined:
        missing.append(term)
if missing:
    raise SystemExit(f'missing required terms: {missing}')
print('OK')
PY
```

## 预期结果

- Focused tests 通过，并覆盖 faithful immediate output、missing premise output、
  deterministic generic fallback、contradictory runtime summaries、missing bounded-run
  evidence 和 redaction failures。
- Related v0.9 regression 通过。
- Backend regression 通过，或用证据记录 unrelated existing failure。
- `git diff --check` 通过。
- Documentation term check 通过。

## 不运行的命令及原因

- Live provider smoke：`0.9.4` 未授权。
- Generated result creation：`0.9.4` 未授权。
- Checker execution 或 external validation：`0.9.4` 未授权。
- Validation Client E2E：不在本包范围内。
- Bounded runtime control verification：归属 `0.9.5`。

## Blocker 记录规则

如果任何 required command 失败，在 `review.md` 记录 exact command、exit status、相关输出、
suspected scope，以及是否 blocks closeout。不得用更窄命令替代失败命令后声明 package pass。

## 禁止未验证声明

只有当前会话实际运行的命令可以记录为 passed。历史 v0.8 或更早 v0.9 evidence 只能作为 handoff context。
