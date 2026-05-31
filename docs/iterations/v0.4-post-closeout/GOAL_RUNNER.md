# Goal Runner

Status: implementation complete / validation passed with P3

## Goal Entry

Natural-language goals covered by this campaign include:

```text
补充 v0.4 E2E 测试，写 Agent 通过页面/CLI 操作的测试用例，然后运行验证。
```

## Route Selection

- If no child package is active, start with `CURRENT_STATE.md`.
- If `CURRENT_STATE.md` points to a child package, read that child package in
  this order: `README.md`, `intent.md`, `contract.md`,
  `technical-design.md`, `test-plan.md`, `plan.md`, `review.md`.
- Do not implement until child `review.md` records implementation
  authorization.

## Subagent / Evaluator Requirements

Because this is a `/goal` mixed campaign, use subagent/evaluator checkpoints:

1. documentation/contract evaluator before implementation authorization.
2. implementation-scope evaluator before broad verification.
3. validation-evidence evaluator before recording pass/fail claims.
4. closeout consistency evaluator before final assessment.

## Reporting Rules

- E2E PASS requires Playwright command exit `0`.
- Agent smoke PASS requires `make validate-agent-smoke-result` exit `0`.
- Basic Agent smoke must not be described as full scorecard-based autonomous.
- Broader autonomous must be reported as not run / future scope unless a
  scorecard checker exists and returns PASS.
