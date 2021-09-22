import { createRouter, createWebHistory } from 'vue-router';
import Barrage from '../components/Barrage.vue';
import LineLogin from '../components/LineLogin.vue';
import LineAuth from '../components/LineAuth.vue';
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
  ],
});

export default router;
