# Intent

Chinese mirror: `intent.zh.md`.

## Problem

The first formal `worldengine-full-lifecycle-autonomous` run covered world
creation, runtime progression, Agent action evidence, and director guidance,
but failed evidence integrity. The saved-result checker rejected the result
because `world-lifecycle-summary.json` reported:

```text
evidence_integrity.redaction_scan_passed: false
```

The failure analysis points to public director guidance output that describes
what was not mutated by naming private/internal markers such as private Agent
memory, goals, relationship internals, `self_state`, and hidden context.

## Why Now

`0.8.9.1` made the WorldEngine public handoff contract available. The next
full lifecycle validation now reaches the director guidance surface and fails
only at public evidence redaction. Fixing this narrow public wording problem is
the next required WorldEngine-side repair before the full lifecycle checker can
be rerun honestly.

## Relationship To Roadmap

This package supports the v0.8 goal of preparing public core-side surfaces for
external validation without moving external validation logic, external app code,
or concrete validation content into this repository.

## Non-Goals

- Do not implement Validation Client behavior.
- Do not relax the autonomous checker to hide a real public-evidence leak.
- Do not remove the director guidance surface.
- Do not mutate Agent private memory, goals, identity, relationships,
  self-state, or private validation internals.
- Do not add concrete demo-world fixtures, seed data, characters, maps,
  locations, resources, or story rules.
- Do not claim full lifecycle autonomous validation PASS without a current
  checker PASS.

## Expected Handoff

After review approval, implementation should update the public response and
focused tests, then rerun the documented verification. If the full lifecycle
run cannot be rerun in the current environment, review must record that blocker
and may only claim the narrower focused repair evidence.
