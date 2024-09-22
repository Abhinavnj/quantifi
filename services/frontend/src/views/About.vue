<template>
  <div data-theme="custom-dark" class="relative flex flex-col min-h-screen">
    <Navbar class="z-50" />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-center items-center text-center p-10 space-y-6">
      <!-- Heading -->
      <h1 class="text-5xl font-bold text-white">About Quantifi</h1>

      <!-- Tagline/Introduction -->
      <p class="text-xl text-gray-300 max-w-3xl">
        At Quantifi, our mission is to simplify investment knowledge and financial analysis for everyone.
        Whether you're an experienced trader or just starting, we provide the tools and insights you need
        to make informed financial decisions.
      </p>

      <!-- Divider Line -->
      <div class="border-t border-gray-600 w-1/2"></div>

      <!-- Vision/Key Features Section -->
      <section class="text-left max-w-4xl space-y-4">
        <h2 class="text-3xl font-semibold text-white">Our Vision</h2>
        <p class="text-lg text-gray-400">
          We believe that understanding the world of finance should be accessible to everyone. Our goal is to empower
          individuals by providing intuitive, data-driven insights that help them make smarter investment choices.
        </p>

        <h2 class="text-3xl font-semibold text-white">Key Features</h2>
        <ul class="list-disc list-inside text-lg text-gray-400 space-y-2">
          <li>Comprehensive financial analysis tools</li>
          <li>Real-time market data and trends</li>
          <li>User-friendly interface designed for beginners and experts alike</li>
        </ul>
      </section>
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
</script>

<style scoped>
/* No additional styles needed */
</style>
