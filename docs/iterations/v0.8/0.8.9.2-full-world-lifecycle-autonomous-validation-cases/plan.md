# Plan

Chinese mirror: `plan.zh.md`.

## Files

Create:

- `docs/iterations/v0.8/0.8.9.2-full-world-lifecycle-autonomous-validation-cases/*`
- `docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md`
- `tools/testing/fixtures/agent-autonomous/valid-worldengine-full-lifecycle/`

Modify:

- `docs/testing/agent-autonomous/README.md`
- `docs/testing/agent-autonomous/scorecard.md`
- `docs/testing/agent-autonomous/result-schema.json`
- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `Makefile`

Do not touch:

- `backend/app/`
- `backend/worldengine/`
- `frontend/`
- Validation Client repository.

## Steps

1. Draft the package documents and scenario contract.
2. Add failing checker tests for the full lifecycle scenario.
3. Extend the checker only enough to validate lifecycle artifacts.
4. Add a generic positive fixture for the new scenario.
5. Update autonomous testing docs and schema.
6. Run focused tests and fixture validation.
7. Update `review.md` with actual evidence.

## Verification

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
make validate-agent-autonomous-fixtures
git diff --check
```
