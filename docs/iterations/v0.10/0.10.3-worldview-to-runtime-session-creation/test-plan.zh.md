# Test Plan

## Exact Commands To Run

```bash
git status --short --branch
git diff --check
```

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.3-worldview-to-runtime-session-creation')
required = {
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
}
missing = sorted(name for name in required if not (pkg / name).exists())
print({'files': len(list(pkg.glob('*.md'))), 'missing': missing})
raise SystemExit(1 if missing else 0)
PY
```

从 `backend` 运行：

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_llm_worldview_generation_api.py app/tests/test_public_handoff_contract_api.py
```

## Commands Not Run And Why

Full backend regression、frontend、E2E、provider live calls、checker result generation、
Validation Client execution、generated-result creation 和 external validation 默认不要求，
除非 focused tests 显示 broader impact。

## Blocker Recording Rule

如果该 flow 需要 live provider execution、runtime run、snapshots、dashboard、checker fixtures、
persistence 或 external client work，停止并记录 `BLOCKED` 或修订 package。

## No Unverified Claims Rule

focused tests 通过后，只能声明 worldview-to-session creation。
