import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import axios from 'axios';
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5001/';  // the FastAPI backend

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.mount('#app')