# Test Plan

英文版本：`test-plan.md`

## Documentation Checks

- 验证 package 拥有全部 required English 和 Chinese mirror documents。
- 验证 package README status 是 `ready for review`。
- 验证 v0.2 milestone index 将 0.2.9 记录为 `ready for review`。
- 验证 v0.2 plan 将 0.2.9 记录为 `ready for review`。
- 验证 Markdown diffs 没有 whitespace errors。
- 验证 changed-file set 只包含 approved documentation paths。
- Audit implementation 后，验证 planned evidence index 和 boundary audit 都有
  English / Chinese mirrors。

## Review 后的 Audit Checks

- 将 milestone index、plan、roadmap 和 scope boundary docs 中的 active v0.2
  claims 映射到 evidence rows。
- 确认 schema claims 引用 EntityRef、WorldCell、WorldSpec contracts 和 package
  review evidence。
- 确认 event claims 引用 EventRef contract 和 package review evidence。
- 确认 external boundary claims 引用 boundary docs 和 cleanup package evidence。
- 确认 legacy boundary claims 引用 current implementation docs，并在需要时保持为
  0.2.10 handoff input。
- 检查 English 和 Chinese v0.2 index / plan documents 的 status consistency。
- 检查 deferred 0.2.7 status finding；要么用 evidence 关闭，要么保留 open 并
  更新 rationale。
- 使用 temporary untracked pattern file，对 active direction 和 audit docs 运行
  concrete demo anchor sweep。

## Commands

Documentation-stage checks：

```bash
git status --short --branch
git diff --check
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/$f.md" && test -f "docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/$f.zh.md" || exit 1; done
rg -n '0\.2\.9-generic-schema-evidence-and-boundary-audit|Status: ready for review|状态：`ready for review`' docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/README.md docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/README.zh.md
git diff --name-only
```

Implementation-stage documentation checks：

```bash
git status --short --branch
git diff --check
test -f docs/iterations/v0.2/evidence-index.md
test -f docs/iterations/v0.2/evidence-index.zh.md
test -f docs/iterations/v0.2/boundary-audit.md
test -f docs/iterations/v0.2/boundary-audit.zh.md
rg -n 'implemented|documented|tested|reviewed|planned|not implemented|historical artifact|finding' docs/iterations/v0.2/evidence-index.md
rg -n 'external|fixture|legacy|runtime|schema|event|status' docs/iterations/v0.2/boundary-audit.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
```

Concrete demo anchor sweep：

使用 `/tmp` 或其他 untracked path 下的 temporary untracked pattern file。对
active direction docs、evidence index、boundary audit 和 touched package docs 运行
sweep。只记录 abstract match categories；不要把 concrete pattern lists 写入
tracked documentation。

## 验收标准

- Documentation-stage package 在 audit implementation 开始前已 complete 且 ready
  for review。
- Acceptance 和 verification requirements 具体且有 command support。
- Assumptions 和 open risks 已记录。
- 本 package 保持 documentation-only。
- Audit implementation 产出 evidence index 和 boundary audit mirrors。
- Missing evidence 被记录为 findings，而不是 code changes。
- Review evidence 记录 changed files、commands、results、compatibility review、
  scope review 和 unresolved findings。

## Not Run

本 documentation-stage pass 不需要运行 backend 和 frontend tests。Audit
implementation 阶段也不预期运行这些 tests，因为本 package 禁止 runtime、schema、
API、frontend、fixture、migration 和 test implementation changes。
