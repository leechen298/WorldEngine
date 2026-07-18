# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Checks

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.2-structured-world-rules-and-parameters')
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

## Focused Backend Tests

After implementation:

```bash
python3 -m pytest app/tests/test_session_rule_parameters_api.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_params.py app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py
```

Expected:

- valid rule set attaches to a session and can be read back as public summary.
- invalid refs/types are rejected without replacing the last accepted summary.
- private markers are rejected without echo.
- existing `/world/params` behavior still passes.
- session create/run/status behavior still passes.
- manifest exposes session rule endpoints.

## Recording Rules

- Do not claim event generation, direction queue, fidelity, provider live, or
  external Validation Client PASS.
- Do not claim tests passed unless run in this session.
