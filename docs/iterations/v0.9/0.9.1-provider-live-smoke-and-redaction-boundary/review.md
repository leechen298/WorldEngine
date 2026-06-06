# Review

Chinese mirror: `review.zh.md`.

Status: implementation complete / non-live focused verification passed
implementation_authorized: yes
evidence_execution_authorized: yes, limited to non-live focused tests in `test-plan.md`
provider_live_call_authorized: no

## Changed Files

Created:

```text
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/README.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/README.zh.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/intent.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/intent.zh.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/contract.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/contract.zh.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/technical-design.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/technical-design.zh.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/test-plan.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/test-plan.zh.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/plan.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/plan.zh.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/review.md
docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary/review.zh.md
```

Implementation files:

```text
backend/app/agent/provider_config.py
backend/app/api/routes/provider.py
backend/app/schemas/provider.py
backend/app/api/app_factory.py
backend/app/api/routes/__init__.py
backend/app/api/routes/world.py
backend/app/tests/test_provider_live_smoke_api.py
backend/app/tests/test_public_handoff_contract_api.py
```

## Commands Run

```bash
git status --short --branch
```

Result: branch `v0.9...origin/v0.9`; changed/untracked files are limited to
v0.9 documentation surfaces, the pre-existing `docs/roadmap.md` planning
update, and the reviewed `0.9.1` backend provider/API/schema/test surfaces.
No frontend, checker, fixture, generated-result, Validation Client, external
repository, concrete world content, or `backend/worldengine/` files were
changed by this package.

```bash
git diff --check
```

Result: passed with no output.

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary')
names = ['README', 'intent', 'contract', 'technical-design', 'test-plan', 'plan', 'review']
missing = [str(root / f'{name}{suffix}') for name in names for suffix in ['.md', '.zh.md'] if not (root / f'{name}{suffix}').exists()]
print('missing_child_docs', len(missing))
if missing:
    print('\n'.join(missing))
    raise SystemExit(1)
