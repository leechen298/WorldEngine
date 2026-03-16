<template>
  <a-card title="Timeline Panel">
    <a-spin :spinning="loading">
      <a-alert v-if="error" type="error" show-icon :message="error" />
      <a-empty v-else-if="events.length === 0" description="No events yet." />
      <a-list v-else item-layout="vertical" :data-source="events" class="timeline-list">
        <template #renderItem="{ item }">
          <a-list-item :key="item.id" class="timeline-item">
            <a-space wrap :size="[8, 8]">
              <a-tag color="blue">#{{ item.tick_id }}</a-tag>
              <a-tag>{{ item.type }}</a-tag>
              <a-typography-text v-if="item.payload?.module_path" code>
                [{{ item.payload.module_path }}]
              </a-typography-text>
              <a-typography-text
                v-if="item.type === 'module.counter' && item.payload?.counter !== undefined"
              >
                counter={{ item.payload.counter }}
              </a-typography-text>
              <a-typography-text type="secondary">
                {{ item.created_at }}
              </a-typography-text>
            </a-space>
          </a-list-item>
        </template>
      </a-list>
    </a-spin>
  </a-card>
</template>

<script setup lang="ts">
import {
  Alert as AAlert,
  Card as ACard,
  Empty as AEmpty,
  List as AList,
  ListItem as AListItem,
  Space as ASpace,
  Spin as ASpin,
  Tag as ATag,
  TypographyText as ATypographyText,
} from "ant-design-vue";
import type { WorldEvent } from "../api/client";

defineProps<{
  events: WorldEvent[];
  loading?: boolean;
  error?: string;
}>();
</script>

<style scoped>
.timeline-list {
  margin-top: 4px;
}

.timeline-item {
  min-width: 0;
  overflow-wrap: anywhere;
  word-break: break-word;
}
</style>
