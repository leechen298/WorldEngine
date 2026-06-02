# Technical Design

## 文档结构

本 package 是 documentation-only，但仍包含 `technical-design.md` 和 `test-plan.md`，因为它定义
observable surface semantics、evidence rules、compatibility rules，以及后续 implementation
authorization criteria。

## 受影响文件

允许文件：

- 本 package 的七个英文文档和七个中文镜像。
- parent v0.8 route/status files。

不影响 runtime、schema、API、frontend、backend test、checker implementation、fixture、
migration、generated result、external repository 或 legacy implementation file。

## Surface 设计

本 package 按 family 组织 observable surfaces，而不是按 endpoint implementation 组织。后续
package 可以把某个 family 映射到一个或多个 API routes、schemas、reports、manifests 或
evidence bundles，但本 package 不创建这些 artifacts。

Surface families 必须遵守：

- 默认 read-only。
- 不包含 hidden reset 或 private runner hooks。
- 不包含 concrete external validation content。
- 只允许 bounded memory summaries。
- 使用 `0.8.1` 的 status taxonomy。
- 与 v0.7 redaction 和 read-model rules 兼容。

## 兼容策略

- 复用 v0.7 projection 和 external-validation contracts 作为 redaction baseline。
- 复用 `docs/current-implementation.md` 和现有 API references 作为 source maps，而不是新的 pass
  evidence。
- 保持所有当前 backend/frontend behavior unchanged。
- 将 implementation 和 focused tests 延后到后续 reviewed packages。

## 防漂移规则

- Surface family 不是已实现 API。
- Read-model contract 不是 projection application readiness。
- Observable boundary 不是 minimum working-state evidence。
- External validation handoff 不是 external validation PASS。
- Bounded memory context 不是 raw memory export。
