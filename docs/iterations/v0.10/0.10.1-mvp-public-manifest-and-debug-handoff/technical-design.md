# Technical Design

## Implementation Structure

The implementation should be additive and centered on the existing public
handoff manifest path.

Schema changes in `backend/app/schemas/world.py`:

- Add status taxonomy and checker-handoff model types.
- Extend `PublicSurface` with optional/defaulted MVP/debug metadata:
  maturity, validation status, required-for-MVP flag, and notes.
- Extend `HandoffManifest` with optional/defaulted v0.10 fields such as
  `mvp_contract_version`, `manifest_status`, `status_taxonomy`,
  `checker_handoff`, `validation_client_role`, `provider_owner`,
  `evaluator_role`, and `worldline_branch_semantics`.

Route changes in `backend/app/api/routes/world.py`:

- Keep `/manifest` at the same path and operation id.
- Keep existing public surface list entries.
- Add v0.10 MVP/debug metadata for existing surfaces.
- Include planned session/debug surfaces as `unavailable` or `not_run` rather
  than pretending they are implemented.
- Add warnings/blockers that clearly distinguish provider readiness from live
  proof and planned session surfaces from available functionality.

Test changes in `backend/app/tests/test_public_handoff_contract_api.py`:

- Assert legacy fields still exist.
- Assert `worldengine_version` and `mvp_contract_version` describe v0.10.
- Assert `status_taxonomy` includes `pass`, `fail`, `blocked`, and `not_run`.
- Assert planned session surfaces are not marked available/pass before
  implementation.
- Assert redaction flags remain false and known secret/raw markers do not
  appear in serialized manifest output.
- Assert branch terminology avoids parent/source-world semantics.

## Affected Files

Implementation files:

- `backend/app/schemas/world.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_public_handoff_contract_api.py`

Documentation files:

- files under
  `docs/iterations/v0.10/0.10.1-mvp-public-manifest-and-debug-handoff/`
- v0.10 parent route/review files as needed.

## Data / Control Flow

The only runtime-facing flow changed by this package is:

```text
GET /manifest
-> provider_readiness_from_env()
-> HandoffManifest with additive v0.10 debug metadata
-> redacted public JSON response
```

No world session state is created. No runtime tick is executed. No provider
live call is made. No checker result is generated.

## Compatibility Strategy

- Keep existing field names and response path.
- Add fields with default values so schema construction remains simple.
- Preserve existing `public_surfaces` list while extending its entries.
- Mark unavailable future surfaces honestly instead of omitting all future
  handoff expectations or reporting them as pass.
- Preserve redaction booleans as false by default and test for known leak
  markers.

## Anti-Drift Rules

- If implementation needs files outside the allowed list, stop and update this
  package for review before editing them.
- If session state or runtime behavior is required, stop and hand off to
  `0.10.2` or later.
- If checker/fixture work is required, stop and record a blocker or revise the
  package.
- If a future surface is unavailable, mark it `unavailable`, `blocked`, or
  `not_run`, never `pass`.
- Do not use parent/source-world wording for worldline or replay branch
  semantics.
