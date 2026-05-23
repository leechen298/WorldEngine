# Test Plan

## Setup

Install frontend dependencies:

```bash
cd frontend
pnpm install
```

Install the Playwright Chromium browser before the first E2E run:

```bash
cd frontend
pnpm exec playwright install chromium
```

## Required Verification

Run and record exact results in `review.md`:

```bash
make check-backend
make check-frontend
make test-e2e
make validate-agent-smoke-result RESULT_DIR=tools/testing/fixtures/agent-smoke/valid-basic-runtime
make validate-agent-smoke-fixtures
cd backend && .venv/bin/python -m pytest app/tests
cd frontend && pnpm test
cd frontend && pnpm build
```

## Expected Coverage

`make test-e2e` must cover:

- `dashboard-basic-runtime`
- `dashboard-params-flow`
- `dashboard-invalid-param`

`make validate-agent-smoke-fixtures` must cover:

- valid fixture passes.
- invalid `verdict_source = agent` fixture fails as expected.
- validator unit tests cover missing artifacts, empty commands, empty
  assertions, assertion evidence requirements, missing/empty operation logs,
  and direct API operation rejection.

## Reporting Rule

Do not claim live Agent smoke passed unless a real result directory exists and
`make validate-agent-smoke-result RESULT_DIR=<dir>` exits `0`.

If only fixtures are run, report only protocol/schema/checker verification.
When a real run is retained for review, mirror its latest raw evidence to
`test-results/agent-smoke/latest/` before commit.
