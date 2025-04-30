<!-- LeftSidebar.vue with Tailwind -->
<template>
  <aside class="w-[240px] fixed left-0 h-screen p-5 border-r border-ig-border-dark bg-ig-dark">
    <div class="py-3 pb-8 italic text-2xl text-white text-center">
      <!-- <img src="" class="w-32" alt="Instagram"> -->
      Instagram
    </div>
    
    <nav class="space-y-2">
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
       <i class="fa-solid fa-house"></i>
        <span>Home</span>
      </RouterLink>
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
        <i class="fa-solid fa-message"></i>
        <span>Message</span>
      </RouterLink>
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
        <i class="fa-solid fa-video"></i>
        <span>Reels</span>
      </RouterLink>
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
        <i class="fa-solid fa-square-plus"></i>
        <span>Create Post</span>
      </RouterLink>
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
        <i class="fa-solid fa-user"></i>
        <span>Profile</span>
      </RouterLink>
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
        <i class="fa-solid fa-gear"></i>
        <span>Settings</span>
      </RouterLink>
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
        <i class="fa-solid fa-bell"></i>
        <span>Notification</span>
      </RouterLink>
      <RouterLink 
        to="/"
        class="flex items-center gap-4 p-3 rounded-lg hover:bg-ig-dark-secondary text-white"
      >
        <i class="fa-solid fa-right-from-bracket"></i>
        <span>Logout</span>
      </RouterLink>
      <!-- Repeat for other nav items -->
    </nav>
  </aside>
</template>