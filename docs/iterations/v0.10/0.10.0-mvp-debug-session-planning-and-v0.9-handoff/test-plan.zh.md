# Test Plan

## Exact Commands To Run

```bash
git status --short --branch
```

预期结果：review closeout 前可见 branch 和 dirty-file scope。

```bash
git diff --check
```

预期结果：无 whitespace errors。

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.10/0.10.0-mvp-debug-session-planning-and-v0.9-handoff')
names = ['README', 'intent', 'contract', 'technical-design', 'test-plan', 'plan', 'review']
missing = []
for name in names:
    for suffix in ['.md', '.zh.md']:
        path = root / f'{name}{suffix}'
        if not path.exists():
            missing.append(str(path))
print('missing_child_docs', len(missing))
if missing:
    print('\\n'.join(missing))
    raise SystemExit(1)
PY
```

预期结果：`missing_child_docs 0`。

```bash
python3 - <<'PY'
from pathlib import Path
paths = list(Path('docs/iterations/v0.10').glob('*.md'))
paths += list(Path('docs/iterations/v0.10/0.10.0-mvp-debug-session-planning-and-v0.9-handoff').glob('*.md'))
errors = []
for path in sorted(paths):
    data = path.read_bytes()
    if data and not data.endswith(b'\\n'):
        errors.append(f'{path}: missing final newline')
    for i, line in enumerate(data.splitlines(), 1):
        if line.rstrip(b' \\t') != line:
            errors.append(f'{path}:{i}: trailing whitespace')
        if b'\\t' in line:
            errors.append(f'{path}:{i}: tab character')
print('markdown_files', len(paths))
if errors:
    print('\\n'.join(errors))
    raise SystemExit(1)
print('OK')
PY
```

预期结果：markdown formatting check 通过。

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.10')
checks = {
    '0.10.0 review complete': '0.10.0-mvp-debug-session-planning-and-v0.9-handoff: review complete',
    '0.10.1 docs needed': '0.10.1-mvp-public-manifest-and-debug-handoff: planned / documentation package needed',
    'current route': '0.10.1-mvp-public-manifest-and-debug-handoff-documentation-package-needed',
    'implementation closed': 'Implementation authorization: no',
    'evidence closed': 'Evidence execution authorization: no',
}
files = [
    root / 'README.md',
    root / 'CURRENT_STATE.md',
    root / 'v0.10-plan.md',
    root / 'review.md',
]
failures = []
for label, needle in checks.items():
    if not any(needle in path.read_text() for path in files if path.exists()):
        failures.append(f'{label}: missing {needle!r}')
print('status_check_failures', len(failures))
if failures:
    print('\\n'.join(failures))
    raise SystemExit(1)
PY
```

预期结果：`status_check_failures 0`。

```bash
python3 - <<'PY'
from pathlib import Path
import re
paths = list(Path('docs/iterations/v0.10').glob('*.md'))
paths += list(Path('docs/iterations/v0.10/0.10.0-mvp-debug-session-planning-and-v0.9-handoff').glob('*.md'))
failures = []
patterns = [
    r'^(parent_implementation_authorized|active_child_implementation_authorized|implementation_authorized|evidence_execution_authorized|provider_live_call_authorized|external_validation_authorized)[:：]\\s*yes\\b',
    r'^(Implementation authorization|Evidence execution authorization|Provider live-call authorization|External validation authorization)[:：]\\s*yes\\b',
]
for path in paths:
    for i, line in enumerate(path.read_text().splitlines(), 1):
        stripped = line.strip().rstrip('.。')
        if any(re.search(pattern, stripped) for pattern in patterns):
            failures.append(f'{path}:{i}: current authorization unexpectedly open: {line}')
print('authorization_guard_failures', len(failures))
if failures:
    print('\\n'.join(failures))
    raise SystemExit(1)
PY
```

预期结果：`authorization_guard_failures 0`。

## Commands Not Run And Why

backend、frontend、API smoke、E2E、Agent smoke、autonomous validation、live provider、
checker saved-result generation、Validation Client、generated-result、external validation 和
runtime tests 不运行，因为本包是 documentation-only routing package，不授权 implementation
或 evidence execution。

## Blocker Recording Rule

如果任何 documentation check 失败，将其记录在 `review.md`，并在 documentation-only scope
内修复后再 closeout。如果修复需要 runtime、schema、API、frontend、checker、provider、
generated-result、Validation Client 或 external repository work，则停止并标为 `BLOCKED`。

## No Unverified Claims Rule

只有当前 session 实际运行的命令可以记录为 passed。本包不得声明 v0.10 runtime、dashboard、
provider、Validation Client、checker、external validation 或 MVP PASS。
