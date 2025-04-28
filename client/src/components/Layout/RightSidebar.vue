<template>
  <aside class="w-80 h-screen fixed right-0 top-0 bg-black text-white p-4 flex flex-col">
    <h2 class="text-lg font-bold mb-6">Suggested for You</h2>
    <div class="flex flex-col gap-4">
      <div v-for="n in 5" :key="n" class="flex items-center gap-3">
        <div class="bg-gray-700 h-10 w-10 rounded-full"></div>
        <div>
          <p>User {{ n }}</p>
          <button class="text-blue-400 text-sm">Follow</button>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup>
</script>
