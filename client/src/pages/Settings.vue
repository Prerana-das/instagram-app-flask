<template>
  <LayoutWrapper>
    <div class="max-w-xl mx-auto text-white">
      <h1 class="text-2xl font-bold mb-6">User Settings</h1>

      <form @submit.prevent="updateProfile" class="flex flex-col gap-4 bg-neutral-900 p-6 rounded-lg shadow">
        <div>
          <label class="block mb-1 text-sm">Name</label>
          <input
            v-model="name"
            type="text"
            class="w-full p-2 rounded bg-neutral-800 border border-neutral-600 text-white"
            required
          />
        </div>

        <div>
          <label class="block mb-1 text-sm">Location</label>
          <input
            v-model="location"
            type="text"
            class="w-full p-2 rounded bg-neutral-800 border border-neutral-600 text-white"
          />
        </div>

        <div>
          <label class="block mb-1 text-sm">Profile Image</label>
          <input
            type="file"
            accept="image/*"
            @change="handleFileChange"
            class="text-sm text-gray-300"
          />
          <div v-if="preview" class="mt-2">
            <img :src="preview" alt="Preview" class="h-20 w-20 rounded-full object-cover" />
          </div>
        </div>

        <button
          type="submit"
          class="bg-blue-600 hover:bg-blue-700 transition-colors text-white font-semibold py-2 px-4 rounded"
          :disabled="isLoading"
        >
          {{ isLoading ? 'Updating...' : 'Update Profile' }}
        </button>
      </form>
    </div>
  </LayoutWrapper>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LayoutWrapper from '@/components/Layout/LayoutWrapper.vue'

const name = ref('')
const location = ref('')
const profileImage = ref(null)
const preview = ref('')
const isLoading = ref(false)

onMounted(async () => {
  const res = await fetch('/api/session')
  const data = await res.json()
  if (res.ok) {
    name.value = data.name
    location.value = data.location || ''
    preview.value = data.profile || ''
  } else {
    window.location.href = '/login'
  }
})

function handleFileChange(event) {
  const file = event.target.files[0]
  if (file) {
    profileImage.value = file
    preview.value = URL.createObjectURL(file)
  }
}

async function updateProfile() {
  isLoading.value = true
  const formData = new FormData()
  formData.append('name', name.value)
  formData.append('location', location.value)
  if (profileImage.value) {
    formData.append('profile', profileImage.value)
  }

  const res = await fetch('/api/update-profile', {
    method: 'POST',
    body: formData,
  })

  const data = await res.json()
  isLoading.value = false

  if (res.ok) {
    alert('Profile updated successfully')
  } else {
    alert(data.error || 'Failed to update profile')
  }
}
</script>
