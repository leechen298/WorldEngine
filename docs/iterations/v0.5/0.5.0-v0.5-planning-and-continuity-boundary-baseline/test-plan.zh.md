# 测试计划

状态：planned / ready for review

## 文档检查

从仓库根目录运行：

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; parent=Path('docs/iterations/v0.5'); child=parent/'0.5.0-v0.5-planning-and-continuity-boundary-baseline'; parent_docs=['README','v0.5-plan','GOAL_RUNNER','CURRENT_STATE','CAMPAIGN_PLAN','review']; child_docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[]; missing += [str(parent/(name+suffix)) for name in parent_docs for suffix in ('.md','.zh.md') if not (parent/(name+suffix)).exists()]; missing += [str(child/(name+suffix)) for name in child_docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed='docs/iterations/v0.5/'; out=subprocess.check_output(['git','status','--short'], text=True); bad=[]; [bad.append(line) for line in out.splitlines() if line and not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

预期结果：

- `git status --short --branch` 只显示本 package 的 v0.5 documentation files。
- `git diff --check` exit 0。
- Required docs and mirrors check 输出 `missing=0`。
- Scope guard 输出 `out_of_scope=0`。

## 回归测试

`0.5.0` 不需要运行 backend、frontend、API、E2E、runtime、Agent smoke、
autonomous validation、build、fixture、migration 或 external validation regression
commands，因为本 package 是 documentation-only，且不得改变 implementation surfaces。

## 接受标准

- 所有必需 v0.5 parent 和 child docs 均存在，并有中文镜像。
- `review.md` 记录 changed files、commands、not-run implementation checks、
  compatibility review、scope review、subagent/evaluator findings 和 unresolved
  findings。
- Implementation authorization 保持 `no`。
- Changed file 不出现在 `docs/iterations/v0.5/**` 之外。
- 没有 unresolved P1/P2 finding。

## 阻塞记录规则

如果任何 documentation check 失败，在 `review.md` 中记录 exact failure，在 docs-only
scope 内修复，并在声明 package ready for review 前重跑失败检查。

如果 scope guard 中出现任何 implementation file，必须停止，直到 file set 与 package
contract 对齐。

## 未运行

以下 checks 有意不运行：

- backend tests
- frontend tests
- E2E tests
- runtime/API smoke tests
- Agent smoke checks
- autonomous validation checks
- builds
- fixture validation
- migrations
- external validation runners

原因：`0.5.0` 是 documentation-only，不修改 implementation、runtime、API、frontend、
fixture、migration 或 validation-runner surfaces。

