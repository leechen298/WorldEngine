# Goal Runner

Status: validation clean pass after frontend build repair

## Goal Entry

Natural-language goals covered by this campaign include:

```text
补充 v0.4 E2E 测试，写 Agent 通过页面/CLI 操作的测试用例，然后运行验证。
对当前产品能力做一次完整测试验证，包含 E2E、Agent smoke、最小 autonomous checker、命令证据和最终通过/未通过判断。
修复 v0.4 post-closeout validation 中阻断 clean pass 的 P1 frontend build failure。
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
- Autonomous PASS requires the documented scorecard checker or deterministic
  checker to exit `0`; Agent self-judgment is never a PASS source.
- Frontend build repair must stay inside the active repair package and must
  not include backend runtime/API changes or full autonomous runner work.
