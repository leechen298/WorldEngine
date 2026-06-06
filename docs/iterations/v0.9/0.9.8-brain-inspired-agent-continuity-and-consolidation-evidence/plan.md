# Plan

Chinese mirror: `plan.zh.md`.

Status: reviewed / ready for implementation

## Objective

Create and review the concrete `0.9.8` mixed implementation package before
any runtime, schema, API, test, checker, fixture, provider, frontend, or
Validation Client implementation starts.

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/iterations/AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/GOAL_RUNNER.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/contract.md`
- current active-backend Agent loop, memory, runtime, event, and public handoff
  surfaces as future implementation inputs.

## Documentation Type

Mixed implementation package documentation. Required files:

```text
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

## Files To Create Or Update

Create:

```text
docs/iterations/v0.9/0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence/*
```

After documentation review, update parent route/status docs only if the
review gate passes.

## Files Explicitly Out Of Scope During Documentation Stage

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- backend tests outside package documentation.
- checker fixtures and generated results.
- external repositories and Validation Client.

## Required Package Status Values

During drafting:

```text
Status: ready for documentation review
implementation_authorized: no
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no
```

After documentation evaluator PASS, status may move to
`reviewed / ready for implementation`, and implementation approval may be
recorded for this package only.

## Review Gates

1. Documentation checks pass.
2. Read-only subagent/evaluator reviews package docs and reports no P0/P1 and
   no blocking P2.
3. `review.md` records findings and authorization state.
4. Parent v0.9 route advances only after review evidence is recorded.

## Implementation Plan After Approval

Implementation, if later authorized, should proceed with TDD:

1. Add focused tests for continuity artifacts, consolidation artifacts,
   accepted autonomous action evidence, no-intent/rest states, event
   reactions, scripted-autonomy rejection, redaction, and compatibility.
2. Add schemas for continuity, consolidation, autonomous action, event
   reaction, diagnostics, and scripted-autonomy rejection evidence.
3. Add deterministic continuity/consolidation helper.
4. Add additive route or event integration only if required by the approved
   contract.
5. Run focused, related, backend, and diff checks.
6. Request implementation-scope subagent review before closeout.

## Stop Conditions

Stop and do not implement if:

- evaluator reports P0/P1 or blocking P2.
- implementation requires raw thought, chain-of-thought, private memory
  payloads, private goals, or hidden context.
- implementation requires provider-backed interpretation.
- implementation requires checker fixtures or external validation.
- implementation requires durable scheduling, generated-result creation, or
  persistent background processes.
- implementation needs narrative projection, diagnostic dialogue, frontend,
  Validation Client, or `backend/worldengine/` changes.
