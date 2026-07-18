# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Gate

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.2-agent-memory-and-rest-consolidation-mvp')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.2-agent-memory-and-rest-consolidation-mvp docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## Focused Backend Verification

After implementation authorization, run:

```bash
python3 -m pytest app/tests/test_session_agent_memory_consolidation_api.py app/tests/test_session_agent_runtime_loop_api.py app/tests/test_agent_memory_substrate.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

Expected coverage:

- memory summary read returns public working/episodic summaries.
- non-rest Agent step or consolidation records bounded public working memory.
- rest consolidation records public episodic summary and consolidation event.
- private marker payloads are rejected or absent from public evidence.
- repeated ordinary ticks do not mutate personality or skills.
- ordinary non-rest ticks do not create episodic, long-term, or consolidation
  records automatically.
- evidence refs identify memory/event/runtime sources.
- existing session Agent runtime loop and memory substrate tests continue to
  pass.
- manifest/public handoff exposes memory surfaces additively.

## Commands Not Run Unless Later Authorized

- Provider live calls: not authorized.
- External Validation Client automation: not authorized.
- Frontend/E2E: not in this package.
- Full autonomous validation/checker: belongs to later packages.
