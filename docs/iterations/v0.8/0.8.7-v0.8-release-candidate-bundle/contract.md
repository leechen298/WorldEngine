# Contract

## Public Concepts

- `ReleaseCandidateBundle`: the documentation artifact that collects reviewed
  v0.8 package evidence before final closeout.
- `BoundedClaim`: a claim supported by named evidence and limited to that
  evidence boundary.
- `Exclusion`: a surface intentionally not claimed by the release-candidate
  bundle.
- `HandoffDecision`: one of `ready_for_final_closeout_review`, `blocked`, or
  `defer_pending_review`.

## Allowed Changes

Documentation stage:

- Create or update this package's docs and Chinese mirrors.
- Create `release-candidate-summary.md` and
  `release-candidate-summary.zh.md`.
- Record evidence references, bounded claims, exclusions, unresolved findings,
  and review gates.
- Update parent v0.8 status surfaces to ready-for-review for this package.

Review stage after evaluator approval:

- Update this package `review.md` and mirrors with evaluator findings.
- Update package status only if review passes.
- Update parent route only if package review authorizes handoff.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  external validator, external application, deployment, or `backend/worldengine/`
  files.
- Do not run new product validation or external validation in this package.
- Do not create final release claims.
- Do not claim external validation PASS, external consumer PASS, product
  readiness, frontend/E2E PASS, Agent smoke PASS, autonomous PASS,
  generation-quality PASS, or final v0.8 readiness.
- Do not convert historical v0.7 evidence into current v0.8 PASS evidence.
- Do not include private external validator details, private repository paths,
  UI selectors, oracle internals, raw prompts, provider traces, secrets, or
  concrete validation-world details.

## Required Bundle Surfaces

The release-candidate summary must include:

- package status matrix for `0.8.0` through `0.8.6`.
- evidence reference table.
- bounded claim table.
- compatibility table.
- exclusion list.
- unresolved finding table.
- handoff decision for `0.8.8-v0.8-final-closeout`.

## Closeout Rule

This package may recommend handoff to `0.8.8-v0.8-final-closeout` only if
documentation/contract review finds no P1 or blocking P2 and the
release-candidate summary does not imply final release or unsupported readiness
claims.
