# Plan

## Files

- Create:
  - `docs/iterations/v0.3/evidence-index.md`
  - `docs/iterations/v0.3/evidence-index.zh.md`
  - `docs/iterations/v0.3/compatibility-audit.md`
  - `docs/iterations/v0.3/compatibility-audit.zh.md`
  - `docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/**`
- Modify:
  - `docs/iterations/v0.3/README.md`
  - `docs/iterations/v0.3/README.zh.md`
  - `docs/iterations/v0.3/v0.3-plan.md`
  - `docs/iterations/v0.3/v0.3-plan.zh.md`
- Do not touch:
  - `backend/`
  - `frontend/`
  - schema implementation files
  - fixtures
  - migrations
  - test implementation files
  - legacy `backend/worldengine/`

## Steps

1. Read repository governance, v0.3 milestone docs, templates, and prior v0.3
   package reviews.
2. Draft evidence index from completed package review evidence.
3. Draft compatibility audit with explicit classifications, assumptions,
   risks, and P1/P2/P3 findings.
4. Create full 0.3.6 package docs and Chinese mirrors.
5. Update milestone status for 0.3.6 to `ready for review`.
6. Run documentation verification commands and record results in `review.md`.

## Verification

Use the commands in `test-plan.md`. This package does not run implementation
tests unless implementation files are unexpectedly modified, which would be a
scope violation.
