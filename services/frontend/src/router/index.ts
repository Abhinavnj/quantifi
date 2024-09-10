import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Analysis from '../views/Analysis.vue';
import Contact from '../views/Contact.vue';
import AnalysisHome from '../views/AnalysisHome.vue';
import LearnHome from '../views/LearnHome.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/analysis/:symbol',
    name: 'Analysis',
    component: Analysis,
    props: true, // Pass route params as props
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact,
  },
  {
    path: '/analysis',
    name: 'AnalysisHome',
    component: AnalysisHome,
  },
  {
    path: '/learn',
    name: 'LearnHome',
    component: LearnHome,
  },
  {
    path: '/personalfinance',
    name: 'PersonalFinance',
    component: LearnHome,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
