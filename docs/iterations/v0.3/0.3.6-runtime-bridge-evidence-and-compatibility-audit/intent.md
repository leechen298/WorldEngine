# Intent

## Problem

v0.3 has separate loader, bridge, and external fixture readiness packages.
Before release-candidate work, the project needs one reviewable audit that
connects their evidence to compatibility surfaces and v0.4 handoff readiness.

## Goal

Create an evidence index and compatibility audit that distinguish implemented
behavior, documented contracts, tested compatibility, missing evidence, and
open findings.

## Non-goals

- Do not implement or patch loader behavior.
- Do not implement or patch runtime context bridge behavior.
- Do not add API, frontend, schema, fixture, migration, or test
  implementation changes.
- Do not start v0.4 Agent-in-World work.
- Do not declare v0.3 release status.

## Why Now

0.3.6 sits between external fixture contract readiness and the release
candidate bundle. It determines whether v0.3 evidence is coherent enough for
release-candidate review.

## North Star Alignment

This package supports the north star by keeping the WorldSpec-to-runtime bridge
generic, evidence-backed, and compatible. It preserves WorldEngine as an engine
foundation rather than narrowing it into a concrete validation world or
application backend.
