# Latest Agent Smoke Evidence

Scenario: `dashboard-agent-autotune`

Status: validated

This directory contains the v0.4 post-closeout live Agent smoke evidence for
`dashboard-agent-autotune`.

Validation command:

```bash
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
```

Validated result:

```text
PASS: validated agent smoke result at test-results/agent-smoke/latest
```

The previous 0.1.9 `dashboard-invalid-param` raw `latest/` evidence is
available in history before this v0.4 post-closeout replacement. The previous
0.1.8 `dashboard-params-flow` raw `latest/` evidence remains available through
commit `c6da552` and is summarized in
`docs/testing/results/2026-05-24-v0.1.8-params-flow-live-smoke.md`.
