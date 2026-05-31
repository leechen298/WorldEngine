# Test Plan

## Red Check

Already reproduced before implementation:

```bash
cd frontend && pnpm build
```

Expected before implementation: exit `1` with the reported TypeScript errors
in `MemoryPanel.test.ts`, `TimelinePanel.test.ts`, `TimelinePanel.vue`, and
`WorldPanel.test.ts`.

## Required Validation Commands

Run and record after implementation:

```bash
cd frontend && pnpm build
cd frontend && pnpm test
make test-e2e
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260531T122230+0800
git diff --check
```

## Acceptance Criteria

- `cd frontend && pnpm build` exits `0`.
- Frontend Vitest exits `0` and preserves existing selector assertions.
- Full E2E exits `0`.
- Agent smoke latest result validates with exit `0`.
- Minimal autonomous saved result validates with exit `0`.
- `git diff --check` exits `0`.
- `review.md` records commands, exact outcomes, scope review, compatibility
  review, subagent/evaluator findings, and final clean-pass or blocked status.

## Not Run

Any required command that cannot run must be recorded with command, exit code
or blocker, and the final assessment must not claim a clean pass.
