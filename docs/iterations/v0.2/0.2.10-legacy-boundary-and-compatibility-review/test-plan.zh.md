# Test Plan

英文版本：`test-plan.md`

## 文档检查

- 验证 package 拥有所有必需的英文和中文镜像文档。
- 验证 package README status 为 `ready for review`。
- 验证 v0.2 milestone index 将 0.2.10 记录为 `ready for review`。
- 验证 v0.2 plan 将 0.2.10 记录为 `ready for review`。
- 验证 Markdown diff 没有 whitespace errors。
- 验证 changed-file set 只包含允许的 documentation paths。
- 评审后 implementation 阶段，验证 planned legacy boundary 和 compatibility
  review docs 存在英文和中文镜像。

## 评审后的兼容性检查

- 对照 repository paths 和 current implementation docs 确认 active backend 与
  dashboard path claims。
- 确认 `backend/worldengine/` 被记录为 legacy，且没有被描述为 active runtime
  behavior。
- 确认 v0.1 runtime scaffold compatibility claims 引用 current implementation
  docs、backend implementation docs、API docs、package reviews 或 current-session
  verification。
- 确认 v0.2 schema 和 event contract claims 保持 additive，且未被描述为 runtime
  loading behavior。
- 确认 v0.3 handoff constraints 明确覆盖 loader、runtime bridge、API
  compatibility、event compatibility、frontend compatibility 和 legacy path
  handling。
- 检查英文和中文 v0.2 index 与 plan documents 的 status consistency。
- 使用 temporary untracked pattern file 对 active direction 和 touched docs 运行
  concrete demo anchor sweep。

## 命令

Documentation-stage checks:

```bash
git status --short --branch
git diff --check
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/$f.md" && test -f "docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/$f.zh.md" || exit 1; done
rg -n '0\.2\.10-legacy-boundary-and-compatibility-review|Status: ready for review|状态：`ready for review`' docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/README.md docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/README.zh.md
git diff --name-only
```

Implementation-stage documentation checks:

```bash
git status --short --branch
git diff --check
test -f docs/legacy-boundary.md
test -f docs/legacy-boundary.zh.md
test -f docs/iterations/v0.2/compatibility-review.md
test -f docs/iterations/v0.2/compatibility-review.zh.md
rg -n 'backend/app|frontend|backend/worldengine|legacy|active|v0\.3' docs/legacy-boundary.md
rg -n 'runtime|API|frontend|schema|event|WorldSpec|compatibility|handoff' docs/iterations/v0.2/compatibility-review.md
git diff --name-only | rg -v '^(docs/legacy-boundary|docs/iterations/v0.2/)'
```

Concrete demo anchor sweep:

使用 `/tmp` 或其他 untracked path 下的 temporary untracked pattern file。对 active
direction docs、legacy boundary docs、compatibility review docs 和 touched
package docs 运行 sweep。只记录抽象匹配类别；不要把 concrete pattern lists 写入
tracked documentation。

## 验收标准

- Documentation-stage package 在 boundary/review implementation 开始前已完整并
  ready for review。
- Acceptance 和 verification requirements 具体且有命令支撑。
- Assumptions 和 open risks 已记录。
- Package 保持 documentation-only。
- Legacy boundary 和 compatibility review implementation 产出英文和中文镜像。
- Missing evidence 或 compatibility concerns 被记录为 findings，而不是代码变更。
- Review evidence 记录 changed files、commands、results、compatibility review、
  scope review 和 unresolved findings。

## 未运行

本 documentation-stage pass 不需要 backend 和 frontend tests。由于本 package 禁止
runtime、schema、API、frontend、fixture、migration 和 test implementation changes，
boundary/review implementation 期间也不预期运行这些测试。
