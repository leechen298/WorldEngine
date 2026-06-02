# Intent

## Problem / Purpose

v0.7 needs trustworthy external-validation evidence rules before later
packages can archive redacted reports, bundle contracts, or claim core-side
compatibility readiness. The current report template is human-readable only
and still lists `pass / fail / blocked`, while the reviewed `0.7.1` readiness
contract requires `pass`, `fail`, `blocked`, `skipped`, and `out_of_scope`
as distinct states.

This package turns those reviewed semantics into a generic report schema and
checker without importing any external validation application or private
consumer detail into WorldEngine.

## Why Now

`0.7.1` completed the public readiness and projection consumer contracts. Its
P3 handoff explicitly requires `0.7.2` to align
`docs/validation-report-template.md` and any future schema/checker with the
new `skipped` and `out_of_scope` semantics.

Later `0.7.3` readiness-manifest work should consume machine-checkable report
semantics rather than relying on prose alone.

## Relationship To Roadmap

This package supports the v0.7 roadmap by preparing WorldEngine for external
validation suites and projection consumers through public contracts and
redacted evidence rules. It does not implement the external suites,
projection applications, runtime features, or product-specific behavior.

## Non-Goals

- Do not run or implement an external validation suite.
- Do not add private examples, fixture paths, UI selectors, hidden reset APIs,
  oracle internals, transcripts, event payloads, concrete worlds, characters,
  locations, story rules, or seed data.
- Do not change runtime, API, frontend, persistence, migrations, generation,
  Agent loop, memory, or event behavior.
- Do not claim product readiness, projection readiness, release readiness, or
  external suite PASS.

## Expected Handoff

After closeout, `0.7.3-contract-bundle-and-readiness-manifest` receives:

- a reviewed report schema path.
- a reviewed checker path.
- focused checker test evidence.
- updated template semantics.
- explicit scope and compatibility evidence proving this package did not
  change runtime/API/frontend behavior or import external consumer internals.
