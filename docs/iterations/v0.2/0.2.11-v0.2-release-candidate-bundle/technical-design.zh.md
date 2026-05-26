# Technical Design

英文版本：`technical-design.md`

## 设计摘要

0.2.11 是 documentation assembly package。它通过读取已有 v0.2 evidence、给每个
claim 分类，并发布 review handoff 来创建 release-candidate bundle。它不新增
implementation behavior。

## 输入来源

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- 0.2.1 到 0.2.10 的 completed v0.2 package reviews。
- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/findings.md`
- `docs/releases/v0.2.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/legacy-boundary.md`

存在 Chinese mirrors 时，必须用于同步 `.zh.md` outputs。

## 输出结构

### Release-Candidate Bundle

`docs/iterations/v0.2/v0.2-release-candidate-bundle.md` 必须包含：

- release-candidate status 和明确的 not-final warning。
- v0.2 scope summary。
- completed package table。
- claim-to-evidence matrix。
- test and verification evidence summary。
- compatibility and boundary summary。
- known limitations and non-goals。
- unresolved findings and blocker classification。
- final-closeout prerequisites。
- human / ChatGPT review request。

`.zh.md` mirror 必须保留相同 headings 和 decisions。

### Final Review Bundle

`final-review-bundle.md` 必须遵循
`docs/iterations/v0.2/final-review-bundle-template.md`，并用 0.2.11-specific
evidence 填写每一节。它必须包含 branch、status、changed files、contract
mapping、forbidden-change confirmation、commands run、test results、grep
classification、unresolved findings、compatibility review、scope review 和
requested reviewer decision。

`.zh.md` mirror 必须保留相同 review information。

### Release Draft Update

`docs/releases/v0.2.md` 必须保持 release draft，同时增加 release-candidate
evidence summary。它必须说明 final release 仍被 0.2.12 approval 阻塞。

`.zh.md` mirror 必须保持同步。

## Claim 分类

每个 claim 必须使用以下一个或多个状态：

- `implemented`
- `documented`
- `tested`
- `reviewed`
- `planned`
- `not implemented`
- `historical artifact`
- `finding`

如果 claim 无法映射到 evidence，应记录为 finding，而不是把 claim 改写成看似完成。

## Findings 处理

使用 `docs/iterations/v0.2/findings.md` 记录 unresolved 或 newly discovered risks：

- P1：阻塞 release-candidate acceptance 和 final closeout。
- P2：阻塞 final closeout，除非被 review explicitly accepted。
- P3：如果已文档化且不阻塞 v0.2，可作为 v0.3 handoff。

## 状态规则

- Documentation-stage preparation 期间，本包状态为 `ready for review`。
- Release-candidate bundle 经批准 implementation 后，本包可标记为
  `review complete`。
- 本包不得把 v0.2 标记为 final。
- 缺少 release-candidate review approval 时，0.2.12 必须保持 planned。

## 双语镜像规则

每个新增或修改的 release-candidate document 都必须有英文和中文 mirror，并保持相同的
status、scope boundaries、acceptance criteria 和 findings classification。

## 安全与边界说明

bundle 不得暴露 private validation internals、concrete external world details、
private runner state 或 application-specific backend logic。它只能用 abstract
classifications 总结 anchor sweeps。
