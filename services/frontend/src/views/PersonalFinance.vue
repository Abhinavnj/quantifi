<template>
  <div data-theme="custom-dark" class="relative flex flex-col min-h-screen">
    <Navbar class="z-50" />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-center items-center text-center p-10 space-y-12">
      <!-- Heading -->
      <h1 class="text-5xl font-bold text-white">Personal Finance Insights</h1>

      <!-- Introduction -->
      <p class="text-xl text-gray-300 max-w-3xl">
        Your go-to resource for mastering your finances. Whether it's budgeting, saving, or investing, explore expert
        advice and actionable insights to take control of your financial future.
      </p>

      <!-- Featured Sections -->
      <section class="flex flex-col items-center space-y-8 max-w-4xl">
        <!-- Recent Blog Posts Section -->
        <h2 class="text-3xl font-semibold text-white">Featured Articles</h2>

        <div v-if="loading" class="text-center text-white">
          Loading blogs...
        </div>

        <div v-if="error" class="text-center text-red-500">
          {{ error }}
        </div>

        <div v-if="blogs.length > 0" class="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
          <!-- Loop through each blog and pass to BlogCard component -->
          <BlogCard v-for="blog in blogs" :key="blog.itemId" :blog="blog" />
        </div>
      </section>

      <!-- Call to Action -->
      <div class="w-full text-center space-y-4">
        <h2 class="text-2xl font-semibold text-white">Join Our Community</h2>
        <p class="text-gray-300 text-lg">Get exclusive updates and resources to master your financial journey.</p>
        <button class="btn btn-primary">Subscribe Now</button>
      </div>
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
import BlogCard from '../components/BlogCard.vue'; // Import BlogCard component

// State variables for blogs, loading, and error handling
const blogs = ref([]);
const loading = ref(true);
const error = ref(null);

// Function to fetch blogs from the API
const fetchBlogs = async () => {
  try {
    const response = await axios.get('https://quantifiapp.com/api/blogs');
    blogs.value = response.data;
  } catch (err) {
    error.value = 'Error fetching blogs.';
  } finally {
    loading.value = false;
  }
  console.log(blogs)
};

// Fetch blogs when the component is mounted
onMounted(() => {
  fetchBlogs();
});
</script>

<style scoped>
/* No additional styles needed */
</style>
