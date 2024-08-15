<!-- <script setup lang="ts">
import Navbar from "./Navbar.vue";
</script>

<template>
	<Navbar />
	<div class="container mx-auto">
		<h1 className="text-center text-7xl font-bold">Welcome to Quantifi.</h1>
		<div>
			<input
				type="text"
				placeholder="Search"
				class="input input-bordered w-24 md:w-auto"
			/>
		</div>
	</div>
</template> -->

<script setup lang="ts">
import Navbar from "./Navbar.vue";
import SymbolSearch from "./SymbolSearch.vue";

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

// Handle the symbol selected from the autocomplete
function handleSymbolSelected(ticker: SymbolObject) {
	console.log("Selected Symbol:", ticker);
	// You can handle the selected symbol here, e.g., fetch more data or navigate to a different page
}
</script>

<template>
	<Navbar />
	<div class="container mx-auto">
		<h1 class="text-center text-7xl font-bold">Welcome to Quantifi.</h1>
		<div class="mt-8">
			<!-- Use the SymbolSearch component instead of the basic input -->
			<SymbolSearch @symbolSelected="handleSymbolSelected" />
		</div>
	</div>
</template>

<style scoped>
/* Add any additional styling you need here */
</style>
