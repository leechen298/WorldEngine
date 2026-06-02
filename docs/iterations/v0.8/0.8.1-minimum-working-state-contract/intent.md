# Intent

## Problem / Purpose

v0.8 cannot claim that WorldEngine works unless the claim has a precise,
reviewable meaning. Prior versions provide generation, runtime, Agent loop,
memory, and projection foundations, but they do not define the combined
minimum working-state claim.

This package defines the claim boundary before observable surface or runtime
readiness work starts.

## Why Now

`0.8.0` completed the planning and v0.7 handoff baseline. The next route needs
a minimum working-state contract so later packages know what evidence to
expose, prove, skip, block, or exclude.

## Relationship To Roadmap

v0.8 prepares core-side readiness for an external validation function. This
package defines what core-side readiness means without implementing the
external validator or external application.

## Non-Goals

- Do not implement code, schemas, checkers, tests, APIs, frontend routes, or
  evidence artifacts.
- Do not run runtime/API/frontend/E2E/Agent/autonomous/external validation.
- Do not claim the minimum working state has been proven.
- Do not define external validator connection workflows or private scenarios.

## Expected Handoff

`0.8.2-core-observable-surface-boundary` receives the required core slices,
claim taxonomy, evidence classes, exclusions, and stop conditions needed to
define observable public surfaces.
