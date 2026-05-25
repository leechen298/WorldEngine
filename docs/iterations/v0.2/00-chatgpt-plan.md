# v0.2 Automatic Iteration Seed Plan

## Purpose

This document seeds the v0.2 automatic iteration workflow. It lets ChatGPT,
Codex A, and Codex B continue v0.2 one package at a time without turning the
core repository into application-specific backend code.

## Current v0.2 State

v0.2 is planned / in progress. Packages 0.2.1 through 0.2.5 are complete or
historical as recorded in the v0.2 index. 0.2.6 resets the remaining package
sequence and prepares the workflow for 0.2.7 through 0.2.12.

## WorldEngine North Star

WorldEngine is a recursive world generation and runtime engine. It supports
world generation, runtime, recursive world structures, agents living in
worlds, memory, feedback-shaped behavior, and pseudo-self formation over time.

v0.2 only establishes foundation pieces. It does not implement future runtime,
agent, memory, generation, projection, or application surfaces.

## v0.2 Boundary

v0.2 can do:

- documentation governance.
- EntityRef / WorldCell / WorldSpec schema foundation.
- EventRef / Event.refs additive event contract.
- generic schema smoke validation.
- external fixture / validation boundary.
- redacted validation report template.
- legacy boundary.
- automation workflow for iterative development.
- evidence / compatibility / release-candidate documentation.

v0.2 cannot do:

- WorldSpec loader.
- RuntimeEngine migration to WorldCell.
- runtime bridge.
- Agent-in-World loop.
- memory / self-continuity substrate.
- world generation.
- projection API.
- external fixture repository.
- external validation repository.
- product UI.
- application-specific backend.
- concrete demo world fixture.
- concrete external-world seed data.

## Completed Packages So Far

- `0.2.1-project-north-star`: documentation governance and north star.
- `0.2.2-recursive-world-contract`: recursive schema foundation.
- `0.2.3-event-contract-extension`: additive event reference structure.
- `0.2.4-worldspec-reference-fixture`: historical concrete fixture artifact
  superseded by 0.2.5.
- `0.2.5-core-boundary-cleanup-and-roadmap-reset`: boundary cleanup, generic
  schema smoke validation, and roadmap reset.

## Planned Remaining Packages

- `0.2.6-iteration-workflow-and-plan-reset`: workflow, plan reset, and
  historical abstraction.
- `0.2.7-recursive-schema-contract-hardening`: schema contract hardening.
- `0.2.8-event-reference-contract-hardening`: event reference contract
  hardening.
- `0.2.9-generic-schema-evidence-and-boundary-audit`: evidence and boundary
  audit.
- `0.2.10-legacy-boundary-and-compatibility-review`: legacy compatibility
  review.
- `0.2.11-v0.2-release-candidate-bundle`: release-candidate bundle.
- `0.2.12-v0.2-final-closeout`: final closeout after review approval.

The execution-grade details for 0.2.7 through 0.2.12 live in
`docs/iterations/v0.2/v0.2-plan.md` and `v0.2-plan.zh.md`.

## Codex A Role

Codex A prepares or reviews package documents. It ensures intent, contract,
technical design, test plan, execution plan, and review evidence match the
current package boundary.

Codex A must not implement code while preparing documentation-stage packages.

## Codex B Role

Codex B implements only after the package is reviewed and approved. It follows
the approved contract, technical design, test plan, and plan. It records
evidence in `review.md`.

Codex B must stop if implementation reveals a design gap that changes the
approved contract.

## Approval Gate

Human / ChatGPT review approves package documents before implementation.
Documentation-only packages may close after documentation checks and review
evidence. Code or mixed packages require an approved package before code work.

## Implementation Gate

Implementation starts only after approval. It must stay inside the package
contract and the v0.2 boundary.

## Test Gate

Run only the tests specified by the package test plan. Do not claim tests,
builds, E2E, UI smoke, runtime behavior, or backend behavior passed unless the
command or flow ran in the current session.

## Diff Review Gate

Codex A reviews Codex B's diff for scope, compatibility, evidence, and
forbidden changes. Findings use P1/P2/P3 severity.

## Fix Loop

Default maximum fix loop count is `N = 3`.

Each loop:

1. Run required tests.
2. Review diff and evidence.
3. Fix P1/P2 issues inside scope.
4. Record results.

If P1/P2 findings remain after `N = 3`, stop and escalate to human / ChatGPT
review.

## Final ChatGPT Review

0.2.11 generates a release-candidate bundle. 0.2.12 final closeout may run
only after human / ChatGPT review approves the release-candidate bundle.
