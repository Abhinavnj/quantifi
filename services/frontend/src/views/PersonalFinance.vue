<template>
  <div data-theme="custom-dark" class="relative flex flex-col min-h-screen">
    <Navbar />

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
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
          <!-- Example of a Blog Post Card -->
          <div class="card bg-neutral shadow-lg">
            <div class="card-body">
              <h3 class="card-title text-white text-2xl">5 Simple Steps to Start Budgeting</h3>
              <p class="text-gray-400">Learn how to create a realistic budget that works for your financial goals.</p>
              <div class="card-actions justify-end">
                <!-- <button class="btn btn-outline btn-primary">Read More</button> -->
                <router-link :to="{
                  name: 'Blog',
                  params: {
                    title: '5 Simple Steps to Start Budgeting',
                    description: 'Learn how to create a realistic budget that works for your financial goals...',
                    date: '2024-09-12',
                    progress: 50
                  }
                }" class="btn btn-primary">
                  Read More
                </router-link>
              </div>
            </div>
          </div>

          <div class="card bg-neutral shadow-lg">
            <div class="card-body">
              <h3 class="card-title text-white text-2xl">Investing 101: A Beginner's Guide</h3>
              <p class="text-gray-400">Discover the basics of investing and how to grow your wealth over time.</p>
              <div class="card-actions justify-end">
                <button class="btn btn-outline btn-primary">Read More</button>
              </div>
            </div>
          </div>

          <div class="card bg-neutral shadow-lg">
            <div class="card-body">
              <h3 class="card-title text-white text-2xl">Maximizing Your Savings Potential</h3>
              <p class="text-gray-400">Tips and tricks to help you save more effectively for the future.</p>
              <div class="card-actions justify-end">
                <button class="btn btn-outline btn-primary">Read More</button>
              </div>
            </div>
          </div>

          <div class="card bg-neutral shadow-lg">
            <div class="card-body">
              <h3 class="card-title text-white text-2xl">Understanding Credit Scores</h3>
              <p class="text-gray-400">A deep dive into how credit scores work and how you can improve yours.</p>
              <div class="card-actions justify-end">
                <button class="btn btn-outline btn-primary">Read More</button>
              </div>
            </div>
          </div>
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
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
</script>

<style scoped>
/* No additional styles needed */
</style>
