# Technical Design

## Audit Artifact

`audit-report.md` is the primary output. It should include:

- reviewed child package table.
- evidence traceability table.
- compatibility assessment.
- scope assessment.
- unresolved findings.
- handoff recommendation.

## Traceability Checks

Use file-existence checks for required reviews and evidence:

- parent `review.md`.
- child `review.md` files for `0.7.0` through `0.7.5`.
- `0.7.5` `evidence-matrix.md`.

Use status consistency searches to confirm the parent points to the next
child after closeout.

Use changed-file scope guard to confirm the active diff is limited to v0.7
docs, v0.7 public contracts, and approved checker/test files.

## Compatibility Rules

- Audit records evidence; it does not alter behavior.
- Checker/schema PASS is not runtime/API/frontend PASS.
- Saved-result checker PASS is not live Agent or full autonomous PASS.
- Release-candidate recommendation is not final release.

## Output Rule

Any blocker must be recorded in both `audit-report.md` and `review.md`.
