# Technical Design

## Current State

WorldEngine 已有来自 `0.7.1` 的 reviewed public contract surfaces，以及来自
`0.7.2` 的 machine-checkable external validation report schema/checker。当前还没有单一的
public manifest 为 external consumers 索引这些 surfaces。

## Implementation Structure

Planned implementation files：

```text
docs/contracts/v0.7-readiness-manifest-schema.json
docs/contracts/v0.7-readiness-manifest.json
tools/testing/validate_readiness_manifest.py
tools/testing/test_validate_readiness_manifest.py
```

Package evidence files：

```text
docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/
```

## Manifest Shape

Manifest 应是 JSON object，包含：

- `manifest_id`
- `manifest_version`
- `engine_reference`
- `generated_from`
- `contract_surfaces`
- `schema_surfaces`
- `template_surfaces`
- `capability_areas`
- `readiness_claim_values`
- `evidence_references`
- `compatibility_notes`
- `redaction_rules`

Surface entries 应使用 repository-relative public paths 和 abstract ids。Manifest 必须包含：

```text
docs/contracts/external-fixture-runner-contract.md
docs/contracts/external-validation-readiness-contract.md
docs/contracts/projection-consumer-contract.md
docs/testing/external-validation-report-schema.json
docs/validation-report-template.md
tools/testing/validate_external_validation_report.py
docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md
docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/review.md
```

本 package 的 evidence references 只能把 evidence 分类为 `contract ready`、
`report format ready`、`blocked`、`skipped` 或 `out of scope`。Manifest 可以在
`readiness_claim_values` 中列出更完整的 reviewed taxonomy，但 checker 必须拒绝把
`external suite pass`、`external consumer pass` 和 `core-side compatibility ready` 作为本
package 的 evidence reference status。Historical reference 必须标记为 historical，且不能被当作当前
v0.7 PASS evidence。

## Checker Flow

Checker 应：

1. Load a JSON manifest file。
2. Validate top-level value is an object。
3. Validate required fields and simple field types。
4. Validate public repository-relative paths，并拒绝 absolute paths 或 parent traversal。
5. Validate required contract/schema/template references exist in the manifest。
6. Validate readiness claim values are from the reviewed taxonomy。
7. Validate evidence references include an allowed non-PASS status and public
   path or command。
8. 使用 synthetic sentinel coverage 拒绝 forbidden private-detail markers。
9. 对每个 error 打印 deterministic `FAIL:` lines，成功时打印一个 deterministic `PASS:` line。

## Test Strategy

Focused tests 使用 in-memory manifest dictionaries 和 temporary JSON files。它们只能使用
abstract identifiers 和 synthetic sentinel strings。

Required cases：

- valid manifest passes。
- missing required field fails。
- manifest missing required contract/schema/template surface fails。
- unsupported readiness claim value fails。
- absolute path or parent traversal path fails。
- evidence reference without status fails。
- synthetic private-detail markers fail。
- CLI returns `0` for valid manifests and `1` for invalid manifests。

## Compatibility Strategy

- Implementation isolated to new manifest schema/checker/test files。
- 不修改 runtime/API/frontend behavior。
- 不修改 `0.7.2` report checker；如需要，只运行其 focused tests 作为 regression evidence。
- 所有 identifiers 保持 generic and public。

## Anti-Drift Rules

- Parent and child status surfaces closeout 前必须一致。
- Implementation authorization 必须在 evaluator approval 前保持关闭。
- Manifest entries 不得暗示 external suite PASS，除非这类 evidence 明确存在且在 scope 内。
- Manifest paths 不得指向 private repositories、external fixture paths 或 generated local artifacts。
