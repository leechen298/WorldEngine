# 评审

状态：ready for review（待评审）

## 变更文件

创建的父级文件：

- `docs/iterations/v0.4/README.md`
- `docs/iterations/v0.4/README.zh.md`
- `docs/iterations/v0.4/v0.4-plan.md`
- `docs/iterations/v0.4/v0.4-plan.zh.md`
- `docs/iterations/v0.4/GOAL_RUNNER.md`
- `docs/iterations/v0.4/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.4/CURRENT_STATE.md`
- `docs/iterations/v0.4/CURRENT_STATE.zh.md`
- `docs/iterations/v0.4/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.4/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.4/review.md`
- `docs/iterations/v0.4/review.zh.md`

创建的 child package 文件：

- `docs/iterations/v0.4/0.4.0-v0.4-planning-and-compatibility-baseline/{README,intent,contract,technical-design,test-plan,plan,review}.md` 及 `.zh.md` 镜像
- `docs/iterations/v0.4/0.4.1-agent-in-world-loop-contract/{README,intent,contract,technical-design,test-plan,plan,review}.md` 及 `.zh.md` 镜像
- `docs/iterations/v0.4/0.4.2-agent-perception-and-schemas/{README,intent,contract,technical-design,test-plan,plan,review}.md` 及 `.zh.md` 镜像
- `docs/iterations/v0.4/0.4.3-action-intent-validation-and-result-adapter/{README,intent,contract,technical-design,test-plan,plan,review}.md` 及 `.zh.md` 镜像
- `docs/iterations/v0.4/0.4.4-minimal-agent-loop-orchestration-and-api/{README,intent,contract,technical-design,test-plan,plan,review}.md` 及 `.zh.md` 镜像
- `docs/iterations/v0.4/0.4.5-agent-loop-evidence-and-compatibility-audit/{README,intent,contract,technical-design,test-plan,plan,review}.md` 及 `.zh.md` 镜像
- `docs/iterations/v0.4/0.4.6-v0.4-release-candidate-bundle/{README,intent,contract,technical-design,test-plan,plan,review}.md` 及 `.zh.md` 镜像
- `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/{README,intent,contract,technical-design,test-plan,plan,review}.md` 及 `.zh.md` 镜像

## 已读文件

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.3-post-closeout/GOAL_RUNNER.md`
- `docs/iterations/v0.3-post-closeout/CURRENT_STATE.md`
- `docs/iterations/v0.3-post-closeout/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.3-post-closeout/05-final-validation-bundle/final-validation-bundle.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `backend/app/schemas/agent.py`
- `backend/app/core/runtime_context.py`

## 已运行命令

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; bad=[]
for path in Path('docs/iterations/v0.4').rglob('*.md'):
    for idx,line in enumerate(path.read_text().splitlines(True),1):
        body=line.rstrip('\n\r')
        if body.rstrip(' \t') != body:
            bad.append(f'{path}:{idx}')
