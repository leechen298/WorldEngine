# Plan

Chinese mirror: `plan.zh.md`.

## Objective

After user review and explicit implementation authorization, implement the
WorldEngine public handoff manifest and world creation contract required by
the 0.8.9 parent package.

## Tasks

### 1. Gate Confirmation

- Confirm this package is approved for implementation.
- Confirm no unrelated dirty files will be modified or staged.
- Keep existing user changes intact.

### 2. Public Schemas

- Add or extend public schema models for manifest, provider readiness,
  redaction, world creation, and director guidance.
- Ensure models forbid extra private fields where appropriate.
- Add schema serialization tests.

### 3. Public Manifest Route

- Add `GET /manifest`.
- Return public provider readiness, public surfaces, redaction flags,
  blockers, and warnings.
- Do not perform live provider calls.
- Do not expose secrets, private prompts, raw traces, or private validator
  details.

### 4. Public World Creation Route

- Add OpenAPI-discoverable `POST /worlds` with operation id `create_world`.
- Accept `world_prompt`.
- Return top-level public `world_id`, `status`, `public_initial_state`, and
  `visualization`.
- Reuse existing generic generation helpers without adding demo content.

### 5. Director Guidance Status

- Add `POST /worlds/{world_id}/director-guidance` if it can remain public and
  non-private.
- Otherwise, record director guidance as unavailable in `/manifest`.

### 6. Redaction And Compatibility Tests

- Add focused tests for manifest shape, OpenAPI discoverability, world creation
  response shape, and forbidden private data absence.
- Preserve existing endpoint behavior.

### 7. Runtime And Optional Client Probe

- Run backend focused tests.
- Run backend full tests.
- Start WorldEngine and probe `/health`, `/manifest`, `/openapi.json`, and
  `/worlds`.
- If available, run Validation Client `/health/worldengine` and
  `/sessions/worldengine` compatibility probes.

### 8. Review Closeout

- Update `review.md` and `review.zh.md`.
- If criteria pass, record only `WORLDENGINE_CONTRACT_READY`.
- Do not claim external validation PASS, Codex autonomous PASS, or human
  validation PASS.

## Out Of Scope

- Validation Client implementation.
- provider runtime calls.
- provider credential storage.
- application-specific worlds or fixtures.
- hidden reset APIs.
- frontend changes.
- migrations.
- `backend/worldengine/`.
