# Technical Design

## Current State

v0.3 has completed or reviewed package evidence through 0.3.6:

- 0.3.1 documented the WorldSpec loader contract.
- 0.3.2 implemented the minimal generic loader with backend pytest evidence.
- 0.3.3 documented the runtime context bridge contract.
- 0.3.4 implemented the optional inert runtime context bridge with focused
  compatibility test evidence.
- 0.3.5 documented the external fixture runner readiness boundary.
- 0.3.6 created `evidence-index.md` and `compatibility-audit.md`.

The release-candidate package assembles those artifacts into reviewable docs.
It does not change implementation files.

## Contract Alignment and Invariants

- Every capability claim must cite an evidence source or be labeled as a
  limitation/finding.
- Existing runtime, schema, API, event, archive, params, frontend, fixture,
  migration, test, and legacy path behavior must remain untouched.
- P1/P2 findings cannot be hidden or downgraded by wording.
- v0.3 remains not final until 0.3.8 closeout after release-candidate review.

## Proposed Documentation Structure

- `v0.3-release-candidate-bundle.md`: human-readable candidate bundle with
  scope, package matrix, compatibility matrix, evidence map, findings,
  assumptions, risks, and closeout prerequisites.
- `final-review-bundle.md`: template-shaped review handoff with changed files,
  contract mapping, forbidden-change confirmation, commands, compatibility
  review, findings, and ChatGPT review request.
- Package docs: README, intent, contract, technical design, test plan, plan,
  and review in English and Chinese.

## Affected Surfaces

Documentation only:

- v0.3 iteration package docs.
- v0.3 milestone index and plan status fields.
- v0.3 release-candidate bundle docs.
- v0.3 final-review bundle docs.

No runtime, schema, API, frontend, fixture, migration, test, release, or
legacy implementation surface is affected.

## Data Model / Schema Changes

None.

## Runtime / Service Design

None. The package does not execute or modify runtime services.

## Compatibility

Compatibility is preserved by scope. The bundle records historical evidence
for loader, bridge, runtime, API, event, archive, params, schema, fixture,
frontend-facing, and legacy boundaries. Any command not run in this session
must remain historical evidence, not a fresh pass claim.

## Risks

- A release-candidate claim may overstate historical evidence. The evidence
  traceability check and review bundle mapping are required to detect this.
- Wording may imply final release. Release-status wording checks are required.
- A new P1/P2 finding may appear during assembly. It must be recorded and must
  block 0.3.8 unless resolved or explicitly accepted.
