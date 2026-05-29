# Contract

## Public Concepts

- Evidence commit: the commit whose behavior was validated.
- Final documentation commit: the commit containing completed validation
  documentation, if separate from the evidence commit.
- Backend deterministic result: deterministic backend test outcome for the
  selected command set.
- API smoke result: lightweight API verification through TestClient or curl.
- E2E result: browser E2E outcome or a recorded not-configured / blocked
  state.

## Allowed Changes

During future execution, this package may:

- Run validation commands.
- Inspect docs, source code, route files, package scripts, and E2E config.
- Update `e2e-validation-report.md`.
- Update `review.md`.
- Record P1/P2/P3 findings and blockers.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend tests, fixtures,
  migrations, or external repositories.
- Do not add E2E tests or fixtures.
- Do not repair implementation.
- Do not change v0.3 release status.
- Do not include concrete demo-world details, UI selectors, seed data, or
  private oracle details.
- Do not report unrun checks as successful.

## Compatibility Requirements

Execution must specifically check or record blockers for:

- WorldSpec loader behavior.
- runtime context bridge behavior.
- inert `RuntimeEngine` context compatibility.
- Event.refs response compatibility.
- existing API response shapes.
- release-claim consistency with v0.3 docs.

## Out-Of-Scope Follow-Ups

Any repair or implementation change belongs to a separate reviewed package.
Codex autonomous review execution belongs to `04`.
