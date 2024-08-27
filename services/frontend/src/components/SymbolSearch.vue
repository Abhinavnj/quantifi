<template>
  <div class="relative w-full max-w-md flex items-center">
    <!-- Search Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-3 h-5 w-5 text-gray-400 opacity-70" fill="none"
      viewBox="0 0 16 16" stroke="currentColor">
      <path fill-rule="evenodd"
        d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
        clip-rule="evenodd" />
    </svg>
    <!-- Search Input -->
    <input type="text" placeholder="Enter a symbol (ex. AAPL, IBM, VOO)"
      class="input input-bordered w-full pl-10 pr-20 text-gray-300 bg-gray-800 rounded-lg" ref="searchInput"
      @input="fetchSymbols" @keydown.down.prevent="handleArrowDown" @keydown.up.prevent="handleArrowUp"
      @keydown.enter.prevent="handleEnter" v-model="query" />
    <!-- Command + K Shortcut -->
    <div class="absolute right-3 flex items-center space-x-1 text-gray-500">
      <kbd class="px-2 py-1 bg-gray-700 rounded text-xs">⌘</kbd>
      <kbd class="px-2 py-1 bg-gray-700 rounded text-xs">K</kbd>
    </div>
    <!-- Dropdown List -->
    <ul v-if="symbols.length && query"
      class="absolute top-full mt-2 w-full bg-gray-800 border border-gray-600 rounded-lg z-10 shadow-lg">
      <li v-for="(symbol, index) in limitedSymbols" :key="index" @click="selectSymbol(symbol)"
        :class="['px-4 py-2 cursor-pointer flex items-center space-x-2', activeIndex === index ? 'bg-gray-700 text-white' : 'text-gray-300']">
        <span class="font-medium">{{ symbol.ticker }}</span>
        <span class="text-sm text-gray-400">- {{ symbol.name }}</span>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, defineExpose } from "vue";
import axios from "axios";

// Reference to the search input
const searchInput = ref<HTMLInputElement | null>(null);

// Expose the searchInput ref to the parent component
defineExpose({ searchInput });

// Define the emit function
const emit = defineEmits(["symbolSelected"]);

// Define reactive state variables
const query = ref("");
const symbols = ref<SymbolObject[]>([]);
const activeIndex = ref(-1); // Track the currently highlighted item in the list

// Computed property to limit the displayed symbols to the top 3
const limitedSymbols = computed(() => symbols.value.slice(0, 3));

// Fetch symbols matching the user query
const fetchSymbols = async () => {
  if (query.value.length < 2) {
    symbols.value = [];
    activeIndex.value = -1; // Reset active index when query changes
    return;
  }

  const url = `http://localhost:5001/api/symbol_search?keywords=${query.value}`;
  // const url = `http://3.22.166.72:5001/api/symbol_search?keywords=${query.value}`;
  // const url = `https://quantifiapp.com/api/symbol_search?keywords=${query.value}`;

  try {
    const response = await axios.get(url);
    symbols.value = response.data.results || [];
    activeIndex.value = -1; // Reset active index when new results are fetched
  } catch (error) {
    console.error("Error fetching symbols:", error);
    symbols.value = [];
  }
};

// Handle the selection of a symbol
const selectSymbol = (symbol: SymbolObject) => {
  query.value = symbol.ticker;
  symbols.value = [];
  activeIndex.value = -1;
  emit("symbolSelected", symbol);
};

// Handle arrow down key
const handleArrowDown = () => {
  if (activeIndex.value < limitedSymbols.value.length - 1) {
    activeIndex.value++;
  }
};

// Handle arrow up key
const handleArrowUp = () => {
  if (activeIndex.value > 0) {
    activeIndex.value--;
  }
};

// Handle enter key
const handleEnter = () => {
  if (activeIndex.value >= 0 && activeIndex.value < limitedSymbols.value.length) {
    selectSymbol(limitedSymbols.value[activeIndex.value]);
  }
};

// Define an interface for the symbol object
interface SymbolObject {
  ticker: string;
  name: string;
  market: string;
  locale: string;
  type: string;
  active: boolean;
  currency_name: string;
  composite_figi?: string;
  share_class_figi?: string;
  last_updated_utc: string;
}
</script>

<style scoped>
/* Scoped styles for the component */
</style>
