<template>
	<div class="relative flex flex-col min-h-screen bg-gray-900 overflow-hidden">
		<!-- Background Animation -->
		<div class="absolute inset-0 z-0 flex items-center justify-center">
			<div
				class="w-96 h-96 bg-gradient-to-br from-purple-700 to-blue-800 rounded-full blur-3xl opacity-20 animate-slow-pulse"
			></div>
		</div>

		<Navbar />

		<!-- Main Content -->
		<main
			class="relative z-10 flex-grow flex flex-col justify-center items-center text-center py-20"
		>
			<h1 class="text-4xl font-bold text-white mb-6">Welcome to Quantifi</h1>
			<p class="text-lg text-gray-300 mb-8">
				Search for a symbol to start your analysis.
			</p>
			<SymbolSearch
				@symbolSelected="handleSymbolSelected"
				ref="symbolSearchRef"
			/>
		</main>

		<!-- Footer -->
		<Footer />
	</div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from "vue";
import { useRouter } from "vue-router"; // Import the useRouter function
import SymbolSearch from "../components/SymbolSearch.vue";
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";

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

// Reference to the SymbolSearch component
const symbolSearchRef = ref<InstanceType<typeof SymbolSearch> | null>(null);

// Initialize Vue Router
const router = useRouter(); // Use Vue Router

// Handle the symbol selected from the autocomplete
function handleSymbolSelected(symbol: SymbolObject) {
	// Redirect to the analysis page for the selected symbol
	router.push({ name: "Analysis", params: { symbol: symbol.ticker } });
}

// Function to focus the search input when Command+K is pressed
function handleKeydown(event: KeyboardEvent) {
	if ((event.metaKey || event.ctrlKey) && event.key === "k") {
		event.preventDefault();
		symbolSearchRef.value?.searchInput?.focus();
	}
}

onMounted(() => {
	window.addEventListener("keydown", handleKeydown);
});

onBeforeUnmount(() => {
	window.removeEventListener("keydown", handleKeydown);
});
</script>

<style scoped>
/* Background animation with a slower pulse */
@keyframes slow-pulse {
	0%,
	100% {
		transform: scale(1);
		opacity: 0.7;
	}
	50% {
		transform: scale(1.1);
		opacity: 0.2;
	}
}

.animate-slow-pulse {
	animation: slow-pulse 6s ease-in-out infinite;
}
</style>
