<template>
  <div class="relative flex flex-col min-h-screen bg-gray-900 overflow-hidden">
    <Navbar />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-start items-start text-left p-10 space-y-8">
      <!-- Company logo and name in the top left -->
      <div class="flex items-center space-x-6 mb-8 animate-fadeIn">
        <!-- Bind src to the tickerLogo variable and make it circular -->
        <img :src="tickerLogo" alt="Logo" v-if="tickerLogo"
          class="h-20 w-20 object-contain rounded-full border border-white shadow-lg" />
        <h1 class="text-5xl font-extrabold text-white">{{ symbolName }}</h1>
      </div>

      <!-- Tab component -->
      <div role="tablist" class="tabs tabs-boxed mb-6 animate-fadeIn">
        <a role="tab" class="tab transition-all hover:scale-105" :class="{ 'tab-active': activeTab === 'overview' }"
          @click="activeTab = 'overview'">Overview</a>
        <a role="tab" class="tab transition-all hover:scale-105" :class="{ 'tab-active': activeTab === 'financials' }"
          @click="activeTab = 'financials'">Financials</a>
        <a role="tab" class="tab transition-all hover:scale-105" :class="{ 'tab-active': activeTab === 'news' }"
          @click="activeTab = 'news'">News</a>
      </div>

      <!-- Tab Content -->
      <div v-if="activeTab === 'overview'" class="w-full animate-fadeIn">
        <div class="flex flex-col items-start lg:flex-row lg:space-x-6 bg-gray-800 p-6 rounded-lg shadow-xl">
          <!-- Display the ticker stats for Previous Open and Previous Close next to each other -->
          <div class="card w-full lg:w-1/2 bg-neutral-focus text-white shadow-lg transition-all hover:shadow-2xl">
            <div class="card-body">
              <StatDisplay v-if="tickerPrevOpen" title="Previous Open" :value="tickerPrevOpen" />
            </div>
          </div>
          <div class="card w-full lg:w-1/2 bg-neutral-focus text-white shadow-lg transition-all hover:shadow-2xl">
            <div class="card-body">
              <StatDisplay v-if="tickerPrevClose" title="Previous Close" :value="tickerPrevClose" />
            </div>
          </div>
        </div>
      </div>

      <div v-if="activeTab === 'financials'" class="animate-fadeIn">
        <div class="card w-full bg-gray-800 p-6 rounded-lg shadow-lg text-gray-100 transition-all hover:shadow-2xl">
          <p class="text-lg">
            Financial data will go here.
          </p>
        </div>
      </div>

      <div v-if="activeTab === 'news'" class="animate-fadeIn">
        <div class="card w-full bg-gray-800 p-6 rounded-lg shadow-lg text-gray-100 transition-all hover:shadow-2xl">
          <p class="text-lg">
            Latest news articles will go here.
          </p>
        </div>
      </div>

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
/* Fade-in animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 1s ease-in-out;
}

/* Card hover effects */
.card {
  transition: transform 0.3s ease-in-out;
}

.card:hover {
  transform: scale(1.03);
}
</style>
