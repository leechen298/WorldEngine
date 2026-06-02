# Intent

## Problem / Purpose

The v0.8 parent package defines the version-level campaign, but the current
route cannot move directly from parent roadmap text into implementation or
evidence execution. `0.8.0` creates the concrete first child package and
records the current v0.7 handoff state before the campaign proceeds.

The immediate drift to correct is the parent v0.8 wording that treated
post-closeout v0.7 code-review blockers as still unresolved. The current v0.7
state records `0.7.9-v07-cr-checker-schema-repair` as review complete, with
`docs/testing/results/2026-06-02-v0.7-overall-validation.md` providing clean
pass evidence for the v0.7 checker/docs validation scope. That evidence clears
the V07-CR checker/docs blocker gate but does not prove v0.8 readiness.

## Why Now

The user started `/goal` development for v0.8. The campaign rules require
parent review and a concrete child package before any implementation-bearing
work. Without this package, later agents could treat planned `0.8.x` entries
as executable contracts or overclaim v0.7 historical evidence as v0.8 pass
evidence.

## Relationship To Roadmap

v0.8 prepares the core-side minimum working-state and external-validation
handoff boundary. This package is the documentation baseline that lets
`0.8.1-minimum-working-state-contract` define the actual readiness claim
taxonomy.

## Non-Goals

- Do not implement minimum working-state behavior.
- Do not implement observable public surfaces.
- Do not run or implement external validation.
- Do not add external application behavior.
- Do not repair runtime, API, frontend, schema, checker, fixture, migration,
  or generated result files.
- Do not claim v0.8 runtime/API/frontend/E2E/Agent/autonomous/product/external
  validation readiness.

## Expected Handoff

`0.8.1-minimum-working-state-contract` receives:

- parent v0.8 route/status synchronized to child selection.
- current v0.7 checker/docs repair status as handoff context only.
- explicit non-claims for v0.8 readiness and external validation PASS.
- implementation and evidence execution still closed.
