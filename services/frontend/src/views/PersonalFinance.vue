<template>
  <div data-theme="custom-dark" class="relative flex flex-col min-h-screen">
    <Navbar />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-center items-center text-center p-10 space-y-6">
      <!-- Heading -->
      <h1 class="text-5xl font-bold text-white">Personal Finance</h1>

      <!-- Placeholder Introduction -->
      <p class="text-xl text-gray-300 max-w-3xl">
        In the Personal Finance section, we will empower you with the knowledge and tools to take control of your
        finances.
        Whether you're budgeting, saving, or investing, our resources will guide you to make informed decisions and
        achieve your financial goals.
      </p>

      <!-- Divider Line -->
      <div class="border-t border-gray-600 w-1/2"></div>

      <!-- Placeholder for Key Features -->
      <section class="text-left max-w-4xl space-y-4">
        <h2 class="text-3xl font-semibold text-white">What to Expect</h2>
        <ul class="list-disc list-inside text-lg text-gray-400 space-y-2">
          <li>Budgeting and expense tracking tools</li>
          <li>Investment strategies and advice for long-term wealth building</li>
          <li>Personalized financial insights and planning</li>
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
