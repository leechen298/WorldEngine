# Plan

Chinese mirror: `plan.zh.md`.

Status: reviewed / ready for implementation

## Documentation Stage

1. Read parent v0.9 state, `v0.9-plan.md`, 0.9.8 closeout, north-star,
   product model, scope boundaries, roadmap, and iteration rules.
2. Create full mixed-package document set for `0.9.9`.
3. Keep implementation authorization closed:
   `implementation_authorized: no`.
4. Run documentation checks from `test-plan.md`.
5. Request a documentation/contract/design/test-plan evaluator.
6. If there are no P0/P1/blocking P2 findings, update review evidence and
   record positive implementation authorization; otherwise repair docs and
   rerun review.

## Implementation Stage After Review Only

Implementation may start only after this package review records positive
implementation authorization.

Planned implementation order:

1. Add additive public schemas for narrative projection, diagnostic dialogue,
   boundary decisions, provenance, redaction status, and mutation flags.
2. Add deterministic helper that rejects private markers and default-canonical
   mutation attempts.
3. Add optional additive route/manifest exposure if implementation chooses
   API inspection.
4. Add focused tests from `test-plan.md`.
5. Run focused, related, and backend regression commands.
6. Request implementation-scope evaluator.
7. Update `review.md` and parent route/status docs after implementation
   closeout.

## Stop Conditions

Stop if implementation would require:

- live provider calls.
- generated-result creation.
- checker fixture or checker execution changes.
- external validation.
- frontend UI or Validation Client code.
- player-in-world chat.
- narrative game content.
- diagnostic-to-Agent-memory bridge.
- `backend/worldengine/` changes.
