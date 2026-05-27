# Intent

## Problem

v0.3 has a release-candidate bundle, but final release status must not be
declared until review approval, blocker classification, and closeout evidence
are recorded in a separate package. Without a narrow final-closeout contract,
status updates could drift into feature cleanup, unreviewed evidence claims, or
premature v0.4 handoff wording.

## Goal

Create the documentation package that defines how v0.3 may be closed after the
0.3.7 release-candidate review. The package should make final-closeout
acceptance testable, list allowed status updates, and keep implementation,
runtime, schema, API, frontend, fixture, migration, and test files out of
scope.

## Non-goals

- Do not declare v0.3 final during the documentation stage.
- Do not rerun or patch runtime, API, frontend, schema, fixture, migration, or
  test implementation behavior.
- Do not implement v0.4 Agent-in-World behavior.
- Do not add memory, self-continuity, generation, projection, product UI, game
  UI, concrete demo worlds, external validation worlds, or external
  repositories.
- Do not convert open P3 handoff items into completed work.

## Why Now

0.3.8 is the planned final package in the v0.3 milestone sequence. It exists
after the release-candidate bundle so reviewers have a separate, reviewable
gate for deciding whether v0.3 can move from planned / not released to final
closeout.

## North Star Alignment

This package protects WorldEngine's recursive-world direction by closing the
loader and runtime bridge milestone through evidence, compatibility review, and
scope boundaries. It does not narrow the engine into application-specific
logic, concrete fixture worlds, NPC chat, or product UI.
