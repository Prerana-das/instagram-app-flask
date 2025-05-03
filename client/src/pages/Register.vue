<template>
  <div class="min-h-screen bg-black text-white flex items-center justify-center px-4">
    <form @submit.prevent="handleRegister" class="bg-gray-900 p-6 rounded-lg w-full max-w-md space-y-4">
      <h2 class="text-2xl font-bold text-center mb-4">Register</h2>

      <input v-model="form.name" type="text" placeholder="Full Name" class="form-field" required />
      <input v-model="form.username" type="text" placeholder="Username" class="form-field" required />
      <input v-model="form.email" type="email" placeholder="Email" class="form-field" required />
      <input v-model="form.password" type="password" placeholder="Password" class="form-field" required />

      <button type="submit" class="w-full bg-red-600 hover:bg-red-700 py-2 rounded-lg font-semibold">Sign Up</button>

      <p class="text-center text-sm text-gray-400">
        Already have an account? <router-link to="/login" class="text-blue-400 hover:underline">Login</router-link>
      </p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  name: '',
  username: '',
  email: '',
  password: '',
})

async function handleRegister() {
  const res = await fetch('/api/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(form.value),
  })

  const data = await res.json()
  if (res.ok) {
    alert('Registered successfully!')
    router.push('/login')
  } else {
    alert(data.error || 'Registration failed.')
  }
}
</script>

<style scoped>
.form-field {
  @apply w-full p-3 rounded-lg bg-gray-800 border border-gray-700 placeholder-gray-400 text-white;
}
</style>
