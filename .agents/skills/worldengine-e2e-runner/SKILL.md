---
name: worldengine-e2e-runner
description: Use when running, debugging, or reporting WorldEngine browser E2E tests, Playwright dashboard scenarios, `make test-e2e`, or E2E evidence for this repository.
---

# WorldEngine E2E Runner

Use this skill only inside the WorldEngine repository.

## Guardrails

- Do not change runtime or product behavior just to make E2E pass unless the
  user explicitly asks for a fix.
- Do not report E2E success from UI observation.
- PASS requires a fresh command exit code from `make test-e2e` or a clearly
  scoped Playwright command.
- If browser dependencies are missing, install Chromium with:

```bash
cd frontend
pnpm exec playwright install chromium
```

## Workflow

1. Check repository state with `git status --short --branch`.
2. Confirm dependencies with:

```bash
make check-backend
make check-frontend
```

3. Run the deterministic browser suite:

```bash
make test-e2e
```

4. Read the command output and exit code.
5. If it fails, report the failing spec, assertion, and artifact path. Do not
   call it passed.
6. If it passes, report the exact command and pass count.

## Evidence

Playwright artifacts live under `test-results/e2e/` and are local test
artifacts. Durable summaries, when needed, belong under `docs/testing/results/`.

Do not infer pass from screenshots, dashboard appearance, or natural-language
agent observations.
