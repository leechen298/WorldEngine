# Technical Design

## Current State

The v0.2 milestone index and plan list 0.2.9 as the evidence and boundary
audit package. Earlier packages already created or updated:

- authoritative direction and boundary docs.
- EntityRef, WorldCell, WorldSpec, EventRef, and Event.refs contracts.
- focused schema and event compatibility tests.
- package reviews with command and test evidence.
- `docs/iterations/v0.2/findings.md`, currently containing a deferred 0.2.7
  status synchronization finding.

The active implementation map still describes v0.1 runtime behavior. v0.2
schema and event contracts are additive foundations and are not loaded into
runtime behavior.

## Contract Alignment and Invariants

- Treat completed package reviews as evidence, not as implementation targets.
- Treat active direction, scope, and boundary docs as source-of-truth
  boundary inputs.
- Distinguish historical artifact evidence from active direction.
- Keep all examples and findings domain-neutral.
- Do not edit code, tests, schemas, fixtures, migrations, API routes, or
  frontend files.

## Proposed Implementation

After documentation review approval:

1. Read completed v0.2 package reviews, contract docs, boundary docs,
   implementation maps, and the findings register.
2. Create `evidence-index.md` / `.zh.md` with a table of active claims,
   evidence source, verification source, status, and notes.
3. Create `boundary-audit.md` / `.zh.md` with boundary checks, repository path
   checks, anchor sweep summary, status drift review, and unresolved findings.
4. Resolve the deferred 0.2.7 status mismatch if it is confirmed to be a
   documentation status drift; otherwise keep it open with updated rationale.
5. Update `findings.md` for new, closed, or retargeted audit findings.
6. Run the documentation checks in `test-plan.md`.
7. Update this package's review files with exact commands, results,
   compatibility review, scope review, and unresolved findings.

## Affected Surfaces

Documentation:

- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/evidence-index.zh.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/boundary-audit.zh.md`
- `docs/iterations/v0.2/findings.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/**`
- v0.2 milestone index and plan status fields.

No runtime, schema, API, frontend, fixture, migration, or test implementation
surface is affected.

## Data Model / Schema Changes

None.

## Runtime / Service Design

None.

## Compatibility

Runtime behavior, schema validation, event behavior, API response shapes,
frontend behavior, fixture behavior, migration behavior, and legacy
`backend/worldengine/` behavior remain unchanged.

The audit may identify missing evidence or status drift, but it must not
change implementation behavior to close those gaps.

## Assumptions

- Package review files contain the most authoritative command and test
  evidence for completed v0.2 work.
- Documentation-only audit outputs are acceptable as 0.2.9 implementation
  deliverables after this documentation gate is reviewed.
- Link/path checks can be performed with shell commands available in the
  repository environment.
- Backend/frontend tests are unnecessary unless implementation files change,
  which this package forbids.

## Risks

- Risk: audit language overstates current runtime behavior. Mitigation: every
  implemented/tested claim must cite review evidence or be marked as planned.
- Risk: anchor sweep finds historical concrete-fixture text in old review
  evidence. Mitigation: classify historical artifacts separately from active
  direction.
- Risk: status drift spans English and Chinese mirrors. Mitigation: status
  checks must include both mirrors.
- Risk: missing evidence tempts code changes. Mitigation: record findings and
  hand off to later packages instead.
