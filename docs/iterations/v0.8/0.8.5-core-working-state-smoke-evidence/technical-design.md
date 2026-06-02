# Technical Design

Status: documentation-stage validation design

## Evidence Matrix Design

The package uses a command matrix with one row per core surface:

```text
surface_id
evidence_class
command
proof_boundary
expected_status
artifact_or_log_reference
non_claims
```

The matrix is recorded in `test-plan.md` before any command is run. Evidence
execution may run only the listed commands after review authorization.

## Required Command Groups

The documentation-stage candidate matrix defines these command groups:

1. Formatting and documentation guards:
   - `git diff --check`
   - required package docs and mirrors check.
   - status consistency check.
   - changed-file scope guard.
   - v0.8 Markdown whitespace check.
2. Generation and loader backend focused tests:
   - WorldSpec schema and loader tests.
   - deterministic generation, plan schema/import/compile, template catalog,
     generation schema, preview, regeneration, runtime-readiness, and
     core-readiness tests.
3. Runtime/event/backend focused tests:
   - runtime context bridge.
   - runtime step.
   - event schema/API compatibility.
   - archive snapshot/summary.
4. Agent/memory backend focused tests:
   - Agent loop service/API/perception/action adapter.
   - memory substrate.
   - params agent and dry-run validation boundaries when used by current core
     behavior.
5. v0.7 handoff compatibility:
   - repository-local public contract/checker commands when needed to confirm
     report/manifest/projection handoff compatibility.
6. Explicit non-run classifications:
   - frontend build/unit, E2E, Agent smoke, autonomous, external validation,
     product readiness, and generation-quality checks unless the reviewed
     package authorizes them and names commands.

## Proof Boundary Design

Each command result must be interpreted narrowly:

- backend/API focused tests prove only their named backend/API surfaces.
- checker tests prove only checker/schema compatibility.
- documentation guards prove only documentation shape, status, and scope.
- historical v0.7/v0.6 results prove only handoff context.
- skipped/out-of-scope entries prove nothing and must not be counted as PASS.

## Artifact Design

This package may record command output summaries in `review.md`. A separate
result artifact under `docs/testing/results/` is optional and must be
repository-local, redacted, and authorized before creation.

Artifact references must not include private external repository paths,
external validator details, private scenario names, UI selectors, screenshots,
transcripts, raw prompts, provider traces, secrets, concrete validation worlds,
or non-redacted external event payloads.

## Authorization Design

Documentation review can authorize evidence execution but should not authorize
implementation changes by default. If evidence reveals a bug or missing test
implementation, stop and create or update the relevant package contract before
changing code.
