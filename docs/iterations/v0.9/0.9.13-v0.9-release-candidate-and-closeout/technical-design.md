# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Closeout Model

The closeout is documentation-only. It derives final status from recorded
evidence rather than executing new runtime behavior.

```text
0.9.1-0.9.10 implementation reviews
        +
0.9.11 handoff contract review
        +
0.9.12 checker-valid BLOCKED result
        ->
v0.9 closeout status: blocked
```

## Status Rules

- Parent `CURRENT_STATE.md` points to the completed 0.9.13 closeout state.
- Parent `README.md`, `GOAL_RUNNER.md`, `CAMPAIGN_PLAN.md`, `v0.9-plan.md`,
  and `review.md` use the same closeout wording.
- `provider_live_call_authorized`, `evidence_execution_authorized`, and
  `implementation_authorized` remain `no`.

## Compatibility Review Shape

This package does not change compatibility-affecting code. It references the
compatibility evidence already recorded by implementation-bearing child
reviews and keeps unresolved provider/runner gaps classified.
