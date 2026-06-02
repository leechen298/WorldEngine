# Plan

## Stage 1: Documentation Gate

1. Create the full 0.8.3 package document set and Chinese mirrors.
2. Keep `implementation_authorized: no` and `evidence_execution_authorized: no`.
3. Run documentation shape, status, scope, and claim guards.
4. Send a read-only documentation/contract evaluator.
5. If evaluator reports no P0/P1 and no blocking P2, update `review.md` with
   evaluator evidence and decide whether implementation may be authorized.

## Stage 2: Implementation If Authorized

1. Read package docs in required order.
2. Add red tests for the core-readiness probe.
3. Add additive schemas in `backend/app/schemas/world_generation.py`.
4. Add isolated probe helper in `backend/app/core/world_generation.py`.
5. Add the read-only route in `backend/app/api/routes/world_generation.py`.
6. Run focused tests until red tests pass.
7. Run adjacent generation/runtime/Agent-loop compatibility tests.
8. Run scope, redaction, and claim guards.
9. Send implementation-scope or code-review evaluator before any broader
   readiness claim.

## Stop Conditions

- Stop before implementation if review does not explicitly record
  `implementation_authorized: yes`.
- Stop if the probe needs files outside the contract.
- Stop if app runtime, app event log, params, memory store, archive store, or
  external state is mutated.
- Stop if evidence would expose raw memory, prompt/provider traces, secrets,
  private transcript data, UI selectors, oracle internals, or external app
  data.
- Stop if implementation starts to define external validator connection,
  external app behavior, product UI, persistence, migrations, or live provider
  calls.

## Handoff

If implementation closes cleanly, hand off bounded core-readiness evidence to
`0.8.4-external-validation-handoff-contract`. If not implemented, hand off the
reviewed design and exact missing authorization/evidence.
