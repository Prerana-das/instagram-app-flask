<template>
  <LayoutWrapper>
    <div class="flex flex-col gap-6">
      <PostItem v-for="post in posts" :key="post.id" :post="post" />
    </div>
  </LayoutWrapper>
</template>

<script setup>
import LayoutWrapper from '@/components/Layout/LayoutWrapper.vue'
import PostItem from '@/components/Feed/PostItem.vue'

const posts = [
  { id: 1, user: 'John Doe', caption: 'Amazing day!', image: 'https://picsum.photos/600/400?1' },
  { id: 2, user: 'Jane Smith', caption: 'Love this view!', image: 'https://picsum.photos/600/400?2' },
]
</script>
