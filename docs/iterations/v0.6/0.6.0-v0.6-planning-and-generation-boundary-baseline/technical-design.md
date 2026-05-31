# Technical Design

Status: planned / ready for review

## Documentation Structure

`0.6.0` creates a v0.6 campaign root and a first child package:

```text
docs/iterations/v0.6/
├── README.md
├── README.zh.md
├── v0.6-plan.md
├── v0.6-plan.zh.md
├── GOAL_RUNNER.md
├── GOAL_RUNNER.zh.md
├── CURRENT_STATE.md
├── CURRENT_STATE.zh.md
├── CAMPAIGN_PLAN.md
├── CAMPAIGN_PLAN.zh.md
├── review.md
├── review.zh.md
└── 0.6.0-v0.6-planning-and-generation-boundary-baseline/
    ├── README.md
    ├── README.zh.md
    ├── intent.md
    ├── intent.zh.md
    ├── contract.md
    ├── contract.zh.md
    ├── technical-design.md
    ├── technical-design.zh.md
    ├── test-plan.md
    ├── test-plan.zh.md
    ├── plan.md
    ├── plan.zh.md
    ├── review.md
    └── review.zh.md
```

## Affected Files

Allowed affected files are limited to `docs/iterations/v0.6/**`.

No backend, frontend, API, migration, fixture, generated result, external
repository, or `backend/worldengine/` files are affected by this package.

## Generation Boundary Model

The parent plan splits v0.6 into reviewable child packages:

1. boundary and campaign planning.
2. contract and template semantics.
3. deterministic template generator core.
4. structured generation plan compiler.
5. AI-assisted plan import boundary.
6. validation, metadata, and preview API.
7. regeneration and runtime-readiness integration.
8. dashboard preview and E2E smoke.
9. evidence audit.
10. release candidate.
11. final closeout.

This package records the sequence only. It does not implement any generator.

## Compatibility Strategy

The campaign identifies compatibility-sensitive surfaces before code:

- `WorldSpec`, `WorldCell`, and `EntityRef`.
- `load_worldspec` and loader errors.
- `RuntimeContext` and runtime-context summaries.
- `RuntimeEngine` tick/time behavior and context storage.
- v0.4 Agent Loop contracts.
- v0.5 memory context surfaces.
- existing API envelope and error shape.

Later children must prove compatibility through current-session commands
before claiming pass.

## Anti-Drift Rules

- The active child package is the only implementation scope.
- Documentation-only packages must not change implementation files.
- Generated examples must stay generic and must not embed concrete demo-world
  content.
- AI-assisted generation means structured plan import unless a later reviewed
  child explicitly authorizes live provider behavior.
- Historical v0.5 evidence is handoff context only.
- Review status must not advance beyond available evidence.

## Risks

- Risk: v0.6 planning accidentally becomes product-specific world authoring.
  Mitigation: explicit forbidden changes and scope guardrails.
- Risk: AI-assisted generation is interpreted as live provider integration.
  Mitigation: provider-independent structured plan boundary.
- Risk: generated `WorldSpec` output breaks loader/runtime-context behavior.
  Mitigation: later child packages must run focused loader and runtime-context
  tests.
- Risk: missing evaluator evidence is mistaken for review completion.
  Mitigation: status remains `planned / ready for review` and
  `implementation_authorized: no`.
