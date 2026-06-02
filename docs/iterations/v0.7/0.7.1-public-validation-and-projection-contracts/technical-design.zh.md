# Technical Design

## Current State

WorldEngine already has:

- `docs/external-fixture-boundary.md`。
- `docs/contracts/external-fixture-runner-contract.md`。
- `docs/validation-report-template.md`。
- v0.6 implementation evidence，但它只作为 handoff context。
- parent v0.7 campaign docs 与已 review 的 `0.7.0` routing baseline。

当前还没有 dedicated external-validation readiness contract 或 projection consumer contract。

## Documentation Structure

本 package 添加：

```text
docs/contracts/external-validation-readiness-contract.md
docs/contracts/projection-consumer-contract.md
docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/
```

这些 contract docs 是 documentation-only public surfaces，不创建 schemas、checkers、APIs、manifests、
projection payloads 或 tests。

## Contract Content

`external-validation-readiness-contract.md` defines:

- public readiness concepts。
- readiness claim taxonomy。
- redacted report semantics。
- required redaction rules。
- compatibility requirements。
- authorization criteria for `0.7.2`。

`projection-consumer-contract.md` defines:

- projection consumer concepts。
- read-only consumer boundary。
- allowed future consumer surfaces。
- redaction and bounded-exposure rules。
- projection readiness taxonomy。
- authorization criteria for later projection implementation packages。

## Affected Surfaces

Documentation only:

- v0.7 parent and child package docs。
- `docs/contracts/external-validation-readiness-contract.md`。
- `docs/contracts/projection-consumer-contract.md`。

No runtime、schema、API、frontend、test、checker、fixture、migration、external repository、
generated result 或 legacy implementation surface is affected。

## Compatibility Strategy

- Keep `external-fixture-runner-contract.md` compatible。
- 添加 readiness taxonomy 与 projection boundary docs，但不改变 public runtime/API behavior。
- 明确区分 contract readiness 与 external suite PASS、projection app readiness、product readiness 和
  current-session validation。

## Anti-Drift Rules

- Parent and child status surfaces must agree on active child and route。
- Contract docs must not contain concrete external world or product-specific examples。
- Contract docs must not imply implementation authorization。
- Review evidence must record code tests as not run because this is documentation-only。

## Risks

- Readiness language 可能暗示 product 或 external-suite PASS claim。
- Projection consumer wording 可能漂移到 v0.8 application readiness。
- Report semantics 可能允许 private details 进入 future evidence。
- Later checker 可能把 `blocked`、`skipped` 或 `out_of_scope` 误认为 `pass`。

Test plan uses documentation checks、scope guards、forbidden-content sentinels 和 subagent review to
catch these risks。
