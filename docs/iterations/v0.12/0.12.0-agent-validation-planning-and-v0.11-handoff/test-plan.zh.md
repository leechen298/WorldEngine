# Test Plan

英文源文件：`test-plan.md`。

本包是 documentation-only，不运行 runtime、API、frontend、provider、checker、
Validation Client 或 Agent behavior tests。

## Documentation Checks

运行：

```bash
git status --short --branch
git diff --check
python3 - <<'PY'
from pathlib import Path

pkg = Path('docs/iterations/v0.12/0.12.0-agent-validation-planning-and-v0.11-handoff')
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
rg -n "implementation_authorized: yes|evidence_execution_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.0-agent-validation-planning-and-v0.11-handoff docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## Expected Results

- Package file check 没有 missing 或 empty files。
- `git diff --check` 无输出。
- Authorization scan 不发现 active yes authorization fields。
- Review 记录未运行 runtime tests，因为本包是 docs-only。

## Commands Not Run

- Backend tests：未运行；本包不修改 runtime code。
- Frontend/E2E：未运行；本包不修改 frontend code。
- Provider live call：未授权，未运行。
- External Validation Client automation：未授权，未运行。
- Agent smoke/autonomous validation：不在范围内，未运行。
