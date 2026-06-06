# Intent

## Problem / Purpose

The v0.9 parent package defines a version-level LLM-backed lifecycle
foundation, but planned `0.9.x` sections are not executable child contracts.
`0.9.0` creates the first concrete child package and records the current v0.8
handoff state so later agents cannot skip from parent roadmap text directly
into provider, runtime, checker, fixture, or Validation Client work.

The key drift risk is overclaiming: v0.8 proved the basic lifecycle through
the official checker, while LLM-backed lifecycle validation is still blocked
by missing provider live smoke, LLM-backed world creation, rule-linked
evolution, event legality, persistent Agent autonomy and consolidation
evidence, and checker/schema support. This package preserves that split.

## Why Now

The user started `/goal` development for v0.9 and explicitly authorized
subagents. The v0.9 `CURRENT_STATE.md` route requires creating or confirming a
concrete `0.9.0` child package before implementation or evidence execution.

Without this package, later work could treat `v0.9-plan.md` as direct
implementation authorization, run live provider calls before redaction rules
are reviewed, or mark planned LLM-backed testing assets as pass-capable
evidence.

## Relationship To Roadmap

v0.9 moves WorldEngine from the proved basic lifecycle toward the first
LLM-backed lifecycle foundation. This package is the documentation baseline
that hands off to `0.9.1-provider-live-smoke-and-redaction-boundary`, where
provider live smoke and provider evidence redaction must be defined before
LLM-backed world generation can start.

## Non-Goals

- Do not implement provider configuration or provider smoke.
- Do not run live provider calls.
- Do not implement LLM-backed world creation.
- Do not implement rule/parameter schemas.
- Do not implement runtime run controls.
- Do not implement user direction, event legality, Agent continuity,
  consolidation, narrative projection, diagnostic dialogue, checker support,
  fixtures, scorecards, or Validation Client handoff behavior.
- Do not modify runtime, API, schema, frontend, backend tests, checker,
  fixture, migration, generated result, external repository, Validation
  Client, provider configuration, or `backend/worldengine/` files.
- Do not claim v0.9 runtime/API/frontend/E2E/Agent/autonomous/product,
  provider, LLM-backed, external validation, or generation-quality PASS.

## Expected Handoff

`0.9.1-provider-live-smoke-and-redaction-boundary` receives:

- parent v0.9 route/status synchronized to the next child selection.
- v0.8 basic full-lifecycle PASS as handoff context only.
- LLM-backed lifecycle blocker taxonomy preserved as current v0.9 starting
  state.
- explicit provider live-call and redaction stop rules.
- implementation and evidence execution still closed until the `0.9.1`
  package documents are created, reviewed, and authorized.
