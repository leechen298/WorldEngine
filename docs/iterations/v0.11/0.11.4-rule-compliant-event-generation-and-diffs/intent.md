# Intent

Chinese mirror: `intent.zh.md`.

Status: documentation drafted / review pending

## Problem / Purpose

v0.11 has public session rules and public direction guidance, but the world
still needs to change through an inspectable event/diff path. This package
connects the rule and direction inputs to a small, public, legality-gated
evolution step.

## Why Now

`0.11.2` made session rules attachable and `0.11.3` made user direction a
bounded queue. `0.11.4` is the first package allowed to turn those public
inputs into legal event candidates and applied public diffs.

## Relationship To Roadmap

This package advances the v0.11 rule-bound world evolution milestone. It still
does not close the full MVP, prove provider-backed generation quality, or
implement Agent autonomy. It prepares the public evolution evidence that
`0.11.5` will use for worldview fidelity validation.

## Non-Goals

- no full narrative simulation.
- no autonomous Agent loop or pseudo-self implementation.
- no provider calls.
- no Validation Client implementation or external validation execution.
- no frontend implementation.
- no persistence or migrations.
- no concrete demo-world fixtures.
- no `backend/worldengine/` changes.

## Expected Handoff

`0.11.5-worldview-fidelity-and-v0.11-validation` receives rule-linked accepted
and rejected event evidence, public state diffs, direction refs, replayable
event records, and session/runtime compatibility evidence.
