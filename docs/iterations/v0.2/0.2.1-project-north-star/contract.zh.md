# Contract

Status: complete

英文版本：`contract.md`。

## Public Concepts

- Project North Star。
- Product Model。
- Scope Boundaries。
- Roadmap。
- Iteration package。
- Documentation governance。

## Compatibility Constraints

- 不改变 backend runtime behavior。
- 不改变 frontend behavior。
- 不改变 API shape。
- 不改变 tests。
- 不把 v0.2 标记为 released。
- 不把 village game 写成 WorldEngine purpose。

## Allowed Changes

- Add `AGENTS.md`。
- Add docs under `docs/`。
- Add iteration templates。
- Add v0.2 planning docs。
- Add release placeholder docs。

## Forbidden Changes

- Do not modify backend code。
- Do not modify frontend code。
- Do not add schema implementation。
- Do not add `backend/data/world_specs/tiny_village.world.json`。
- Do not modify `backend/worldengine/`。
- Do not run or claim E2E/UI/runtime smoke tests。

## North Star Check

- North star 明确 world generation、world runtime、recursive worlds、Agent lived experience 和
  pseudo-self。
- Product model 明确 WorldEngine 不是 village game backend。
- Scope boundaries 明确 v0.2 does/does not。
- Iteration templates 足以支持后续 code packages。

## Out-of-Scope Follow-ups

- WorldCell / WorldSpec schema implementation belongs to `0.2.2`。
- Event contract extension belongs to `0.2.3`。
- Reference fixture belongs to `0.2.4`。
