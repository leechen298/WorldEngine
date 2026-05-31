# 测试计划

Status: review complete

## 文档检查

运行：

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics'); required=['WorldGenerationRequest','WorldTemplate','GenerationPlan','GeneratedWorldSpec','GenerationMetadata','GenerationPreview','RegenerationRequest','diagnostics','implementation_authorized: no']; bad=[]; text='\\n'.join(path.read_text() for path in child.glob('*.md')); [bad.append(term) for term in required if term not in text]; print('missing_required_terms=' + str(len(bad))); [print(term) for term in bad]; raise SystemExit(1 if bad else 0)"
python3 -c "import subprocess; allowed_prefixes=('docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/',); lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[]; [bad.append(line) for line in lines if line and not line[3:].startswith(allowed_prefixes)]; print('unexpected_status=' + str(len(bad))); [print(item) for item in bad]; raise SystemExit(1 if bad else 0)"
```

预期：

- `git diff --check` exit `0`。
- required docs/mirrors check 输出 `missing=0`。
- required term check 输出 `missing_required_terms=0`。
- 在更新 parent status files 前，scope guard 输出 `unexpected_status=0`。

更新 parent status files 后，用 `docs/iterations/v0.6/` 作为 allowed prefix 重新运行
scope guard，并预期 `unexpected_status=0`。

## 镜像质量检查

运行：

```bash
python3 -c 'from pathlib import Path
import re
bad=[]
for path in Path("docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics").glob("*.zh.md"):
    in_fence=False
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        if line.startswith("```"):
            in_fence=not in_fence
            continue
        if in_fence or not line.startswith("#"):
            continue
        text=line.lstrip("#").strip()
        has_latin=bool(re.search(r"[A-Za-z]", text))
        has_cjk=bool(re.search(r"[\u4e00-\u9fff]", text))
        code_like=text.startswith("`") or text.startswith("0.6.") or "`" in text
        if has_latin and not has_cjk and not code_like:
            bad.append(f"{path}:{lineno}:{line}")
print("generic_english_only_headings=" + str(len(bad)))
for item in bad:
    print(item)
raise SystemExit(1 if bad else 0)'
```

预期：`generic_english_only_headings=0`。

## 状态一致性检查

记录 evaluator evidence 并更新 parent status files 后，搜索 reviewed handoff：

```bash
rg -n "0\\.6\\.1-world-generation-contracts-and-template-semantics: review complete|0\\.6\\.2-template-catalog-and-deterministic-generator-core|implementation_authorized: no" docs/iterations/v0.6
```

预期：status surface 对 active 或 next child 的表述一致，implementation
authorization 保持 closed。

## 未运行命令

Backend、frontend、API、E2E、runtime、Agent smoke、autonomous validation、build、
fixture、migration 和 external validation 命令不会为 `0.6.1` 运行，因为本 package
是 documentation-only，且不修改 implementation surface。

## Blocker 记录规则

如果文档检查失败，在 `review.md` 记录准确 command、exit status 和 failure
summary。在失败被修复或明确分类前，不得将本 package 标记为 review complete。

如果 documentation evaluator 不可用或报告阻塞性 P1/P2，则保持
`planned / ready for review`，或记录 blocker。不得标记 `implementation_authorized:
yes`。

## 不做未验证声明

只有当前 session 实际运行的命令才能记录为 passed。除非相关 command 或 flow 已实际
运行且属于当前范围，否则不得把 backend、frontend、API、E2E、runtime、Agent
smoke、autonomous、build、release、product-readiness 或 generated-world quality
claim 记录为 passed。
