<template>
	<div class="relative flex flex-col min-h-screen bg-gray-900 overflow-hidden">
		<Navbar />

		<!-- Main Content -->
		<main
			class="relative z-10 flex-grow flex flex-col justify-center items-center text-center py-20"
		>
			<h1 class="text-4xl font-bold text-white mb-6">
				Analysis for {{ symbol }}
			</h1>
			<p class="text-lg text-gray-300 mb-8">
				Detailed analysis for the selected symbol.
			</p>
			<!-- Analysis content goes here -->
		</main>

		<Footer />
	</div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRoute } from "vue-router";
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";

// Use route to get the symbol parameter
const route = useRoute();
const symbol = ref(route.params.symbol);

// You can now use the symbol to fetch and display analysis data
</script>

<style scoped></style>
