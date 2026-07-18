# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Gate

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## Focused Backend Verification

After implementation authorization, run:

```bash
cd backend
python3 -m pytest app/tests/test_session_narrative_diagnostic_inspection_api.py app/tests/test_external_narrative_diagnostic_boundary.py app/tests/test_session_agent_runtime_loop_api.py app/tests/test_session_agent_memory_consolidation_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

Expected coverage:

- session narrative projection accepts public session/tick-range evidence.
- session narrative projection can filter by branch ID and Agent ID.
- diagnostic inspection answers from public evidence and records out-of-world
  classification.
- projection/diagnostic calls do not append events, write direction queue,
  mutate canonical state, or write Agent memory.
- private markers and unsupported mutation flags are rejected without public
  payload echo.
- rejected requests expose public diagnostic codes for missing evidence,
  invalid range, or invalid refs.
- provenance fields identify session, tick range, branch, Agent focus, and
  public refs.
- existing world-level projection, session Agent runtime, Agent memory, and
  manifest tests continue to pass.

## Commands Not Run Unless Later Authorized

- Provider live calls: not authorized.
- External Validation Client automation: not authorized.
- Frontend/E2E: not in this package.
- Full autonomous validation/checker: belongs to later packages.
