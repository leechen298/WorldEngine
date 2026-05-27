# Plan

## Files

Create:

- `docs/contracts/worldspec-loader-contract.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/intent.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/contract.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/technical-design.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/test-plan.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/plan.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/review.md`

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

1. Read repository and v0.3 milestone guidance.
2. Draft the loader contract in `docs/contracts/`.
3. Draft full 0.3.1 package docs with assumptions, risks, and verification.
4. Synchronize package status in English and Chinese milestone docs.
5. Run documentation and scope checks.
6. Record actual evidence in `review.md`.

## Verification

Use the commands listed in `test-plan.md`. Runtime and frontend tests are not
planned unless implementation files are accidentally touched; if that happens,
stop and report the scope violation.
