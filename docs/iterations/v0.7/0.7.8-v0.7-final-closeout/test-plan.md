# Test Plan

## Final Verification Commands

```bash
backend/.venv/bin/python -m pytest tools/testing
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
backend/.venv/bin/python -m json.tool docs/testing/external-validation-report-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python -m json.tool docs/contracts/projection-read-model-schema.json
git diff --check
```

Run docs/evidence link checks:

```bash
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.8-v0.7-final-closeout")
names=["README","intent","contract","technical-design","test-plan","plan","review","final-closeout"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_8_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'from pathlib import Path
paths=[
 "docs/iterations/v0.7/review.md",
 "docs/testing/results/2026-06-02-v0.7-code-review.md",
 "docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/review.md",
 "docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md",
 "docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/review.md",
 "docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/review.md",
 "docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/review.md",
 "docs/iterations/v0.7/0.7.5-quality-regression-and-compatibility-evidence/review.md",
 "docs/iterations/v0.7/0.7.5-quality-regression-and-compatibility-evidence/evidence-matrix.md",
 "docs/iterations/v0.7/0.7.6-v0.7-evidence-and-compatibility-audit/review.md",
 "docs/iterations/v0.7/0.7.6-v0.7-evidence-and-compatibility-audit/audit-report.md",
 "docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle/review.md",
 "docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle/release-candidate-summary.md",
]
missing=[p for p in paths if not Path(p).exists()]
print("missing_v0_7_final_refs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

## V07-CR Blocker Gate

Read the post-closeout code-review result before any final closeout or clean
PASS statement:

```bash
rg -n "Status: review complete with blocking findings|### P1|### P2|V07-CR-0[1-5]" docs/testing/results/2026-06-02-v0.7-code-review.md
```

Expected gate result:

- If the code-review file still records blocking findings, final closeout and
  clean PASS are blocked until the repair package records current-session
  evidence that V07-CR-01 through V07-CR-05 are fixed or explicitly downgraded
  with reviewer-approved rationale.
- L1 blocker regression is mandatory before clean PASS: accepted/deferred P1/P2
  report cases, private report markers, private manifest command/text,
  `private_application_state_summary`, and schema-valid/checker-invalid
  authority cases must all be exercised by focused checker tests or recorded as
  unresolved blockers.
- JSON parse, manifest CLI PASS, projection CLI PASS, or `tools/testing` PASS
  cannot override unresolved V07-CR P1/P2 findings.

## Changed-File Scope Guard

Run the full cumulative v0.7 changed-file scope guard:

```bash
python3 -c 'import subprocess
allowed_prefixes=(
    "docs/iterations/v0.7/",
    "docs/contracts/external-validation-readiness-contract.md",
    "docs/contracts/projection-consumer-contract.md",
    "docs/contracts/v0.7-readiness-manifest-schema.json",
    "docs/contracts/v0.7-readiness-manifest.json",
    "docs/contracts/projection-read-model-contract.md",
    "docs/contracts/projection-read-model-schema.json",
    "docs/testing/external-validation-report-schema.json",
    "docs/validation-report-template.md",
    "tools/testing/validate_external_validation_report.py",
    "tools/testing/test_validate_external_validation_report.py",
    "tools/testing/validate_readiness_manifest.py",
    "tools/testing/test_validate_readiness_manifest.py",
    "tools/testing/validate_projection_read_model_contract.py",
    "tools/testing/test_validate_projection_read_model_contract.py",
)
tracked=subprocess.check_output(["git","diff","--name-only"], text=True).splitlines()
untracked=subprocess.check_output(["git","ls-files","--others","--exclude-standard"], text=True).splitlines()
files=tracked+untracked
bad=[p for p in files if not any(p.startswith(prefix) if prefix.endswith("/") else p == prefix for prefix in allowed_prefixes)]
print("changed_or_untracked=" + str(len(files)))
print("out_of_scope_changed_or_untracked=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

Expected results:

- `tools/testing` exits `0`.
- Manifest and projection CLI checks exit `0`.
- JSON parse commands exit `0`.
- `git diff --check` exits `0`.
- Required `0.7.8` package docs, final-closeout record, and Chinese mirrors
  exist.
- Final evidence references back to parent, completed child package reviews, and
  the post-closeout V07-CR code-review result exist.
- V07-CR blocker gate is classified. If blockers remain unresolved or L1
  blocker regression evidence is absent, final closeout remains blocked.
- Changed-file scope guard exits `0` with `out_of_scope_changed_or_untracked=0`.

## Commands Not Run

External validation suite, projection application validation, product-readiness
checks, runtime/API/frontend/E2E/live Agent/full autonomous/generation-quality
checks, and v0.8 checks are not run by this closeout.

## Blocker Recording Rule

If any final verification command, docs completeness check, evidence-reference
check, V07-CR blocker gate, scope guard, or evaluator checkpoint fails, record
it in `review.md` and `final-closeout.md` before parent status updates. Do not
mark final closeout complete while a P1, unresolved P2, or unexercised L1
blocker regression remains.

## No Unverified Claims Rule

Do not claim external validation suite PASS, projection application readiness,
product readiness, runtime/API/frontend/E2E/live Agent/full autonomous/
generation-quality PASS, or v0.8 readiness unless current-session evidence
explicitly covers that surface. Checker/schema PASS supports only the matching
checker/schema surface.
