# Intent

## Problem / Purpose

v0.10 begins a narrower MVP delivery track after v0.9 closed as BLOCKED for
full LLM-backed lifecycle validation. Without a concrete first child package,
agents could either treat the v0.10 parent plan as implementation
authorization or keep waiting on v0.9 provider/client blockers.

This package turns the parent route into a concrete documentation baseline and
records the handoff boundary.

## Why Now

The v0.10 parent docs are drafted and ready for review. The current
`CURRENT_STATE.md` route says no active child exists and the next step is to
review the parent documentation, then create or approve `0.10.0`.

## Relationship To Roadmap

The roadmap defines v0.10 as "MVP Debug Contract And Runnable World Session".
This package does not build that session. It prepares the route so the next
package can define and implement the public manifest/debug handoff contract
before session work begins.

## Non-Goals

- No backend, frontend, schema, API, checker, fixture, migration, provider, or
  Validation Client implementation.
- No evidence execution or live provider call.
- No claim that v0.10 is runnable, validated, product-ready, or externally
  automated.
- No conversion of v0.9 BLOCKED evidence into a v0.10 PASS claim.
- No concrete demo-world content or application-specific backend behavior.

## Expected Handoff

After this package closes, v0.10 should route to
`0.10.1-mvp-public-manifest-and-debug-handoff-documentation-package-needed`.
Implementation remains closed until the `0.10.1` package document set is
created, reviewed, and records `implementation_authorized: yes`.
