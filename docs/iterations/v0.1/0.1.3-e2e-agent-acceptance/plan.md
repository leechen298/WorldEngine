# Plan

1. Add validator tests and fixtures first.
2. Run validator tests and confirm they fail before the validator exists.
3. Implement `tools/testing/validate_agent_smoke_result.py`.
4. Run validator tests and confirm they pass.
5. Add Playwright dependency, config, and E2E tests.
6. Add stable `data-test` selectors to dashboard components.
7. Add Make targets for E2E and agent smoke validation.
8. Add `test-results/` to `.gitignore`.
9. Add Agent smoke documentation and result schema.
10. Update v0.1 iteration index and plan docs.
11. Run required verification commands.
12. Update `review.md` and durable test result summary with only actual command
    results.
