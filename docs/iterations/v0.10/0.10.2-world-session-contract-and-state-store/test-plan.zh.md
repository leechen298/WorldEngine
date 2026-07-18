# Test Plan

## Exact Commands To Run

```bash
git status --short --branch
git diff --check
```

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.2-world-session-contract-and-state-store')
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

从 `backend` 运行 focused backend verification：

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py
```

预期结果：focused session、manifest compatibility 和 runtime compatibility tests 通过。

## Commands Not Run And Why

Full backend regression、frontend unit/build、E2E、Agent smoke、autonomous validation、
provider live calls、checker result generation、Validation Client execution、generated-result
creation 和 external validation 默认不要求，除非 focused tests 或 review 显示 broader impact。

## Blocker Recording Rule

如果 session create/list/read/status 无法在不做 runtime execution、dashboard、persistence、
provider、checker 或 external client work 的情况下实现，则停止并记录 `BLOCKED` 或修订 package。

## No Unverified Claims Rule

只有列出的 focused tests 通过后，本包才能声明 focused session contract/state-store behavior。
