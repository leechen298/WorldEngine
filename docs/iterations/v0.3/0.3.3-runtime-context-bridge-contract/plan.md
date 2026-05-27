# Plan

## Files

Create:

- `docs/contracts/runtime-context-bridge-contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/README.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/intent.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/plan.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/review.md`
- matching `*.zh.md` mirrors.

Modify:

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

Do not touch:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- implementation tests, fixtures, migrations, API routes, schemas, runtime
  services, archive, params, event, or persistence code.

## Steps

1. Read repository guidance, v0.3 milestone docs, loader contract, loader
   package review, and current runtime implementation docs.
2. Draft the runtime context bridge contract in `docs/contracts/`.
3. Draft full 0.3.3 package docs with assumptions, risks, acceptance criteria,
   and verification commands.
4. Synchronize English and Chinese mirrors.
5. Mark 0.3.3 as `ready for review` in package README and milestone index.
6. Run documentation and scope checks.
7. Record current-session documentation evidence in `review.md`.

## Verification

Use the documentation checks in `test-plan.md`. Runtime and frontend tests are
not planned because this package does not modify implementation files.
