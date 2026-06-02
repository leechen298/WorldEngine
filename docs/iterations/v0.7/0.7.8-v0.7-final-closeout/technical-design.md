# Technical Design

## Primary Artifact

`final-closeout.md` is the final closeout record for v0.7. It records the
final status decision, evidence, exclusions, and v0.8 handoff boundary.

## Final Verification Groups

- checker regression: `tools/testing`.
- CLI validation: readiness manifest and projection read-model.
- JSON syntax: v0.7 report schema, readiness manifest schema/json, projection
  read-model schema.
- evidence links: all child reviews plus evidence/audit/release-candidate
  artifacts.
- formatting: `git diff --check`.
- scope: changed-file scope guard.
- status: parent and child status consistency after final update.

## Final Output Rule

If any final command or evaluator reports a blocker, final status must remain
not complete and the blocker must be recorded.
