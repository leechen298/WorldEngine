# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Checks

Run before implementation authorization:

```bash
git status --short --branch
git diff --check
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

Expected result: child docs and mirrors exist; no runtime files changed before
authorization.

## Focused Backend Tests

Run after implementation:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py -q
```

Expected coverage:

- unconfigured provider returns `call_status=not_configured`.
- unsupported provider returns a public blocked/failure category.
- safe mock provider path can return public success without network access.
- live smoke response contains only public/redacted fields.
- injected secret-like env values do not appear in serialized responses.
- `/manifest` remains additive-compatible.
- OpenAPI exposes the provider smoke path if API implementation is chosen.

## Checker / Redaction Tests

If checker support is implemented, run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
```

Expected coverage:

- provider live summary with redacted public fields passes.
- provider live summary containing forbidden markers fails.
- provider-live-smoke scenario is not treated as basic full-lifecycle PASS.

## Regression Tests

Run before implementation closeout when code changed:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

## Optional Live Provider Smoke

Run only when provider environment is configured and this package review has
authorized bounded live calls:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
WORLDENGINE_LLM_PROVIDER=deepseek .venv/bin/python -m pytest app/tests/test_provider_live_smoke_live.py -q
```

or the equivalent documented API probe:

```bash
curl -i -X POST http://127.0.0.1:8000/provider/live-smoke
```

If the environment is not configured, record `not_configured` or `blocked`.
Do not mark provider live PASS.

## Commands Not Run And Why

Do not run E2E, Agent smoke, autonomous full lifecycle validation, Validation
Client flows, generated-result rewrites, or LLM-backed world creation tests
for this package unless a later reviewed update expands scope. They do not
prove this provider boundary and can overclaim v0.9 readiness.

## Pass Criteria

Implementation closeout may pass only when:

- documentation/contract evaluator reports no P0/P1/blocking P2.
- focused backend tests pass.
- `/manifest` compatibility is preserved.
- public provider summary redaction tests pass.
- optional live smoke is either passed with current-session evidence or
  honestly classified as not configured/blocked.
- review evidence records exact commands, exit status, compatibility review,
  scope review, unresolved findings, and final handoff.
