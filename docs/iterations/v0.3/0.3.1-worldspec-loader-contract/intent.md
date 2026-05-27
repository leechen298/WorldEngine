# Intent

## Problem

v0.2 defined `WorldSpec` as a schema object, but it did not define how
WorldEngine should load `WorldSpec` data into the active code boundary. Without
a reviewed loader contract, the first implementation could accidentally
invent input forms, error semantics, fixture policy, or runtime authority while
coding.

## Goal

Create a reviewable loader contract that defines accepted inputs, successful
output, error categories, validation behavior, domain-neutral example policy,
and compatibility boundaries for a future minimal loader implementation.

## Non-goals

- Do not implement a loader.
- Do not connect loaded data to `RuntimeEngine`.
- Do not add API routes or response shapes.
- Do not add persistence, archive, params, event, or frontend behavior.
- Do not create concrete WorldSpec fixture data.
- Do not create external fixture or validation repositories.
- Do not implement world generation, Agent-in-World loop, memory,
  self-continuity, projection, story generation, or NPC chat behavior.

## Why Now

v0.3 exists to bridge generic `WorldSpec` data toward runtime context while
preserving v0.1 compatibility. The loader is the first boundary in that path,
so its contract must be explicit before `0.3.2` writes code.

## North Star Alignment

This package supports the north star by preparing a generic path for
structured world specifications to enter WorldEngine. It keeps the core
domain-neutral and prevents loader work from becoming demo-specific,
application-specific, or runtime-authoritative before the bridge contract is
reviewed.

## Assumptions

- `WorldSpec` remains the schema source for v0.3 loader validation until a
  reviewed package changes that.
- The initial loader can be useful without connecting to runtime.
- A file-backed JSON input may be allowed by the implementation package, but
  only as a generic source form.

## Open Risks

- Error path formatting may depend on the validation library unless the
  implementation normalizes it.
- File-backed loading could expand scope if it starts implying fixture
  directories or external repositories.
- Future bridge work may need additional metadata, but this package keeps
  loader metadata neutral and non-runtime-authoritative.
