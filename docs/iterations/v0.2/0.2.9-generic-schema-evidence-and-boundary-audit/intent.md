# Intent

## Problem

v0.2 now has multiple completed schema, event, workflow, boundary, and contract
packages. Before legacy compatibility review and release-candidate packaging,
the milestone needs a single evidence map that distinguishes implemented,
documented, tested, reviewed, planned, and explicitly out-of-scope claims.

Without this audit, future automation may treat planned work as implemented
capability, miss stale status drift, or blur external consumer boundaries.

## Goal

Create a documentation-only audit package that, after review approval, will:

- map active v0.2 capability claims to contract, review, and verification
  evidence.
- audit external fixture, validation, concrete-demo, and legacy boundaries.
- record missing evidence as explicit findings.
- resolve or record the deferred 0.2.7 milestone status inconsistency.
- leave runtime, schema, API, frontend, fixture, migration, and test
  implementation files untouched.

## Non-goals

- Do not implement code.
- Do not change schema behavior or tests.
- Do not fix schema or event gaps opportunistically.
- Do not implement WorldSpec loading, runtime bridge, generation, projection,
  agent loop, memory, self-continuity, external repositories, or frontend
  behavior.
- Do not restore concrete external-world fixtures, seed data, roles,
  locations, resources, story rules, product UI, or application-specific
  backend logic.
- Do not declare v0.2 release-candidate or final status.

## Why Now

0.2.7 and 0.2.8 hardened the recursive schema and event reference contracts.
0.2.10 will review v0.1 runtime compatibility and legacy boundaries. 0.2.9 is
the audit step between those efforts: it makes current evidence explicit
before compatibility and release-candidate documentation rely on it.

## North Star Alignment

This package supports the recursive world foundation by keeping evidence,
boundaries, and status claims inspectable. It protects WorldEngine from
drifting into application-specific or demo-specific behavior while preserving
the event and schema foundations needed for future runtime, agent, memory, and
projection work.
