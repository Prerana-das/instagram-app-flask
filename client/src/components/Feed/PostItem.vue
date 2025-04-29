<template>
  <div class="bg-neutral-900 border border-neutral-700 rounded-lg overflow-hidden shadow-md">
    <div class="p-4 flex items-center gap-4">
      <img :src="post.image_url" alt="Avatar" class="w-10 h-10 rounded-full" />
      <!-- <div>
        <h3 class="text-white font-semibold">{{ post.username }}</h3>
        <p class="text-gray-400 text-sm">{{ post.location }}</p>
      </div> -->
    </div>
    <img :src="post.image" alt="Post Image" class="w-full max-h-[500px] object-cover" />
    <div class="p-4 flex flex-col gap-2">
      <div class="flex gap-4 text-white text-2xl">
        ❤️ 💬 ✈️
      </div>
      <!-- <p class="text-white text-sm"><span class="font-bold">{{ post.username }}</span> {{ post.caption }}</p>
      <p class="text-gray-500 text-xs">{{ post.timeAgo }}</p> -->
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
