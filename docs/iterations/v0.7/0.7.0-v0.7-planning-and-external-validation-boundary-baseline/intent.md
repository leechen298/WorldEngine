# Intent

## Problem

The v0.7 parent docs define a full `/goal` campaign, but the parent roadmap
intentionally treats `0.7.x` entries as planned package specs only. To keep the
goal moving without bypassing iteration gates, the first planned child must be
created as a concrete, reviewable package before any later public contract or
implementation work starts.

## Goal

Create and review the `0.7.0` documentation-only baseline package. The
successful end state is a reviewed child package that confirms v0.7 campaign
controls, v0.6 handoff boundaries, external-validation boundaries, projection
consumer boundaries, verification expectations, and the handoff to `0.7.1`.

## Why Now

`完成 v0.7` must begin with deterministic route selection. Parent review has
confirmed the v0.7 campaign docs are internally consistent, but the campaign
cannot proceed to later children until the first child package exists and its
own review gate is satisfied.

## Relationship To Roadmap

v0.7 exists to prepare WorldEngine for external validation readiness and
projection consumer readiness through public contracts, redacted reports,
readiness manifests, and compatibility evidence. This child provides the
documentation baseline for that sequence without implementing the later
contract, checker, manifest, projection, or regression work.

## Non-goals

- Do not implement `0.7.1` public readiness contracts.
- Do not implement `0.7.2` report schema or redaction checker support.
- Do not implement `0.7.3` readiness manifest or contract bundle support.
- Do not implement `0.7.4` projection consumer read models.
- Do not run or claim v0.7 product validation, external suite pass, Agent
  smoke, autonomous, E2E, frontend, API, runtime, or release readiness.
- Do not modify runtime, schema, API, frontend, tests, checkers, fixtures,
  migrations, external repositories, generated results, or legacy
  `backend/worldengine/` code.

## Expected Handoff

After review, `0.7.0` hands off to
`0.7.1-public-validation-and-projection-contracts`. The handoff is
documentation-only and says that `0.7.1` may define public validation and
projection contract semantics, but must still create or confirm its own
complete package docs and pass review before any later implementation is
authorized.

## North Star Alignment

This package protects WorldEngine as a generic recursive world generation and
runtime engine by keeping external validation worlds and projection
applications as consumers. It prepares public readiness boundaries without
turning the core repository into a product-specific validation app or
projection application.
