# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Gate

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## Focused Backend Verification

After implementation authorization, run:

```bash
python3 -m pytest app/tests/test_session_agent_runtime_loop_api.py app/tests/test_agent_loop_service.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

Expected coverage:

- session Agent list/read returns public default Agent state.
- session Agent step records public observation and intent evidence.
- no client-submitted action payload is accepted as autonomy.
- event log contains public Agent evidence with `client_scripted_action: false`.
- redaction-sensitive strings are rejected or absent from public evidence.
- manifest/public handoff exposes session Agent endpoints additively.
- existing request-driven Agent loop tests continue to pass.

## Commands Not Run Unless Later Authorized

- Provider live calls: not authorized.
- External Validation Client automation: not authorized.
- Frontend/E2E: not in this package unless future review expands scope.
- Full Agent smoke/autonomous validation: belongs to later packages.
- Full MVP checker/scorecard: belongs to `0.12.5` and `0.12.6`.
