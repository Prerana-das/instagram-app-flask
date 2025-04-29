<template>
  <aside class="w-80 h-screen fixed top-0 right-0 bg-black text-white p-4 flex flex-col border-l border-gray-800">
    <h2 class="text-lg font-bold mb-6">Suggested for You</h2>
    <div class="flex flex-col gap-6">
      <div v-for="n in 5" :key="n" class="flex items-center gap-4">
        <div class="bg-gray-700 h-12 w-12 rounded-full"></div>
        <div class="flex flex-col">
          <p class="font-semibold">User {{ n }}</p>
          <button class="text-blue-400 text-sm hover:underline">Follow</button>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup>
</script>
