<template>
  <div class="min-h-screen bg-black text-white flex items-center justify-center px-4">
    <form @submit.prevent="handleLogin" class="bg-gray-900 p-6 rounded-lg w-full max-w-md space-y-4">
      <h2 class="text-2xl font-bold text-center mb-4">Login</h2>

      <input v-model="form.email" type="email" placeholder="Email" class="form-field" required />
      <input v-model="form.password" type="password" placeholder="Password" class="form-field" required />

      <button type="submit" class="w-full bg-red-600 hover:bg-red-700 py-2 rounded-lg font-semibold">Login</button>

      <p class="text-center text-sm text-gray-400">
        Don’t have an account? <router-link to="/register" class="text-blue-400 hover:underline">Register</router-link>
      </p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  email: '',
  password: '',
})

async function handleLogin() {
  const res = await fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(form.value),
  })

  const data = await res.json()
  if (res.ok) {
    localStorage.setItem('token', data.token) // store token
    alert('Login successful!')
    router.push('/') // redirect to home or dashboard
  } else {
    alert(data.error || 'Login failed.')
  }
}
</script>

<style scoped>
.form-field {
  @apply w-full p-3 rounded-lg bg-gray-800 border border-gray-700 placeholder-gray-400 text-white;
}
</style>
