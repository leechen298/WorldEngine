import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

import DashboardPage from "./DashboardPage.vue";

const { fetchHealthMock, getRuntimeStateMock } = vi.hoisted(() => ({
  fetchHealthMock: vi.fn(),
  getRuntimeStateMock: vi.fn(),
}));

vi.mock("../api/client", () => ({
  fetchHealth: fetchHealthMock,
  getRuntimeState: getRuntimeStateMock,
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
        },
      },
    });

    await flushPromises();

    expect(fetchHealthMock).toHaveBeenCalledTimes(1);
    expect(getRuntimeStateMock).toHaveBeenCalledTimes(1);
    expect(wrapper.text()).toContain("ok (worldengine-backend)");
    expect(wrapper.text()).toContain("tick_id=3");
    expect(wrapper.text()).toContain("updated_at=2026-03-09T00:00:00+00:00");
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

    await wrapper.get("[data-test='runtime-controls']").trigger("click");
    await flushPromises();

    expect(getRuntimeStateMock).toHaveBeenCalledTimes(2);
    expect(wrapper.text()).toContain("tick_id=4");
  });
});