print('trailing_whitespace_findings=' + str(len(bad)))
[print(x) for x in bad]
raise SystemExit(1 if bad else 0)"
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.4'); parents=['README.md','README.zh.md','v0.4-plan.md','v0.4-plan.zh.md','GOAL_RUNNER.md','GOAL_RUNNER.zh.md','CURRENT_STATE.md','CURRENT_STATE.zh.md','CAMPAIGN_PLAN.md','CAMPAIGN_PLAN.zh.md','review.md','review.zh.md']; packages=['0.4.0-v0.4-planning-and-compatibility-baseline','0.4.1-agent-in-world-loop-contract','0.4.2-agent-perception-and-schemas','0.4.3-action-intent-validation-and-result-adapter','0.4.4-minimal-agent-loop-orchestration-and-api','0.4.5-agent-loop-evidence-and-compatibility-audit','0.4.6-v0.4-release-candidate-bundle','0.4.7-v0.4-final-closeout']; docs=['README.md','intent.md','contract.md','technical-design.md','test-plan.md','plan.md','review.md']; expected=[base/p for p in parents]; expected += [base/pkg/doc for pkg in packages for doc in docs]; expected += [base/pkg/(doc[:-3]+'.zh.md') for pkg in packages for doc in docs]; missing=[str(p) for p in expected if not p.exists()]; file_count=sum(1 for p in base.rglob('*') if p.is_file()); print('file_count=' + str(file_count)); print('missing=' + str(len(missing))); [print(x) for x in missing]; raise SystemExit(1 if missing or file_count != 124 else 0)"
python3 -c "from pathlib import Path; text='\n'.join(p.read_text() for p in Path('docs/iterations/v0.4').rglob('*.md')); terms=['完成 v0.4','Active child package','active child','implementation_authorized','subagent','evaluator','P1','P2','P3','Stop Conditions','停止条件']; missing=[term for term in terms if term not in text]; print('route_terms_missing=' + str(len(missing))); [print(x) for x in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess,sys; out=subprocess.check_output(['git','status','--porcelain=v1','-uall'],text=True); bad=[]; [bad.append(line) for line in out.splitlines() if not line[3:].startswith('docs/iterations/v0.4/')]; print('out_of_scope=' + str(len(bad))); [print(x) for x in bad]; sys.exit(1 if bad else 0)"
python3 -c "from pathlib import Path; terms=('TBD','TODO','PLACEHOLDER','Pending until verification','not yet','to be filled'); bad=[]; base=Path('docs/iterations/v0.4')
for path in base.rglob('*.md'):
    in_code=False
    for idx,line in enumerate(path.read_text().splitlines(),1):
        if line.strip().startswith(chr(96)*3):
            in_code = not in_code
            continue
        if in_code:
            continue
        if any(term in line for term in terms):
            bad.append(f'{path}:{idx}:{line}')
