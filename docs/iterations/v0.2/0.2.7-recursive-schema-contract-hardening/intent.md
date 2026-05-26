# Intent

## Problem

v0.2 introduced the recursive schema foundation with EntityRef, WorldCell, and
WorldSpec, plus generic schema smoke tests. Before v0.3 starts loader or
runtime bridge work, those schema contracts need clearer documentation and
focused validation evidence.

The current code already validates basic nested cells, entity references,
schema version, invalid empty identifiers, serialization, and reconstruction.
The remaining risk is that future agents could infer loader behavior,
runtime-side semantics, or domain-specific examples from sparse schema
documentation instead of an explicit contract.

## Goal

Define the documentation and implementation plan for hardening EntityRef,
WorldCell, and WorldSpec as generic, additive, recursive schema contracts with
testable acceptance criteria.

The successful implementation state is:

- contract docs exist for EntityRef, WorldCell, and WorldSpec.
- schema tests prove recursive nesting, invalid generic values, and model
  dump / validate round trips.
- runtime loading remains unimplemented.
- examples and test payloads remain domain-neutral.

## Non-goals

- Do not implement a WorldSpec loader.
- Do not connect WorldSpec to RuntimeEngine.
- Do not change runtime behavior.
- Do not change API response shapes.
- Do not modify frontend behavior.
- Do not add concrete external-world fixtures, seed data, roles, locations,
  resources, story rules, or product UI.
- Do not implement generation, projection, memory, agent loop, or
  self-continuity behavior.
- Do not create external repositories.

## Why Now

0.2.5 removed concrete external-world anchors and restored generic schema
smoke coverage. 0.2.6 reset the remaining v0.2 plan. 0.2.7 is the next
foundation step because v0.3 loader work needs stable schema semantics and
evidence before it can safely consume WorldSpec data.

## North Star Alignment

This package supports recursive world structures by clarifying the generic
schema language for worlds, child worlds, and referenced entities. It keeps
WorldEngine aligned with the north star by strengthening reusable engine
contracts without narrowing the repository into a demo-specific backend or
implementing future runtime surfaces early.
