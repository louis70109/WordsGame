import { createRouter, createWebHistory } from 'vue-router';
import Barrage from '../components/Barrage.vue';
import LineLogin from '../components/LineLogin.vue';
import LineAuth from '../components/LineAuth.vue';
import Record from '../components/Record.vue';
const routerHistory = createWebHistory();

const router = createRouter({
  history: routerHistory,
  routes: [
    {
      path: '/barrage',
      component: Barrage,
    },
    {
      path: '/line',
      component: LineLogin,
    },
    {
      path: '/line/auth',
      component: LineAuth,
    },
    {
      path: '/record',
      component: Record,
    },
  ],
});

export default router;
