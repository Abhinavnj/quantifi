<template>
	<div class="relative">
		<input
			v-model="query"
			@input="fetchSymbols"
			type="text"
			placeholder="Search for a stock symbol"
			class="input input-bordered w-full"
		/>
		<ul
			v-if="symbols.length && query"
			class="absolute w-full bg-white border border-gray-300 mt-1 rounded-lg z-10"
		>
			<li
				v-for="(symbol, index) in symbols"
				:key="index"
				@click="selectSymbol(symbol)"
				class="px-4 py-2 cursor-pointer hover:bg-gray-100"
			>
				{{ symbol["1. symbol"] }} - {{ symbol["2. name"] }}
			</li>
		</ul>
	</div>
</template>

<script>
import axios from "axios";

export default {
	data() {
		return {
			query: "",
			symbols: [],
			apiKey: "your_api_key_here", // Replace with your AlphaVantage API key
		};
	},
	methods: {
		fetchSymbols() {
			if (this.query.length < 2) {
				this.symbols = [];
				return;
			}

			const url = `https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=${this.query}&apikey=${this.apiKey}`;

			axios
				.get(url)
				.then((response) => {
					this.symbols = response.data.bestMatches || [];
				})
				.catch((error) => {
					console.error("There was an error fetching the symbols!", error);
				});
		},
		selectSymbol(symbol) {
			this.query = symbol["1. symbol"];
			this.symbols = [];
			// You can emit the selected symbol or take any other action here
			this.$emit("symbolSelected", symbol);
		},
	},
};
</script>

<style scoped>
/* You can add additional styling if necessary */
</style>
