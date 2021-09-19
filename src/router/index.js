import { createRouter, createWebHistory } from 'vue-router';
import Barrage from '../components/Barrage.vue';
import Setting from '../components/Setting.vue';
import Line from '../components/Line.vue';
const routerHistory = createWebHistory();

const router = createRouter({
  history: routerHistory,
  routes: [
    {
      path: '/',
      component: Barrage,
    },
    {
      path: '/line',
      component: Setting,
    },
    {
      path: '/line/auth',
      component: Line,
    },
  ],
});

export default router;
