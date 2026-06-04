# 0.8.9.2 Full World Lifecycle Autonomous Validation Cases

Status: implementation complete / AUTONOMOUS_LIFECYCLE_CASE_READY
Type: mixed validation package
implementation_authorized: user-authorized by active goal on 2026-06-04
evidence_execution_authorized: yes, bounded to test protocol, checker fixtures, and validation commands

Chinese mirror: `README.zh.md`.

## Package

Name: `0.8.9.2-full-world-lifecycle-autonomous-validation-cases`

This package supplements the current autonomous validation coverage so a future
validation run can judge the full WorldEngine lifecycle instead of only the
Validation Client UI smoke or historical dashboard saved-result scenarios.

## Goal

Add a checker-supported autonomous validation scenario for the complete
WorldEngine lifecycle:

- create a world through the external client surface.
- verify WorldEngine returns a runnable public world state.
- run the world forward across ticks.
- observe state, event, snapshot, and replay evidence.
- observe in-world Agent behavior produced by WorldEngine evidence rather than
  client-side scripted actions.
- apply natural-language direction only to external events or world
  environment.
- export evidence that another Agent can review without private prompts,
  secrets, or hidden WorldEngine internals.

## Required Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`
- [x] Chinese mirrors

## Scope Summary

Allowed:

- autonomous testing protocol docs.
- full lifecycle autonomous scenario docs.
- autonomous result schema/checker extensions.
- focused checker unit tests.
- generic checker fixtures.
- review evidence.

Forbidden:

- core runtime behavior changes.
- provider API implementation.
- Validation Client repository changes.
- concrete validation-world seed content.
- private prompt, raw provider response, private Agent memory, private goals,
  `self_state`, hidden context, credentials, or account data in fixtures or
  public evidence.

## Handoff

This package makes the full WorldEngine lifecycle validation case executable as
a saved-result checker. It still does not by itself prove live WorldEngine
PASS; a later run must generate real evidence and validate that result
directory.
