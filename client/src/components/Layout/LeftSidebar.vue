<!-- LeftSidebar.vue with Tailwind -->
<template>
  <aside class="w-[240px] fixed left-0 h-screen p-5 border-r border-ig-border-dark bg-ig-dark">
    <div class="py-3 pb-8">
      <img src="" class="w-32" alt="Instagram">
    </div>
    
    <nav class="space-y-2">
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
        <HomeIcon class="w-6 h-6" />
        <span>Home</span>
      </RouterLink>
      <!-- Repeat for other nav items -->
    </nav>
  </aside>
</template>