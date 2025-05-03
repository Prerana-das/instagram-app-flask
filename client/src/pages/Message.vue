<template>
  <LayoutWrapper>
    <div class="bg-black text-white min-h-screen px-6 py-10 max-w-4xl mx-auto">
      <!-- Message Header -->
      <div class="flex items-center gap-10 mb-10">
        <!-- Message Picture -->
        
        <img
          v-if="user.message !== null && user.message !== undefined"
          class="w-24 h-24 rounded-full object-cover border border-gray-600"
          :src="user.message || 'https://via.placeholder.com/150'"
          alt="Message"
        />
        <div v-else class="bg-gray-700 h-12 w-12 rounded-full"></div> 
        

        <!-- User Info -->
        <div>
          <h2 class="text-2xl font-bold">{{ user.username }}</h2>
          <div class="flex gap-6 mt-2 text-sm text-gray-400">
            <span><strong>{{ posts.length }}</strong> posts</span>
            <span><strong>{{ user.followers }}</strong> followers</span>
            <span><strong>{{ user.following }}</strong> following</span>
          </div>
          <p class="mt-2 text-gray-300">{{ user.bio }}</p>
        </div>
      </div>

      <!-- Posts Grid -->
      <div v-if="posts.length" class="grid grid-cols-3 gap-4">
        <div
          v-for="post in posts"
          :key="post.id"
          class="relative group cursor-pointer aspect-square overflow-hidden"
        >
          <img
            :src="post.image_url"
            alt="Post"
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
          />
          <!-- Optional overlay -->
          <div
            class="absolute inset-0 bg-black bg-opacity-30 hidden group-hover:flex items-center justify-center text-white"
          >
            <p class="text-sm font-medium px-2 text-center">{{ post.caption }}</p>
          </div>
        </div>
      </div>

      <div v-else class="text-center text-gray-500 mt-10">No posts yet.</div>
    </div>
  </LayoutWrapper>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import LayoutWrapper from '@/components/Layout/LayoutWrapper.vue'

const user = ref(null)
const posts = ref([])

const fetchUserData = async () => {
  try {
    // 1. Get user from session
    const sessionRes = await fetch('/api/session')
    if (!sessionRes.ok) throw new Error('Failed to fetch session')
    const sessionUser = await sessionRes.json()
    user.value = sessionUser

    // 2. Get posts for this user
    const postsRes = await fetch(`/api/users/${sessionUser.id}/posts`)
    if (!postsRes.ok) throw new Error('Failed to fetch posts')
    posts.value = await postsRes.json()
  } catch (err) {
    console.error(err)
  }
}

onMounted(() => {
  fetchUserData()
})
</script>

