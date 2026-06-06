# Plan

Chinese mirror: `plan.zh.md`.

Status: documentation reviewed / no implementation authorized

## Objective

Create a reviewable 0.9.11 documentation package that defines the Validation
Client evidence handoff contract after 0.9.10 checker/schema/fixture support.

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/contract.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.md`
- `docs/iterations/v0.9/0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence/technical-design.md`
- `docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/technical-design.md`

## Files

Create:

- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/README.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/README.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/intent.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/intent.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/contract.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/contract.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/technical-design.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/technical-design.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/test-plan.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/test-plan.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/plan.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/plan.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/review.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/review.zh.md`

Update:

- parent v0.9 route/status/review docs from documentation-package-needed to
  documentation-review-needed.

Do not touch:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- `tools/testing/**`
- generated result directories
- external repositories or Validation Client code

## Steps

1. Draft the complete 0.9.11 package document set.
2. Update parent route/status docs to documentation-review-needed.
3. Run documentation checks from `test-plan.md`.
4. Send the package to a read-only documentation evaluator.
5. If the evaluator reports no P0/P1/blocking P2, update review evidence and
   route toward the next package. If findings remain, repair docs before any
   further route advancement.

## Stop Conditions

- The handoff requires client-owned provider calls or provider keys.
- The handoff lets the client decide PASS.
- Required artifacts cannot stay redacted and public.
- Any implementation or runtime change becomes necessary.
- Documentation evaluator reports P0/P1/blocking P2.
