# Contract

## Public Concepts

- Evidence index: a documentation table mapping v0.3 package evidence to
  changed files, commands, compatibility surfaces, and findings.
- Compatibility audit: a documentation assessment that classifies runtime,
  API, event, archive, params, frontend-facing, schema, fixture, and legacy
  impacts.
- Handoff readiness: a reviewable statement about whether v0.3 evidence can
  inform v0.4 planning after release-candidate and closeout gates.

## Compatibility Constraints

- Runtime behavior must not change.
- API response shapes must not change.
- Schema behavior must not change.
- Frontend behavior must not change.
- Fixture, migration, and test implementation files must not change.
- Existing evidence must be cited from package reviews and must not be
  inflated into unrun test claims.

## Allowed Changes

- Add `docs/iterations/v0.3/evidence-index.md`.
- Add `docs/iterations/v0.3/evidence-index.zh.md`.
- Add `docs/iterations/v0.3/compatibility-audit.md`.
- Add `docs/iterations/v0.3/compatibility-audit.zh.md`.
- Create this 0.3.6 package documentation in English and Chinese.
- Update v0.3 milestone index and plan status for 0.3.6 to
  `ready for review`.

## Forbidden Changes

- Do not modify `backend/`, `frontend/`, schema implementation, fixtures,
  migrations, or test implementation files.
- Do not add new runtime features.
- Do not patch loader or bridge code from this package.
- Do not hide P1 or P2 findings.
- Do not declare v0.3 final release status.
- Do not mark this package `ready for implementation`.
- Do not add concrete demo world or external validation-world details.

## Acceptance Requirements

- The package README and v0.3 milestone index mark 0.3.6 as
  `ready for review`.
- Evidence index maps packages 0.3.0 through 0.3.5 to evidence sources,
  commands or results, compatibility coverage, and findings.
- Compatibility audit classifies runtime, API, event, archive, params,
  frontend-facing, schema, fixture, and legacy impacts.
- P1/P2/P3 findings, assumptions, and open risks are explicit.
- Test and verification requirements are phrased as runnable commands or
  checkable documentation assertions.
- English and Chinese mirrors remain synchronized.

## North Star Check

The audit reinforces a generic engine boundary. It does not introduce
application-specific world content, product UI, external fixture internals, or
agent self-continuity implementation.

## Out-of-Scope Follow-ups

- v0.3 release-candidate bundle.
- v0.3 final closeout.
- v0.4 Agent-in-World minimal loop planning and implementation.
- Machine-readable external report schema.
- Broader UI or E2E smoke coverage.
