# Campaign Plan

Status: validation clean pass after frontend build repair
Type: post-closeout mixed validation campaign

## Purpose

Control the work required to add and run v0.4 post-closeout E2E and Agent
UI/CLI smoke tests without reopening v0.4 implementation scope.

## Sequence

### 1. E2E And Agent Test Expansion

Package: `01-e2e-agent-test-expansion`

Purpose:

- add Playwright E2E coverage for `POST /world/agent/loop/step`.
- strengthen existing dashboard Auto-Tune E2E compatibility evidence.
- add executable Agent smoke support for `dashboard-agent-autotune`.
- run focused and broad verification and record current-session evidence.

Required gates:

- package docs drafted: complete.
- documentation/contract evaluator reports no P1 or unresolved P2: complete.
- implementation authorization recorded in child `review.md`: complete.
- focused tests run: complete.
- broad E2E and Agent smoke validation run: complete.
- validation-evidence evaluator reviews pass/fail evidence before final
  assessment: complete after P2 follow-up fixes.

Stop conditions:

- the test implementation requires product runtime/API/UI behavior changes.
- Agent smoke cannot pass without direct API operations in `operation-log.jsonl`.
- broader autonomous PASS is requested without a validating saved-result
  scorecard/checker result.
- E2E or Agent smoke commands cannot run and no blocker is recorded.

### 2. Overall Product Capability Validation

Package: `02-overall-product-capability-validation`

Purpose:

- create a current product capability test matrix.
- fill v0.4 Agent Loop E2E boundary coverage gaps.
- add a minimal executable Codex/test-runner autonomous checker, schema, and
  fixtures.
- run the required validation command set and report pass/partial/fail.

Required gates:

- package contract records product-code no-change boundary.
- focused E2E and autonomous checker tests run: complete.
- broad backend, frontend, E2E, smoke, autonomous, and docs checks run:
  complete.
- frontend build failure is recorded as P1 if still present: complete.

Stop conditions:

- any required work would modify product implementation.
- autonomous PASS would come from Agent self-judgment.
- clean pass would be claimed while `pnpm build` still fails.

### 3. Frontend Build Type Repair

Package: `03-frontend-build-type-repair`

Purpose:

- repair only the P1 frontend TypeScript build failure recorded by package
  `02-overall-product-capability-validation`.
- rerun the validation command matrix needed to decide clean pass versus a new
  blocker.
- keep full autonomous runner implementation and backend runtime/API changes
  out of scope.

Required gates:

- repair package documents drafted: complete.
- documentation/contract evaluator reports no P1 or unresolved P2: complete.
- implementation authorization recorded in child `review.md`: complete.
- focused frontend build rerun: complete.
- broad build, Vitest, E2E, Agent smoke, autonomous, and whitespace validation
  rerun: complete.
- frontend type/build reviewer complete before broad validation: complete.
- scope/evidence evaluator complete before final assessment: complete.

Stop conditions:

- the fix requires backend runtime/API behavior changes.
- the fix expands beyond the reported frontend TypeScript failures.
- clean pass would be claimed while any required validation command fails.
- full autonomous runner work is required to continue.
