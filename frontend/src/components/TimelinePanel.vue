<template>
  <section class="panel">
    <h2>Timeline Panel</h2>
    <p v-if="error" class="timeline-error">{{ error }}</p>
    <p v-else-if="loading">Loading events...</p>
    <p v-else-if="events.length === 0">No events yet.</p>
    <ul v-else class="timeline-list">
      <li v-for="event in events" :key="event.id" class="timeline-item">
        <strong>#{{ event.tick_id }}</strong>
        <span>{{ event.type }}</span>
        <span>{{ event.created_at }}</span>
      </li>
    </ul>
  </section>
</template>

<script setup lang="ts">
import type { WorldEvent } from "../api/client";

defineProps<{
  events: WorldEvent[];
  loading?: boolean;
  error?: string;
}>();
</script>
