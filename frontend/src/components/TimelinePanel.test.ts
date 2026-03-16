import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import TimelinePanel from "./TimelinePanel.vue";

describe("TimelinePanel", () => {
  it("renders step summary for module events", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        steps: [
          {
            tick_id: 1,
            world_time_seconds: 600,
            created_at: "2026-03-09T00:10:00+00:00",
            event_count: 1,
            items: [
              {
                id: "evt-1",
                tick_id: 1,
                world_time_seconds: 600,
                type: "module.counter",
                source: "root.counter",
                payload: {
                  module_path: "root.counter",
                  counter: 1,
                },
                created_at: "2026-03-09T00:10:00+00:00",
              },
            ],
          },
        ],
      },
    });

    expect(wrapper.text()).toContain("module.counter x1");
    expect(wrapper.text()).toContain("1 events");
    expect(wrapper.text()).toContain("Page size");
  });

  it("renders counter values and current page state", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        steps: [
          {
            tick_id: 3,
            world_time_seconds: 1800,
            created_at: "2026-03-09T00:30:00+00:00",
            event_count: 1,
            items: [
              {
                id: "evt-counter",
                tick_id: 3,
                world_time_seconds: 1800,
                type: "module.counter",
                source: "root.counter",
                payload: {
                  module_path: "root.counter",
                  counter: 3,
                },
                created_at: "2026-03-09T00:30:00+00:00",
              },
            ],
          },
        ],
        currentPage: 3,
      },
    });

    const vm = wrapper.vm as unknown as {
      formatDetails: (event: {
        payload: Record<string, unknown>;
        type: string;
      }) => string;
      summarizeStep: (step: {
        items: Array<{ type: string }>;
      }) => string;
    };

    expect(
      vm.formatDetails({
        type: "module.counter",
        payload: {
          module_path: "root.counter",
          counter: 3,
        },
      }),
    ).toContain("counter=3");
    expect(
      vm.summarizeStep({
        items: [
          { type: "tick.advanced" },
          { type: "module.counter" },
          { type: "module.counter" },
        ],
      }),
    ).toContain("module.counter x2");
    expect(wrapper.text()).toContain("Page 3");
    expect(wrapper.text()).toContain("Newest first");
  });

  it("keeps long timeline rows in the table markup", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        steps: [
          {
            tick_id: 2,
            world_time_seconds: 1200,
            created_at: "2026-03-09T00:20:00+00:00",
            event_count: 1,
            items: [
              {
                id: "evt-2",
                tick_id: 2,
                world_time_seconds: 1200,
                type: "module.aggregate",
                source: "root",
                payload: {
                  module_path: "root.really.long.module.path.that.should.wrap.cleanly",
                },
                created_at: "2026-03-09T00:20:00+00:00",
              },
            ],
          },
        ],
      },
    });

    expect(wrapper.find(".timeline-table").exists()).toBe(true);
    expect(
      (wrapper.vm as unknown as { formatDetails: (event: { payload: Record<string, unknown>; type: string }) => string }).formatDetails({
        type: "module.aggregate",
        payload: {
          module_path: "root.really.long.module.path.that.should.wrap.cleanly",
        },
      }),
    ).toContain("root.really.long.module.path.that.should.wrap.cleanly");
  });

  it("emits pagination and page-size change events", async () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        steps: [
          {
            tick_id: 4,
            world_time_seconds: 2400,
            created_at: "2026-03-09T00:40:00+00:00",
            event_count: 1,
            items: [
              {
                id: "evt-4",
                tick_id: 4,
                world_time_seconds: 2400,
                type: "tick.advanced",
                source: "system",
                payload: {},
                created_at: "2026-03-09T00:40:00+00:00",
              },
            ],
          },
        ],
        canPrevious: true,
        hasMore: true,
        pageSize: 20,
      },
    });

    await wrapper.get("[data-test='timeline-prev-page']").trigger("click");
    await wrapper.get("[data-test='timeline-next-page']").trigger("click");
    await wrapper.get("[data-test='timeline-page-size']").setValue("50");

    expect(wrapper.emitted("previous-page")).toHaveLength(1);
    expect(wrapper.emitted("next-page")).toHaveLength(1);
    expect(wrapper.emitted("page-size-change")).toEqual([[50]]);
  });
});
