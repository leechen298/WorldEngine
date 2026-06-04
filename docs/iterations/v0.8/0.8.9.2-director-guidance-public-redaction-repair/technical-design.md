# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Implementation Structure

The expected runtime repair is a narrow wording change in:

```text
backend/app/api/routes/world.py
```

The current `submit_director_guidance` response uses public-facing text that
contains private/internal marker terms. The repair should replace that text
with public-safe wording such as:

```text
Public director guidance was accepted as external world-environment direction.
No direct internal state mutation was performed.
```

The final wording must avoid all known public evidence markers and should not
name protected private Agent concepts.

## Test Structure

Focused tests should live in:

```text
backend/app/tests/test_public_handoff_contract_api.py
```

The current test asserts that `"private memory"` appears in
`public_explanation`; implementation must first replace that assertion with a
redaction-boundary assertion that fails against the current implementation.

The test should check:

- response status remains `200`.
- response status remains `accepted`.
- `applied_event_id` is present.
- `public_explanation` contains no forbidden evidence markers.
- the event payload still omits raw `instruction_text`.
- the event payload still omits private state markers.

If the autonomous checker lacks regression coverage for direct API operation
records in full lifecycle operation logs, add focused checker coverage in
`tools/testing/tests/` or the local testing convention already used by this
repository. Do not weaken existing checker rules.

## Data And Control Flow

```text
Validation Client UI
  -> Validation Client public API
  -> WorldEngine POST /worlds/{world_id}/director-guidance
  -> WorldEngine appends director.guidance.accepted event
  -> WorldEngine returns DirectorGuidanceResponse.public_explanation
  -> Validation Client evidence exporter scans public evidence
  -> WorldEngine saved-result checker validates exported evidence
```

This package changes only the public explanation text and, if required,
checker regression coverage. It does not add a new private mutation path.

## Compatibility Strategy

- Keep response schema fields unchanged.
- Keep operation id unchanged.
- Keep event type and event payload shape unchanged except no raw instruction
  text may be added.
- Keep public manifest and world creation behavior unchanged.

## Anti-Drift Rules

- Do not describe private boundary guarantees by spelling out private marker
  terms in public API output.
- Do not move evidence redaction responsibility from public output to the
  Validation Client.
- Do not treat the old failed result as passing after code changes. It remains
  historical FAIL evidence.
- Do not claim full lifecycle PASS unless a new result directory passes the
  documented checker.
