# Plan

## Files

Create:

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/architecture.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/glossary.md`
- `docs/iterations/README.md`
- `docs/iterations/templates/README.md`
- `docs/iterations/templates/intent.md`
- `docs/iterations/templates/contract.md`
- `docs/iterations/templates/technical-design.md`
- `docs/iterations/templates/test-plan.md`
- `docs/iterations/templates/plan.md`
- `docs/iterations/templates/review.md`
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/0.2.1-project-north-star/README.md`
- `docs/iterations/v0.2/0.2.1-project-north-star/intent.md`
- `docs/iterations/v0.2/0.2.1-project-north-star/contract.md`
- `docs/iterations/v0.2/0.2.1-project-north-star/plan.md`
- `docs/iterations/v0.2/0.2.1-project-north-star/review.md`
- `docs/releases/v0.1.md`
- `docs/releases/v0.2.md`
- `docs/testing/README.md`
- `docs/testing/results/.gitkeep`

Do not touch:

- `backend/`
- `frontend/`
- `docs/v1-design.md`

## Steps

1. Read local WebAgentFlow process documents for engineering rhythm.
2. Create WorldEngine-specific governance docs.
3. Create iteration templates.
4. Create v0.2 package index and plan.
5. Create 0.2.1 package docs.
6. Create release and testing entry documents.
7. Verify changed files stay docs-only.
8. Update `review.md` with evidence.

## Verification

Run:

```bash
git status --short
find docs -maxdepth 4 -type f | sort
```

Expected:

- only `AGENTS.md` and files under `docs/` are new or modified by this package.
- no backend or frontend files are changed by this package.
- tests are not run because this package is docs-only.
