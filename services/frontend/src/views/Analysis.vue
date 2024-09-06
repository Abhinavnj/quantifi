<template>
  <div class="relative flex flex-col min-h-screen bg-gray-900 overflow-hidden">
    <Navbar />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-start items-start text-left p-10">
      <!-- Company logo and name in the top left -->
      <div class="flex items-center space-x-4 mb-6">
        <!-- Bind src to the tickerLogo variable and make it circular -->
        <img :src="tickerLogo" alt="Logo" v-if="tickerLogo"
          class="h-16 w-16 object-contain rounded-full border border-white" />
        <h1 class="text-4xl font-bold text-white">{{ symbolName }}</h1>
      </div>

      <!-- Tab component -->
      <div role="tablist" class="tabs tabs-boxed mb-6">
        <a role="tab" class="tab" :class="{ 'tab-active': activeTab === 'overview' }"
          @click="activeTab = 'overview'">Overview</a>
        <a role="tab" class="tab" :class="{ 'tab-active': activeTab === 'financials' }"
          @click="activeTab = 'financials'">Financials</a>
        <a role="tab" class="tab" :class="{ 'tab-active': activeTab === 'news' }" @click="activeTab = 'news'">News</a>
      </div>

      <!-- Tab Content -->
      <div v-if="activeTab === 'overview'">
        <!-- Display the ticker stats for Previous Open and Previous Close next to each other -->
        <div class="grid grid-cols-2 gap-6">
          <StatDisplay v-if="tickerPrevOpen" title="Previous Open" :value="tickerPrevOpen" />
          <StatDisplay v-if="tickerPrevClose" title="Previous Close" :value="tickerPrevClose" />
        </div>
      </div>

      <div v-if="activeTab === 'financials'">
        <p class="text-lg text-gray-300">
          Financial data will go here.
        </p>
      </div>

      <div v-if="activeTab === 'news'">
        <p class="text-lg text-gray-300">
          Latest news articles will go here.
        </p>
      </div>

      <p class="text-lg text-gray-300 mt-8">
        Detailed analysis for the selected symbol: {{ symbol }}.
      </p>

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
const tickerPrevClose = ref("");
const tickerPrevOpen = ref("");
const tickerLogo = ref("");
const activeTab = ref('overview'); // Track which tab is active

// Function to fetch ticker data from the API
const fetchTickerData = async () => {
  try {
    const response = await axios.get(`http://localhost:5001/api/analysis/ticker?ticker=${symbol.value}`);

    tickerPrevClose.value = response.data.close;
    tickerPrevOpen.value = response.data.open;
    tickerLogo.value = response.data.logo_base64;  // Assuming 'logo_base64' is the key for the logo
    symbolName.value = response.data.name;  // Assuming 'name' is the key for the symbol name
  } catch (error) {
    console.error("Error fetching ticker data:", error);
    tickerPrevClose.value = "N/A";
    tickerPrevOpen.value = "N/A";
  }
};

// Fetch ticker data on component mount
onMounted(() => {
  fetchTickerData();
});
</script>

<style scoped>
img {
  border-radius: 50%;
  /* Circular view */
  border: 2px solid white;
  /* Optional: add a border around the logo */
}
</style>
