# Plan

Status: review complete

## Steps

1. Create this post-closeout repair package and keep implementation
   authorization closed until review.
2. Run or record a documentation/contract evaluator checkpoint.
3. If no P0/P1/blocking P2 remains, update review evidence to
   `implementation_authorized: yes`.
4. Add failing regression tests for fallback digest seed preservation.
5. Add public preview API coverage for sensitive imported-plan provenance
   failure.
6. Patch fallback digest payloads to preserve canonical seed material.
7. Run focused backend tests and then broader backend/frontend/E2E/checker
   verification from `test-plan.md`.
8. Update the reliability result, parent review, implementation summaries, and
   package review with exact evidence.
9. Keep final verdict partial pass unless the scope guard is zero and all P1/P2
   blockers are resolved or explicitly accepted by review.

## Stop Conditions

- documentation/contract evaluator reports a P0/P1 or blocking P2.
- scope guard cannot be made `out_of_scope=0` without widening beyond the
  package contract.
- backend/API P2s cannot be fixed inside the allowed file set.
- verification fails and no root-cause repair is available inside this package.
