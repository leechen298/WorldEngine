# 测试计划

## 需要运行的精确命令

```bash
git status --short --branch
```

预期结果：changed/untracked files 仅限授权的 `docs/iterations/v0.8/**` documentation
surfaces。

```bash
git diff --check
```

预期结果：退出码 `0`，无输出。

```bash
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.8/0.8.1-minimum-working-state-contract")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_child_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

预期结果：`missing_child_docs=0`。

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

预期结果：`status_check_failures=0`。

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

预期结果：`out_of_scope_changed_or_untracked=0`。

```bash
python3 -c '<v0.8 markdown shape and authorization/claim guards>'
```

预期结果：无 trailing whitespace、无 tabs、无 unauthorized implementation/evidence execution，且无
unverified positive PASS claims。

## 未运行命令及原因

Backend、frontend、API、E2E、Agent smoke、autonomous、external validation 和 runtime
tests 未运行，因为本 package 是 documentation-only，且不授权 implementation 或 evidence
execution。

## Blocker 记录规则

任何 failed documentation check、missing mirror、out-of-scope changed file、positive
readiness overclaim 或 evaluator P1/P2，都必须在 `review.md` 中记录为 blocker。

## 未验证声明规则

本 package 只能声明当前 session 实际运行的 documentation checks。不得声明 minimum
working-state、runtime、API、frontend、E2E、Agent、autonomous、external validation、product、
projection 或 release pass。
