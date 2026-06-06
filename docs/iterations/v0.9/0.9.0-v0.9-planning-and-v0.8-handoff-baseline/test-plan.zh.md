# Test Plan

## 要运行的精确命令

```bash
git status --short --branch
```

预期结果：changed 和 untracked files 限于 v0.9 documentation surfaces，以及任何已存在的
v0.9 parent documentation changes。没有 runtime、schema、API、frontend、backend
test、checker、fixture、migration、generated result、external repository、
Validation Client、provider configuration 或 `backend/worldengine/` implementation
文件被本包改变。

```bash
git diff --check
```

预期结果：tracked diffs 中没有 whitespace errors。

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline')
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
paths = list(Path('docs/iterations/v0.9').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline').glob('*.md'))
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

预期结果：所有 checked v0.9 Markdown files 都有 final newline，没有 trailing
whitespace，也没有 tab characters。

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9')
checks = {
    '0.9.0 review complete': '0.9.0-v0.9-planning-and-v0.8-handoff-baseline: review complete',
    '0.9.1 docs needed': '0.9.1-provider-live-smoke-and-redaction-boundary: planned / documentation package needed',
    'current route': '0.9.1-provider-live-smoke-and-redaction-boundary-documentation-package-needed',
    'implementation closed': 'Implementation authorization: no',
    'provider closed': 'Provider live-call authorization: no',
}
files = [
    root / 'README.md',
    root / 'CURRENT_STATE.md',
    root / 'v0.9-plan.md',
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
paths = list(Path('docs/iterations/v0.9').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline').glob('*.md'))
failures = []
patterns = [
    r'^(parent_implementation_authorized|active_child_implementation_authorized|implementation_authorized|evidence_execution_authorized|provider_live_call_authorized)[:：]\s*yes\b',
    r'^(Implementation authorization|Evidence execution authorization|Provider live-call authorization|External validation authorization)[:：]\s*yes\b',
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

## 未运行命令及原因

Backend tests、frontend tests、E2E、API smoke、Agent smoke、autonomous validation、
live provider smoke、Validation Client flows、checker fixture execution，以及
generated-result validation 不为本包运行。

原因：本包是 documentation-only。它不授权 runtime、API、schema、frontend、checker、
fixture、provider、generated-result、external repository、Validation Client 或
`backend/worldengine/` implementation changes 或 evidence execution。

## Blocker Recording Rule

如果任何 documentation check 失败，把它记录到 `review.md`，并且不要把 package 标记为
review complete，直到失败被修复或以正确 severity 明确接受。

如果 subagent/evaluator tooling 不可用，或返回 P0/P1/blocking P2，把 blocker 记录到
`review.md`，并且不要把 route 推进到 `0.9.1`。

## No Unverified Claims Rule

除非相关 command 或 flow 在当前会话中运行并且结果记录到 `review.md`，否则不要声称
tests、builds、E2E、UI smoke、runtime behavior、provider live smoke、LLM-backed
generation、checker support、autonomous validation、Validation Client handoff、
product readiness 或 external validation passed。
