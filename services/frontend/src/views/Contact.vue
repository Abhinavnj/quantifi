<template>
  <div class="relative flex flex-col min-h-screen text-white">
    <Navbar class="z-50" />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-center items-center text-center py-20 px-4">
      <h1 class="text-4xl font-bold mb-6">Contact Us</h1>
      <p class="text-lg text-gray-300 mb-8">
        We'd love to hear from you! Fill out the form below to get in touch.
      </p>

      <div class="w-full max-w-lg bg-gray-800 p-8 rounded-lg shadow-md">
        <form @submit.prevent="handleSubmit">
          <div class="mb-4">
            <label for="name" class="block text-left text-gray-300">Name</label>
            <input type="text" id="name" v-model="form.name" required
              class="input input-bordered w-full text-gray-300 bg-gray-700 mt-1" />
          </div>

          <div class="mb-4">
            <label for="email" class="block text-left text-gray-300">Email</label>
            <input type="email" id="email" v-model="form.email" required
              class="input input-bordered w-full text-gray-300 bg-gray-700 mt-1" />
          </div>

          <div class="mb-6">
            <label for="message" class="block text-left text-gray-300">Message</label>
            <textarea id="message" v-model="form.message" required
              class="textarea textarea-bordered w-full text-gray-300 bg-gray-700 mt-1" rows="4"></textarea>
          </div>

          <button type="submit" class="btn btn-primary w-full">
            Send Message
          </button>
        </form>
      </div>
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";

// Define form data
const form = ref({
  name: "",
  email: "",
  message: "",
});

// Handle form submission
function handleSubmit() {
  console.log("Form submitted:", form.value);
  // You can add form submission logic here, like sending the data to an API
  alert("Message sent successfully!");
  // Reset form after submission
  form.value.name = "";
  form.value.email = "";
  form.value.message = "";
}
</script>

<style scoped></style>
