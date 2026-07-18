# Technical Design

Chinese mirror: `technical-design.zh.md`.

This is a documentation-only package. It has no runtime architecture changes.

## Documentation Architecture

- `README.md` records scope, v0.11 handoff facts, caveats, and next route.
- `intent.md` explains why Agent continuity work must start from rule-bound
  world evidence.
- `contract.md` defines allowed/forbidden changes and compatibility
  constraints.
- `test-plan.md` defines documentation checks and commands not run.
- `plan.md` defines the execution order for this handoff package.
- `review.md` records documentation-stage evidence, evaluator review, and
  parent route synchronization.

## Handoff Model

The package treats v0.11 evidence as input only:

```text
v0.11 rule-bound world PASS
-> 0.12.0 handoff docs
-> 0.12.1 Agent public state/runtime loop docs
```

The package must not infer Agent autonomy from v0.11 event/diff evidence.
Agent behavior starts only in a later reviewed package.

## Parent Route Update

After documentation evaluator review passes, parent v0.12 docs may update:

- active child package: none after this docs-only package closes.
- current route:
  `0.12.1-agent-public-state-and-runtime-loop-documentation-package-needed`.
- implementation authorization: no.
- evidence execution authorization: no.
