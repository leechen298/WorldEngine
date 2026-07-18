# Plan

Chinese mirror: `plan.zh.md`.

## Phase 1: Documentation Gate

1. Create the complete package document set and mirrors.
2. Run documentation completeness, authorization, and whitespace checks.
3. Request documentation evaluator review.
4. Record findings and repair docs if needed.
5. Authorize implementation only after review passes.

## Phase 2: TDD Red

1. Add focused failing tests in
   `backend/app/tests/test_session_narrative_diagnostic_inspection_api.py`.
2. Cover session/tick-range/branch/Agent-focused narrative projection.
3. Cover out-of-world diagnostic inspection.
4. Cover read-only behavior and redaction failures.

## Phase 3: Implementation

1. Add additive public inspection schemas.
2. Add read-only inspection helper logic, reusing external projection boundary
   validation where possible.
3. Add session route endpoints.
4. Add manifest surfaces.
5. Keep implementation scoped to active package files and avoid
   `backend/worldengine/`.

## Phase 4: Verification

1. Run the new focused test file.
2. Run the package focused suite from `test-plan.md`.
3. Run `git diff --check`.
4. Run active-package whitespace checks.
5. Run a small public evidence probe showing no event/memory/direction-queue
   mutation.

## Phase 5: Review And Handoff

1. Request implementation-scope evaluator review.
2. Repair any in-scope P1/P2 findings.
3. Record changed files, commands, results, compatibility, scope review,
   evaluator evidence, and unresolved findings.
4. Update parent route to `0.12.4-validation-client-mvp-evidence-handoff`.
