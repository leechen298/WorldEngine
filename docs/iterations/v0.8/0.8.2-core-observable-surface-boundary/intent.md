# Intent

## Problem / Purpose

`0.8.1` defines the minimum working-state taxonomy, but later packages still
need a precise boundary for what a validator or projection consumer may
observe from the core repository. Without that boundary, v0.8 could drift into
private validator behavior, product-specific backend logic, or overbroad
memory/runtime exposure.

This package defines the observable public surface families before any
implementation or smoke evidence package starts.

## Why Now

The `/goal` route selected `0.8.2` after `0.8.1` review. The next
implementation-bearing package, `0.8.3`, must know which public core surfaces
it may harden and which exposures remain forbidden.

## Relationship To Roadmap

v0.8 prepares core-side readiness for an external validator. This package
turns the v0.8 and v0.7 projection/readiness contracts into a concrete
observable boundary for future work, without implementing those surfaces.

## Non-Goals

- Do not implement schemas, checkers, APIs, UI, tests, evidence artifacts, or
  runtime changes.
- Do not run core-side smoke evidence.
- Do not define external validator connection flows or private scenarios.
- Do not claim observable surface readiness or minimum working-state evidence.

## Expected Handoff

`0.8.3-generation-runtime-agent-loop-readiness` receives:

- allowed observable surface families.
- forbidden exposure rules.
- implementation authorization criteria.
- compatibility and redaction expectations.
