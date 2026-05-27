# Technical Design

Status: ready for review

## Documentation Structure

This package creates the v0.3 iteration directory:

```text
docs/iterations/v0.3/
├── README.md
├── README.zh.md
├── v0.3-plan.md
├── v0.3-plan.zh.md
├── 00-chatgpt-plan.md
├── development-workflow.md
├── final-review-bundle-template.md
└── 0.3.0-v0.3-planning-and-compatibility-baseline/
    ├── README.md
    ├── intent.md
    ├── contract.md
    ├── technical-design.md
    ├── test-plan.md
    ├── plan.md
    └── review.md
```

It also creates v0.3 release placeholders:

```text
docs/releases/v0.3.md
docs/releases/v0.3.zh.md
```

## Package Sequence

v0.3 progresses through small reviewed packages:

1. 0.3.0 planning and compatibility baseline.
2. 0.3.1 WorldSpec loader contract.
3. 0.3.2 WorldSpec loader implementation.
4. 0.3.3 runtime context bridge contract.
5. 0.3.4 runtime context bridge implementation.
6. 0.3.5 external fixture contract readiness.
7. 0.3.6 runtime bridge evidence and compatibility audit.
8. 0.3.7 release-candidate bundle.
9. 0.3.8 final closeout after release-candidate review approval.

## Compatibility Baseline Strategy

The first code package that changes runtime, API, event, archive, params,
frontend-facing, or legacy-path behavior must produce current-session evidence
for the existing behavior before making or claiming behavior changes.

Baseline surfaces:

- RuntimeEngine tick and `world_time_seconds`.
- API envelope and error shape.
- `/runtime/step`.
- `/world/events`.
- `/world/event-steps`.
- world params and params apply behavior.
- archive snapshot and summary behavior.
- optional `Event.refs` response compatibility.
- frontend-facing response shapes.
- legacy `backend/worldengine/` boundary.

## Pre-Code Knowledge Needed

Before 0.3.2 or 0.3.4 changes code, the active package must identify:

- which v0.1 runtime behaviors must remain unchanged.
- which API response shapes are compatibility-sensitive.
- how Event.refs remains optional and additive.
- how archive and params behavior coexist with any runtime context.
- whether frontend-facing data shape is unchanged.
- whether legacy code remains untouched.

## Incremental Progression

The loader and bridge are split contract-first, implementation-second. Loader
work must validate generic WorldSpec data before bridge work. Bridge work must
be minimal, optional, and compatibility-proven before any future Agent-in-World
package starts.
