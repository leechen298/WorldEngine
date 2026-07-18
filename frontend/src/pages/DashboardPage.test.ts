import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

import DashboardPage from "./DashboardPage.vue";

const {
  createSessionFromWorldviewMock,
  fetchHealthMock,
  getRuntimeStateMock,
  getWorldEventStepsMock,
  getWorldParamsMock,
  getWorldSummariesMock,
  listSessionSnapshotsMock,
  pauseSessionMock,
  resumeSessionMock,
  runSessionMock,
} = vi.hoisted(() => ({
  createSessionFromWorldviewMock: vi.fn(),
  fetchHealthMock: vi.fn(),
  getRuntimeStateMock: vi.fn(),
  getWorldEventStepsMock: vi.fn(),
  getWorldParamsMock: vi.fn(),
  getWorldSummariesMock: vi.fn(),
  listSessionSnapshotsMock: vi.fn(),
  pauseSessionMock: vi.fn(),
  resumeSessionMock: vi.fn(),
  runSessionMock: vi.fn(),
}));

vi.mock("../api/client", () => ({
  createSessionFromWorldview: createSessionFromWorldviewMock,
  fetchHealth: fetchHealthMock,
  getRuntimeState: getRuntimeStateMock,
  getWorldEventSteps: getWorldEventStepsMock,
  getWorldParams: getWorldParamsMock,
  getWorldSummaries: getWorldSummariesMock,
  listSessionSnapshots: listSessionSnapshotsMock,
  pauseSession: pauseSessionMock,
  resumeSession: resumeSessionMock,
  runSession: runSessionMock,
}));

