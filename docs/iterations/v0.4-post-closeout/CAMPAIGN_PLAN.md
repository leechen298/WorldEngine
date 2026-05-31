# Campaign Plan

Status: implementation complete / validation passed with P3
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
- broader autonomous PASS is requested before a scorecard checker exists.
- E2E or Agent smoke commands cannot run and no blocker is recorded.
