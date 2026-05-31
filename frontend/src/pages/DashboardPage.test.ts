import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

import DashboardPage from "./DashboardPage.vue";

const { fetchHealthMock, getRuntimeStateMock, getWorldEventStepsMock, getWorldParamsMock, getWorldSummariesMock } = vi.hoisted(() => ({
  fetchHealthMock: vi.fn(),
  getRuntimeStateMock: vi.fn(),
  getWorldEventStepsMock: vi.fn(),
  getWorldParamsMock: vi.fn(),
  getWorldSummariesMock: vi.fn(),
}));

vi.mock("../api/client", () => ({
  fetchHealth: fetchHealthMock,
  getRuntimeState: getRuntimeStateMock,
  getWorldEventSteps: getWorldEventStepsMock,
  getWorldParams: getWorldParamsMock,
  getWorldSummaries: getWorldSummariesMock,
}));

describe("DashboardPage", () => {
  beforeEach(() => {
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
});
