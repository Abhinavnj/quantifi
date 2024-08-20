<template>
	<div v-if="stockInfo.open !== null" class="stats shadow mt-6">
		<!-- Display the previous open and close prices using the StatDisplay component -->
		<StatDisplay title="Previous Open" :value="stockInfo.open" />
		<StatDisplay title="Previous Close" :value="stockInfo.close" />
	</div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import axios from "axios";
import StatDisplay from "./StatDisplay.vue";

// Define props to receive the selected ticker symbol
const props = defineProps({
	ticker: {
		type: String,
		required: true,
	},
});

// Define reactive state for stock information
const stockInfo = ref({ open: String, close: String });

// Watch for changes in the ticker prop and fetch stock information
watch(
	() => props.ticker,
	async (newTicker) => {
		if (!newTicker) return;

		const url = `http://localhost:5001/api/ticker/open_close?ticker=${newTicker}`;

		try {
			const response = await axios.get(url);
			stockInfo.value = response.data;
			console.log("Stock Info:", stockInfo.value);
		} catch (error) {
			console.error("Error fetching stock info:", error);
			stockInfo.value = { open: null, close: null };
		}
	},
	{ immediate: true }
);
</script>

<style scoped>
/* Add any specific styles if needed */
</style>
