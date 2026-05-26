# Intent

## Problem

v0.2 has added recursive schema and additive event reference foundations while
preserving the v0.1 runtime scaffold. Before v0.3 begins loader or runtime
bridge design, the project needs a clear compatibility boundary that states
what is active, what is legacy, what is preserved, and what must not be
changed accidentally.

Without that boundary, future bridge work could blur additive schema contracts
with current runtime behavior, revive legacy code paths, or treat v0.2
documentation as evidence that runtime loading already exists.

## Desired Outcome

After review approval, this package will produce:

- a legacy boundary document for active, legacy, placeholder, and future paths.
- a v0.2 compatibility review that maps current runtime/API/frontend
  compatibility expectations to evidence and handoff constraints.
- findings for unresolved compatibility gaps or status drift.
- package review evidence showing the documentation work stayed within scope.

## Users

- Codex A preparing v0.2 release-candidate documentation.
- Codex B or future implementation agents preparing v0.3 bridge work.
- Human / ChatGPT reviewers checking whether v0.2 preserved v0.1 behavior.
- External consumers that need to know which contracts are active and which
  bridge behavior is future scope.

## Non-Goals

- Do not implement a WorldSpec loader.
- Do not migrate RuntimeEngine to WorldCell.
- Do not implement a runtime bridge.
- Do not modify runtime behavior.
- Do not change API response shapes.
- Do not modify frontend behavior.
- Do not refactor or revive `backend/worldengine/`.
- Do not add tests, fixtures, migrations, or concrete external-world anchors.

## Success Definition

The package is successful when the documentation package is ready for review,
and, after review approval, the implementation pass can create legacy boundary
and compatibility review docs that make v0.1/v0.2 compatibility explicit
without changing code.
