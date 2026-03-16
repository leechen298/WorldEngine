import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import TimelinePanel from "./TimelinePanel.vue";

describe("TimelinePanel", () => {
  it("renders module_path when present in the event payload", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        events: [
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
    });

    expect(wrapper.text()).toContain("module.counter");
    expect(wrapper.text()).toContain("[root.counter]");
  });

  it("renders counter values for module.counter events", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        events: [
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
    });

    expect(wrapper.text()).toContain("counter=3");
  });

  it("keeps long timeline rows in wrap-enabled markup", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        events: [
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
    });

    expect(wrapper.find(".timeline-list").exists()).toBe(true);
    expect(wrapper.get(".timeline-item").classes()).toContain("timeline-item");
    expect(wrapper.text()).toContain("root.really.long.module.path.that.should.wrap.cleanly");
  });
});
