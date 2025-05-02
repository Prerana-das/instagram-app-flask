import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Profile from './pages/Profile.vue'
import Settings from './pages/Settings.vue'

const router = createRouter({
  history: createWebHistory(),
  // history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/settings',
      name: 'Settings',
      component: Settings
    },
  ]
})

export default router