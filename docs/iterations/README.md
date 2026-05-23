# Iteration Documentation Standard

Status: process standard

This directory is the process source of truth for WorldEngine iteration work.
It exists so future coding agents can understand what is being built, why, how
far it is allowed to go, and what evidence closed the work.

## Directory Shape

```text
docs/iterations/
├── README.md
├── templates/
│   ├── README.md
│   ├── intent.md
│   ├── contract.md
│   ├── technical-design.md
│   ├── test-plan.md
│   ├── plan.md
│   └── review.md
└── v<N>/
    ├── README.md
    ├── v<N>-plan.md
    └── <version-package>-<slug>/
        ├── README.md
        ├── intent.md
        ├── contract.md
        ├── technical-design.md
        ├── test-plan.md
        ├── plan.md
        └── review.md
```

## Package Types

### Documentation-only package

Used for north star, product model, roadmap, scope, process, release, or
architecture documentation that does not modify runtime code.

Required:

- `README.md`
- `intent.md`
- `contract.md`
- `plan.md`
- `review.md`

`technical-design.md` and `test-plan.md` may be omitted only when the package
does not prepare code, schema, API, UI, or test implementation.

### Code package

Used when the iteration modifies runtime code, schemas, APIs, services, UI,
tests, fixtures, or migrations.

Required:

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`

### Mixed package

Used when documentation changes and code/schema/API/UI/test changes happen in
the same package. Mixed packages follow code package rules.

## Required Work Order

For code or mixed packages:

1. Draft the full package document set.
2. Review and approve `contract.md`, `technical-design.md`, `test-plan.md`,
   and `plan.md`.
3. Implement only the approved package.
4. Run the verification commands listed in `test-plan.md`.
5. Update `review.md` with changed files, commands run, test results,
   compatibility review, scope review, unresolved findings, and final
   assessment.

## Contract Rules

`contract.md` defines what the package may and may not change. It must cover:

- public concepts.
- field or schema semantics.
- compatibility constraints.
- allowed changes.
- forbidden changes.
- relationship to the north star and roadmap.

Implementation must not silently reinterpret the contract.

## Review Evidence Rules

Every package must close with review evidence:

- changed files.
- commands run.
- test results or explicit docs-only no-test rationale.
- compatibility review.
- scope review.
- unresolved P1/P2/P3 findings.

Do not claim tests or runtime behavior passed without current-session evidence.
