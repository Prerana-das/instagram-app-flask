<template>
  <div>
    <h2>📸 Latest Posts online</h2>

    <div v-if="loading">Loading posts...</div>
    <div v-else>
      <div v-for="post in posts" :key="post.id" class="post">
        <!-- <h3>{{ post.username }}</h3> -->
        <p>{{ post.image_url }}</p>
        <img :src="post.image_url" alt="Post image" />
        <p>{{ post.caption }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { apiGet } from '@/services/api'  // 👈 import the common API function

const posts = ref([])
const loading = ref(true)

onMounted(async () => {
  const res = await apiGet('/api/posts')  // 👈 call apiGet
  console.log(res, 'resss')

  if (res) {
    posts.value = res
    console.log(res, 'posts')
  }

  loading.value = false
})
</script>

<style>
.post {
  margin-bottom: 20px;
}
img {
  width: 150px;
  height: auto;
  border-radius: 8px;
}
</style>
