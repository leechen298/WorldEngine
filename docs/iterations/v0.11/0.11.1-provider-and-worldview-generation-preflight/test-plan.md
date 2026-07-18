# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Checks

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.1-provider-and-worldview-generation-preflight')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
```

Expected: no whitespace errors, no missing or empty package docs.

## Focused Backend Tests

After implementation:

```bash
python3 -m pytest app/tests/test_provider_worldview_preflight_api.py app/tests/test_llm_worldview_generation_api.py app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py
```

Expected:

- not configured provider is classified without crashing.
- deterministic fallback remains labeled non-LLM and non-provider-backed.
- configured provider without live-call authorization remains blocked.
- mock provider remains safe mock / non-live.
- private markers are rejected or redacted without echo.
- manifest exposes the preflight surface.

## Recording Rules

- Do not claim live provider PASS.
- Do not claim external Validation Client PASS.
- Do not claim tests passed unless run in the current session.
