# Technical Design

## Current State

v0.3 has completed package reviews through 0.3.5. Loader and bridge
implementation evidence lives in package review files, while the milestone
index still lists 0.3.6 as planned.

## Contract Alignment and Invariants

This package changes documentation only. It aggregates evidence from existing
reviews and keeps every implementation surface read-only.

The audit must preserve these invariants:

- No runtime, schema, API, frontend, fixture, migration, or test implementation
  files are modified.
- Evidence claims cite commands already recorded in package reviews or commands
  run in this documentation session.
- Missing or indirect evidence is recorded as a finding or risk.
- v0.4 handoff readiness is planning readiness, not implementation permission.

## Proposed Documentation Structure

- `evidence-index.md`: package-by-package evidence matrix and compatibility
  surface index.
- `compatibility-audit.md`: acceptance question results, compatibility
  classifications, findings, assumptions, and release-candidate verification
  requirements.
- 0.3.6 package docs: intent, contract, technical design, test plan, execution
  plan, and review evidence.
- Chinese mirrors for all new audit and package docs.

## Affected Surfaces

- Documentation: v0.3 iteration docs and package status indexes.
- Runtime: not touched.
- API: not touched.
- Schema: not touched.
- Frontend: not touched.
- Tests/fixtures/migrations: not touched.
- Legacy `backend/worldengine/`: not touched.

## Data Model / Schema Changes

None.

## Runtime / Service Design

None. The audit does not add service behavior.

## Compatibility

Compatibility is assessed from prior package evidence:

- 0.3.2 proves the data-only loader with focused backend tests.
- 0.3.4 proves optional inert runtime context with focused bridge and
  compatibility tests.
- 0.3.5 proves the external fixture consumer boundary by documentation
  contract.

## Risks

- Prior review evidence may omit a compatibility surface; the audit records
  that as missing or indirect evidence instead of assuming success.
- Broader frontend-facing behavior may need extra release-candidate smoke
  coverage.
- External runner reports may need stricter machine-readable shape later.
