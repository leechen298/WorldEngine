# 测试计划

状态：review complete

## 文档检查

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.9-v0.6-release-candidate-bundle'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n 'release-candidate|0\.6\.8|0\.6\.10|product readiness|external validation|projection readiness|generation quality|final release' docs/iterations/v0.6/0.6.9-v0.6-release-candidate-bundle
```

## 范围守卫

```bash
python3 -c "import subprocess,sys; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_generation_regeneration_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','frontend/src/api/client.ts','frontend/src/api/client.test.ts','frontend/src/components/GenerationPanel.vue','frontend/src/components/GenerationPanel.test.ts','frontend/src/pages/DashboardPage.vue','frontend/src/pages/DashboardPage.test.ts','frontend/src/style.css','frontend/e2e/dashboard-generation.spec.ts'); bad=[line for line in lines if not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); print('\n'.join(bad)); sys.exit(1 if bad else 0)"
```

## 状态一致性

Evaluator review 前，检查 current parent status 是否指向 `0.6.9` ready for review；
只有在本 package 标记为 review complete 后，才可以指向 `0.6.10`。

## 运行时测试

本 documentation-only package 不要求 implementation command。Runtime、frontend、E2E
和 backend regression evidence 继承自 review-complete child packages，必须明确引用，
不能声明为 `0.6.9` 新运行。

## 评审门禁

本 package 标记为 review complete 前，必须由 read-only release-candidate evaluator
评审。
