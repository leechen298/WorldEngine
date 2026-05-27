# Contract

## Public Concepts

- External fixture runners are external consumers of WorldEngine.
- Public contract surfaces are documented API routes, CLI contracts, schemas,
  contract docs, exported templates, and redacted review evidence.
- Redacted validation reports are evidence records that describe public
  behavior without leaking external consumer internals.

## Required Contract Behavior

This package must:

- add `docs/contracts/external-fixture-runner-contract.md`.
- define the external runner as a consumer, not core code.
- identify allowed public consumption surfaces.
- require redacted validation reports to follow
  `docs/validation-report-template.md`.
- list forbidden leaked details.
- use abstract identifiers only.
- keep all examples domain-neutral.
- keep v0.3 scope aligned with loader and runtime bridge evidence.

## Allowed Changes

- Add the external fixture runner contract.
- Create the 0.3.5 package documentation.
- Update v0.3 package status in the English and Chinese milestone indexes and
  detailed plans.
- Add documentation-only examples using abstract identifiers.
- Record documentation-stage verification in `review.md`.

## Forbidden Changes

- Do not modify runtime, schema, API, event, archive, params, frontend,
  fixture, migration, or test implementation files.
- Do not create external repositories.
- Do not add concrete fixture data.
- Do not add concrete external world names, characters, locations, resources,
  story rules, map data, seed data, or private transcripts.
- Do not add UI selectors, hidden reset APIs, or private oracle behavior.
- Do not implement a product validation app.
- Do not narrow loader or bridge APIs around one external consumer.
- Do not mark runtime, build, test, E2E, UI smoke, or Agent smoke behavior as
  passed without current-session evidence.

## Compatibility

This is a documentation-only package. It must preserve existing behavior for:

- runtime.
- schemas.
- public APIs.
- events.
- archive.
- params.
- frontend-facing behavior.
- fixtures.
- migrations.
- tests.
- legacy `backend/worldengine/`.

Any future implementation prompted by this contract must go through a separate
reviewed package and must describe the need as a generic engine capability.

## Assumptions

- The 0.3.2 loader and 0.3.4 bridge reviews provide enough public contract
  context for external fixture readiness.
- `docs/validation-report-template.md` remains the source template for
  redacted report fields.
- Future external fixture runners can adapt to abstract suite, target, and
  scenario identifiers.

## Open Risks

- P3: Future external runners may need public CLI or API details that are not
  yet documented. That gap should be recorded as a generic contract gap, not
  filled with private fixture details.
- P3: Redaction may hide evidence needed for debugging. Follow-up packages may
  need a more structured redacted evidence schema.
- P3: Status terms in older v0.3 docs are mixed between English and Chinese;
  this package updates only the 0.3.5 status entries it owns.

## North Star Alignment

The package supports the north star by keeping WorldEngine generic while
allowing external validation consumers to exercise public engine behavior.
It does not turn the core repository into an application backend or fixture
repository.
