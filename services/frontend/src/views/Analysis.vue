<template>
  <div class="relative flex flex-col min-h-screen overflow-hidden">
    <Navbar class="z-50" />

    <!-- Main Content -->
    <main class="relative z-10 flex-grow flex flex-col justify-start items-start text-left px-10 xl:px-10">
      <!-- Skeleton Loader or Main Content -->
      <Skeleton v-if="isLoading" />

      <template v-else>
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
        <div v-if="activeTab === 'overview'" class="w-full">
          <div class="flex flex-wrap w-full gap-6">
            <!-- Stats display grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full">
              <StatDisplay v-if="overview.open" title="Previous Open" :value="overview.open.value"
                :info="overview.open.info" />
              <StatDisplay v-if="overview.close" title="Previous Close" :value="overview.close.value"
                :info="overview.close.info" />
              <StatDisplay v-if="overview.high" title="High" :value="overview.high.value" :info="overview.high.info" />
              <StatDisplay v-if="overview.low" title="Low" :value="overview.low.value" :info="overview.low.info" />
              <StatDisplay v-if="overview.todays_change" title="Today's Change" :value="overview.todays_change.value"
                :info="overview.todays_change.info" />
              <StatDisplay v-if="overview.todays_change_percentage" title="Change %"
                :value="overview.todays_change_percentage.value" :info="overview.todays_change_percentage.info" />
              <StatDisplay v-if="overview.last_minute_price" title="Last Minute Price"
                :value="overview.last_minute_price.value" :info="overview.last_minute_price.info" />
            </div>

            <!-- Chart Component -->
            <div class="w-full xl:w-8/12 mt-10">
              <Chart :aggregateData="aggregateData" />
            </div>
          </div>
        </div>

        <!-- Financials Tab Content -->
        <div v-if="activeTab === 'financials'">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <StatDisplay v-if="basicEarningsPerShare" title="Earnings Per Share" :value="basicEarningsPerShare" />
          </div>
        </div>

        <!-- News Tab Content -->
        <div v-if="activeTab === 'news'">
          <div v-for="article in news" :key="article.title" class="p-4 mb-4 rounded-lg bg-base-300">
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
      </template>
    </main>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
import StatDisplay from '../components/StatDisplay.vue';
import Chart from '../components/Chart.vue';
import Skeleton from '../components/Skeleton.vue'; // Import Skeleton component

// Use route to get the symbol parameter
const route = useRoute();
const symbol = ref(route.params.symbol);
const symbolName = ref("");
const overview = ref({});
const aggregateData = ref([]);
const basicEarningsPerShare = ref("");
const news = ref([]);
const activeTab = ref('overview');
const tickerLogo = ref("");
const isLoading = ref(true); // Loading state

// Function to fetch ticker data from the API
const fetchTickerData = async () => {
  try {
    const response = await axios.get(`https://quantifiapp.com/api/analysis?ticker=${symbol.value}`);
    // const response = await axios.get(`http://localhost:5001/api/analysis?ticker=${symbol.value}`);
    overview.value = response.data.overview;
    symbolName.value = overview.value.name.value;
    tickerLogo.value = overview.value.logo_base64.value;
    basicEarningsPerShare.value = response.data.financials.basic_earnings_per_share;
    news.value = response.data.news;
    aggregateData.value = response.data.aggregate_data;
    isLoading.value = false; // Stop loading when data is fetched
  } catch (error) {
    console.error("Error fetching ticker data:", error);
    isLoading.value = false; // Stop loading on error
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
  border: 2px solid white;
}
</style>
