<template>
  <a-card data-test="memory-panel" title="Memory Panel" class="memory-panel">
    <a-spin :spinning="loading">
      <a-alert v-if="error" type="error" show-icon :message="error" />
      <a-empty
        v-else-if="!summary"
        data-test="memory-summary-empty"
        description="No summaries yet. Step the simulation to generate archive data."
      />
      <div v-else data-test="memory-summary-stats">
        <a-descriptions :column="1" size="small" bordered>
          <a-descriptions-item label="Tick Range">
            {{ summary.from_tick }} - {{ summary.to_tick }}
          </a-descriptions-item>
          <a-descriptions-item label="Total Events">
            {{ summary.stats.total_events }}
          </a-descriptions-item>
          <a-descriptions-item label="Created">
            {{ summary.created_at }}
          </a-descriptions-item>
        </a-descriptions>

        <div class="summary-text">
          <a-typography-text strong>Summary</a-typography-text>
          <a-typography-paragraph data-test="memory-summary-text" class="summary-body">
            {{ summary.text }}
          </a-typography-paragraph>
        </div>

        <div v-if="Object.keys(summary.stats.type_counts).length > 0" class="type-counts">
          <a-typography-text strong>Event Types</a-typography-text>
          <div class="type-counts-grid">
            <a-tag
              v-for="(count, type) in summary.stats.type_counts"
              :key="type"
            >
              {{ type }}: {{ count }}
            </a-tag>
          </div>
        </div>
      </div>
    </a-spin>
  </a-card>
</template>

<script setup lang="ts">
import {
  Alert as AAlert,
  Card as ACard,
  Descriptions as ADescriptions,
  DescriptionsItem as ADescriptionsItem,
  Empty as AEmpty,
  Spin as ASpin,
  Tag as ATag,
  TypographyParagraph as ATypographyParagraph,
  TypographyText as ATypographyText,
} from "ant-design-vue";
import type { WorldSummary } from "../api/client";

defineProps<{
  summary: WorldSummary | null;
  loading: boolean;
  error: string;
}>();
</script>

<style scoped>
.summary-text {
  margin-top: 12px;
}

.summary-body {
  margin-top: 4px;
  padding: 8px 12px;
  background: #f5f5f5;
  border-radius: 4px;
  white-space: pre-wrap;
}

.type-counts {
  margin-top: 12px;
}

.type-counts-grid {
  margin-top: 4px;
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}
</style>
