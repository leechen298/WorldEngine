# Latest Agent Smoke Evidence

Scenario: `dashboard-invalid-param`

Status: validated

This directory contains the 0.1.9 live Agent smoke evidence for
`dashboard-invalid-param`.

Validation command:

```bash
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
```

Validated result:

```text
PASS: validated agent smoke result at test-results/agent-smoke/latest
```

The previous 0.1.8 `dashboard-params-flow` raw `latest/` evidence remains
available through commit `c6da552` and is summarized in
`docs/testing/results/2026-05-24-v0.1.8-params-flow-live-smoke.md`.
