<template>
  <section class="projection-panel" data-test="projection-panel">
    <div class="panel-heading">
      <div>
        <span class="section-kicker">SERVER PROJECTION</span>
        <h2>权威投影</h2>
      </div>
      <a-tag v-if="projection" :color="projection.status === 'ready' ? 'green' : 'default'">
        {{ projection.status }}
      </a-tag>
    </div>

    <a-empty v-if="!projection" :image="simpleImage" description="尚未启动会话" />

    <template v-else>
      <div class="projection-metrics">
        <div class="metric-cell">
          <span>Tick</span>
          <strong data-test="projection-tick">{{ projection.tick }}</strong>
        </div>
        <div class="metric-cell">
          <span>Revision</span>
          <strong data-test="projection-revision">{{ projection.revision }}</strong>
        </div>
        <div class="metric-cell">
          <span>世界时间</span>
          <strong>{{ projection.world_time_seconds }}s</strong>
        </div>
        <div class="metric-cell">
          <span>事件游标</span>
          <strong data-test="projection-event-cursor">{{ projection.event_cursor }}</strong>
        </div>
        <div class="metric-cell">
          <span>反馈数</span>
          <strong data-test="projection-feedback-count">{{ projection.feedback_count }}</strong>
        </div>
        <div class="metric-cell">
          <span>地点数</span>
          <strong data-test="projection-location-count">{{ projection.locations.length }}</strong>
        </div>
        <div class="metric-cell">
          <span>实体数</span>
          <strong data-test="projection-entity-count">{{ projection.entities.length }}</strong>
        </div>
      </div>

      <dl class="identity-grid">
        <div>
          <dt>session_id</dt>
          <dd data-test="projection-session-id">{{ projection.session_id }}</dd>
        </div>
        <div>
          <dt>world_id</dt>
          <dd>{{ projection.world_id }}</dd>
        </div>
        <div class="identity-wide">
          <dt>source_package_hash</dt>
          <dd>{{ projection.source_package_hash }}</dd>
        </div>
        <div class="identity-wide">
          <dt>state_hash</dt>
          <dd data-test="projection-state-hash">{{ projection.state_hash }}</dd>
        </div>
      </dl>

      <div class="projection-columns">
        <section>
          <h3>状态变量</h3>
          <div class="table-scroll">
            <table>
              <thead>
                <tr>
                  <th>变量</th>
                  <th>当前值</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="([key, value]) in variableEntries" :key="key">
                  <td><code>{{ key }}</code></td>
                  <td>{{ value }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section>
          <h3>Agent 公共状态</h3>
          <div class="table-scroll">
            <table>
              <thead>
                <tr>
                  <th>Agent</th>
                  <th>位置</th>
                  <th>Cycle</th>
                  <th>决策模式</th>
                  <th>经验引用</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="agent in projection.agents" :key="agent.agent_id">
                  <td><code>{{ agent.agent_id }}</code></td>
                  <td><code>{{ agent.location_id }}</code></td>
                  <td data-test="agent-cycle-count">{{ agent.cycle_count }}</td>
                  <td data-test="agent-decision-mode">{{ agent.decision_mode }}</td>
                  <td data-test="agent-experience-count">{{ agent.experience_refs.length }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </div>

      <div class="window-row">
        <div>
          <span>当前干预窗口</span>
          <code data-test="active-window-id">{{ projection.active_intervention_window.window_id }}</code>
        </div>
        <a-tag :color="projection.active_intervention_window.status === 'open' ? 'green' : 'default'">
          {{ projection.active_intervention_window.status }} · tick
          {{ projection.active_intervention_window.open_tick }}
        </a-tag>
      </div>
    </template>
  </section>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { Empty as AEmpty, Tag as ATag } from "ant-design-vue";
import type { PublicProjection } from "../../api/engineV1";

const simpleImage = AEmpty.PRESENTED_IMAGE_SIMPLE;

const props = defineProps<{
  projection: PublicProjection | null;
}>();

const variableEntries = computed(() => Object.entries(props.projection?.variables ?? {}));
</script>

<style scoped>
.projection-panel {
  box-sizing: border-box;
  width: 100%;
  max-width: 100%;
  min-width: 0;
  padding: 20px;
  border: 1px solid #d9dee5;
  border-radius: 6px;
  background: #ffffff;
}

.panel-heading,
.window-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.panel-heading {
  margin-bottom: 16px;
}

.section-kicker {
  display: block;
  margin-bottom: 4px;
  color: #667085;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0;
}

h2,
h3,
dl,
dd {
  margin: 0;
}

h2 {
  color: #17202a;
  font-size: 20px;
  line-height: 1.35;
}

h3 {
  margin-bottom: 10px;
  color: #344054;
  font-size: 14px;
}

.projection-metrics {
  display: grid;
  grid-template-columns: repeat(7, minmax(88px, 1fr));
  border: 1px solid #e4e7ec;
  border-radius: 4px;
  background: #f8fafb;
}

.metric-cell {
  min-width: 0;
  padding: 12px 14px;
  border-right: 1px solid #e4e7ec;
}

.metric-cell:last-child {
  border-right: 0;
}

.metric-cell span {
  display: block;
  margin-bottom: 3px;
  color: #667085;
  font-size: 12px;
}

.metric-cell strong {
  color: #101828;
  font-size: 18px;
  font-variant-numeric: tabular-nums;
}

.identity-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10px 18px;
  margin-top: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid #eaecf0;
}

.identity-grid div {
  min-width: 0;
}

.identity-wide {
  grid-column: 1 / -1;
}

.identity-grid dt {
  margin-bottom: 3px;
  color: #667085;
  font-size: 11px;
}

.identity-grid dd {
  overflow: hidden;
  color: #1d2939;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 12px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.projection-columns {
  display: grid;
  grid-template-columns: minmax(220px, 0.8fr) minmax(380px, 1.2fr);
  gap: 20px;
  margin-top: 16px;
}

.projection-columns > section {
  min-width: 0;
}

.table-scroll {
  overflow-x: auto;
  border: 1px solid #e4e7ec;
  border-radius: 4px;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}

th,
td {
  padding: 8px 10px;
  border-bottom: 1px solid #eaecf0;
  text-align: left;
  white-space: nowrap;
}

th {
  color: #475467;
  background: #f8fafb;
  font-weight: 600;
}

tbody tr:last-child td {
  border-bottom: 0;
}

code {
  color: #344054;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 12px;
}

.window-row {
  margin-top: 16px;
  padding: 12px 14px;
  border-left: 3px solid #2f855a;
  background: #f4faf6;
}

.window-row span {
  display: block;
  margin-bottom: 2px;
  color: #475467;
  font-size: 12px;
}

@media (max-width: 860px) {
  .projection-metrics {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .metric-cell {
    border-bottom: 1px solid #e4e7ec;
  }

  .metric-cell:nth-child(2n) {
    border-right: 0;
  }

  .projection-columns {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 520px) {
  .projection-panel {
    padding: 14px;
  }

  .identity-grid {
    grid-template-columns: 1fr;
  }

  .identity-wide {
    grid-column: auto;
  }

  .window-row {
    align-items: flex-start;
    flex-direction: column;
  }
}
</style>
