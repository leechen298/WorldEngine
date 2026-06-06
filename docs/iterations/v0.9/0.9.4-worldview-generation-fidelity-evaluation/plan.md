# Plan

Chinese mirror: `plan.zh.md`.

## Ordered Execution Steps

1. Read parent v0.9 state, v0.9 plan, 0.9.2 output contract, 0.9.3
   rule/parameter contract, LLM-backed lifecycle validation plan, scorecard,
   artifact contract, and iteration rules.
2. Draft the concrete `0.9.4` package documents and Chinese mirrors.
3. Run documentation checks and required-term checks.
4. Request a read-only subagent documentation/contract evaluator.
5. Fix or record evaluator findings. Do not authorize implementation with any
   P0/P1 or blocking P2.
6. If review passes, update `review.md` by flipping
   `implementation_authorized` from `no` to `yes` while keeping:

```text
provider_live_call_authorized: no
generated_result_creation_authorized: no
external_validation_authorized: no
```

7. Implement only the reviewed `0.9.4` helper/schema/test scope.
8. Run focused tests, related regressions, backend regression, and documentation
   checks from `test-plan.md`.
9. Request implementation-scope/code-review subagent evaluation.
10. Fix blocking findings or stop.
11. Update package `review.md`, package README status, and parent v0.9 state
    only after implementation evidence is current and consistent.

## Phase Boundaries

Documentation phase ends only after subagent review records no P0/P1 and no
blocking P2.

Implementation phase starts only after `review.md` records implementation
authorization as enabled.

Closeout phase starts only after focused and regression verification commands
have current-session evidence.

## Stop Conditions

Stop if:

- implementation would start before review authorization.
- bounded runtime controls are needed to implement the immediate evaluator.
- fidelity PASS requires subjective judgement instead of deterministic public
  evidence.
- live provider calls or generated result creation appear necessary.
- any implementation file outside the contract must change.
- a subagent reports unresolved P0/P1 or blocking P2.
- tests fail in a way that cannot be fixed inside `0.9.4`.

## Review Update Step

`review.md` must record changed files, exact commands, command results,
compatibility review, scope review, subagent findings, unresolved findings, and
handoff to `0.9.5`.
