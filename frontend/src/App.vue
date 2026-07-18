<template>
  <a-layout class="app-shell">
    <a-layout-header class="app-header">
      <div class="app-brand">WorldEngine</div>
      <nav class="app-nav" aria-label="Primary navigation">
        <RouterLink to="/admin/runnable-anchor">可运行锚点</RouterLink>
        <RouterLink to="/">历史控制台</RouterLink>
      </nav>
    </a-layout-header>
    <a-layout-content class="app-content">
      <RouterView />
    </a-layout-content>
  </a-layout>
</template>

<script setup lang="ts">
import {
  Layout as ALayout,
  LayoutContent as ALayoutContent,
  LayoutHeader as ALayoutHeader,
} from "ant-design-vue";
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
.app-shell {
  min-height: 100vh;
  background: #f4f6f8;
}

.app-header {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: 32px;
  height: 52px;
  padding: 0 24px;
  border-bottom: 1px solid #d8dde3;
  background: #ffffff;
  line-height: 1;
}

.app-brand {
  color: #17212b;
  font-size: 16px;
  font-weight: 700;
}

.app-nav {
  display: flex;
  align-items: stretch;
  gap: 24px;
  height: 100%;
}

.app-nav a {
  display: inline-flex;
  align-items: center;
  border-bottom: 2px solid transparent;
  color: #52606d;
  font-size: 14px;
}

.app-nav a.router-link-active {
  border-bottom-color: #1677ff;
  color: #102a43;
  font-weight: 600;
}

.app-content {
  min-width: 0;
}

@media (max-width: 640px) {
  .app-header {
    gap: 18px;
    padding: 0 14px;
  }

  .app-nav {
    gap: 14px;
  }
}
</style>
