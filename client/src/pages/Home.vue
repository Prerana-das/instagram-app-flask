<template>
  <LayoutWrapper>
    <div v-if="loading" class="flex justify-center items-center h-[calc(100vh-5rem)]">
      <p class="text-gray-400">Loading posts...</p>
    </div>
    <div v-else class="flex flex-col gap-6 w-[70%] mx-auto">
      <PostItem v-for="post in posts" :key="post.id" :post="post" />
    </div>
  </LayoutWrapper>
</template>

<script setup>
import LayoutWrapper from '@/components/Layout/LayoutWrapper.vue'
import PostItem from '@/components/Feed/PostItem.vue'
import { onMounted, ref } from 'vue'
import { apiGet } from '@/services/api'  
import { useRouter } from 'vue-router'

const posts = ref([])
const loading = ref(true)

const router = useRouter()
const user = ref(null)

async function fetchSessionUser() {
  try {
    const res = await fetch('/api/session')
    if (res.ok) {
      user.value = await res.json()
    } else if (res.status === 401) {
      router.push('/login') // Redirect if not logged in
    } else {
      console.error('Failed to fetch session user')
    }
  } catch (error) {
    console.error('Error fetching session user:', error)
  }
}

onMounted(async () => {
  try {
    const res = await apiGet('/api/posts')
    console.log(res, 'Fetched posts')

    if (res) {
      posts.value = res
    }
  } catch (error) {
    console.error('Error fetching posts:', error)
  } finally {
    loading.value = false
  }
})
</script>

import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'


