<template>
  <div class="relative flex flex-col min-h-screen bg-gray-900 overflow-hidden">
    <Navbar />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-center items-center text-center py-20">
      <h1 class="text-4xl font-bold text-white mb-6">
        Analysis for {{ symbolName }}
      </h1>
      <p class="text-lg text-gray-300 mb-8">
        Detailed analysis for the selected symbol: {{ symbol }}.
      </p>

      <!-- Display the ticker price using StatDisplay -->
      <StatDisplay v-if="tickerPrevClose" title="Previous Close" :value="tickerPrevClose" />

    </main>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
import StatDisplay from "../components/StatDisplay.vue";

// Use route to get the symbol parameter
const route = useRoute();
const symbol = ref(route.params.symbol);
const symbolName = ref("");
const tickerPrevClose = ref(""); // Reactive variable to store the ticker price

// Function to fetch ticker name from API
const fetchTickerName = async () => {
  try {
    const response = await axios.get(`http://localhost:5001/api/ticker/name?ticker=${symbol.value}`);
    symbolName.value = response.data; // Assuming response is the name directly
  } catch (error) {
    console.error("Error fetching ticker name:", error);
    symbolName.value = "Unknown";
  }
};

// Function to fetch ticker price from API
const fetchtickerPrevClose = async () => {
  try {
    const response = await axios.get(`http://localhost:5001/api/ticker/prev_close?ticker=${symbol.value}`);
    tickerPrevClose.value = response.data
  } catch (error) {
    console.error("Error fetching ticker price:", error);
    tickerPrevClose.value = "N/A";
  }
};

// Fetch ticker name and price on component mount
onMounted(() => {
  fetchTickerName();
  fetchtickerPrevClose();
});
</script>

<style scoped></style>
