# Plan

## Steps

1. Read governing project, scope, roadmap, iteration, v0.3 plan, external
   fixture boundary, validation report template, loader contract, and bridge
   contract docs.
2. Create the external fixture runner public contract.
3. Create the 0.3.5 package docs with English and Chinese mirrors.
4. Mark 0.3.5 `ready for review` in the package README, v0.3 milestone index,
   and v0.3 detailed plan.
5. Run documentation verification checks.
6. Record commands, results, compatibility review, scope review, assumptions,
   and open risks in `review.md`.

## Acceptance Criteria

- 0.3.5 package docs are complete.
- `docs/contracts/external-fixture-runner-contract.md` exists.
- Public consumption surfaces are limited to APIs, CLI contracts, schemas,
  exported contracts, and redacted reports.
- Redacted report requirements are testable against
  `docs/validation-report-template.md`.
- Concrete external-world details are forbidden.
- The package and v0.3 index statuses are `ready for review`.
- Documentation verification passes.
- Implementation tests are not claimed.

## Not Planned

- Runtime implementation.
- Schema implementation.
- API implementation.
- Frontend implementation.
- Fixture implementation.
- Migration implementation.
- Test implementation.
- External repository creation.
- Product validation app implementation.

## Review Gate

This package is ready for documentation review after the checks in
`test-plan.md` pass. It must not become `ready for implementation` because
there is no implementation in this package.
