# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Checks

```bash
git diff --check
python3 -c "from pathlib import Path; pkg=Path('docs/iterations/v0.9/0.9.13-v0.9-release-candidate-and-closeout'); required={'README.md','README.zh.md','intent.md','intent.zh.md','contract.md','contract.zh.md','technical-design.md','technical-design.zh.md','test-plan.md','test-plan.zh.md','plan.md','plan.zh.md','review.md','review.zh.md'}; missing=sorted(name for name in required if not (pkg/name).exists()); print({'files': len(list(pkg.glob('*.md'))), 'missing': missing}); raise SystemExit(1 if missing else 0)"
rg -n 'provider_live_call_authorized[:：] yes|evidence_execution_authorized[:：] yes|implementation_authorized[:：] yes|external_validation_authorized[:：] yes|product readiness|external validation PASS|LLM-backed full lifecycle PASS' docs/iterations/v0.9/0.9.13-v0.9-release-candidate-and-closeout docs/iterations/v0.9/README.md docs/iterations/v0.9/README.zh.md docs/iterations/v0.9/CURRENT_STATE.md docs/iterations/v0.9/CURRENT_STATE.zh.md
```

The final search may find forbidden phrases only inside explicit "does not
claim" boundary text. Any positive claim is blocking.

## Evidence Checks

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260606T142210+0800-llm-backed-full-lifecycle
```

## Not In Scope

- provider live call.
- full LLM-backed lifecycle rerun.
- Validation Client export.
- external validation.
- runtime, API, schema, checker, fixture, or frontend tests beyond evidence
  checks already recorded.
