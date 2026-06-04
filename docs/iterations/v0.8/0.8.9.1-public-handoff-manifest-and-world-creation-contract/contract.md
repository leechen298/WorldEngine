# Contract

Chinese mirror: `contract.zh.md`.

## Public Deliverables

Implementation must provide:

- `GET /manifest`.
- OpenAPI-discoverable `POST /worlds` with operation id `create_world`.
- public world creation request accepting `world_prompt`.
- public world creation response containing:
  - `world_id`
  - `status`
  - `public_initial_state`
  - `visualization`
- provider readiness summary containing only:
  - `provider_class`
  - `provider_readiness`
  - `credential_source_class`
  - `model_label`
  - optional public quota or rate-limit note
- redaction confirmation flags.
- blockers and warnings.
- public director guidance status, either as
  `POST /worlds/{world_id}/director-guidance` or as an explicit manifest
  unavailable reason.

## Allowed Changes

After approval, this package may modify:

- `backend/app/api/routes/`
- `backend/app/api/app_factory.py`
- `backend/app/schemas/`
- `backend/app/core/world_generation.py` only for reusable public summary or
  redaction helpers needed by the contract.
- focused backend tests under `backend/app/tests/`.
- package review evidence under this directory.

## Forbidden Changes

This package must not:

- modify the Validation Client repository.
- modify `backend/worldengine/`.
- introduce concrete demo-world names, maps, characters, resources, story
  rules, seed data, or application-specific behavior.
- implement provider calls.
- store provider keys, account ids, tokens, credentials, or authorization
  headers.
- expose private prompts, raw provider requests, raw provider responses,
  private evaluator oracle data, private validation scenarios, private Agent
  memory, private goals, relationship state, `self_state`, hidden context,
  private file paths, or hidden reset APIs.
- use an `ApiResponse` envelope for `POST /worlds` if that prevents Validation
  Client from reading top-level `world_id`.
- claim external validation PASS, product readiness, live provider PASS, Agent
  autonomous PASS, E2E PASS, or human validation PASS.

## Compatibility Constraints

- Existing generation endpoints must remain compatible.
- Existing v0.8 closeout evidence remains historical and bounded.
- Schema changes must be additive.
- Public responses must use generic WorldEngine concepts, not external
  application details.
- Missing provider configuration must not be reported as ready.

## Stop Rules

Stop implementation if:

- the contract requires changing Validation Client code.
- world creation cannot be implemented without concrete demo content.
- a public response would expose secrets, private prompts, provider raw traces,
  or private Agent state.
- director guidance would directly mutate private Agent memory, goals,
  identity, relationships, or `self_state`.
- tests cannot prove OpenAPI discoverability for `POST /worlds`.