print('placeholder_findings=' + str(len(bad)))
[print(x) for x in bad]
raise SystemExit(1 if bad else 0)"
rg -n '^# (Contract|Intent|Technical Design|Test Plan|Plan|Review)$|^## (Public Concepts|Allowed Changes|Forbidden Changes|Compatibility Requirements|Implementation Authorization|Out-of-Scope Follow-ups|Changed Files|Commands Run|Test Results|Compatibility Review|Scope Review|Final Assessment)$' docs/iterations/v0.4 -g '*.zh.md'
rg -n '状态：待评审$|Campaign status：文档待评审$|Status: 待评审$' docs/iterations/v0.4 -g '*.zh.md'
rg -n 'concrete demo-world|memory/self-continuity|self-continuity|world generation|external validation runner|backend/worldengine/' docs/iterations/v0.4
```

## 测试结果

- `git status --short --branch` 显示分支为 `v0.4...origin/v0.4`，且只有未跟踪目录 `docs/iterations/v0.4/`。
- `git diff --check` 退出 `0`；未报告空白错误。
- 对 `docs/iterations/v0.4/*.md` 的直接行尾空白扫描退出 `0`；`trailing_whitespace_findings=0`。
- 文件存在性检查退出 `0`；`file_count=124` 且 `missing=0`。
- route/status term check 退出 `0`；`route_terms_missing=0`。
- changed-file scope guard 退出 `0`；`out_of_scope=0`，当前改动仅限 `docs/iterations/v0.4/**`。
- 占位符扫描退出 `0`；`placeholder_findings=0`。
- 中文镜像标题扫描退出 `1` 且无输出，通用 review heading 已本地化。
- 中文状态漂移扫描退出 `1` 且无输出，没有仅本地化、缺少 canonical status 的状态字面量。
- 禁止范围词扫描只发现边界/禁止范围引用和命令证据行，没有实现声明或实现文件变更。
- 本轮是 documentation-only 创建，没有修改实现文件，因此未运行 backend、frontend、API smoke、E2E、Agent smoke、runtime behavior、build、schema execution、fixture、migration 或 test implementation 命令。

## 兼容性评审

本轮仅修改文档。runtime behavior、schema behavior、API behavior、frontend behavior、fixture behavior、migration behavior、Event.refs behavior、WorldSpec loader behavior、runtime context bridge behavior、既有 ParamsAgent behavior 和 legacy `backend/worldengine/` behavior 保持不变。

## 范围评审

变更预期只位于 `docs/iterations/v0.4/**`。本轮只创建 v0.4 planning 和 campaign 文档，不授权实现；带实现 child package 必须通过自己的 review gates。

## Subagent / Evaluator Checkpoint

本轮文档创建定义 goal routing、package sequencing、evidence rules、automation-consumption contracts 和英文/中文镜像义务，因此需要 read-only evaluator review。

Evaluator 结果：

- Scope / goal-runner evaluator：未发现 P1 或 P2。曾发现一项 P3，即本文件在更新前仍有 stale pending review evidence；本次 review 更新已修复。
- Mirror / automation-consumption evaluator：未发现 P1。曾发现两项 P2：stale pending review evidence 与中文状态 literal 不一致；本次 review 更新均已修复。曾发现一项 P3：中文镜像有机械英文标题；本次已翻译通用中文标题。

## 外部审核跟进

来源：用户粘贴的 ChatGPT audit，发生在 commit `a08eec7` 之后。

本次跟进修改文件：

- `README.md`
- `README.zh.md`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`
- `docs/iterations/v0.4/README.md`
- `docs/iterations/v0.4/README.zh.md`
- `docs/iterations/v0.4/review.md`
- `docs/iterations/v0.4/review.zh.md`

已处理 findings：

- P2：根 README 状态现在说明 `v0.4` 分支处于 planning ready for review，当前已实现能力仍是 v0.3 final / closeout complete。
- P2：roadmap v0.4 小节现在记录 `Status: planned / ready for review`。
- P3：v0.4 README 的包索引改为按包分节，不再使用过宽 Markdown 表格。
- P3：v0.4 中文 README 和 roadmap 的普通说明已做中文 polish，同时保留 canonical status literal、路径和契约术语。

本次跟进运行命令：

```bash
git status --short --branch
git diff --check
rg -n 'current `v0\.3` branch|当前 `v0\.3` 分支|Status: v0\.3 final|状态：`v0\.3 final' README.md README.zh.md
rg -n -A2 '## v0\.4 - Agent-in-World Minimal Loop' docs/roadmap.md docs/roadmap.zh.md
rg -n '^\| Package \||^\| 包 \|' docs/iterations/v0.4/README.md docs/iterations/v0.4/README.zh.md
rg -n 'deliverables|compatibility constraints|handoff rules|request-driven loop orchestration|child sequence' docs/iterations/v0.4/README.zh.md docs/roadmap.zh.md
python3 -c "import subprocess,sys; allowed={'README.md','README.zh.md','docs/roadmap.md','docs/roadmap.zh.md','docs/iterations/v0.4/README.md','docs/iterations/v0.4/README.zh.md','docs/iterations/v0.4/review.md','docs/iterations/v0.4/review.zh.md'}; out=subprocess.check_output(['git','diff','--name-only'],text=True).splitlines(); bad=[p for p in out if p not in allowed]; print('changed_files=' + str(len(out))); print('out_of_scope=' + str(len(bad))); [print(x) for x in bad]; sys.exit(1 if bad else 0)"
```

本次跟进结果：

- `git diff --check` 退出 `0`。
- changed-file scope guard 退出 `0`；`changed_files=8` 且 `out_of_scope=0`。
- 根 README stale status 扫描退出 `1` 且无输出。
- roadmap v0.4 status 扫描退出 `0`，英文和中文 roadmap 都包含新的 v0.4 状态。
- 包索引表格扫描退出 `1` 且无输出，package index 已改为分节。
- 中文措辞扫描退出 `1` 且无输出，审核指出的混排短语已处理。
- 本次跟进是 documentation-only，未修改实现文件，因此未运行 backend、frontend、API smoke、E2E、Agent smoke、runtime behavior、build、schema execution、fixture、migration 或 test implementation 命令。

## 未解决 P1/P2/P3

- P1：未发现。
- P2：review evidence 和中文状态修复后未发现。
- P3：v0.4 implementation evidence 尚未执行。target_package：`0.4.2-agent-perception-and-schemas`。defer_reason：implementation 只能在 contract/design/test-plan review 后启动。

## 最终评估

ready for review
