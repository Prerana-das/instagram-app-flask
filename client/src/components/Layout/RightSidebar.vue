<template>
  <aside class="w-80 h-screen fixed top-0 right-0 bg-black text-white p-4 flex flex-col border-l border-gray-800">
    <!-- Logged-in user info -->
    <div v-if="user" class="flex items-center gap-4 mb-6">
      <img
        v-if="user.profile"
        :src="user.profile"
        alt="User Profile"
        class="h-12 w-12 rounded-full object-cover"
      />
      <div v-else class="bg-gray-700 h-12 w-12 rounded-full"></div>
      <div class="flex flex-col">
        <p class="font-semibold">{{ user.username }}</p>
        <p class="text-sm text-gray-400">{{ user.name }}</p>
      </div>
    </div>

    <!-- Followers Section -->
    <h2 class="text-lg font-bold mb-4">All Followers</h2>
    <div class="flex flex-col gap-6 overflow-y-auto">
      <div v-for="follower in followers" :key="follower.id" class="flex items-center gap-4">
        <img
          v-if="follower.profile"
          :src="follower.profile"
          alt="Follower Profile"
          class="h-12 w-12 rounded-full object-cover"
        />
        <div v-else class="bg-gray-700 h-12 w-12 rounded-full"></div>
        <div class="flex flex-col">
          <p class="font-semibold">{{ follower.username }}</p>
          <p class="text-sm text-gray-400">{{ follower.name }}</p>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const user = ref(null)
const followers = ref([])
const isLoading = ref(true)

async function fetchSessionUser() {
  try {
    const res = await fetch('/api/session')
    if (res.ok) {
      user.value = await res.json()
    } else {
      console.error('Failed to fetch session user')
    }
  } catch (error) {
    console.error('Error fetching session user:', error)
  }
}

async function fetchFollowers(userId) {
  try {
    const res = await fetch(`/api/followers/${userId}`)
    const data = await res.json()
    if (res.ok) {
      followers.value = data.followers
    } else {
      alert('Error fetching followers')
    }
  } catch (error) {
    console.error('Error fetching followers:', error)
    alert('There was an error fetching the followers.')
  } finally {
    isLoading.value = false
  }
}

onMounted(async () => {
  await fetchSessionUser()
})

// Automatically fetch followers after user is loaded
watch(user, (newUser) => {
  if (newUser?.id) {
    fetchFollowers(newUser.id)
  }
})
</script>
