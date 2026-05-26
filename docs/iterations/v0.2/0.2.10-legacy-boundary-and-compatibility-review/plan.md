# Plan

## Stage 1: Documentation Package

- Read repository guidance, project direction docs, iteration standard, v0.2
  index, v0.2 plan, templates, and adjacent package docs.
- Classify the package as documentation-only.
- Draft English and Chinese package docs.
- Set package README and milestone status to `ready for review`.
- Run documentation-stage checks.
- Record documentation-stage evidence in review docs.

## Stage 2: After Documentation Review Approval

- Read implementation maps, architecture docs, API docs, v0.2 evidence and
  boundary docs, completed package reviews, and findings.
- Create `docs/legacy-boundary.md` and `.zh.md`.
- Create `docs/iterations/v0.2/compatibility-review.md` and `.zh.md`.
- Update `docs/iterations/v0.2/findings.md` for unresolved compatibility
  issues or handoff risks.
- Run documentation checks, path checks, status checks, and anchor sweep.
- Update package review docs with changed files, commands, results,
  compatibility review, scope review, and unresolved findings.

## Review Gate

Implementation of the planned documentation deliverables must wait until this
package is reviewed. Do not mark this package `ready for implementation`; this
documentation-only package moves from `ready for review` to review completion
only after the documentation review and allowed docs implementation are done.

## Stop Conditions

- A requested change requires runtime, schema, API, frontend, fixture,
  migration, or test implementation edits.
- The compatibility review needs to assert behavior that is neither documented
  nor verified.
- A concrete external-world anchor would be added to active docs.
- English and Chinese mirrors cannot be kept synchronized.
