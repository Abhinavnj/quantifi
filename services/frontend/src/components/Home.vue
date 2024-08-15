<script setup lang="ts">
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
</template>
