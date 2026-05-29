# Contract

Status: planned / ready for review

## Public Concepts

- E2E validation: browser E2E when the repository has a runnable framework.
- Integration validation: backend deterministic tests and route-level checks.
- API smoke validation: public endpoint checks using TestClient or curl.
- Release claim validation: comparison of v0.2 release docs against observed
  behavior and reviewed evidence.
- Concrete demo-world regression check: verification that validation does not
  reintroduce concrete demo-world details into core docs or code.

## Allowed Changes

- Add validation planning docs under this directory.
- Define future execution checks and fallback rules.
- Define report evidence requirements.

## Forbidden Changes

- Do not run backend, frontend, E2E, API smoke, runtime, schema execution,
  fixture, migration, or autonomous validation commands in this package.
- Do not change implementation files.
- Do not change v0.2 release status.
- Do not hardcode an observed branch name.
- Do not add concrete demo-world details.

## Compatibility Requirements

The plan must preserve existing v0.2 closeout wording. It may describe the
need for fresh validation evidence, but it must not imply v0.2 is incomplete
or reopened.

## Out-of-Scope Follow-Ups

- Executing E2E / integration / API smoke validation.
- Repairing failures found by execution.
- Adding missing E2E framework support.
- Updating runtime, API, schema, or frontend behavior.
