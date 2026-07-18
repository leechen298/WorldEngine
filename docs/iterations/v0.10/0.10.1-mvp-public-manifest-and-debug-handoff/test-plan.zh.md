# Test Plan

## Exact Commands To Run

Documentation and status checks：

```bash
git status --short --branch
git diff --check
```

Package document completeness：

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.1-mvp-public-manifest-and-debug-handoff')
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

Focused backend verification：

```bash
../../.venv/bin/pytest backend/app/tests/test_public_handoff_contract_api.py
```

预期结果：所有 focused manifest/debug handoff tests 通过。

如果 focused changes 触及 shared manifest/provider readiness behavior，可选兼容检查：

```bash
../../.venv/bin/pytest backend/app/tests/test_public_handoff_contract_api.py backend/app/tests/test_provider_live_smoke_api.py
```

预期结果：两个 focused files 都通过。

## Commands Not Run And Why

Full backend regression、frontend unit、frontend build、E2E、Agent smoke、autonomous
validation、live provider calls、checker saved-result generation、Validation Client
execution、generated-result creation 和 external validation 默认不要求运行，除非 focused
verification 或 review 发现更大范围破坏。本包只改变 `/manifest` schema、route construction
和 focused tests。

## Blocker Recording Rule

如果 focused backend tests 失败，在 approved file scope 内修复。如果修复需要 session runtime、
checker fixture、frontend、provider live-call、Validation Client、migration、generated-result
或 external repository work，则将 package 记录为 `BLOCKED`，或先更新 contract 供 review 后再继续。

## No Unverified Claims Rule

不得从本包声明 v0.10 runnable session、dashboard flow、provider readiness PASS、external
validation、autonomous validation、checker PASS 或 full MVP PASS。只有当前 session 中列出的命令
通过后，才能声明 focused manifest/debug handoff behavior。
