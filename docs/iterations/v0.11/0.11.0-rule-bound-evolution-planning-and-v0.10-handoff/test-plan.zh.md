# Test Plan

英文版本：`test-plan.md`。

本包是 documentation-only。无需 runtime tests。

## Documentation Checks

从 repo root 运行：

```bash
git status --short --branch
git diff --check
python3 - <<'PY'
from pathlib import Path

pkg = Path('docs/iterations/v0.11/0.11.0-rule-bound-evolution-planning-and-v0.10-handoff')
required = [
    'README.md', 'README.zh.md',
    'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md',
    'technical-design.md', 'technical-design.zh.md',
    'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md',
    'review.md', 'review.zh.md',
]
missing = [name for name in required if not (pkg / name).exists()]
empty = [name for name in required if (pkg / name).exists() and not (pkg / name).read_text().strip()]
print({'missing': missing, 'empty': empty})
PY
```

Expected results：

- 记录 `git status --short --branch`，不 stage，不 commit。
- `git diff --check` 通过。
- package completeness check 没有 missing 或 empty files。

## No-Code-Test Rationale

本包不改 backend、frontend、schema、provider、checker、fixture、migration、
Validation Client 或 runtime files。运行 runtime tests 不能验证本 handoff document change。

## Recording Rules

- 未在当前 session 运行的 runtime tests，不得声明通过。
- 不声明 provider、external Validation Client、Agent autonomy、durable persistence 或
  product readiness PASS。
