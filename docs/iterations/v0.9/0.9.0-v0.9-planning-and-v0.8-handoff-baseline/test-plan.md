# Test Plan

## Exact Commands To Run

```bash
git status --short --branch
```

Expected result: changed and untracked files are limited to v0.9 documentation
surfaces and any pre-existing v0.9 parent documentation changes. No runtime,
schema, API, frontend, backend test, checker, fixture, migration, generated
result, external repository, Validation Client, provider configuration, or
`backend/worldengine/` implementation files are changed by this package.

```bash
git diff --check
```

Expected result: no whitespace errors in tracked diffs.

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

Expected result: `missing_child_docs 0`.

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

Expected result: all checked v0.9 Markdown files have final newlines, no
trailing whitespace, and no tab characters.

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

Expected result: `status_check_failures 0`.

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

Expected result: `authorization_guard_failures 0`.

## Commands Not Run And Why

Backend tests, frontend tests, E2E, API smoke, Agent smoke, autonomous
validation, live provider smoke, Validation Client flows, checker fixture
execution, and generated-result validation are not run for this package.

Reason: this is documentation-only. It does not authorize runtime, API,
schema, frontend, checker, fixture, provider, generated-result, external
repository, Validation Client, or `backend/worldengine/` implementation
changes or evidence execution.

## Blocker Recording Rule

If any documentation check fails, record it in `review.md` and do not mark the
package review complete until the failure is fixed or explicitly accepted at
the correct severity.

If subagent/evaluator tooling is unavailable or returns P0/P1/blocking P2,
record the blocker in `review.md` and do not advance the route to `0.9.1`.

## No Unverified Claims Rule

Do not claim tests, builds, E2E, UI smoke, runtime behavior, provider live
smoke, LLM-backed generation, checker support, autonomous validation,
Validation Client handoff, product readiness, or external validation passed
unless the relevant command or flow ran in the current session and the result
is recorded in `review.md`.
