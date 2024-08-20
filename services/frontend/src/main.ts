import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios';
import App from './App.vue'
import './index.css'
import router from './router'

const pinia = createPinia()
const app = createApp(App)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5001/';

app.use(pinia)
app.use(router)
app.mount('#app')