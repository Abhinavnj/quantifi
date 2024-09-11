import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Analysis from '../views/Analysis.vue';
import Contact from '../views/Contact.vue';
import AnalysisHome from '../views/AnalysisHome.vue';
import LearnHome from '../views/LearnHome.vue';
import PersonalFinance from '../views/PersonalFinance.vue';
import About from '../views/About.vue';

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
    component: PersonalFinance,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
