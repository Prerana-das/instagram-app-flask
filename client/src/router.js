import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Profile from './pages/Profile.vue'
import Settings from './pages/Settings.vue'
import CreatePost from './pages/CreatePost.vue'
import Register from './pages/Register.vue'
import Login from './pages/Login.vue'
import Message from './pages/Message.vue'

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
  },
  {
    path: '/settings', // Route for Profile page
    name: 'Settings',
    component: Settings
  },
  {
    path: '/create', 
    name: 'CreatePost',
    component: CreatePost
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/message',
    name: 'Message',
    component: Message
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.VITE_BASE_URL),
  routes
})

export default router