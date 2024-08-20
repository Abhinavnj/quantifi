<script setup lang="ts">
import { ref } from "vue";
import Navbar from "./Navbar.vue";
import SymbolSearch from "./SymbolSearch.vue";
import TickerOpenClose from "./TickerOpenClose.vue";

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

// Define reactive state for the selected ticker symbol
const selectedTicker = ref("");

// Handle the symbol selected from the autocomplete
function handleSymbolSelected(ticker: SymbolObject) {
	console.log("Selected Symbol:", ticker);
	selectedTicker.value = ticker.ticker;
}
</script>

<template>
	<Navbar />
	<div class="container mx-auto">
		<h1 class="text-center text-5xl font-bold">Enter a symbol below.</h1>
		<div class="mt-8">
			<!-- Use the SymbolSearch component -->
			<SymbolSearch @symbolSelected="handleSymbolSelected" />
		</div>
		<!-- Use the TickerOpenClose component -->
		<TickerOpenClose v-if="selectedTicker" :ticker="selectedTicker" />
	</div>
</template>

<style scoped>
/* Add any additional styling you need here */
</style>
