# 执行计划

状态：planned / ready for review

## 文件

创建：

- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/README.zh.md`
- `docs/iterations/v0.5/v0.5-plan.md`
- `docs/iterations/v0.5/v0.5-plan.zh.md`
- `docs/iterations/v0.5/GOAL_RUNNER.md`
- `docs/iterations/v0.5/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.5/CURRENT_STATE.md`
- `docs/iterations/v0.5/CURRENT_STATE.zh.md`
- `docs/iterations/v0.5/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.5/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.5/review.md`
- `docs/iterations/v0.5/review.zh.md`
- `docs/iterations/v0.5/0.5.0-v0.5-planning-and-continuity-boundary-baseline/`
  下所有 required docs 和 mirrors

不得触碰：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- `tools/**`
- `test-results/**`
- `docs/testing/**`
- migrations
- external repositories
- generated result artifacts

## 步骤

1. 用 `git status --short --branch` 确认当前 branch 和 working tree。
2. 确认不存在既有 `docs/iterations/v0.5/` package。
3. 创建 v0.5 parent campaign documents 和中文镜像。
4. 创建 `0.5.0` child package documents 和中文镜像。
5. 写入 capability boundary split：
   - working memory：现在只做 contract，后续作为第一批 implementation candidate。
   - episodic memory：现在只做 contract，后续作为第一批 implementation candidate。
   - relationship state：behavior 前只做 contract/schema semantics。
   - self-summary：summarization 前只做 contract/schema semantics。
   - reflection records：automatic reflection 前只做 contract/schema semantics。
   - personality drift signals：action modifiers 前只做 contract/schema semantics。
6. 在 parent 和 child reviews 中记录 subagent/evaluator findings。
7. 运行 `test-plan.md` 列出的 documentation checks。
8. 用精确 command results 更新 `review.md` 和 `review.zh.md`。
9. 停在 documentation-stage ready-for-review state。

## 停止条件

遇到以下情况时停止并记录 blocker：

- 缺少任何 required parent 或 child doc。
- 缺少任何中文镜像。
- 任何 changed file 出现在 `docs/iterations/v0.5/**` 之外。
- 需要把 implementation authorization 改成 `yes`。
- 需要修改 runtime、schema、API、frontend、backend test、fixture、migration、
  generated result、external repository 或 `backend/worldengine/` files。
- v0.4 evidence 被当作当前 v0.5 pass evidence。

## 验证

运行：

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; parent=Path('docs/iterations/v0.5'); child=parent/'0.5.0-v0.5-planning-and-continuity-boundary-baseline'; parent_docs=['README','v0.5-plan','GOAL_RUNNER','CURRENT_STATE','CAMPAIGN_PLAN','review']; child_docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[]; missing += [str(parent/(name+suffix)) for name in parent_docs for suffix in ('.md','.zh.md') if not (parent/(name+suffix)).exists()]; missing += [str(child/(name+suffix)) for name in child_docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed='docs/iterations/v0.5/'; out=subprocess.check_output(['git','status','--short'], text=True); bad=[]; [bad.append(line) for line in out.splitlines() if line and not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

## 审核更新步骤

Verification 后，同时更新 parent 和 child 的 `review.md` 与 `.zh.md`：

- exact changed files。
- commands run 和 results。
- not-run implementation checks 和 rationale。
- compatibility review。
- scope review。
- subagent/evaluator findings。
- unresolved P1/P2/P3。
- final assessment。

