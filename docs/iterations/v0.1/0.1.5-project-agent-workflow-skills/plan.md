# Plan

1. Review this package's `contract.md`, `technical-design.md`, `test-plan.md`,
   and `plan.md`.
2. Add `.agents/skills/worldengine-iteration-docs/SKILL.md`.
3. Add `.agents/skills/worldengine-iteration-dev/SKILL.md`.
4. Add `.agents/skills/worldengine-agent-autonomous-test-runner/SKILL.md`.
5. Update the existing skill helper and Make targets so project skill validation
   covers all five repository-owned skills without copying them into personal
   skills by default.
6. Remove or deprecate `make sync-codex-skills` unless an explicit opt-in local
   copy command is still needed.
7. Add root agent guidance references only if needed for reliable discovery.
8. Run the required validation commands from `test-plan.md`.
9. Update `review.md` with actual changed files, command output summary,
   compatibility review, scope review, unresolved findings, and final
   assessment.

The documentation review gate is complete. Implementation starts at step 2.
