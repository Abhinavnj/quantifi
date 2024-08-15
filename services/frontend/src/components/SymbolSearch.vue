<template>
	<div class="relative">
		<input
			v-model="query"
			@input="fetchSymbols"
			type="text"
			placeholder="Search"
			class="input input-bordered w-full"
		/>
		<ul
			v-if="symbols.length && query"
			class="absolute w-full bg-white border mt-1 rounded-lg z-10"
		>
			<li
				v-for="(symbol, index) in symbols"
				:key="index"
				@click="selectSymbol(symbol)"
				class="px-4 py-2 cursor-pointer hover:bg-gray-100"
			>
				<span>{{ symbol.ticker }} - {{ symbol.name }}</span>
			</li>
		</ul>
	</div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

// Define the emit function
const emit = defineEmits(["symbolSelected"]);

// Define reactive state variables
const query = ref("");
const symbols = ref([]);

// Your Polygon.io API key
// const apiKey = "YOUR_API_KEY"; // Replace with your actual API key

// Fetch symbols matching the user query
const fetchSymbols = async () => {
	if (query.value.length < 2) {
		symbols.value = [];
		return;
	}

	// const url = `https://api.polygon.io/v3/reference/tickers?search=${query.value}&active=true&limit=10&apiKey=${apiKey}`;
	const url = `http://localhost:5001/api/symbol_search?keywords=${query.value}`;

	try {
		const response = await axios.get(url);
		symbols.value = response.data.results || [];
		console.log(symbols.value);
	} catch (error) {
		console.error("Error fetching symbols:", error);
		symbols.value = [];
	}
};

// Handle the selection of a symbol
const selectSymbol = (symbol: SymbolObject) => {
	query.value = symbol.ticker;
	symbols.value = [];
	emit("symbolSelected", symbol);
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
