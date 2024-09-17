<template>
  <div data-theme="custom-dark" class="relative flex flex-col min-h-screen">
    <Navbar />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-start items-start text-left p-10 space-y-8">
      <!-- Blog Post Title -->
      <h1 class="text-5xl font-bold text-white">{{ title }}</h1>

      <!-- Blog Post Date -->
      <p class="text-lg text-gray-400">{{ formattedDate }}</p>

      <!-- Blog Post Description -->
      <p class="text-lg text-gray-300 leading-relaxed max-w-4xl">
        {{ description }}
      </p>
    </main>

    <!-- Progress Bar at the bottom -->
    <div class="fixed bottom-0 left-0 w-full p-4 bg-neutral">
      <div class="progress bg-base-200 h-2">
        <div class="progress-bar bg-primary" :style="{ width: progress + '%' }"></div>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";

// Props to be passed from the home page
const props = defineProps({
  title: String,
  description: String,
  date: String,
  progress: Number,  // Optional: progress value, can be calculated dynamically
});

// Format the date in a readable way
const formattedDate = computed(() => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  const parsedDate = new Date(props.date);
  return parsedDate.toLocaleDateString(undefined, options);
});
</script>

<style scoped>
/* No additional styles needed */
</style>
