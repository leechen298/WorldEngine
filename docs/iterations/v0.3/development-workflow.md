# v0.3 External Automation Consumption Contract

Status: process contract

## Purpose

This document defines how v0.3 iteration documents can be consumed by external
automation. It is not an automation controller design and does not define
agent roles, retry loops, scheduling, or orchestration.

## WorldEngine Provides

WorldEngine provides:

- iteration docs.
- package specs.
- allowed-change and forbidden-change boundaries.
- verification expectations.
- review evidence requirements.
- final review bundle templates.
- deterministic package handoff language.

## External Automation Controller Owns

An external automation controller may decide:

- agent roles.
- retry loops.
- scheduling.
- orchestration.
- dispatch and closeout mechanics.
- storage for automation state.

Those controller details must not become WorldEngine core runtime, schema, API,
frontend, fixture, or package-contract behavior.

## Package Determinism

Every future v0.3 package must be deterministic enough for external automation
to consume. Each package must state:

- contract.
- allowed changes.
- forbidden changes.
- expected deliverables.
- expected tests or verification.
- review evidence requirements.
- compatibility constraints.
- scope guardrails.
- handoff to the next package.

## Evidence Rules

- Do not claim tests, builds, runtime behavior, E2E, UI smoke, or backend
  behavior passed without current-session evidence.
- Documentation-only packages may skip code tests only when they record why.
- Code or mixed packages must record exact commands, test results,
  compatibility review, scope review, unresolved findings, and final
  assessment in package `review.md`.

## Scope Rules

- Do not expand beyond the package contract.
- Do not implement future-version behavior inside the current package.
- Do not add concrete demo worlds or external validation internals to core.
- Do not change runtime, schema, API, frontend, tests, fixtures, or legacy-path
  behavior without a reviewed package contract and compatibility evidence.
