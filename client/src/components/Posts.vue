<template>
  <div>
    <h2>📸 Latest Posts</h2>
    <div v-for="post in posts" :key="post.id" class="post">
      <h3>{{ post.username }}</h3>
      <img :src="post.image" alt="Post image" />
      <p>{{ post.caption }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const posts = ref([])

onMounted(async () => {
  const res = await fetch('/api/posts')
  posts.value = await res.json()
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
