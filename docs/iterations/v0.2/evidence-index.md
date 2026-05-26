# v0.2 Evidence Index

Status: 0.2.9 audit evidence

This index maps active v0.2 claims to their evidence. It distinguishes
implemented, documented, tested, reviewed, planned, not implemented,
historical artifact, and finding states so later compatibility and release
work does not promote planned scope into implemented behavior.

## Evidence Status Key

- `implemented`: repository code or documentation deliverable exists.
- `documented`: contract, boundary, roadmap, or implementation-map text exists.
- `tested`: current-session package review records command evidence.
- `reviewed`: package review or documentation review records approval.
- `planned`: listed as future or later-package work.
- `not implemented`: explicitly out of current implementation scope.
- `historical artifact`: retained only as historical record.
- `finding`: unresolved or closed item recorded in `findings.md`.

## Active Claim Map

| Claim | Source | Evidence | Verification source | Status | Notes |
|---|---|---|---|---|---|
| v0.2 is the Recursive World Foundation milestone, not a final release. | `docs/iterations/v0.2/README.md`, `docs/iterations/v0.2/v0.2-plan.md`, `docs/roadmap.md` | v0.2 plan and roadmap keep the milestone `planned / in progress`. | 0.2.6 review records documentation checks for the remaining package sequence. | documented / reviewed | 0.2.11 and 0.2.12 remain future release-candidate and final-closeout packages. |
| WorldEngine remains a generic recursive world engine, not a demo-specific backend. | `docs/project-north-star.md`, `docs/product-model.md`, `docs/scope-boundaries.md` | 0.2.5 cleaned active concrete external-world anchors and added external consumer boundaries. | 0.2.5 review records targeted active-docs/tests/fixtures grep with no active concrete demo anchors. | documented / reviewed / tested | Historical package text is classified separately from active direction. |
| `backend/app/` is the active backend path. | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md` | Current implementation docs describe active FastAPI assembly and routes. | 0.2.5, 0.2.7, and 0.2.8 reviews record no runtime path changes. | documented / reviewed | 0.2.10 will perform the detailed compatibility review. |
| `backend/worldengine/` is legacy. | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md` | Current implementation docs state the legacy path is not wired into the active app. | 0.2.7 and 0.2.8 reviews record no `backend/worldengine/` changes. | documented / reviewed | Detailed legacy boundary documentation is planned for 0.2.10. |
| `EntityRef` exists as a domain-neutral schema reference. | `docs/contracts/entity-ref-contract.md`, `backend/app/schemas/entity.py` | 0.2.2 added the schema; 0.2.7 added the contract document. | 0.2.2 review: focused schema test `15 passed`; backend tests `78 passed`. 0.2.7 review: focused schema tests `19 passed`; `make check-backend` passed. | implemented / documented / tested / reviewed | No resolver, loader, registry, memory, projection, or external fixture semantics are implemented. |
| `WorldCell` exists as a recursive schema object. | `docs/contracts/worldcell-contract.md`, `backend/app/schemas/world_cell.py` | 0.2.2 added the schema; 0.2.7 documented recursive child semantics. | 0.2.2 and 0.2.7 reviews record focused schema tests and backend checks passing. | implemented / documented / tested / reviewed | Runtime loading, tick behavior, generation, and projection remain out of scope. |
| `WorldSpec` exists as a versioned recursive schema wrapper. | `docs/contracts/worldspec-contract.md`, `backend/app/schemas/world_cell.py` | 0.2.2 added the schema; 0.2.7 documented versioning and round-trip expectations. | 0.2.7 review records `19 passed` for schema smoke and world-cell tests plus `make check-backend`. | implemented / documented / tested / reviewed | It is not a loader interface in v0.2. |
| Generic WorldSpec schema smoke coverage replaced concrete fixture tests. | `backend/app/tests/test_worldspec_schema_smoke.py`, 0.2.5 review | 0.2.5 deleted concrete fixture data/test and added domain-neutral in-memory schema smoke tests. | 0.2.5 review: smoke test `4 passed`; backend app tests `91 passed`. | implemented / tested / reviewed | Active fixtures do not store concrete external-world seed data. |
| `EventRef` and optional `Event.refs` exist as additive event reference structure. | `docs/contracts/event-ref-contract.md`, `backend/app/schemas/event.py` | 0.2.3 added event-local refs; 0.2.8 added the contract and free-form metadata coverage. | 0.2.3 review: focused event tests `9 passed`; backend tests `87 passed`. 0.2.8 review: focused event tests `10 passed`; `make check-backend` passed. | implemented / documented / tested / reviewed | No resolver, causality engine, runtime binding, memory link, or projection behavior is implemented. |
| Existing event payload and API behavior remain compatible. | 0.2.3 and 0.2.8 reviews | Reviews state `Event.refs` remains optional and payload/runtime/API/frontend behavior was unchanged. | Focused event compatibility tests passed in both implementation reviews. | tested / reviewed | This is schema-local compatibility evidence, not a runtime causality claim. |
| External fixture and validation worlds are consumers, not core fixtures. | `docs/external-fixture-boundary.md`, `docs/validation-report-template.md`, `docs/scope-boundaries.md` | 0.2.5 added boundary and redacted validation report docs. | 0.2.5 review records concrete fixture deletion and active anchor sweep. | documented / reviewed / tested | External repositories are not created in v0.2. |
| v0.1 runtime scaffold behavior is preserved during v0.2 foundation work. | `docs/current-implementation.md`, `docs/backend-implementation.md`, completed package reviews | Code packages 0.2.2, 0.2.3, 0.2.5, 0.2.7, and 0.2.8 record compatibility reviews. | Backend regression passed in 0.2.2, 0.2.3, and 0.2.5; 0.2.7 and 0.2.8 ran focused checks because no schema/runtime code changed. | documented / tested / reviewed | 0.2.10 remains responsible for explicit legacy compatibility review. |
| Iteration workflow requires documentation gates before implementation. | `docs/iterations/README.md`, `docs/iterations/v0.2/development-workflow.md` | 0.2.1 established iteration standards; 0.2.6 added workflow docs and final review bundle template. | 0.2.6 review records detailed plan acceptance checks and bilingual mirror checks. | documented / reviewed | 0.2.9 follows that gate as a documentation-only audit implementation. |
| 0.2.4 concrete fixture package is superseded and historical only. | `docs/iterations/v0.2/README.md`, 0.2.5 review | v0.2 index marks 0.2.4 as `historical artifact`; 0.2.5 review records cleanup. | 0.2.5 review records deletion of concrete fixture data and replacement tests. | historical artifact / reviewed | Historical evidence must not drive future engine abstractions. |
| WorldSpec loader and RuntimeEngine bridge are not implemented in v0.2. | `docs/scope-boundaries.md`, `docs/roadmap.md`, `docs/iterations/v0.2/v0.2-plan.md` | v0.2 non-goals and v0.3 roadmap handoff define future scope. | Completed package reviews repeatedly record no loader or runtime bridge changes. | planned / not implemented / reviewed | v0.3 may address this only through a later reviewed package. |
| Agent loop, memory, self-continuity, generation, projection API, product UI, and external repositories are future scope. | `docs/project-north-star.md`, `docs/scope-boundaries.md`, `docs/roadmap.md`, `docs/iterations/v0.2/v0.2-plan.md` | Roadmap places these in later milestones. | 0.2.5, 0.2.7, and 0.2.8 scope reviews record no such implementation. | planned / not implemented / reviewed | North Star direction exists, but runtime implementation is outside v0.2. |
| 0.2.7 and 0.2.8 status drift is resolved by this audit. | `docs/iterations/v0.2/findings.md`, `docs/iterations/v0.2/v0.2-plan.md`, `docs/iterations/v0.2/v0.2-plan.zh.md` | 0.2.9 updates detailed plan status fields to match milestone index. | 0.2.9 verification records status grep across English and Chinese mirrors. | finding / reviewed | Findings are closed with status-synchronization evidence. |

## Evidence Limits

- This index does not add implementation evidence for runtime behavior beyond
  what completed package reviews already record.
- Backend and frontend tests are not rerun for 0.2.9 because this package is
  documentation-only and forbids runtime, schema, API, frontend, fixture,
  migration, and test implementation changes.
- 0.2.10 remains the handoff for detailed legacy/runtime compatibility
  boundary review.
