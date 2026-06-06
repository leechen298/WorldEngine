# Review

英文原文：`review.md`。

Status: implementation complete / non-live focused verification passed
implementation_authorized: yes
evidence_execution_authorized: yes, limited to non-live focused tests in `test-plan.md`
provider_live_call_authorized: no

## Changed Files

创建：

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

Implementation files：

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

Result：branch `v0.9...origin/v0.9`；changed/untracked files 限于 v0.9
documentation surfaces、已存在的 `docs/roadmap.md` planning update，以及 reviewed `0.9.1`
backend provider/API/schema/test surfaces。本包未改变 frontend、checker、fixture、
generated-result、Validation Client、external repository、concrete world content 或
`backend/worldengine/` files。

```bash
git diff --check
```

Result：passed with no output。

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

Result：`missing_child_docs 0`。

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

Result：`markdown_files 40`；`OK`。

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

Documentation-gate result before implementation authorization：
`authorization_guard_failures 0`。

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

Final implementation closeout result：`shape_failures 0`。

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py -q
```

Initial result before review-found fixes：`13 passed`。

Final result after fixing evaluator P1/P2 findings：`16 passed in 0.67s`。

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

Initial result before review-found fixes：`255 passed`。

Final result after fixing evaluator P1/P2 findings：`258 passed in 2.12s`。

```bash
git diff --check
```

Final result after implementation：passed with no output。

## Test Results

Documentation checks passed：

- `git diff --check`：passed。
- Required `0.9.1` child docs and mirrors：`missing_child_docs 0`。
- Markdown formatting：`markdown_files 40`；`OK`。
- Documentation-gate authorization status guard before implementation：
  `authorization_guard_failures 0`。
- Final implementation package shape check：`shape_failures 0`。

Backend、frontend、API、E2E、Agent smoke、autonomous、live provider、Validation
Client、checker fixture、generated-result、external validation 和 runtime tests 尚未运行。
除上述 backend regression 外未运行。Live provider calls 未被本包授权，因此没有对外部
provider 执行 live smoke。

## Subagent / Evaluator Evidence

Read-only documentation/contract evaluator
`019e9845-56d4-7421-a417-4e15edc5c9e5`：PASS。

Findings：

- P0：none。
- P1：none。
- P2：none。
- P3：none。

Evaluator conclusion：本包可以通过 documentation/contract gate，并记录
`implementation_authorized: yes`。它建议保持 `provider_live_call_authorized: no`，
除非后续明确授权 bounded live provider calls。Implementation 应先从 unconfigured/safe
mock behavior 和 focused backend tests 开始。

Read-only implementation-scope/code-review evaluator
`019e984d-9a34-7a31-b8ac-bacbe7d96760`：initial review 报告两个 P1、两个 P2 和一个
P3 finding。

Initial findings and resolution：

- P1：global 422 validation errors 可能回显被拒绝的 private input。已通过 sanitizing
  `RequestValidationError` payloads 修复，移除 `input` 并 redacted private field labels
  或 values。
- P1：provider summary redaction markers 漏掉 `raw_thought` 和 `hidden context`。已扩展
  forbidden markers 和 redaction tests。
- P2：injected provider runner 可以在没有 explicit live-call gate 时执行。已改为要求
  `app.state.provider_smoke_runner_mode == "safe_mock"` 才执行 runner。默认路径和
  configured-without-safe-mock 路径返回 `blocked`，不会调用 runner。
- P2：worktree 包含较早的 v0.9 parent、`0.9.0` 和 roadmap docs。当前 no-commit goal
  state 接受该情况，但任何 package-scoped commit 或 staging 前必须隔离。
- P3：unsupported provider manifest behavior 缺少覆盖。已添加 `unknown/blocked` 且不回显
  private label 的 manifest test。

Re-review result：code-level P1/P2/P3 findings 已关闭。剩余 note 是 closeout evidence /
staging scope，已在本 review 中处理。

## Compatibility Review

Implementation 只改变本包授权的 active backend provider/API/schema/test surfaces，以及
package review evidence 和 v0.9 route/status documentation。既有 `/manifest` 保持
additive-compatible，既有 `POST /worlds` 行为保持 deterministic 且不变，unconfigured provider
state 仍安全且可测试。

## Scope Review

Implementation scope 留在 reviewed `0.9.1` backend/provider/test surface 和 package
evidence 内。没有修改 `backend/worldengine/`、Validation Client、frontend、fixture、
migration、generated-result、external repository，也没有添加 concrete world content。

当前 worktree 还包含本 v0.9 goal 中较早的 parent、`0.9.0` 和 `docs/roadmap.md` changes。
这些不是 backend implementation surface 的一部分。如果后续要求 commit，staging 必须隔离目标
package scope，或明确包含 parent/previous-package documentation scope。

## Unresolved Findings

- P1: none.
- P2: none.
- P3: worktree 包含 earlier v0.9 documentation changes，位于 backend implementation surface
  之外；任何 package-scoped commit 前必须 isolate staging。

## Final Assessment

`0.9.1-provider-live-smoke-and-redaction-boundary` 在 reviewed non-live provider smoke
boundary 内 implementation complete。Focused tests 和 backend regression passed。Live
provider calls 保持关闭，且未执行。

下一条合法 route 是
`0.9.2-llm-worldview-ingestion-and-generation-contract-documentation-package-needed`。
