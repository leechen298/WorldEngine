import { flushPromises, mount, type VueWrapper } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

import type {
  ActionResult,
  AgentCycleEvidence,
  CapabilityManifest,
  DirectionDecision,
  EvidenceBundle,
  FeedbackResult,
  PublicProjection,
  RunnableWorldPackage,
  SessionStepResult,
  WorldSessionView,
} from "../api/engineV1";
import RunnableAnchorPage from "./RunnableAnchorPage.vue";

const api = vi.hoisted(() => ({
  createWorldPackage: vi.fn(),
  createWorldSession: vi.fn(),
  exportSessionEvidence: vi.fn(),
  getEngineCapabilities: vi.fn(),
  getPublicProjection: vi.fn(),
  getWorldPackage: vi.fn(),
  getWorldSession: vi.fn(),
  pollWorldEvents: vi.fn(),
  stepWorldSession: vi.fn(),
  submitWorldAction: vi.fn(),
  submitWorldDirection: vi.fn(),
  submitWorldFeedback: vi.fn(),
}));

vi.mock("../api/engineV1", () => ({
  EngineV1ApiError: class EngineV1ApiError extends Error {
    data?: unknown;
  },
  ...api,
}));

const PACKAGE_HASH = "a".repeat(64);
const INITIAL_STATE_HASH = "b".repeat(64);

const capabilities: CapabilityManifest = {
  engine_id: "worldengine",
  engine_build: "worldengine-test-build",
  instance_id: "instance-test",
  contract_version: "engine-v1-mvp",
  schema_version: "worldengine.engine.v1",
  state_hash_algorithm: "sha256-canonical-json-v1",
  operations: [
    {
      operation_id: "world_packages.create",
      method: "POST",
      path: "/api/v1/world-packages",
      maturity: "anchor",
    },
    {
      operation_id: "sessions.step",
      method: "POST",
      path: "/api/v1/sessions/{session_id}/steps",
      maturity: "anchor",
    },
  ],
};

const runnablePackage: RunnableWorldPackage = {
  schema_version: "worldengine.engine.v1",
  package_id: "package-test",
  package_hash: PACKAGE_HASH,
  brief: {
    seed: "anchor-seed-0130",
    premise: "public premise",
    constraints: {},
    state_variables: [
      { key: "world_signal", initial: 0, minimum: -100, maximum: 100, step: 1 },
    ],
    agent_count: 1,
    step_seconds: 1,
  },
  world_spec: { world_id: "world-test" },
  rule_catalog: [],
  action_catalog: [
    {
      action_id: "action.adjust.world_signal",
      target_ref: "world_signal",
      minimum_amount: -3,
      maximum_amount: 3,
    },
  ],
  agent_seed_set: [{ agent_id: "agent-test" }],
  projection_manifest: { allowed_feedback_types: ["local_outcome_observed"] },
  evidence_policy: {},
  readiness: { status: "ready", diagnostics: [] },
};

function makeProjection(overrides: Partial<PublicProjection> = {}): PublicProjection {
  return {
    schema_version: "worldengine.engine.v1",
    session_id: "session-test",
    world_id: "world-test",
    source_package_hash: PACKAGE_HASH,
    status: "ready",
    tick: 0,
    world_time_seconds: 0,
    revision: 0,
    state_hash: INITIAL_STATE_HASH,
    variables: { world_signal: 0 },
    feedback_count: 0,
    locations: [{ location_id: "location-test", kind: "root", connections: [] }],
    entities: [
      {
        entity_id: "entity-test",
        kind: "public_state_carrier",
        location_id: "location-test",
      },
    ],
    agents: [
      {
        agent_id: "agent-test",
        location_id: "location-test",
        cycle_count: 0,
        last_intent: "observe",
        decision_mode: "initial_policy",
        experience_refs: [],
      },
    ],
    allowed_actions: ["action.adjust.world_signal"],
    active_intervention_window: {
      window_id: "window-session-test-t0",
      open_tick: 0,
      status: "open",
    },
    event_cursor: 1,
    ...overrides,
  };
}

function makeSession(projection: PublicProjection): WorldSessionView {
  return {
    schema_version: "worldengine.engine.v1",
    session_id: projection.session_id,
    package_id: runnablePackage.package_id,
    source_package_hash: PACKAGE_HASH,
    initial_snapshot_id: "snapshot-initial",
    projection,
  };
}

