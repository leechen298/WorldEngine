# Technical Design

## Documentation Structure

This documentation-only package creates the standard package file set under:

```text
docs/iterations/v0.10/0.10.0-mvp-debug-session-planning-and-v0.9-handoff/
```

The package includes English and Chinese mirrors for `README`, `intent`,
`contract`, `technical-design`, `test-plan`, `plan`, and `review` because it
changes routing, evidence, and process semantics.

## Affected Files

Allowed package-local files:

- `README.md`
- `README.zh.md`
- `intent.md`
- `intent.zh.md`
- `contract.md`
- `contract.zh.md`
- `technical-design.md`
- `technical-design.zh.md`
- `test-plan.md`
- `test-plan.zh.md`
- `plan.md`
- `plan.zh.md`
- `review.md`
- `review.zh.md`

Allowed parent status files:

- `docs/iterations/v0.10/README.md`
- `docs/iterations/v0.10/README.zh.md`
- `docs/iterations/v0.10/v0.10-plan.md`
- `docs/iterations/v0.10/v0.10-plan.zh.md`
- `docs/iterations/v0.10/GOAL_RUNNER.md`
- `docs/iterations/v0.10/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.10/CURRENT_STATE.md`
- `docs/iterations/v0.10/CURRENT_STATE.zh.md`
- `docs/iterations/v0.10/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.10/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.10/review.md`
- `docs/iterations/v0.10/review.zh.md`

## Data / Control Flow

This package changes only the documented goal route:

```text
v0.10-parent-documentation-ready-for-review
-> 0.10.0 review complete
-> 0.10.1-mvp-public-manifest-and-debug-handoff-documentation-package-needed
```

No runtime data flow, API control flow, frontend state flow, checker flow, or
external Validation Client flow changes.

## Compatibility Strategy

- Keep parent planned-package specs intact as future route-map inputs.
- Mark only `0.10.0` as review complete.
- Mark `0.10.1` as documentation-package-needed, not implementation-ready.
- Keep all authorization fields closed.
- Preserve v0.9 as BLOCKED rather than rewriting earlier evidence.

## Anti-Drift Rules

- Do not use this package to sneak in code, tests, fixtures, checker assets,
  generated results, provider configuration, or Validation Client behavior.
- Do not describe future `0.10.1` implementation as already reviewed.
- Do not let the external client become the owner of provider calls, world
  generation, runtime mutation, or evaluator authority.
- Do not use parent/source-world wording for replay or worldline branches.
- Do not claim any current-session runtime behavior beyond documentation
  checks actually run in this package.
