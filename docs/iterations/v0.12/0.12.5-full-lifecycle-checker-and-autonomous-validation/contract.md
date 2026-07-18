# Contract

Chinese mirror: `contract.zh.md`.

## Classification Boundary

This package may classify the full lifecycle from current-session evidence:

- `PASS`: current exported v0.12 evidence directory passes checker/scorecard and
  read-only evaluator review with no blocking P1/P2.
- `PARTIAL`: deterministic checker/fixture evidence passes, but required fresh
  external export or review evidence is incomplete.
- `BLOCKED`: external client capability, result directory, provider/environment,
  permissions, or checker assets are missing.
- `FAIL`: current evidence exists and checker/scorecard/review finds a blocking
  product or contract issue.

Historical saved results may prove checker behavior, but they must not be used
as current v0.12 PASS evidence.

## Allowed Changes

- Package docs and result evidence docs.
- Running existing checker commands:
  - `make validate-agent-autonomous-fixtures`
  - `make validate-agent-autonomous-result RESULT_DIR=<current-or-fixture-dir>`
- Reading existing `test-results/agent-autonomous/**` as historical context.
- Recording checker outputs, scorecard summary, read-only evaluator review, and
  blocker classification.

## Forbidden Changes

- No product code changes to force PASS.
- No Validation Client implementation in this repository.
- No provider live-call without explicit authorization.
- No external validation agent represented as an in-world Agent.
- No UI smoke as full lifecycle PASS.
- No historical result reused as current v0.12 PASS.
- No hidden evaluator data or raw/private evidence.
- No final MVP closeout; `0.12.6` owns closeout.

## Required Evidence

- exact checker command and exit status.
- result directory or fixture directory.
- scorecard/verdict source.
- skipped or unverified items.
- redaction status.
- read-only evaluator review status.
- final package classification with rationale.

## Exit Criteria

- Documentation evaluator records no P1/P2 findings.
- Evidence execution authorization is recorded before checker commands run.
- Checker commands run or blockers are explicitly recorded.
- Read-only evaluator review records no blocking P1/P2 or the package records
  PARTIAL/BLOCKED/FAIL.
- Parent route advances to `0.12.6-mvp-release-candidate-and-closeout`.
