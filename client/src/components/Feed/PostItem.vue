<template>
  <div class="bg-neutral-900 border border-neutral-700 rounded-lg overflow-hidden shadow-md">
    <div class="p-4 flex items-center gap-4">
      <img
        v-if="post.user?.profile"
        :src="post.user?.profile"
        alt="Avatar"
        class="w-10 h-10 rounded-full"
      />
      <div v-else class="bg-gray-700 h-12 w-12 rounded-full"></div>
      <div>
        <h3 class="text-white font-semibold">{{ post.user?.username }}</h3>
      </div>
    </div>

    <p class="text-white text-sm px-4 mb-2">{{ post.caption }}</p>

    <div class="pt-2">
      <template v-if="isVideo(post.image_url)">
        <video
          :src="post.image_url"
          controls
          class="w-full max-h-[500px] object-cover rounded-lg"
        ></video>
      </template>
      <template v-else>
        <img
          :src="post.image_url"
          alt="Post Image"
          class="w-full max-h-[500px] object-cover rounded-lg"
        />
      </template>
    </div>

    <div class="p-4 flex flex-col gap-2">
      <div class="flex gap-4 text-white text-2xl">
        <i
          class="fa-solid fa-heart cursor-pointer"
          :class="{ 'text-red-500': liked }"
          @click="handleLike"
        ></i>
        <i class="fa-solid fa-comment cursor-pointer"></i>
        <i class="fa-solid fa-paper-plane cursor-pointer"></i>
      </div>
      <span class="text-white text-sm">{{ likes }} {{ likes === 1 ? 'like' : 'likes' }}</span>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'

const props = defineProps({
  post: {
    type: Object,
    required: true,
  },
})

const likes = ref(props.post.likes || 0)
const liked = ref(!!props.post.user_liked)

async function handleLike() {
  try {
    const res = await fetch(`/api/posts/${props.post.id}/like`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    })

    const data = await res.json()

    if (res.ok) {
      likes.value = data.likes
      liked.value = data.message === 'liked'
    } else {
      alert(data.error || 'Failed to like post.')
    }
  } catch (err) {
    console.error('Like error:', err)
    alert('Something went wrong.')
  }
}

function isVideo(url) {
  return /\.(mp4|webm|ogg|mov)$/i.test(url)
}
</script>
