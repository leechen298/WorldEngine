# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Checks

```bash
git diff --check
python3 -c "from pathlib import Path; pkg=Path('docs/iterations/v0.9/0.9.12-llm-backed-full-lifecycle-validation-execution'); required={'README.md','README.zh.md','intent.md','intent.zh.md','contract.md','contract.zh.md','technical-design.md','technical-design.zh.md','test-plan.md','test-plan.zh.md','plan.md','plan.zh.md','review.md','review.zh.md'}; missing=sorted(name for name in required if not (pkg/name).exists()); print({'files': len(list(pkg.glob('*.md'))), 'missing': missing}); raise SystemExit(1 if missing else 0)"
rg -n 'implementation_authorized[:：] yes|provider_live_call_authorized[:：] yes|evidence_execution_authorized[:：] yes|external_validation_authorized[:：] yes|Status[:：].*execution authorized|Status[:：].*implementation complete' docs/iterations/v0.9/0.9.12-llm-backed-full-lifecycle-validation-execution docs/iterations/v0.9/README.md docs/iterations/v0.9/README.zh.md docs/iterations/v0.9/CURRENT_STATE.md docs/iterations/v0.9/CURRENT_STATE.zh.md
```

## Execution Checks After Review

After documentation review explicitly authorizes evidence execution:

- run preflight and budget checks.
- run the staged LLM-backed lifecycle suite or classify the blocker.
- run `make validate-agent-autonomous-fixtures` to confirm fixture regression.
- run `make validate-agent-autonomous-result RESULT_DIR=<result-dir>` for the
  generated result directory.
- run or request second-Agent read-only review.
- write durable result summaries in English and Chinese.

## Not Run During Documentation Draft

No provider call, evidence execution, external validation, runtime smoke,
Validation Client execution, generated-result creation, or code test is run
during documentation drafting.

## Acceptance Criteria

- Documentation review passes with no P0/P1/blocking P2.
- If execution is later authorized, output is PASS or honestly classified as
  FAIL/BLOCKED/NOT_RUN with durable evidence.
- No secrets or private evidence are written.
