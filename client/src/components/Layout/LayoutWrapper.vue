<template>
  <div class="bg-black text-white min-h-screen flex">
    <LeftSidebar />
    <div class="flex-1 ml-60 mr-80">
        <TopHeader />
        <main class="pt-20 px-6">
        <slot />
        </main>
    </div>
    <RightSidebar />
    </div>
</template>

<script setup>
import LeftSidebar from './LeftSidebar.vue'
import TopHeader from './TopHeader.vue'
import RightSidebar from './RightSidebar.vue'
</script>
