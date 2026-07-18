# Campaign Plan

Chinese mirror: `CAMPAIGN_PLAN.zh.md`.

Status: closeout complete / PARTIAL

## Objective

Run v0.12 as a review-gated `/goal` campaign that completes the MVP through
visible Agent continuity and checker-backed Validation Client automation.

The campaign objective is to make WorldEngine capable of:

- producing public Agent state and actions during runtime.
- preserving public memory summaries and consolidation evidence.
- exposing read-only novel-style narrative and diagnostic inspection surfaces.
- keeping narrative and diagnostic conversation outside the canonical world
  timeline and Agent memory.
- defining stable MVP evidence artifacts for the external client.
- running or classifying a full lifecycle autonomous validation result.
- closing the MVP as PASS, PARTIAL, BLOCKED, or FAIL with evidence.

## Authoritative Inputs Read For Parent Drafting

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-plan.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/README.md`
- `docs/iterations/v0.10/README.md`
- `docs/iterations/v0.11/README.md`
- `docs/iterations/v0.11/v0.11-plan.md`

## Campaign Rules

- v0.12 must start from v0.11 rule-bound world evidence.
- Planned `0.12.x` sections do not authorize implementation.
- Agent autonomy must originate from WorldEngine public runtime state, not
  client scripting.
- Documents and evidence must distinguish in-world Agents from external
  validation agents such as Codex or OpenClaw.
- Memory/consolidation evidence must be public summaries only.
- Narrative and diagnostic surfaces are read-only by default and must not
  steer future world evolution outside the direction queue.
- Complete MVP PASS requires checker, scorecard, and read-only review
  evidence.

## Campaign Exit Criteria

v0.12 can close the MVP only when:

- active child packages are review complete or explicitly deferred.
- Agent observe/intent/action-or-rest/memory evidence exists.
- public/private redaction boundaries pass.
- no external validation agent is recorded as an in-world Agent or player.
- Validation Client evidence handoff is implemented or honestly blocked.
- full lifecycle checker/scorecard/review classifies the result.
- no P1/P2 finding remains without accepted rationale.

## Handoff

If v0.12 closes as PASS, the project has a complete MVP baseline. If it closes
as PARTIAL or BLOCKED, the closeout must identify whether the next work belongs
to WorldEngine, WorldEngine-Validation-Client, provider/environment setup, or
testing/checker assets.
