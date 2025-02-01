import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Pricing from '../views/Pricing.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/pricing',
      name: 'pricing',
      component: Pricing,
    },
  ],
});

export default router;