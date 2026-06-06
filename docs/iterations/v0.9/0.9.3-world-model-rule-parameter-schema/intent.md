# Intent

Chinese mirror: `intent.zh.md`.

## Problem

Generated worlds cannot be validated as evolving systems if their parameters
and rules are only prose or loose outline dictionaries. `0.9.2` intentionally
stopped at a public generated model candidate and deferred full rule/parameter
schema to this package.

The current runtime parameter path also remains narrow: `/world/params` accepts
patches against a small registered parameter set such as `counter.increment`,
`heartbeat.enabled`, and `scene.weather`. That path must stay compatible while
v0.9 adds a generated-world rule/parameter contract for future lifecycle
validation.

## Goal

Create the reviewed contract, design, and test plan for an additive
implementation that can:

- represent generated world parameters with ids, value types, bounds,
  visibility, provenance, and public descriptions.
- represent world evolution rules with stable rule ids, trigger conditions,
  target parameter refs, allowed operations, effects, constraints, and public
  evidence fields.
- represent constraints and boundaries that validators can inspect without
  hidden provider traces.
- validate and summarize rule/parameter sets deterministically.
- preserve existing `/world/params` behavior.

## Non-goals

- Do not run or evaluate rules across ticks.
- Do not prove worldview fidelity.
- Do not implement event legality or rule-linked event generation.
- Do not execute live provider calls.
- Do not persist generated worlds or install generated rules into active
  runtime state.
- Do not add concrete game worlds, maps, characters, resources, locations, or
  story rules.
- Do not modify Validation Client or any external repository.
- Do not change `backend/worldengine/`.
- Do not implement bounded runtime controls, Agent continuity, narrative
  projection, diagnostic dialogue, checker fixtures, or full lifecycle
  validation.

## Why Now

`0.9.4` needs fidelity checks and later packages need bounded runs, world
direction, event legality, and rule-linked evolution evidence. Those packages
need a deterministic public rule/parameter schema before they can verify
generated behavior.

## North Star Alignment

This package strengthens WorldEngine as a generic world generation and runtime
engine. It creates public contracts for generated world parameters and rules
without narrowing the repository into a specific game, story, validation world,
or product client.
