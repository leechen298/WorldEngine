# Intent

## Problem

v0.1 has working backend, frontend, API, validation, archive, and test pieces,
but the implementation details were scattered across code, tests, closeout
notes, and commit history.

## Goal

Add a compact but complete implementation documentation set:

- current implementation overview.
- backend implementation map.
- frontend implementation map.
- v0.1 API reference.
- v0.1 test map.

## Non-goals

- Do not change runtime behavior.
- Do not change API contracts.
- Do not add new tests.
- Do not design v0.2 schemas.
- Do not document planned recursive WorldCell behavior as existing behavior.

## Why Now

The project is about to enter v0.2 planning. v0.1 needs a stable implementation
map first so future changes can preserve the scaffold while replacing or
extending the right seams.

## North Star Alignment

This package separates the current scaffold implementation from the long-term
recursive world engine. It makes clear which pieces are real in v0.1 and which
remain future work.
