<template>
  <div class="bg-gray-900 rounded-lg overflow-hidden shadow-md">
    <div class="flex items-center gap-4 p-4">
      <div class="bg-gray-700 h-10 w-10 rounded-full"></div>
      <p class="font-bold">{{ post.user }}</p>
    </div>
    <img :src="post.image" alt="Post" class="w-full object-cover" />
    <div class="p-4">
      <p>{{ post.caption }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  post: Object
})
</script>
