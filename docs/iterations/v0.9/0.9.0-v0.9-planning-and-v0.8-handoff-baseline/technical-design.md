# Technical Design

## Documentation Structure

This package creates a documentation-only child package:

```text
docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline/
  README.md
  README.zh.md
  intent.md
  intent.zh.md
  contract.md
  contract.zh.md
  technical-design.md
  technical-design.zh.md
  test-plan.md
  test-plan.zh.md
  plan.md
  plan.zh.md
  review.md
  review.zh.md
```

The child package records the first v0.9 route transition. Parent v0.9
surfaces may be synchronized so the next route points to
`0.9.1-provider-live-smoke-and-redaction-boundary-documentation-package-needed`.

## Affected Files

Allowed files:

- `docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline/**`
- `docs/iterations/v0.9/README.md`
- `docs/iterations/v0.9/README.zh.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/v0.9-plan.zh.md`
- `docs/iterations/v0.9/GOAL_RUNNER.md`
- `docs/iterations/v0.9/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/CURRENT_STATE.zh.md`
- `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.9/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.9/review.md`
- `docs/iterations/v0.9/review.zh.md`

Forbidden files include all runtime, schema, API, frontend, backend test,
checker, fixture, migration, generated result, external repository,
Validation Client, provider configuration, and `backend/worldengine/`
implementation files.

## Route State Flow

Before this package:

```text
Active child package: none
Current route: 0.9.0-v0.9-planning-and-v0.8-handoff-baseline-documentation-package-needed
Implementation authorization: no
Evidence execution authorization: no
Provider live-call authorization: no
```

After this package:

```text
Active child package: 0.9.1-provider-live-smoke-and-redaction-boundary selected / documentation package needed
Current route: 0.9.1-provider-live-smoke-and-redaction-boundary-documentation-package-needed
Implementation authorization: no
Evidence execution authorization: no
Provider live-call authorization: no
```

The route transition does not create `0.9.1` package documents and does not
authorize provider work. It only selects the next documentation package target.

## Compatibility Strategy

- Keep all changes documentation-only.
- Keep v0.8 basic lifecycle PASS as handoff context, not as v0.9 PASS.
- Keep LLM-backed lifecycle validation `BLOCKED` until a future package
  records current-session checker or scorecard evidence.
- Keep provider live-call authorization closed until `0.9.1` package review
  explicitly opens it.
- Preserve English and Chinese status semantics.

## Anti-Drift Rules

- Planned package specs in `v0.9-plan.md` remain route-map inputs only.
- The next child package must create its own complete document set before
  implementation.
- Do not turn LLM-backed testing documentation into PASS evidence.
- Do not reinterpret external diagnostic dialogue as in-world dialogue or
  Agent memory.
- Do not reinterpret narrative projection as canonical world mutation.
- Do not weaken provider redaction rules for convenience.
- Do not add concrete world content to the core repository.
