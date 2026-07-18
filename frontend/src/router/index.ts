import { createRouter, createWebHistory } from "vue-router";
import DashboardPage from "../pages/DashboardPage.vue";
import RunnableAnchorPage from "../pages/RunnableAnchorPage.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: DashboardPage,
    },
    {
      path: "/admin/runnable-anchor",
      name: "runnable-anchor",
      component: RunnableAnchorPage,
    },
  ],
});

export default router;
