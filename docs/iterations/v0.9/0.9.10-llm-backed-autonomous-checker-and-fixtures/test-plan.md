# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Unit Tests

Add or update `tools/testing/test_validate_agent_autonomous_result.py` with
focused tests for:

- supported LLM-backed scenario enum acceptance.
- LLM-backed `pass`, `fail`, `blocked`, and `not_run` status classification.
- provider live smoke PASS-critical artifact validation.
- world creation rejects deterministic generic fallback for PASS.
- rule parameter evolution rejects unexplained changes or fixed-counter-only
  PASS.
- event legality rejects direct final-state mutation for PASS.
- Agent persistent autonomy rejects single-event-only or client-scripted
  action PASS.
- full lifecycle requires every critical scorecard item to pass.
- full lifecycle requires `second-agent-review.md` with no blocking P1/P2.
- redaction leak fixtures fail for raw prompt, raw provider response, provider
  trace, private memory, raw thought, hidden context, and private evaluator
  markers.
- missing required artifact fixtures fail.
- existing dashboard and basic lifecycle fixtures still pass/fail as before.

## Regression Tests

- `make validate-agent-autonomous-fixtures`
- `backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q`
- `git diff --check`
- package completeness and status scans for this package and parent v0.9 docs.

## Commands

```bash
make validate-agent-autonomous-fixtures
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
git diff --check
python - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures')
required = {
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
}
missing = sorted(name for name in required if not (pkg / name).exists())
print({'files': len(list(pkg.glob('*.md'))), 'missing': missing})
raise SystemExit(1 if missing else 0)
PY
```

## Acceptance Criteria

- LLM-backed scenarios are checker-supported in schema, validator, fixtures,
  and docs.
- PASS is rejected when critical artifacts, scorecard items, redaction scan, or
  second-Agent review evidence is missing.
- BLOCKED and NOT_RUN can be represented honestly without becoming PASS.
- Existing autonomous saved-result checker behavior is preserved.
- No provider calls, runtime behavior changes, frontend changes, Validation
  Client changes, generated-result rewrites, or `backend/worldengine/` changes.

## Not Run During Documentation Stage

No implementation tests are run during documentation drafting. The commands
above become mandatory after implementation.
