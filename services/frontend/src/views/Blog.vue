<template>
  <div data-theme="custom-dark" class="relative flex flex-col min-h-screen">
    <Navbar class="z-50" />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-start items-start text-left p-10 space-y-8">
      <!-- Blog Post Title -->
      <h1 class="text-5xl font-bold text-white">{{ blog.title }}</h1>

      <!-- Blog Post Date -->
      <p class="text-lg text-gray-400">{{ formattedDate(blog.date) }}</p>

      <!-- Blog Post Description -->
      <p class="text-lg text-gray-300 leading-relaxed max-w-4xl">
        {{ blog.description }}
      </p>

      <!-- Blog Content -->
      <section class="text-left max-w-4xl space-y-4">
        <p class="text-lg text-gray-200">
          {{ blog.content }}
        </p>
      </section>
    </main>
    <Footer />
  </div>
</template>

<script setup lang="ts">
// import { computed } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
import { ref, onMounted } from 'vue';

const route = useRoute();
const blog = ref({
  title: '',
  description: '',
  content: '',
  date: ''
});
const error = ref('');
const loading = ref(true);

// Fetch the blog data based on the query parameter
const fetchBlog = async (id) => {
  try {
    const response = await axios.get(`https://quantifiapp.com/api/blogs/${id}`);
    // const response = await axios.get(`http://localhost:5001/api/blogs/${id}`);
    blog.value = response.data;
  } catch (err) {
    error.value = 'Error fetching blog post.';
  } finally {
    loading.value = false;
  }
};

// Fetch blogs when the component is mounted
onMounted(() => {
  const id = route.query.id;
  if (id) {
    fetchBlog(id);
  } else {
    error.value = 'Blog ID is missing.';
    loading.value = false;
  }
});

// Function to format date
const formattedDate = (dateString: string) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
};
</script>

<style scoped>
/* No additional styles needed */
</style>