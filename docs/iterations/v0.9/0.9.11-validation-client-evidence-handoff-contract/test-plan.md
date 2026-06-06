# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Checks

Run:

```bash
git diff --check
python3 -c "from pathlib import Path; pkg=Path('docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract'); required={'README.md','README.zh.md','intent.md','intent.zh.md','contract.md','contract.zh.md','technical-design.md','technical-design.zh.md','test-plan.md','test-plan.zh.md','plan.md','plan.zh.md','review.md','review.zh.md'}; missing=sorted(name for name in required if not (pkg/name).exists()); print({'files': len(list(pkg.glob('*.md'))), 'missing': missing}); raise SystemExit(1 if missing else 0)"
rg -n 'implementation_authorized[:：] yes|provider_live_call_authorized[:：] yes|evidence_execution_authorized[:：] yes|external_validation_authorized[:：] yes|Validation Client repository implementation|provider key handling in client|client-side evaluator authority' docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract docs/iterations/v0.9/README.md docs/iterations/v0.9/README.zh.md docs/iterations/v0.9/CURRENT_STATE.md docs/iterations/v0.9/CURRENT_STATE.zh.md
```

The authorization scan is expected to report only forbidden-scope prose, not
positive authorization.

## Review Checks

A read-only documentation evaluator must verify:

- package has all required files and mirrors.
- contract keeps client role to display/export only.
- provider ownership remains WorldEngine.
- PASS authority remains checker/second-Agent review.
- artifact names align with 0.9.10 checker and LLM-backed artifact contract.
- redaction and relative-path rules are explicit.
- parent route points to documentation review, not implementation.

## Not Run

No code tests, provider calls, checker fixture execution, frontend smoke,
Validation Client execution, generated-result creation, or external validation
are run for this documentation-only package.

## Acceptance Criteria

- Validation Client handoff contract is stable enough for a later client
  package to implement display/export behavior.
- No implementation authorization is granted.
- No client-owned LLM behavior, provider key handling, or evaluator authority
  is introduced.
