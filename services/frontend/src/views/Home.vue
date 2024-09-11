<template>
  <div data-theme="custom-dark" class="relative flex flex-col min-h-screen">
    <Navbar />

    <!-- Main Content -->
    <main class="flex flex-col justify-center items-center text-center flex-grow p-6 space-y-6">
      <!-- Heading -->
      <h1 class="text-6xl font-bold text-white">
        Welcome to Quantifi
      </h1>

      <!-- Tagline -->
      <p class="text-xl text-gray-300 max-w-xl">
        Simplifying investment knowledge and financial analysis.
      </p>

      <!-- Call-to-Action Buttons (Router Links) -->
      <div class="space-x-4">
        <!-- Learn More button routes to /about -->
        <router-link to="/about" class="btn btn-primary">Learn More</router-link>

        <!-- Get Started button routes to /analysis -->
        <router-link to="/analysis" class="btn btn-outline btn-accent">Get Started</router-link>
      </div>
    </main>

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
