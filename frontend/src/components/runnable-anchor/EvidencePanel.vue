<template>
  <section class="evidence-panel" data-test="evidence-panel">
    <div class="panel-heading">
      <div>
        <span class="section-kicker">PUBLIC EVIDENCE</span>
        <h2>证据检查台</h2>
      </div>
      <a-space wrap>
        <a-tag
          v-if="evidence"
          data-test="evidence-status"
          :color="evidenceStatusColor"
        >
          完整性 {{ evidence.completeness.integrity.status }} · 场景
          {{ evidence.completeness.scenario_coverage.status }}
        </a-tag>
        <a-button
          data-test="refresh-evidence"
          :disabled="!canRefresh || loading"
          :loading="loading"
          @click="$emit('refresh')"
        >
          刷新证据
        </a-button>
        <a-button
          data-test="download-evidence"
          type="primary"
          :disabled="!canRefresh || !evidence"
          :loading="loading"
          @click="$emit('download')"
        >
          导出 JSON
        </a-button>
      </a-space>
    </div>

    <a-empty v-if="!evidence" :image="simpleImage" description="尚无会话证据" />

    <template v-else>
      <div class="evidence-metrics">
        <div><span>事件</span><strong data-test="event-count">{{ displayEvents.length }}</strong></div>
        <div><span>Diff</span><strong data-test="diff-count">{{ evidence.diffs.length }}</strong></div>
        <div><span>Snapshot</span><strong data-test="snapshot-count">{{ evidence.snapshots.length }}</strong></div>
        <div><span>Agent Cycle</span><strong data-test="evidence-agent-cycle-count">{{ evidence.agent_cycles.length }}</strong></div>
        <div><span>方向判定</span><strong data-test="direction-count">{{ evidence.direction_decisions.length }}</strong></div>
      </div>

      <div class="completeness-strip">
        <span
          v-for="([name, passed]) in completenessChecks"
          :key="name"
          class="check-item"
          :class="{ failed: !passed }"
        >
          <b>{{ passed ? "通过" : "缺失" }}</b>{{ name }}
        </span>
      </div>

      <a-tabs v-model:active-key="activeTab" class="evidence-tabs" size="small">
        <a-tab-pane key="events" :tab="`事件 ${displayEvents.length}`">
          <div class="table-scroll">
            <table data-test="events-table">
              <thead>
                <tr>
                  <th>Seq</th>
                  <th>Tick / Rev</th>
                  <th>状态</th>
                  <th>事件</th>
                  <th>来源</th>
                  <th>request_id</th>
                  <th>Diff</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="event in displayEvents" :key="event.event_id">
                  <td>{{ event.sequence }}</td>
                  <td>{{ event.tick }} / {{ event.revision }}</td>
                  <td><StatusTag :status="event.status" /></td>
                  <td><code>{{ event.event_type }}</code></td>
                  <td>{{ event.source }}</td>
                  <td><code>{{ event.request_id }}</code></td>
                  <td>{{ event.diff_refs.length }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </a-tab-pane>

        <a-tab-pane key="diffs" :tab="`Diff ${evidence.diffs.length}`">
          <div class="record-list" data-test="diff-list">
            <article v-for="diff in evidence.diffs" :key="diff.diff_id" class="record-row">
              <div class="record-head">
                <code>{{ diff.diff_id }}</code>
                <span>tick {{ diff.tick }} · rev {{ diff.revision }}</span>
              </div>
              <ul>
                <li v-for="operation in diff.operations" :key="`${diff.diff_id}-${operation.path}`">
                  <code>{{ operation.path }}</code>
                  <span>{{ formatValue(operation.before) }} → {{ formatValue(operation.after) }}</span>
                </li>
              </ul>
            </article>
          </div>
        </a-tab-pane>

        <a-tab-pane key="snapshots" :tab="`Snapshot ${evidence.snapshots.length}`">
          <div class="record-list" data-test="snapshot-list">
            <article
              v-for="snapshot in [...evidence.snapshots].reverse()"
              :key="snapshot.snapshot_id"
              class="record-row"
            >
              <div class="record-head">
                <code>{{ snapshot.snapshot_id }}</code>
                <span>tick {{ snapshot.tick }} · rev {{ snapshot.revision }}</span>
              </div>
              <div class="hash-line">{{ snapshot.state_hash }}</div>
              <pre>{{ stringify(snapshot.canonical_state) }}</pre>
            </article>
          </div>
        </a-tab-pane>

        <a-tab-pane key="agent" :tab="`Agent ${evidence.agent_cycles.length}`">
          <a-empty v-if="!latestAgentCycle" :image="simpleImage" description="尚无 Agent cycle" />
          <template v-else>
            <div class="agent-chain-heading">
              <div>
                <strong>{{ latestAgentCycle.agent_id }}</strong>
                <span>{{ latestAgentCycle.cycle_id }} · tick {{ latestAgentCycle.tick }}</span>
              </div>
              <a-tag :color="latestAgentCycle.experience_refs_used.length ? 'green' : 'default'">
                经验引用 {{ latestAgentCycle.experience_refs_used.length }}
              </a-tag>
            </div>
            <div class="causal-chain" data-test="agent-causal-chain">
              <section><h3>感知</h3><pre>{{ stringify(latestAgentCycle.perception) }}</pre></section>
              <section><h3>决策</h3><pre>{{ stringify(latestAgentCycle.decision) }}</pre></section>
              <section><h3>ActionRequest</h3><pre>{{ stringify(latestAgentCycle.action_request) }}</pre></section>
              <section><h3>规则判定</h3><pre>{{ stringify(latestAgentCycle.rule_judgment) }}</pre></section>
              <section><h3>ActionResult</h3><pre>{{ stringify(latestAgentCycle.action_result) }}</pre></section>
              <section><h3>ExperienceRef</h3><pre>{{ stringify(latestAgentCycle.experience_refs_used) }}</pre></section>
            </div>
          </template>
        </a-tab-pane>

        <a-tab-pane key="directions" :tab="`方向 ${evidence.direction_decisions.length}`">
          <div class="table-scroll">
            <table data-test="direction-table">
              <thead>
                <tr>
                  <th>状态</th>
                  <th>应用状态</th>
                  <th>window_id</th>
                  <th>reason_code</th>
                  <th>event_ref</th>
                  <th>Diff</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="decision in evidence.direction_decisions" :key="decision.request_id">
                  <td><StatusTag :status="decision.status" /></td>
                  <td>
                    <code>{{ decision.application_status }}</code>
                    <small v-if="decision.application_reason_code">
                      {{ decision.application_reason_code }}
                    </small>
                  </td>
                  <td><code>{{ decision.window_id }}</code></td>
                  <td><code>{{ decision.reason_code }}</code></td>
                  <td><code>{{ decision.event_ref }}</code></td>
                  <td>{{ decision.applied_diff_refs.length }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </a-tab-pane>
      </a-tabs>
    </template>
  </section>
</template>

<script setup lang="ts">
import { computed, defineComponent, h, ref } from "vue";
import {
  Button as AButton,
  Empty as AEmpty,
  Space as ASpace,
  TabPane as ATabPane,
  Tabs as ATabs,
  Tag as ATag,
} from "ant-design-vue";
import type { EventPage, EvidenceBundle } from "../../api/engineV1";

defineEmits<{
  refresh: [];
  download: [];
}>();

const props = defineProps<{
  eventPage: EventPage | null;
  evidence: EvidenceBundle | null;
  loading: boolean;
  canRefresh: boolean;
}>();

const simpleImage = AEmpty.PRESENTED_IMAGE_SIMPLE;
const activeTab = ref("events");

const displayEvents = computed(() => props.eventPage?.items ?? props.evidence?.events ?? []);
const completenessChecks = computed(() => {
  const completeness = props.evidence?.completeness;
  if (!completeness) {
    return [];
  }
  return [
    ...Object.entries(completeness.integrity.checks).map(
      ([name, passed]) => [`完整性/${name}`, passed] as const,
    ),
    ...Object.entries(completeness.scenario_coverage.checks).map(
      ([name, passed]) => [`场景/${name}`, passed] as const,
    ),
  ];
});
const evidenceStatusColor = computed(() => {
  const completeness = props.evidence?.completeness;
  if (!completeness || completeness.integrity.status === "invalid") {
    return "red";
  }
  return completeness.scenario_coverage.status === "covered" ? "green" : "orange";
});
const latestAgentCycle = computed(() => {
  const cycles = props.evidence?.agent_cycles ?? [];
  return cycles.length > 0 ? cycles[cycles.length - 1] : null;
});

const StatusTag = defineComponent({
  props: { status: { type: String, required: true } },
  setup(componentProps) {
    return () =>
      h(
        ATag,
        { color: componentProps.status === "accepted" ? "green" : "red" },
        () => componentProps.status,
      );
  },
});

function stringify(value: unknown): string {
  return JSON.stringify(value, null, 2);
}

function formatValue(value: unknown): string {
  if (typeof value === "string") {
    return value;
  }
  return JSON.stringify(value);
}
</script>

<style scoped>
.evidence-panel {
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
.record-head,
.agent-chain-heading {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.panel-heading {
  margin-bottom: 16px;
}

.panel-heading > * {
  min-width: 0;
  max-width: 100%;
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
h3 {
  margin: 0;
}

h2 {
  color: #17202a;
  font-size: 20px;
  line-height: 1.35;
}

h3 {
  margin-bottom: 8px;
  color: #344054;
  font-size: 12px;
}

.evidence-metrics {
  display: grid;
  grid-template-columns: repeat(5, minmax(90px, 1fr));
  border: 1px solid #e4e7ec;
  border-radius: 4px;
  background: #f8fafb;
}

.evidence-metrics div {
  padding: 10px 12px;
  border-right: 1px solid #e4e7ec;
}

.evidence-metrics div:last-child {
  border-right: 0;
}

.evidence-metrics span {
  display: block;
  color: #667085;
  font-size: 11px;
}

.evidence-metrics strong {
  color: #101828;
  font-size: 18px;
  font-variant-numeric: tabular-nums;
}

.completeness-strip {
  display: flex;
  overflow-x: auto;
  gap: 8px;
  margin: 14px 0 4px;
  padding-bottom: 4px;
}

.check-item {
  display: inline-flex;
  align-items: center;
  flex: 0 0 auto;
  gap: 5px;
  padding: 4px 7px;
  border: 1px solid #b7dbc4;
  border-radius: 3px;
  color: #356246;
  background: #f4faf6;
  font-size: 11px;
}

.check-item b {
  font-weight: 700;
}

.check-item.failed {
  border-color: #f3c4a8;
  color: #9a4e13;
  background: #fff8f1;
}

.evidence-tabs {
  min-width: 0;
  margin-top: 6px;
}

.evidence-tabs :deep(.ant-tabs-nav-wrap) {
  max-width: 100%;
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

code,
pre,
.hash-line {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}

code {
  color: #344054;
  font-size: 11px;
}

.record-list {
  display: grid;
  gap: 10px;
  max-height: 520px;
  overflow-y: auto;
}

.record-row {
  padding: 12px;
  border: 1px solid #e4e7ec;
  border-radius: 4px;
  background: #ffffff;
}

.record-head span {
  color: #667085;
  font-size: 11px;
}

.record-row ul {
  margin: 10px 0 0;
  padding: 0;
  list-style: none;
}

.record-row li {
  display: grid;
  grid-template-columns: minmax(130px, 0.7fr) minmax(180px, 1.3fr);
  gap: 12px;
  padding: 5px 0;
  border-top: 1px solid #f0f2f5;
  color: #475467;
  font-size: 11px;
}

.hash-line {
  overflow: hidden;
  margin-top: 8px;
  color: #667085;
  font-size: 10px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

pre {
  max-height: 210px;
  margin: 8px 0 0;
  padding: 10px;
  overflow: auto;
  color: #344054;
  background: #f8fafb;
  font-size: 10px;
  line-height: 1.55;
  white-space: pre-wrap;
  word-break: break-word;
}

.agent-chain-heading {
  margin-bottom: 12px;
}

.agent-chain-heading div {
  min-width: 0;
}

.agent-chain-heading strong,
.agent-chain-heading span {
  display: block;
}

.agent-chain-heading span {
  margin-top: 2px;
  color: #667085;
  font-size: 11px;
}

.causal-chain {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  border-top: 1px solid #e4e7ec;
  border-left: 1px solid #e4e7ec;
}

.causal-chain section {
  min-width: 0;
  padding: 10px;
  border-right: 1px solid #e4e7ec;
  border-bottom: 1px solid #e4e7ec;
  background: #ffffff;
}

.causal-chain pre {
  height: 150px;
  margin: 0;
}

@media (max-width: 760px) {
  .panel-heading {
    align-items: flex-start;
    flex-direction: column;
  }

  .evidence-metrics {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .evidence-metrics div {
    border-bottom: 1px solid #e4e7ec;
  }

  .evidence-metrics div:nth-child(2n) {
    border-right: 0;
  }

  .causal-chain {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 520px) {
  .evidence-panel {
    padding: 14px;
  }

  .record-row li {
    grid-template-columns: 1fr;
    gap: 3px;
  }
}
</style>
