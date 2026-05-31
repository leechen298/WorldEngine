# 测试计划

状态：final / closeout complete

## 文档与范围检查

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; parent=Path('docs/iterations/v0.6'); parent_docs=['README','v0.6-plan','GOAL_RUNNER','CURRENT_STATE','CAMPAIGN_PLAN','review']; child_docs=['README','intent','contract','technical-design','test-plan','plan','review']; child_extra={'0.6.10-v0.6-final-closeout':['final-closeout']}; missing=[]; missing += [str(parent/(name+suffix)) for name in parent_docs for suffix in ('.md','.zh.md') if not (parent/(name+suffix)).exists()];
for child in [p for p in parent.iterdir() if p.is_dir() and p.name.startswith('0.6.')]:
    docs=child_docs + child_extra.get(child.name, [])
    missing += [str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]
print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
python3 -c "import subprocess,sys; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('README.md','README.zh.md','docs/iterations/v0.6/','docs/roadmap.md','docs/roadmap.zh.md','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_generation_regeneration_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','frontend/src/api/client.ts','frontend/src/api/client.test.ts','frontend/src/components/GenerationPanel.vue','frontend/src/components/GenerationPanel.test.ts','frontend/src/pages/DashboardPage.vue','frontend/src/pages/DashboardPage.test.ts','frontend/src/style.css','frontend/e2e/dashboard-generation.spec.ts'); bad=[line for line in lines if not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); print('\n'.join(bad)); sys.exit(1 if bad else 0)"
```

```bash
git status --short -- backend/worldengine backend/app/alembic backend/migrations
```

## 最终运行时验证

```bash
cd backend && PYTHONPATH=. .venv/bin/pytest app/tests -q
```

```bash
cd frontend && pnpm test
```

```bash
cd frontend && pnpm build
```

```bash
make test-e2e
```

## 状态一致性

Final sync 前，current status 应指向 `0.6.10 ready for review`。Final sync 后，
current parent status、package status、review、final-closeout record 和 roadmap
status 应一致为 `final / closeout complete`。

## 评审门禁

必须由 closeout consistency evaluator 评审 final evidence 和 status synchronization，
v0.6 才能视为 complete。
