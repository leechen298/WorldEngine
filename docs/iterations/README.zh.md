# Iteration Documentation Standard

Status: process standard

英文版本：`README.md`。

本目录是 WorldEngine iteration work 的 process source of truth。它让未来 coding agents 能理解正在
构建什么、为什么构建、允许走到哪里，以及用什么 evidence 关闭工作。

创建或修改 iteration documents 前，先读取 `docs/iterations/AGENTS.zh.md`。

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

用于 north star、product model、roadmap、scope、process、release 或 architecture documentation，
且不修改 runtime code。

Required：

- `README.md`
- `intent.md`
- `contract.md`
- `plan.md`
- `review.md`

只有当 package 不准备 code、schema、API、UI 或 test implementation 时，才能省略
`technical-design.md` 和 `test-plan.md`。

### Code package

用于修改 runtime code、schemas、APIs、services、UI、tests、fixtures 或 migrations 的 iteration。

Required：

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`

### Mixed package

用于 documentation changes 与 code/schema/API/UI/test changes 同时发生的 package。Mixed packages
遵循 code package rules。

## Required Work Order

对于 code 或 mixed packages：

1. Draft full package document set。
2. Review and approve `contract.md`、`technical-design.md`、`test-plan.md` 和 `plan.md`。
3. 只实现 approved package。
4. 运行 `test-plan.md` 中列出的 verification commands。
5. 更新 `review.md`，记录 changed files、commands run、test results、compatibility review、scope
   review、unresolved findings 和 final assessment。

## Contract Rules

`contract.md` 定义 package 可以和不可以改变的内容。它必须覆盖：

- public concepts。
- field 或 schema semantics。
- compatibility constraints。
- allowed changes。
- forbidden changes。
- 与 north star 和 roadmap 的关系。

Implementation 不能 silent reinterpret contract。

## Review Evidence Rules

每个 package 都必须用 review evidence 收口：

- changed files。
- commands run。
- test results 或明确的 docs-only no-test rationale。
- compatibility review。
- scope review。
- unresolved P1/P2/P3 findings。

不要在没有 current-session evidence 的情况下声称 tests 或 runtime behavior passed。
