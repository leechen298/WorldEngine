# Plan

英文版本：`plan.md`

## Stage 1: Documentation Package

- 阅读 repository guidance、project direction docs、iteration standard、v0.2
  index、v0.2 plan、templates 和相邻 package docs。
- 将 package 分类为 documentation-only。
- 起草英文和中文 package docs。
- 将 package README 和 milestone status 设置为 `ready for review`。
- 运行 documentation-stage checks。
- 在 review docs 中记录 documentation-stage evidence。

## Stage 2: After Documentation Review Approval

- 阅读 implementation maps、architecture docs、API docs、v0.2 evidence and
  boundary docs、completed package reviews 和 findings。
- 创建 `docs/legacy-boundary.md` 和 `.zh.md`。
- 创建 `docs/iterations/v0.2/compatibility-review.md` 和 `.zh.md`。
- 更新 `docs/iterations/v0.2/findings.md`，记录 unresolved compatibility issues
  或 handoff risks。
- 运行 documentation checks、path checks、status checks 和 anchor sweep。
- 更新 package review docs，记录 changed files、commands、results、
  compatibility review、scope review 和 unresolved findings。

## Review Gate

Planned documentation deliverables 的 implementation 必须等待本 package 通过评审。
不要把本 package 标记为 `ready for implementation`；这个 documentation-only
package 只会在 documentation review 和允许的 docs implementation 完成后进入 review
completion。

## Stop Conditions

- 请求的变更需要 runtime、schema、API、frontend、fixture、migration 或 test
  implementation edits。
- Compatibility review 需要断言既没有文档证据也没有当前 session 验证的行为。
- 将 concrete external-world anchor 添加到 active docs。
- 无法保持英文和中文镜像同步。
