# v0.2 Development Workflow

## Role Model

- Human + ChatGPT: define version and package intent, approve gates, and run
  holistic reviews.
- Codex A: prepares package docs, self-reviews docs, reviews implementation
  diffs, and checks evidence.
- Codex B: implements approved packages and fixes reviewed findings.

## Artifact Flow

0. Human + ChatGPT discuss a version / package plan.
1. Save plan as `docs/iterations/<version>/00-chatgpt-plan.md`.
2. Codex A generates package docs.
3. Codex A self-reviews / strengthens package docs.
4. Human approval or script gate allows implementation.
5. Codex B implements from approved package.
6. Local tests run.
7. Codex A reviews Codex B diff.
8. Codex B fixes.
9. Repeat 6-8 up to `N = 3` rounds by default.
10. Generate `final-review-bundle.md`.
11. ChatGPT performs holistic review.

## State Machine

```text
planned
  -> docs drafted
  -> ready for human / ChatGPT review
  -> approved for implementation
  -> implementation in progress
  -> tests/evidence complete
  -> diff review
  -> fix loop if needed
  -> final review bundle ready
  -> holistic review approved
```

Documentation-only packages may stop at `ready for human / ChatGPT review` or
at a later documentation review state if their contract requires it. They must
not silently become code packages.

## Gates

- Approval gate: package docs must be reviewed before implementation.
- Implementation gate: implementation must follow the approved package only.
- Test gate: commands in `test-plan.md` must run, or skipped tests must be
  justified for documentation-only packages.
- Diff review gate: changed files and behavior must match the package
  contract.
- Final review gate: release-candidate or closeout work waits for holistic
  review.

## Severity

- P1: blocking correctness, compatibility, scope, or evidence issue.
- P2: required fix before package can be treated as ready.
- P3: non-blocking polish, clarity, or follow-up.

## Evidence Rules

- Do not claim tests, builds, runtime behavior, E2E, UI smoke, or backend
  behavior passed unless verified in the current session.
- Every code or mixed package records changed files, commands run, test
  results, compatibility review, scope review, unresolved findings, and final
  assessment in `review.md`.
- Documentation-only packages may skip code tests only with an explicit reason.

## Scope Rules

- No scope expansion beyond the active package.
- No concrete demo worlds in the core repository.
- External fixture and validation worlds are consumers only.
- Future-version work must not be implemented inside the current package.
- `backend/app/` is the active backend code path.
- `frontend/` is the active dashboard code path.
- `backend/worldengine/` remains legacy unless a later approved iteration
  contract says otherwise.

## Default Fix Loop

Default maximum loop count: `N = 3`.

If P1/P2 findings remain after three review/fix cycles, stop and request human
/ ChatGPT review instead of widening scope.
