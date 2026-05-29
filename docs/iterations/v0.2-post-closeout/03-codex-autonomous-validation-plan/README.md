# Codex Autonomous Validation Plan

Status: package complete / plan accepted current campaign
Type: autonomous validation planning

## Goal

Define how an independent Codex reviewer validates v0.2 post-closeout claims
without relying on implementer summaries.

## Current Campaign Note

This planning package became the active child after current-campaign
`02-e2e-validation-execution` evidence passed. The current `/goal` run has
reviewed and accepted this plan for handoff to
`04-codex-autonomous-validation-execution`.

## Naming Rule

Use `Codex autonomous validation`, not Agent autonomous testing. This avoids
confusion with WorldEngine Agent-in-World concepts.

## Scope

The independent reviewer must read release docs, evidence docs, code, schemas,
and tests. The reviewer must run available validation commands or record a
blocker. The reviewer must not modify code.

## Deliverables

- `intent.md`
- `intent.zh.md`
- `contract.md`
- `contract.zh.md`
- `test-plan.md`
- `test-plan.zh.md`
- `plan.md`
- `plan.zh.md`
- `review.md`
- `review.zh.md`

## Final Assessment State

Plan accepted in the current campaign. No autonomous validation has been
executed in this package; `04-codex-autonomous-validation-execution` owns that
execution.