describe("DashboardPage", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    fetchHealthMock.mockResolvedValue({
      status: "ok",
      service: "worldengine-backend",
    });
    getRuntimeStateMock.mockResolvedValue({
      tick_id: 3,
      world_time_seconds: 1800,
      step_seconds: 600,
      updated_at: "2026-03-09T00:00:00+00:00",
    });
    getWorldEventStepsMock.mockResolvedValue({
      items: [
        {
          tick_id: 3,
          world_time_seconds: 1800,
          event_count: 1,
          created_at: "2026-03-09T00:00:00+00:00",
          items: [
            {
              id: "evt-1",
              tick_id: 3,
              world_time_seconds: 1800,
              type: "tick.advanced",
              source: "system",
              payload: {},
              created_at: "2026-03-09T00:00:00+00:00",
            },
          ],
        },
      ],
      next_cursor: null,
      has_more: false,
      limit: 20,
    });
    getWorldParamsMock.mockResolvedValue({
      counter: {
        increment: 2,
      },
    });
    getWorldSummariesMock.mockResolvedValue({
      items: [],
      total: 0,
    });
    listSessionSnapshotsMock.mockResolvedValue({
      session_id: "session-1",
      world_id: "world-1",
      items: [],
      total: 0,
      limit: 5,
      timeline_label: "timeline branch for session session-1",
      redaction_status: "passed",
    });
    createSessionFromWorldviewMock.mockResolvedValue({
      session_id: "session-1",
      world_id: "world-1",
      public_label: "generated-world",
      status: "created",
      runtime_ref: {
        tick_id: 0,
        world_time_seconds: 0,
        step_seconds: 600,
      },
      evidence_refs: {
        event_count_at_create: 0,
        snapshot_count_at_create: 0,
        current_event_count: 0,
        current_snapshot_count: 0,
      },
      generation_summary: {
        request_id: "request-1",
        generation_id: "generation-1",
        generation_status: "fallback",
        generation_mode: "deterministic_fallback",
        creation_mode: "deterministic_generic_fallback",
        provider_class: "unconfigured",
        provider_backed: false,
        llm_backed: false,
        deterministic_generic_fallback_detected: true,
        premise_digest: "abc123",
        runtime_ready: "true",
        blockers: [],
        warnings: [],
        public_world_model_refs: {},
      },
      created_at: "2026-03-09T00:00:00+00:00",
      updated_at: "2026-03-09T00:00:00+00:00",
      persistence: "in_memory",
    });
    runSessionMock.mockResolvedValue({
      session_id: "session-1",
      world_id: "world-1",
      run_summary: {
        schema_version: "0.9.5",
        status: "completed",
        stop_reason: "requested_ticks_reached",
        start_tick: 0,
        end_tick: 2,
        start_world_time_seconds: 0,
        end_world_time_seconds: 1200,
        step_seconds: 600,
        ticks_requested: 2,
        duration_requested_seconds: null,
        ticks_executed: 2,
        guard_summary: { max_ticks: 100 },
        provider_calls_used: 0,
        estimated_cost_units_used: 0,
        redaction_status: "passed",
        control_status: "idle",
      },
      runtime_delta: {
        start_tick: 0,
        end_tick: 2,
        start_world_time_seconds: 0,
        end_world_time_seconds: 1200,
      },
      event_evidence: {
        event_count_before: 0,
        event_count_after: 2,
        event_delta_count: 2,
      },
      snapshot_evidence: {
        snapshot_count_before: 0,
        snapshot_count_after: 2,
        snapshot_delta_count: 2,
        snapshot_ids: ["snap-1", "snap-2"],
      },
      timeline_label: "timeline branch for session session-1",
      redaction_status: "passed",
    });
    pauseSessionMock.mockResolvedValue({ status: "paused" });
    resumeSessionMock.mockResolvedValue({
      session_id: "session-1",
      world_id: "world-1",
      public_label: "generated-world",
      status: "ready",
      runtime_ref: {
        tick_id: 2,
        world_time_seconds: 1200,
        step_seconds: 600,
      },
      evidence_refs: {
        event_count_at_create: 0,
        snapshot_count_at_create: 0,
        current_event_count: 2,
        current_snapshot_count: 2,
      },
      created_at: "2026-03-09T00:00:00+00:00",
      updated_at: "2026-03-09T00:20:00+00:00",
      persistence: "in_memory",
    });
  });

  it("loads and renders health and runtime state on mount", async () => {
    const wrapper = mount(DashboardPage, {
      global: {
        stubs: {
          RuntimeControls: true,
          TimelinePanel: true,
          WorldPanel: true,
          AgentPanel: true,
          MemoryPanel: true,
          GenerationPanel: true,
        },
      },
    });

    await flushPromises();

    expect(fetchHealthMock).toHaveBeenCalledTimes(1);
    expect(getRuntimeStateMock).toHaveBeenCalledTimes(1);
    expect(getWorldEventStepsMock).toHaveBeenCalledTimes(1);
    expect(getWorldEventStepsMock).toHaveBeenCalledWith({ cursor: undefined, limit: 20 });
    expect(getWorldParamsMock).toHaveBeenCalledTimes(1);
    expect(wrapper.text()).toContain("Status");
    expect(wrapper.text()).toContain("ok");
    expect(wrapper.text()).toContain("Service");
    expect(wrapper.text()).toContain("worldengine-backend");
    expect(wrapper.text()).toContain("tick_id");
    expect(wrapper.text()).toContain("3");
    expect(wrapper.text()).toContain("updated_at");
    expect(wrapper.text()).toContain("2026-03-09T00:00:00+00:00");
  });

  it("reloads runtime state after the controls emit stepped", async () => {
    const wrapper = mount(DashboardPage, {
      global: {
        stubs: {
          RuntimeControls: {
            template: "<button data-test='runtime-controls' @click=\"$emit('stepped')\">Step</button>",
          },
          TimelinePanel: true,
          WorldPanel: true,
          AgentPanel: true,
          MemoryPanel: true,
          GenerationPanel: true,
        },
      },
    });

    await flushPromises();
    getRuntimeStateMock.mockResolvedValueOnce({
      tick_id: 4,
      world_time_seconds: 2400,
      step_seconds: 600,
      updated_at: "2026-03-09T00:10:00+00:00",
    });
    getWorldEventStepsMock.mockResolvedValueOnce({
      items: [
        {
          tick_id: 4,
          world_time_seconds: 2400,
          event_count: 1,
          created_at: "2026-03-09T00:10:00+00:00",
          items: [
            {
              id: "evt-2",
              tick_id: 4,
              world_time_seconds: 2400,
              type: "tick.advanced",
              source: "system",
              payload: {},
              created_at: "2026-03-09T00:10:00+00:00",
            },
          ],
        },
      ],
      next_cursor: null,
      has_more: false,
      limit: 20,
    });

    await wrapper.get("[data-test='runtime-controls']").trigger("click");
    await flushPromises();

    expect(getRuntimeStateMock).toHaveBeenCalledTimes(2);
    expect(getWorldEventStepsMock).toHaveBeenCalledTimes(2);
    expect(getWorldEventStepsMock).toHaveBeenLastCalledWith({ cursor: undefined, limit: 20 });
    expect(getWorldParamsMock).toHaveBeenCalledTimes(1);
    expect(wrapper.text()).toContain("tick_id");
    expect(wrapper.text()).toContain("4");
  });

  it("mounts the generation panel in the dashboard grid", async () => {
    const wrapper = mount(DashboardPage, {
      global: {
        stubs: {
          RuntimeControls: true,
          TimelinePanel: true,
          WorldPanel: true,
          AgentPanel: true,
          MemoryPanel: true,
          GenerationPanel: {
            template: "<section data-test='generation-panel-stub'>Generation</section>",
          },
        },
      },
    });

    await flushPromises();

    expect(wrapper.find("[data-test='generation-panel-stub']").exists()).toBe(true);
  });

  it("creates a session from worldview input and renders public session summary", async () => {
    const wrapper = mount(DashboardPage, {
      global: {
        stubs: {
          RuntimeControls: true,
          TimelinePanel: true,
          WorldPanel: true,
          AgentPanel: true,
          MemoryPanel: true,
          GenerationPanel: true,
        },
      },
    });

    await flushPromises();
    await wrapper.get("[data-test='session-premise-input']").setValue("public workshop world");
    await wrapper.get("[data-test='session-create-button']").trigger("click");
    await flushPromises();

    expect(createSessionFromWorldviewMock).toHaveBeenCalledWith(
      expect.objectContaining({
        worldview_premise: "public workshop world",
        allow_deterministic_fallback: true,
      }),
    );
    expect(listSessionSnapshotsMock).toHaveBeenCalledWith("session-1", {
      limit: 5,
      order: "desc",
    });
    expect(wrapper.get("[data-test='session-id']").text()).toBe("session-1");
    expect(wrapper.get("[data-test='session-status']").text()).toBe("created");
    expect(wrapper.get("[data-test='session-generation-mode']").text()).toBe("deterministic_fallback");
  });

  it("runs the current session and displays public evidence", async () => {
    const wrapper = mount(DashboardPage, {
      global: {
        stubs: {
          RuntimeControls: true,
          TimelinePanel: true,
          WorldPanel: true,
          AgentPanel: true,
          MemoryPanel: true,
          GenerationPanel: true,
        },
      },
    });

    await flushPromises();
    await wrapper.get("[data-test='session-premise-input']").setValue("public workshop world");
    await wrapper.get("[data-test='session-create-button']").trigger("click");
    await flushPromises();
    await wrapper.get("[data-test='session-run-ticks-input']").setValue(2);
    await wrapper.get("[data-test='session-run-button']").trigger("click");
    await flushPromises();

    expect(runSessionMock).toHaveBeenCalledWith("session-1", {
      ticks: 2,
      max_ticks: 100,
    });
    expect(wrapper.get("[data-test='session-status']").text()).toBe("ready");
    expect(wrapper.get("[data-test='session-run-evidence']").text()).toContain("2");
    expect(wrapper.get("[data-test='session-snapshot-delta']").text()).toBe("2");
  });
});
