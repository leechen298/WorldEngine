# Technical Design

## Audit Shape

The audit report uses five matrices:

1. Package status matrix: `0.8.0` through `0.8.5` status, review source,
   evaluator source, and closeout state.
2. Evidence reference matrix: command result, source file, proof boundary,
   and claim allowed.
3. Compatibility matrix: v0.3 through v0.7 compatibility surfaces and current
   v0.8 evidence relationship.
4. Boundary matrix: external validation, product readiness, frontend/E2E,
   Agent smoke, autonomous, generation-quality, and final readiness non-claims.
5. Findings matrix: P1/P2/P3, source, disposition, and handoff impact.

## Evidence Source Rules

- Current-session evidence may support only the exact proof boundary recorded
  in its package review.
- Historical v0.7 and v0.6 evidence is handoff context only.
- `0.8.5` v0.7 checker and contract commands are handoff compatibility, not
  external validation PASS.
- Skipped or out-of-scope checks are not PASS.

## Audit Report Generation

The audit stage fills `audit-report.md` and `audit-report.zh.md` from:

- parent route/status docs.
- child package reviews.
- testing result docs under `docs/testing/results/`.
- repository-local contract paths referenced by reviews.

The report must use explicit citations to file paths and avoid private
external app or validator details.

## Release-Candidate Recommendation

The recommendation is `recommended` only if:

- all required evidence references resolve.
- no P1 or blocking P2 remains.
- status surfaces are synchronized.
- no forbidden private detail or overclaim is accepted.
- skipped/out-of-scope checks are visible.

Otherwise it is `blocked` or `defer_pending_review`.
