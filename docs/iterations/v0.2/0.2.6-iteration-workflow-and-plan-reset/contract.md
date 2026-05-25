# Contract

## Public Concepts

- Iteration workflow and plan reset: the v0.2 package sequence from 0.2.6
  through 0.2.12 is explicitly planned before final release work.
- Quasi-package specification: each planned package from 0.2.7 through 0.2.12
  is documented with enough detail for a later agent to generate full package
  docs without inventing scope.
- Automatic iteration workflow: a ChatGPT / Codex A / Codex B process with
  approval, implementation, test, review, and fix gates.
- Final-review-bundle template: the review artifact expected before holistic
  human / ChatGPT review.
- Historical abstraction: historical concrete fixture details are abstracted
  while preserving the fact that superseded concrete fixture work happened.

## Compatibility Constraints

- Existing runtime behavior must stay unchanged.
- Existing API response shapes must stay unchanged.
- Existing schema behavior must stay unchanged.
- Existing frontend behavior must stay unchanged.
- Existing tests and fixtures must stay unchanged.
- v0.2 remains planned / in progress after this package.

## Allowed Changes

- Update `docs/iterations/v0.2/README.md` and `README.zh.md`.
- Update `docs/iterations/v0.2/v0.2-plan.md` and `v0.2-plan.zh.md`.
- Update `docs/roadmap.md` and `docs/roadmap.zh.md` only for v0.2 and
  0.2.6 through 0.2.12 planning.
- Update `docs/releases/v0.2.md` and `docs/releases/v0.2.zh.md` as draft /
  planned / not released documents.
- Add this package directory and English / Chinese mirror documents.
- Add `docs/iterations/v0.2/00-chatgpt-plan.md` and
  `docs/iterations/v0.2/00-chatgpt-plan.zh.md`.
- Add `docs/iterations/v0.2/development-workflow.md` and
  `docs/iterations/v0.2/development-workflow.zh.md`.
- Add `docs/iterations/v0.2/final-review-bundle-template.md` and
  `docs/iterations/v0.2/final-review-bundle-template.zh.md`.
- Abstract historical concrete demo details inside `docs/iterations/v0.2/**`
  and v0.2 release docs.

## Forbidden Changes

- Do not modify runtime code.
- Do not modify schema code.
- Do not modify API code.
- Do not modify frontend code.
- Do not modify backend tests.
- Do not modify fixtures.
- Do not create 0.2.7 through 0.2.12 package directories.
- Do not create external repositories.
- Do not implement loader, runtime bridge, agent loop, memory,
  self-continuity, generation, projection API, product UI, or application-specific backend
  behavior.
- Do not write concrete demo names, fixture filenames, locations, roles,
  resources, buildings, plot anchors, or a concrete grep term list into
  tracked docs.
- Do not mark v0.2 as final release.

## Detailed Plan Acceptance Gate

Before final output, verify that `docs/iterations/v0.2/v0.2-plan.md` and
`docs/iterations/v0.2/v0.2-plan.zh.md` contain full quasi-package
specifications for every package from 0.2.7 through 0.2.12.

If any package is missing one of these fields, record it as a P2 finding and
do not claim the plan is ready:

- Package name
- Status
- Type
- Goal
- Why this exists
- Inputs / required reading
- Allowed changes
- Forbidden changes
- Expected deliverables
- Expected tests / verification
- Compatibility constraints
- Scope guardrails
- Exit criteria
- Handoff to next package

`README.md` and `README.zh.md` may stay summary-level only, but
`v0.2-plan.md` and `v0.2-plan.zh.md` must be detailed enough for a later
Codex planning pass to generate the next package without inventing scope.

## North Star Check

This package does not narrow WorldEngine into a demo-specific backend. It
removes ambiguity that could make future automation treat historical concrete
fixture direction as active scope.

## Out-of-Scope Follow-ups

- 0.2.7: recursive schema contract hardening.
- 0.2.8: event reference contract hardening.
- 0.2.9: evidence and boundary audit.
- 0.2.10: legacy compatibility review.
- 0.2.11: release candidate bundle.
- 0.2.12: final closeout after approval.
