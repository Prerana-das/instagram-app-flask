<template>
  <div class="bg-neutral-900 border border-neutral-700 rounded-lg overflow-hidden shadow-md">
    <div class="p-4 flex items-center gap-4">
      <img :src="post.user?.profile" alt="Avatar" class="w-10 h-10 rounded-full" />
      <div>
        <h3 class="text-white font-semibold">{{ post.user?.username }}</h3>
      </div>
    </div>
    <p class="text-white text-sm px-4 mb-2">{{ post.caption }}</p>
    <div class="pt-2">
      <img :src="post.image_url" alt="Post Image" class="w-full max-h-[500px] object-cover" />
    </div>
    <div class="p-4 flex flex-col gap-2">
      <div class="flex gap-4 text-white text-2xl">
        <i class="fa-solid fa-heart"></i>
        <i class="fa-solid fa-comment"></i>
        <i class="fa-solid fa-paper-plane"></i>
      </div>
      <!-- <p class="text-white text-sm"><span class="font-bold">{{ post.username }}</span> {{ post.caption }}</p>
      <p class="text-gray-500 text-xs">{{ post.timeAgo }}</p> -->
      {{ post.likes }} likes
    </div>
  </div>
</template>

<script setup>
defineProps({
  post: {
    type: Object,
    required: true,
  },
})
</script>