function makeAgentCycle(tick: number, withExperience: boolean): AgentCycleEvidence {
  return {
    cycle_id: `cycle-${tick}`,
    agent_id: "agent-test",
    tick,
    perception: { state_hash: "public" },
    decision: {
      intent: withExperience ? "repeat_rule_accepted_action" : "explore_allowed_action",
      decision_mode: withExperience ? "experience_guided_policy" : "initial_policy",
    },
    action_request: { request_id: `agent-action-${tick}` },
    rule_judgment: { accepted: true },
    action_result: { status: "accepted", event_ref: `event-agent-${tick}` },
    experience_refs_used: withExperience
      ? [
          {
            ref_id: "event-agent-1",
            ref_type: "action_result",
            source_tick: 1,
            public_effect: "world_signal:+1",
          },
        ]
      : [],
    event_refs: [`event-agent-${tick}`],
    diff_refs: [`diff-agent-${tick}`],
  };
}

function makeEvidence(
  projection: PublicProjection,
  options: { cycles?: AgentCycleEvidence[]; decisions?: DirectionDecision[]; complete?: boolean } = {},
): EvidenceBundle {
  return {
    schema_version: "worldengine.engine.v1",
    contract_version: "engine-v1-mvp",
    state_hash_algorithm: "sha256-canonical-json-v1",
    package: runnablePackage,
    projection,
    events: [],
    diffs: [],
    snapshots: [
      {
        snapshot_id: "snapshot-initial",
        tick: projection.tick,
        revision: projection.revision,
        state_hash: projection.state_hash,
        canonical_state: { variables: projection.variables },
      },
    ],
    agent_cycles: options.cycles ?? [],
    direction_decisions: options.decisions ?? [],
    request_correlations: [],
    completeness: {
      integrity: {
        status: "valid",
        checks: { event_diff_links: true, request_correlations: true },
        failures: [],
      },
      scenario_coverage: {
        status: options.complete ? "covered" : "partial",
        checks: { agent: options.complete ?? false, feedback: false },
        missing: options.complete ? [] : ["agent", "feedback"],
      },
    },
  };
}

const projectionStub = {
  props: ["projection"],
  template: `
    <div data-test="projection-stub">
      <span data-test="projection-tick">{{ projection?.tick ?? '-' }}</span>
      <span data-test="projection-revision">{{ projection?.revision ?? '-' }}</span>
      <span data-test="projection-state-hash">{{ projection?.state_hash ?? '-' }}</span>
      <span data-test="projection-feedback-count">{{ projection?.feedback_count ?? '-' }}</span>
      <span data-test="active-window-id">{{ projection?.active_intervention_window?.window_id ?? '-' }}</span>
      <span data-test="agent-decision-mode">{{ projection?.agents?.[0]?.decision_mode ?? '-' }}</span>
    </div>
  `,
};

const evidenceStub = {
  name: "EvidencePanel",
  props: ["eventPage", "evidence", "loading", "canRefresh"],
  emits: ["refresh", "download"],
  template: `
    <div data-test="evidence-stub">
      <span data-test="evidence-status">{{ evidence ? '完整性 ' + evidence.completeness.integrity.status + ' · 场景 ' + evidence.completeness.scenario_coverage.status : '-' }}</span>
      <button data-test="refresh-evidence" :disabled="!canRefresh || loading" @click="$emit('refresh')">refresh</button>
      <button data-test="download-evidence" :disabled="!canRefresh || !evidence" @click="$emit('download')">download</button>
    </div>
  `,
};

let canonicalProjection: PublicProjection;
let canonicalEvidence: EvidenceBundle;

function mountPage(): VueWrapper {
  return mount(RunnableAnchorPage, {
    global: {
      stubs: {
        ProjectionPanel: projectionStub,
        EvidencePanel: evidenceStub,
      },
    },
  });
}

async function generateAndBoot(wrapper: VueWrapper): Promise<void> {
  await wrapper.get("[data-test='generate-package']").trigger("click");
  await flushPromises();
  await wrapper.get("[data-test='boot-session']").trigger("click");
  await flushPromises();
}

