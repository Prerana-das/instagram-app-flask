<template>
 <LayoutWrapper>
    <div class="bg-black text-white min-h-screen px-6 py-10 max-w-4xl mx-auto">
    <h2 class="text-xl font-bold text-white mb-4">Messages</h2>

    <div v-if="loading" class="text-gray-400">Loading messages...</div>

    <div v-else-if="conversations.length === 0" class="text-gray-400">
      No messages yet.
    </div>

    <div v-else>
      <div
        v-for="(conversation, index) in conversations"
        :key="index"
        class="flex items-center gap-4 p-4 border-b border-neutral-700 hover:bg-neutral-800 transition"
      >
        <img
          v-if="conversation.user?.profile"
          :src="conversation.user.profile || '/default-avatar.png'"
          alt="Profile"
          class="w-12 h-12 rounded-full object-cover"
        />
        <div v-else class="bg-gray-700 h-12 w-12 rounded-full"></div>
        <div class="flex-1">
          <h3 class="text-white font-medium">{{ conversation.user.username }}</h3>
          <p class="text-gray-400 text-sm truncate">
            {{ conversation.latest_message.content }}
          </p>
        </div>
        <div class="text-gray-500 text-xs whitespace-nowrap">
          {{ formatTimestamp(conversation.latest_message.timestamp) }}
        </div>
      </div>
    </div>
  </div>
  </LayoutWrapper>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LayoutWrapper from '@/components/Layout/LayoutWrapper.vue'

const conversations = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await fetch('/api/conversations')
    const data = await res.json()

    if (res.ok) {
      conversations.value = data
    } else {
      console.error('Error:', data.error || 'Failed to fetch messages')
    }
  } catch (err) {
    console.error('Fetch error:', err)
  } finally {
    loading.value = false
  }
})

function formatTimestamp(timestamp) {
  const date = new Date(timestamp)
  return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}
</script>
