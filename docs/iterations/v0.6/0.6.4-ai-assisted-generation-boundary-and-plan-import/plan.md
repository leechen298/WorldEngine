# Plan

Status: review complete

## Objective

Create and review the `0.6.4` AI-assisted plan import boundary package, then
implement only after `implementation_authorized: yes`.

## Inputs Read

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `0.6.1` generation contract
- `0.6.3` structured plan compiler contract and review
- current generation schemas and core implementation

## Execution Steps

1. Create the seven required package docs and Chinese mirrors.
2. Keep initial status at `planned / ready for review` and
   `implementation_authorized: no`.
3. Run documentation checks.
4. Request documentation/contract evaluator review.
5. After evaluator PASS, record `implementation_authorized: yes` and sync
   parent status surfaces.
6. Implement only the approved import schema/core/test files.
7. Run focused, adjacent, full backend, diff, and scope checks.
8. Request code-review, validation-evidence, and closeout consistency
   evaluators.

## Stop Conditions

- Implementation starts before authorization.
- Import requires live provider access, prompts, network, credentials, API,
  frontend, persistence, runtime, Agent/memory, external validation,
  projection, concrete content, or `backend/worldengine/`.
- Imported plans bypass structured validation.

## Handoff

After closeout, `0.6.5-generation-validation-metadata-and-preview-api`
receives reviewed import/provenance semantics for API exposure.
