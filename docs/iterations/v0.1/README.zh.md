# v0.1 Runtime Scaffold

Status: closeout documented

英文版本：`README.md`。

## Goal

建立 WorldEngine 的 runtime scaffold baseline：backend、frontend、runtime tick、event log、params、
archive、agent-assist 和 dashboard surface。

## Boundary

v0.1 还不是 recursive world engine implementation。它不包含 WorldCell、WorldSpec、world generation、
Agent memory 或 pseudo-self continuity。

## Package Index

| Package | Type | Status | Purpose |
|---|---|---|---|
| `0.1.1-v0.1-closeout` | documentation-only | review complete | Inventory v0.1 capability, run verification, and update closeout docs. |
| `0.1.2-current-implementation-docs` | documentation-only | review complete | Document current backend, frontend, API, and test implementation. |
| `0.1.3-e2e-agent-acceptance` | mixed | review complete | Add post-closeout E2E tests and Agent smoke evidence validation without changing product behavior. |
| `0.1.4-codex-test-skills` | mixed | review complete | Add project-local Codex skills and sync tooling for E2E and Agent smoke workflows. |
| `0.1.5-project-agent-workflow-skills` | mixed | review complete | Add project-local workflow skills for iteration documentation and reviewed implementation gates. |
| `0.1.6-current-code-test-case-expansion` | documentation-only | review complete | Define current-code E2E、Agent smoke 和 Codex/test-runner autonomous scenario contracts before implementing or running more tests. |
| `0.1.7-current-code-validator-expansion` | mixed | review complete | Add selector 和 Agent smoke validator infrastructure before live test execution. |
| `0.1.8-current-code-test-execution` | mixed | ready for review | 文档审核通过后，先执行一个 live `dashboard-params-flow` Agent smoke，再实现 `dashboard-archive-summary` E2E。 |

## Required Reading

- `docs/releases/v0.1.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/testing/v0.1-test-map.md`
- `docs/testing/results/2026-05-23-v0.1-closeout.md`
- `docs/testing/results/2026-05-23-v0.1-e2e-agent-acceptance.md`
- `docs/iterations/v0.1/0.1.1-v0.1-closeout/review.md`
- `docs/iterations/v0.1/0.1.2-current-implementation-docs/review.md`
- `docs/iterations/v0.1/0.1.3-e2e-agent-acceptance/review.md`
- `docs/iterations/v0.1/0.1.4-codex-test-skills/review.md`
- `docs/iterations/v0.1/0.1.5-project-agent-workflow-skills/review.md`
- `docs/iterations/v0.1/0.1.6-current-code-test-case-expansion/review.md`
- `docs/iterations/v0.1/0.1.7-current-code-validator-expansion/review.md`
- `docs/iterations/v0.1/0.1.8-current-code-test-execution/review.md`