PY
```

Result: `missing_child_docs 0`.

```bash
python3 - <<'PY'
from pathlib import Path
paths = list(Path('docs/iterations/v0.9').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary').glob('*.md'))
errors = []
for path in sorted(paths):
    data = path.read_bytes()
    if data and not data.endswith(b'\n'):
        errors.append(f'{path}: missing final newline')
    for i, line in enumerate(data.splitlines(), 1):
        if line.rstrip(b' \t') != line:
            errors.append(f'{path}:{i}: trailing whitespace')
        if b'\t' in line:
            errors.append(f'{path}:{i}: tab character')
print('markdown_files', len(paths))
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('OK')
PY
```

Result: `markdown_files 40`; `OK`.

```bash
python3 - <<'PY'
from pathlib import Path
import re
paths = list(Path('docs/iterations/v0.9').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary').glob('*.md'))
patterns = [
    r'^(parent_implementation_authorized|active_child_implementation_authorized|implementation_authorized|evidence_execution_authorized|provider_live_call_authorized)[:：]\s*yes\b',
    r'^(Implementation authorization|Evidence execution authorization|Provider live-call authorization|External validation authorization)[:：]\s*yes\b',
]
failures = []
for path in paths:
    for i, line in enumerate(path.read_text().splitlines(), 1):
        stripped = line.strip().rstrip('.。')
        if any(re.search(pattern, stripped) for pattern in patterns):
            failures.append(f'{path}:{i}: current authorization unexpectedly open: {line}')
print('authorization_guard_failures', len(failures))
if failures:
    print('\n'.join(failures))
    raise SystemExit(1)
PY
```

Documentation-gate result before implementation authorization:
`authorization_guard_failures 0`.

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary')
required = {
    'README.md': ['Status: implementation complete / non-live focused verification passed', 'implementation_authorized: yes', 'provider_live_call_authorized: no'],
    'contract.md': ['Public Provider Live Summary', 'Allowed Changes', 'Forbidden Changes', 'Compatibility Requirements', 'Stop Rules'],
    'technical-design.md': ['POST /provider/live-smoke', 'Provider Call Strategy', 'Redaction Strategy', 'Compatibility Strategy'],
    'test-plan.md': ['Focused Backend Tests', 'Optional Live Provider Smoke', 'Pass Criteria'],
    'plan.md': ['Ordered Steps', 'Phase Boundaries', 'Stop Conditions'],
    'review.md': ['Status: implementation complete / non-live focused verification passed', 'implementation_authorized: yes', 'provider_live_call_authorized: no'],
}
failures=[]
for name, needles in required.items():
    text=(root/name).read_text()
    for needle in needles:
        if needle not in text:
            failures.append(f'{name}: missing {needle!r}')
print('shape_failures', len(failures))
if failures:
    print('\n'.join(failures))
    raise SystemExit(1)
PY
```

Final implementation closeout result: `shape_failures 0`.

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py -q
```

Initial result before review-found fixes: `13 passed`.

Final result after fixing evaluator P1/P2 findings: `16 passed in 0.67s`.

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

Initial result before review-found fixes: `255 passed`.

Final result after fixing evaluator P1/P2 findings: `258 passed in 2.12s`.

```bash
git diff --check
```

Final result after implementation: passed with no output.

## Test Results

Documentation checks passed:

- `git diff --check`: passed.
- Required `0.9.1` child docs and mirrors: `missing_child_docs 0`.
- Markdown formatting: `markdown_files 40`; `OK`.
- Documentation-gate authorization status guard before implementation:
  `authorization_guard_failures 0`.
- Final implementation package shape check: `shape_failures 0`.

Backend, frontend, API, E2E, Agent smoke, autonomous, live provider,
Validation Client, checker fixture, generated-result, external validation, and
runtime tests beyond the backend regression above were not run. Live provider
calls are not authorized by this package, so the live provider smoke path was
not executed against an external provider.

## Subagent / Evaluator Evidence

Read-only documentation/contract evaluator
`019e9845-56d4-7421-a417-4e15edc5c9e5`: PASS.

Findings:

- P0: none.
- P1: none.
- P2: none.
- P3: none.

Evaluator conclusion: this package can pass the documentation/contract gate
and record `implementation_authorized: yes`. It recommended keeping
`provider_live_call_authorized: no` unless a later step explicitly authorizes
bounded live provider calls. Implementation should begin with
unconfigured/safe mock behavior and focused backend tests.

Read-only implementation-scope/code-review evaluator
`019e984d-9a34-7a31-b8ac-bacbe7d96760`: initial review reported two P1, two
P2, and one P3 finding.

Initial findings and resolution:

- P1: global 422 validation errors could echo rejected private input. Fixed by
  sanitizing `RequestValidationError` payloads to remove `input` and redact
  private field labels or values.
- P1: provider summary redaction markers missed `raw_thought` and
  `hidden context`. Fixed by expanding forbidden markers and redaction tests.
- P2: injected provider runner could execute without explicit live-call gate.
  Fixed by requiring `app.state.provider_smoke_runner_mode == "safe_mock"` for
  runner execution. Default and configured-without-safe-mock paths return
  `blocked` without calling the runner.
- P2: worktree contains earlier v0.9 parent, `0.9.0`, and roadmap docs. This
  is accepted for the current no-commit goal state but must be isolated before
  any package-scoped commit or staging operation.
- P3: unsupported provider manifest behavior lacked coverage. Fixed with a
  manifest test for `unknown/blocked` without private label echo.

Re-review result: code-level P1/P2/P3 findings closed. Remaining note is
closeout evidence/staging scope, addressed in this review.

## Compatibility Review

Implementation changed only active backend provider/API/schema/test surfaces
authorized by this package, plus package review evidence and v0.9 route/status
documentation. Existing `/manifest` remains additive-compatible, existing
`POST /worlds` behavior remains deterministic and unchanged, and unconfigured
provider state remains safe and testable.

## Scope Review

Implementation scope stayed within reviewed `0.9.1` backend/provider/test
surface and package evidence. No `backend/worldengine/`, Validation Client,
frontend, fixture, migration, generated-result, external repository, or
concrete world content changes were made.

The current worktree also contains earlier v0.9 parent, `0.9.0`, and
`docs/roadmap.md` changes from the ongoing v0.9 goal. They are not part of the
backend implementation surface. If a commit is requested, staging must isolate
the intended package scope or explicitly include the parent/previous-package
documentation scope.

## Unresolved Findings

- P1: none.
- P2: none.
- P3: worktree contains earlier v0.9 documentation changes outside the
  backend implementation surface; isolate staging before any package-scoped
  commit.

## Final Assessment

`0.9.1-provider-live-smoke-and-redaction-boundary` is implementation complete
for the reviewed non-live provider smoke boundary. Focused tests and backend
regression passed. Live provider calls remain closed and were not executed.

The next valid route is
`0.9.2-llm-worldview-ingestion-and-generation-contract-documentation-package-needed`.
