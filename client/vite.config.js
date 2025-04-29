import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  build: {
    outDir: '../client/dist',  // 👈 Build into Flask's static folder
    emptyOutDir: true,
  }, 
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  // Flask backend
  server: {
    port: 5000, //
    proxy: {
      '/api': {
        target: 'http://localhost:5001', // Flask is now on same port
        changeOrigin: true,
      }
    }
  },
})

