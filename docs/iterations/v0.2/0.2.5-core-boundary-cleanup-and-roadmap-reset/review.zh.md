# Review

英文版本：`review.md`

状态：`review complete`

## 变更文件

- `AGENTS.md` / `AGENTS.zh.md`：将 concrete projection wording 替换为
  external consumer boundaries，并增加 generic core scope hard rules。
- `CLAUDE.md` / `CLAUDE.zh.md`：同步 existing Claude entry files 的 agent
  guidance cleanup。
- `README.md` / `README.zh.md`：移除 concrete reference-world limitation，并说明
  external projection applications 是 consumers。
- `docs/project-north-star.md` / `.zh.md`：将 first concrete user-surface wording
  替换为 external projection application guidance。
- `docs/product-model.md` / `.zh.md`：移除 concrete product-surface wording，保留
  public consumers 表述。
- `docs/scope-boundaries.md` / `.zh.md`：增加 core-vs-external fixture 和
  validation boundaries。
- `docs/roadmap.md` / `.zh.md`：围绕 generic engine 和 external consumer
  milestones 重置 v0.2.5 到 v0.8。
- `docs/architecture.md` / `.zh.md`：用 generic schema smoke validation 替换
  concrete fixture direction。
- `docs/glossary.md` / `.zh.md`：用 external validation world 和 projection consumer
  terms 替换 concrete reference-world vocabulary。
- `docs/releases/v0.2.md` / `.zh.md`：更新 planned capability 和 non-goal wording，
  指向 generic schema smoke 和 external boundaries。
- `docs/iterations/v0.2/README.md` / `.zh.md`：将 0.2.4 标为 historical，并将
  0.2.5 标为 review complete。
- `docs/iterations/v0.2/v0.2-plan.md` / `.zh.md`：用 0.2.5 cleanup 和 0.2.6
  workflow / plan reset 替换 legacy fixture direction。
- `docs/iterations/v0.2/0.2.4-worldspec-reference-fixture/README.md` /
  `README.zh.md`：增加 historical artifact notes，明确 concrete fixture
  direction 已被 supersede。
- `docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/README.md`：
  同步 status 和 checklist 为 review complete。
- `backend/data/world_specs/historical concrete fixture path`：删除 concrete
  external-world fixture。
- `backend/app/tests/test_worldspec_fixture.py`：删除 concrete fixture test。
- `backend/app/tests/test_worldspec_schema_smoke.py`：增加 domain-neutral
  in-memory WorldSpec schema smoke tests。
- `backend/app/tests/test_world_cell_schema.py`：将 concrete invalid `kind` value
  替换为 domain-neutral invalid value。
- `docs/external-fixture-boundary.md`：增加 external fixture 和 validation
  consumer boundary guide。
- `docs/validation-report-template.md`：增加 redacted validation report template，
  使用 `redacted target id`。
- `docs/current-implementation.md` / `.zh.md`：follow-up docs polish 将 stale
  product-surface limitation 替换为 external projection application consumer wording。

## 已运行命令

```bash
git status --short --branch
sed commands for the 0.2.5 package documents
concrete demo anchor sweep using temporary untracked pattern files
git diff --check
make check-backend
cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_schema_smoke.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
git diff --name-status
git diff --stat
targeted stale-text grep
git diff --check
```

## 测试结果

- `git diff --check` 退出码为 `0`，没有 whitespace errors。
- `make check-backend` 退出码为 `0`，backend virtual environment 存在。
- focused schema smoke pytest 退出码为 `0`，结果为 `4 passed in 0.08s`。
- broader backend pytest 退出码为 `0`，结果为 `91 passed in 0.94s`。
- 未运行 frontend tests，因为本 package 未修改 frontend files，且 contract 禁止
  frontend dashboard changes。
- follow-up docs polish：`git diff --check` 退出码为 `0`；targeted stale-text
  grep 没有命中。

## grep 残留

full repository grep 仍报告以下允许残留分类：

- `frontend/pnpm-lock.yaml` 中的 dependency false positives。
- historical release artifacts。
- historical iteration artifacts 和 review evidence。
- 0.2.5 cleanup-scope mentions。

targeted active-docs/tests/fixtures grep 已确认 active docs、active tests 和 active
fixtures 不再保留 concrete Demo-world semantic anchors。

## 兼容性审核

generic schema contracts 已保留。`WorldCell`、`WorldSpec`、`EntityRef` 和
`EventRef` 未被删除或收窄。runtime behavior、API routes、API response shapes、
production event log storage、frontend dashboard behavior 和 `backend/worldengine/`
behavior 均未改变。

test cleanup 移除 concrete fixture data，并用 in-memory、domain-neutral schema smoke
coverage 替换 concrete fixture assertions。未增加 production WorldSpec loader。

## 范围审核

implementation 保持在 0.2.5 contract 内：

- 清理 active documentation anchors。
- 重置 active roadmap language。
- 将 0.2.4 标记为 historical。
- 删除 concrete fixture data。
- 用 generic schema smoke tests 替换 concrete fixture tests。
- 增加 external fixture 和 redacted validation report docs。
- 更新 review evidence。

未引入 external fixture repository、external validation repository、loader、runtime
bridge、Agent loop、memory/self-continuity implementation、world generation、
frontend work、API work、event storage change、generic schema deletion 或 new
concrete world。

## 未解决发现

- P1：none。
- P2：none。follow-up docs polish 已解决 stale `docs/current-implementation*`
  wording 和 0.2.5 README planning-pass wording。
- P3：none。

## 最终评估

0.2.5 implementation is review complete。WorldEngine core repository 在 current
docs、tests 和 fixtures 中不再保留 active concrete Demo-world anchors；roadmap 已围绕
generic engine 和 external consumer milestones 重置；focused 和 full backend tests
在当前 session 通过。
