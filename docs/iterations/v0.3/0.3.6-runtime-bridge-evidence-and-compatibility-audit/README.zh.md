# 0.3.6 运行时桥接证据与兼容性审计

状态：`review complete`

类型：仅文档

## 目标

在准备发布候选包之前，审计 v0.3 加载器、运行时桥接、外部样例契约准备和兼容性证据。

## 范围

本包只新增证据和兼容性审计文档。它不修改运行时、schema、API、前端、样例、
迁移、测试实现或旧运行时代码文件。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

包含 `technical-design.md` 和 `test-plan.md`，因为本审计会准备发布候选证据和
v0.4 交接标准。

## 交付物

- `docs/iterations/v0.3/evidence-index.md`
- `docs/iterations/v0.3/evidence-index.zh.md`
- `docs/iterations/v0.3/compatibility-audit.md`
- `docs/iterations/v0.3/compatibility-audit.zh.md`
- `docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/**`
- 本包文档对应的 `*.zh.md` 镜像。

## 状态清单

- [x] 文档已起草
- [x] 契约已评审
- [x] 技术设计已评审
- [x] 测试计划已评审
- [ ] 实现完成
- [x] 文档证据完成
- [x] 评审完成

## 交接

本包评审后，0.3.7 可以准备 v0.3 发布候选包。本包不能标记为
`ready for implementation`，因为它只执行文档审计。
