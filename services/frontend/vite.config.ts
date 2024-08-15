import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',  // This ensures the server is accessible externally
    port: 8080,       // You can specify the port here, matching your Docker setup
  }
})
