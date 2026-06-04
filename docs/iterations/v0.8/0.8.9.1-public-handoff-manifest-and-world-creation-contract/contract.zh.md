# Contract

英文源文件：`contract.md`。

## Public Deliverables

实现必须提供：

- `GET /manifest`。
- OpenAPI 可发现的 `POST /worlds`，operation id 为 `create_world`。
- public world creation request，接受 `world_prompt`。
- public world creation response，包含：
  - `world_id`
  - `status`
  - `public_initial_state`
  - `visualization`
- provider readiness summary，只包含：
  - `provider_class`
  - `provider_readiness`
  - `credential_source_class`
  - `model_label`
  - 可选 public quota 或 rate-limit note
- redaction confirmation flags。
- blockers 和 warnings。
- public director guidance status，即 `POST /worlds/{world_id}/director-guidance`，或明确 manifest unavailable reason。

## Allowed Changes

批准后，本包可修改：

- `backend/app/api/routes/`
- `backend/app/api/app_factory.py`
- `backend/app/schemas/`
- `backend/app/core/world_generation.py`，仅限 contract 所需的 reusable public summary 或 redaction helper。
- `backend/app/tests/` 下的 focused backend tests。
- 本目录下的 package review evidence。

## Forbidden Changes

本包不得：

- 修改 Validation Client 仓库。
- 修改 `backend/worldengine/`。
- 引入具体 demo-world names、maps、characters、resources、story rules、seed data 或 application-specific behavior。
- 实现 provider calls。
- 存储 provider keys、account ids、tokens、credentials 或 authorization headers。
- 暴露 private prompts、raw provider requests、raw provider responses、private evaluator oracle data、private validation scenarios、private Agent memory、private goals、relationship state、`self_state`、hidden context、private file paths 或 hidden reset APIs。
- 如果会阻止 Validation Client 读取顶层 `world_id`，不得对 `POST /worlds` 使用 `ApiResponse` envelope。
- 声明 external validation PASS、product readiness、live provider PASS、Agent autonomous PASS、E2E PASS 或 human validation PASS。

## Compatibility Constraints

- 现有 generation endpoints 必须保持兼容。
- 现有 v0.8 closeout evidence 保持历史且有边界。
- Schema changes 必须 additive。
- Public responses 必须使用 generic WorldEngine concepts，而不是外部应用细节。
- Provider configuration 缺失时不得报告为 ready。

## Stop Rules

如出现以下情况，停止实现：

- contract 需要修改 Validation Client code。
- world creation 无法在不添加 concrete demo content 的情况下实现。
- public response 会暴露 secrets、private prompts、provider raw traces 或 private Agent state。
- director guidance 会直接修改 private Agent memory、goals、identity、relationships 或 `self_state`。
- tests 无法证明 `POST /worlds` OpenAPI discoverability。
