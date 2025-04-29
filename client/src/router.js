import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Profile from './pages/Profile.vue'

const routes = [
  {
    path: '/', // Route for Home page
    name: 'home',
    component: Home
  },
  {
    path: '/profile', // Route for Profile page
    name: 'profile',
    component: Profile
  }
  // Add more routes here as needed
]

const router = createRouter({
  history: createWebHistory(import.meta.env.VITE_BASE_URL),
  routes
})

export default router
