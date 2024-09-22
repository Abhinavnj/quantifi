<template>
  <div class="card bg-neutral shadow-lg">
    <div class="card-body text-left"> <!-- Added text-left for left alignment -->
      <!-- Title -->
      <h3 class="card-title text-white text-2xl">{{ blog.title }}</h3>
      <!-- Description -->
      <p class="text-gray-400">{{ blog.description }}</p>
      <!-- Read More Button -->
      <div class="card-actions justify-end">
        <!-- Pass itemId as a query parameter to Blog.vue -->
        <router-link :to="{ name: 'Blog', query: { id: blog.itemId } }" class="btn btn-primary">
          Read More
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  blog: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
/* No additional styles needed */
</style>
