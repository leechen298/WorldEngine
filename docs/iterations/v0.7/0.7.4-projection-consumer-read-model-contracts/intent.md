# Intent

## Problem / Purpose

v0.7 now exposes public readiness manifest discovery, but projection consumers
still need generic read-model contracts that define what future read-only
payloads may contain. Without those contracts, later work could leak private
consumer details, create product-specific surfaces, or imply v0.8 projection
application readiness too early.

## Why Now

`0.7.3` completed public contract discovery semantics. The next boundary is
the read-only projection model language that `0.7.5` compatibility evidence
and v0.8 application work can reference.

## Relationship To Roadmap

This package implements the v0.7 roadmap step for projection consumer
read-model contracts. It is schema/contract oriented. It does not build a
projection application, UI, product backend, or write-enabled API.

## Non-Goals

- Do not build a projection app or dashboard.
- Do not add API routes unless a reviewed update explicitly expands scope.
- Do not add write APIs, reset APIs, persistence, migrations, private runner
  hooks, or consumer-specific backend logic.
- Do not expose concrete external validation worlds, private app state, UI
  selectors, raw memory records, provider secrets, prompts, traces,
  transcripts, or event payloads.
- Do not claim projection app readiness, product readiness, v0.8 readiness, or
  external consumer PASS.

## Expected Handoff

After closeout, `0.7.5-quality-regression-and-compatibility-evidence`
receives reviewed projection read-model contract/schema/checker evidence and
can run compatibility checks against the public surfaces that v0.7 has
created.
