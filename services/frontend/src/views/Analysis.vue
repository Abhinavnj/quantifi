<template>
  <div class="relative flex flex-col min-h-screen overflow-hidden">
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

      <!-- Overview Tab Content -->
      <div v-if="activeTab === 'overview'">
        <!-- Display all the 'overview' data -->
        <div class="grid grid-cols-2 gap-6">
          <StatDisplay v-if="tickerPrevOpen" title="Previous Open" :value="tickerPrevOpen" />
          <StatDisplay v-if="tickerPrevClose" title="Previous Close" :value="tickerPrevClose" />
          <StatDisplay v-if="tickerHigh" title="High" :value="tickerHigh" />
          <StatDisplay v-if="tickerLow" title="Low" :value="tickerLow" />
          <StatDisplay v-if="todaysChange" title="Today's Change" :value="todaysChange" />
          <StatDisplay v-if="todaysChangePercentage" title="Change %" :value="todaysChangePercentage" />
          <StatDisplay v-if="lastMinutePrice" title="Last Minute Price" :value="lastMinutePrice" />
        </div>
      </div>

      <!-- Financials Tab Content -->
      <div v-if="activeTab === 'financials'">
        <div class="grid grid-cols-2 gap-6">
          <StatDisplay v-if="basicEarningsPerShare" title="Earnings Per Share" :value="basicEarningsPerShare" />
        </div>
      </div>

      <!-- News Tab Content -->
      <div v-if="activeTab === 'news'">
        <div v-for="article in news" :key="article.title" class="p-4 mb-4 rounded-lg bg-base-300">
          <!-- News Item -->
          <div class="flex items-center space-x-4 mb-4">
            <img :src="article.publisher_logo" alt="Publisher Logo" class="h-10 w-10 object-contain" />
            <div>
              <h3 class="text-xl font-bold">{{ article.publisher_name }}</h3>
              <p class="text-sm text-gray-400">{{ article.published_datetime }}</p>
            </div>
          </div>
          <h4 class="text-lg font-semibold mb-2">{{ article.title }}</h4>
          <p class="text-sm text-gray-300">Sentiment: <span :class="getSentimentColor(article.sentiment)">{{
          article.sentiment }}</span></p>
          <p class="text-sm text-gray-400 italic">Reasoning: {{ article.sentiment_reasoning }}</p>
        </div>
      </div>

      <!-- <p class="text-lg text-gray-300 mt-8">
        Selected symbol: {{ symbol }}
      </p> -->

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
const tickerHigh = ref("");
const tickerLow = ref("");
const todaysChange = ref("");
const todaysChangePercentage = ref("");
const lastMinutePrice = ref("");
const tickerLogo = ref("");
const basicEarningsPerShare = ref("");
const activeTab = ref('overview'); // Track which tab is active
const news = ref([]); // Store news articles

// Function to fetch ticker data from the API
const fetchTickerData = async () => {
  try {
    const response = await axios.get(`http://localhost:5001/api/analysis/ticker?ticker=${symbol.value}`);
    // const response = await axios.get(`https://quantifiapp.com/api/analysis/ticker?ticker=${symbol.value}`);
    console.log(response);
    tickerPrevClose.value = response.data.overview.close;
    tickerPrevOpen.value = response.data.overview.open;
    tickerHigh.value = response.data.overview.high;
    tickerLow.value = response.data.overview.low;
    todaysChange.value = response.data.overview.todays_change;
    todaysChangePercentage.value = response.data.overview.todays_change_percentage;
    lastMinutePrice.value = response.data.overview.last_minute_price;
    tickerLogo.value = response.data.overview.logo_base64;
    symbolName.value = response.data.overview.name;
    basicEarningsPerShare.value = response.data.financials.basic_earnings_per_share;
    news.value = response.data.news; // Store news articles
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

// Helper function to get the sentiment color
const getSentimentColor = (sentiment) => {
  if (sentiment === 'positive') return 'text-green-500';
  if (sentiment === 'negative') return 'text-red-500';
  return 'text-yellow-500'; // Neutral sentiment
};
</script>

<style scoped>
img {
  border-radius: 50%;
  /* Circular view */
  border: 2px solid white;
  /* Optional: add a border around the logo */
}
</style>