describe("RunnableAnchorPage", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    canonicalProjection = makeProjection();
    canonicalEvidence = makeEvidence(canonicalProjection);

    api.getEngineCapabilities.mockResolvedValue(capabilities);
    api.createWorldPackage.mockResolvedValue(runnablePackage);
    api.getWorldPackage.mockResolvedValue(runnablePackage);
    api.createWorldSession.mockImplementation(async () => makeSession(canonicalProjection));
    api.getWorldSession.mockImplementation(async () => makeSession(canonicalProjection));
    api.getPublicProjection.mockImplementation(async () => canonicalProjection);
    api.pollWorldEvents.mockImplementation(async () => ({
      session_id: canonicalProjection.session_id,
      after_sequence: 0,
      items: canonicalEvidence.events,
      next_sequence: canonicalProjection.event_cursor,
      has_more: false,
    }));
    api.exportSessionEvidence.mockImplementation(async () => canonicalEvidence);

    api.submitWorldDirection.mockImplementation(
      async (_sessionId: string, request: { kind: string; request_id: string; window_id: string }) => {
        const accepted = request.kind === "bounded_pressure";
        const result: DirectionDecision = {
          request_id: request.request_id,
          window_id: request.window_id,
          status: accepted ? "accepted" : "rejected",
          reason_code: accepted ? "bounded_direction_queued" : "direct_final_fact_forbidden",
          public_reason: accepted ? "queued" : "forbidden",
          queued: accepted,
          application_status: accepted ? "queued" : "not_applicable",
          rule_refs: ["rule.direction.world_signal"],
          event_ref: accepted ? "event-direction-accepted" : "event-direction-rejected",
          application_event_refs: [],
          applied_diff_refs: [],
          tick: canonicalProjection.tick,
          revision: canonicalProjection.revision,
          state_hash_before: canonicalProjection.state_hash,
          state_hash_after: canonicalProjection.state_hash,
        };
        canonicalProjection = {
          ...canonicalProjection,
          event_cursor: canonicalProjection.event_cursor + 1,
        };
        canonicalEvidence = makeEvidence(canonicalProjection, {
          decisions: [...canonicalEvidence.direction_decisions, result],
        });
        return result;
      },
    );

    api.stepWorldSession.mockImplementation(
      async (_sessionId: string, request: { request_id: string; step_count: number }) => {
        const start = canonicalProjection;
        canonicalProjection = makeProjection({
          tick: start.tick + request.step_count,
          world_time_seconds: start.world_time_seconds + request.step_count,
          revision: start.revision + request.step_count * 2,
          state_hash: "c".repeat(64),
          variables: { world_signal: request.step_count + 1 },
          agents: [
            {
              agent_id: "agent-test",
              location_id: "location-test",
              cycle_count: 2,
              last_intent: "repeat_rule_accepted_action",
              decision_mode: "experience_guided_policy",
              experience_refs: [
                {
                  ref_id: "event-agent-1",
                  ref_type: "action_result",
                  source_tick: 1,
                  public_effect: "world_signal:+1",
                },
              ],
            },
          ],
          active_intervention_window: {
            window_id: `window-session-test-t${request.step_count}`,
            open_tick: request.step_count,
            status: "open",
          },
          event_cursor: 8,
        });
        canonicalEvidence = makeEvidence(canonicalProjection, {
          cycles: [makeAgentCycle(1, false), makeAgentCycle(2, true)],
          decisions: canonicalEvidence.direction_decisions.map((decision) =>
            decision.status === "accepted"
              ? {
                  ...decision,
                  queued: false,
                  application_status: "applied",
                  application_reason_code: "direction_applied",
                  application_event_refs: ["event-direction-applied"],
                  applied_diff_refs: ["diff-direction-applied"],
                }
              : decision,
          ),
          complete: true,
        });
        const result: SessionStepResult = {
          request_id: request.request_id,
          status: "completed",
          step_count: request.step_count,
          start_tick: start.tick,
          end_tick: canonicalProjection.tick,
          start_revision: start.revision,
          end_revision: canonicalProjection.revision,
          start_state_hash: start.state_hash,
          end_state_hash: canonicalProjection.state_hash,
          event_refs: ["event-step"],
          snapshot_refs: ["snapshot-step"],
          projection: makeProjection({ tick: 999, revision: 999 }),
        };
        return result;
      },
    );

    api.submitWorldAction.mockImplementation(async (_sessionId: string, request: { request_id: string }) => {
      canonicalProjection = {
        ...canonicalProjection,
        revision: canonicalProjection.revision + 1,
        state_hash: "d".repeat(64),
        variables: { world_signal: canonicalProjection.variables.world_signal + 1 },
      };
      canonicalEvidence = makeEvidence(canonicalProjection);
      const result: ActionResult = {
        request_id: request.request_id,
        status: "accepted",
        reason_code: "action_rule_accepted",
        rule_refs: ["rule.range.world_signal"],
        event_ref: "event-client-action",
        applied_diff_refs: ["diff-client-action"],
        projection: makeProjection({ tick: 999, revision: 999, state_hash: "f".repeat(64) }),
      };
      return result;
    });

    api.submitWorldFeedback.mockImplementation(
      async (_sessionId: string, request: { request_id: string }) => {
        canonicalProjection = {
          ...canonicalProjection,
          revision: canonicalProjection.revision + 1,
          state_hash: "e".repeat(64),
          feedback_count: canonicalProjection.feedback_count + 1,
        };
        canonicalEvidence = makeEvidence(canonicalProjection);
        const result: FeedbackResult = {
          request_id: request.request_id,
          status: "accepted",
          reason_code: "feedback_accepted",
          rule_refs: ["rule.feedback.manifest"],
          event_ref: "event-client-feedback",
          applied_diff_refs: ["diff-client-feedback"],
          projection: makeProjection({ tick: 999, revision: 999 }),
        };
        return result;
      },
    );
  });

  it("loads and renders the public capability manifest", async () => {
    const wrapper = mountPage();
    await flushPromises();

    expect(api.getEngineCapabilities).toHaveBeenCalledTimes(1);
    expect(wrapper.get("[data-test='engine-build']").text()).toBe("worldengine-test-build");
    expect(wrapper.get("[data-test='operation-count']").text()).toBe("2");
    expect(wrapper.get("[data-test='capability-operations']").text()).toContain(
      "world_packages.create",
    );
  });

  it("generates twice, verifies the server package, boots, and re-fetches canonical views", async () => {
    const wrapper = mountPage();
    await flushPromises();

    await generateAndBoot(wrapper);

    expect(api.createWorldPackage).toHaveBeenCalledTimes(2);
    expect(api.createWorldPackage.mock.calls[0][0].brief).toEqual(
      api.createWorldPackage.mock.calls[1][0].brief,
    );
    expect(api.getWorldPackage).toHaveBeenCalledWith("package-test");
    expect(wrapper.get("[data-test='package-readiness']").text()).toBe("ready");
    expect(wrapper.get("[data-test='determinism-status']").text()).toContain("2/2 hash 一致");
    expect(api.createWorldSession).toHaveBeenCalledWith(
      expect.objectContaining({ package_id: "package-test", package_hash: PACKAGE_HASH }),
    );
    expect(api.getWorldSession).toHaveBeenCalledWith("session-test");
    expect(api.getPublicProjection).toHaveBeenCalledWith("session-test");
    expect(api.pollWorldEvents).toHaveBeenCalledWith("session-test", {
      afterSequence: 0,
      limit: 200,
    });
    expect(api.exportSessionEvidence).toHaveBeenCalledWith("session-test");
    expect(wrapper.get("[data-test='projection-state-hash']").text()).toBe(INITIAL_STATE_HASH);
  });

  it("disables evidence refresh before a session and never reports a false success", async () => {
    const wrapper = mountPage();
    await flushPromises();
    vi.clearAllMocks();

    expect(wrapper.get("[data-test='refresh-evidence']").attributes("disabled")).toBeDefined();
    wrapper.findComponent({ name: "EvidencePanel" }).vm.$emit("refresh");
    await flushPromises();

    expect(api.getPublicProjection).not.toHaveBeenCalled();
    expect(api.exportSessionEvidence).not.toHaveBeenCalled();
    expect(wrapper.get("[data-test='operation-warning']").text()).toContain("无法刷新证据");
    expect(wrapper.find("[data-test='operation-message']").exists()).toBe(false);
  });

  it("validates WorldBrief fields against the backend variable constraints", async () => {
    const wrapper = mountPage();
    await flushPromises();
    vi.clearAllMocks();

    await wrapper.get("[data-test='state-key']").setValue("World-Signal");
    await flushPromises();
    expect(wrapper.get("[data-test='state-key-error']").text()).toContain("小写字母");
    expect(wrapper.get("[data-test='generate-package']").attributes("disabled")).toBeDefined();

    await wrapper.get("[data-test='state-key']").setValue("world_signal");
    await wrapper.get("[data-test='state-minimum']").setValue("0");
    await wrapper.get("[data-test='state-maximum']").setValue("10");
    await wrapper.get("[data-test='state-initial']").setValue("5");
    await wrapper.get("[data-test='state-step']").setValue("6");
    await flushPromises();
    expect(wrapper.get("[data-test='state-step-error']").text()).toContain("至少要能");

    await wrapper.get("[data-test='brief-constraints']").setValue("[]");
    await flushPromises();
    expect(wrapper.get("[data-test='brief-constraints-error']").text()).toContain("必须是对象");
    expect(api.createWorldPackage).not.toHaveBeenCalled();
  });

  it("invalidates the generated package, session, and evidence as soon as the brief changes", async () => {
    const wrapper = mountPage();
    await flushPromises();
    await generateAndBoot(wrapper);

    const fingerprint = wrapper.get("[data-test='brief-fingerprint']").text();
    expect(fingerprint).toMatch(/^brief-[a-f0-9]{8}-\d+$/);
    expect(wrapper.get("[data-test='refresh-evidence']").attributes("disabled")).toBeUndefined();

    await wrapper.get("[data-test='brief-premise']").setValue("修改后的公开世界前提。");
    await flushPromises();

    expect(wrapper.find("[data-test='package-result']").exists()).toBe(false);
    expect(wrapper.find("[data-test='session-result']").exists()).toBe(false);
    expect(wrapper.get("[data-test='projection-tick']").text()).toBe("-");
    expect(wrapper.get("[data-test='evidence-status']").text()).toBe("-");
    expect(wrapper.get("[data-test='boot-session']").attributes("disabled")).toBeDefined();
    expect(wrapper.get("[data-test='refresh-evidence']").attributes("disabled")).toBeDefined();
    expect(wrapper.get("[data-test='operation-warning']").text()).toContain("请重新生成");
  });

  it("keeps a successful direction receipt visible when the other command fails", async () => {
    const wrapper = mountPage();
    await flushPromises();
    await generateAndBoot(wrapper);
    vi.clearAllMocks();

    await wrapper.get("[data-test='submit-bounded-direction']").trigger("click");
    await flushPromises();
    expect(wrapper.get("[data-test='accepted-direction-result']").text()).toContain("accepted");

    api.submitWorldDirection.mockRejectedValueOnce(new Error("final command unavailable"));
    await wrapper.get("[data-test='submit-final-fact-direction']").trigger("click");
    await flushPromises();

    expect(wrapper.get("[data-test='accepted-direction-result']").text()).toContain("accepted");
    expect(wrapper.get("[data-test='rejected-direction-result']").text()).toContain("未提交");
    expect(wrapper.get("[data-test='final-fact-direction-error']").text()).toContain(
      "final command unavailable",
    );
    expect(wrapper.get("[data-test='operation-error']").text()).toContain("最终事实命令提交失败");
  });

  it("submits the two direction commands independently, then exact-steps into experience evidence", async () => {
    const wrapper = mountPage();
    await flushPromises();
    await generateAndBoot(wrapper);
    vi.clearAllMocks();

    await wrapper.get("[data-test='submit-bounded-direction']").trigger("click");
    await flushPromises();

    expect(api.submitWorldDirection).toHaveBeenCalledTimes(1);
    const acceptedRequest = api.submitWorldDirection.mock.calls[0][1];
    expect(acceptedRequest).toMatchObject({
      window_id: "window-session-test-t0",
      kind: "bounded_pressure",
    });
    expect(wrapper.get("[data-test='accepted-direction-result']").text()).toContain("accepted");
    expect(wrapper.get("[data-test='rejected-direction-result']").text()).toContain("未提交");

    await wrapper.get("[data-test='submit-final-fact-direction']").trigger("click");
    await flushPromises();

    expect(api.submitWorldDirection).toHaveBeenCalledTimes(2);
    const rejectedRequest = api.submitWorldDirection.mock.calls[1][1];
    expect(rejectedRequest).toMatchObject({
      window_id: "window-session-test-t0",
      kind: "direct_final_fact",
    });
    expect(api.getPublicProjection).toHaveBeenCalledTimes(4);
    expect(api.exportSessionEvidence).toHaveBeenCalledTimes(2);
    expect(wrapper.get("[data-test='accepted-direction-result']").text()).toContain("accepted");
    expect(wrapper.get("[data-test='rejected-direction-result']").text()).toContain(
      "direct_final_fact_forbidden",
    );

    await wrapper.get("[data-test='step-session']").trigger("click");
    await flushPromises();

    expect(api.stepWorldSession).toHaveBeenCalledWith(
      "session-test",
      expect.objectContaining({ step_count: 2, expected_revision: 0 }),
    );
    expect(wrapper.get("[data-test='projection-tick']").text()).toBe("2");
    expect(wrapper.get("[data-test='projection-revision']").text()).toBe("4");
    expect(wrapper.get("[data-test='agent-decision-mode']").text()).toBe(
      "experience_guided_policy",
    );
    expect(wrapper.get("[data-test='evidence-status']").text()).toBe(
      "完整性 valid · 场景 covered",
    );
    expect(wrapper.get("[data-test='accepted-direction-result']").text()).toContain("applied");
    expect(wrapper.text()).not.toContain("999");
  });

  it("re-fetches projection and evidence after generic action and typed feedback mutations", async () => {
    const wrapper = mountPage();
    await flushPromises();
    await generateAndBoot(wrapper);
    vi.clearAllMocks();

    await wrapper.get("[data-test='submit-action']").trigger("click");
    await flushPromises();

    expect(api.submitWorldAction).toHaveBeenCalledWith(
      "session-test",
      expect.objectContaining({
        action_id: "action.adjust.world_signal",
        target_ref: "world_signal",
        amount: 1,
        expected_revision: 0,
      }),
    );
    expect(api.getPublicProjection).toHaveBeenCalledTimes(2);
    expect(api.exportSessionEvidence).toHaveBeenCalledTimes(1);
    expect(wrapper.get("[data-test='projection-tick']").text()).toBe("0");
    expect(wrapper.get("[data-test='projection-state-hash']").text()).toBe("d".repeat(64));
    expect(wrapper.text()).not.toContain("999");

    vi.clearAllMocks();
    await wrapper.get("[data-test='submit-feedback']").trigger("click");
    await flushPromises();

    expect(api.submitWorldFeedback).toHaveBeenCalledWith(
      "session-test",
      expect.objectContaining({
        feedback_type: "local_outcome_observed",
        related_event_ref: "event-client-action",
        expected_revision: 1,
      }),
    );
    expect(api.getWorldSession).toHaveBeenCalledTimes(1);
    expect(api.getPublicProjection).toHaveBeenCalledTimes(2);
    expect(api.pollWorldEvents).toHaveBeenCalledTimes(1);
    expect(api.exportSessionEvidence).toHaveBeenCalledTimes(1);
    expect(wrapper.get("[data-test='projection-feedback-count']").text()).toBe("1");
  });

  it("retries instead of displaying a mixed canonical revision", async () => {
    const wrapper = mountPage();
    await flushPromises();
    await generateAndBoot(wrapper);
    vi.clearAllMocks();

    const stale = makeProjection({ revision: 0, state_hash: INITIAL_STATE_HASH });
    canonicalProjection = makeProjection({
      revision: 1,
      state_hash: "e".repeat(64),
      event_cursor: 2,
    });
    canonicalEvidence = makeEvidence(canonicalProjection);
    api.getPublicProjection
      .mockResolvedValueOnce(stale)
      .mockResolvedValueOnce(canonicalProjection)
      .mockResolvedValueOnce(canonicalProjection)
      .mockResolvedValueOnce(canonicalProjection);

    await wrapper.get("[data-test='refresh-evidence']").trigger("click");
    await flushPromises();

    expect(api.getPublicProjection).toHaveBeenCalledTimes(4);
    expect(api.getWorldSession).toHaveBeenCalledTimes(2);
    expect(api.exportSessionEvidence).toHaveBeenCalledTimes(2);
    expect(wrapper.get("[data-test='projection-revision']").text()).toBe("1");
    expect(wrapper.get("[data-test='projection-state-hash']").text()).toBe(
      "e".repeat(64),
    );
    expect(wrapper.find("[data-test='operation-error']").exists()).toBe(false);
  });
});
