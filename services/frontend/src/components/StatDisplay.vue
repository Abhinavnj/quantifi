<template>
	<div class="stat">
		<div class="stat-title">{{ title }}</div>
		<div class="stat-value">${{ value }}</div>
	</div>
</template>

<!-- import { defineProps } from "vue"; -->

<script setup lang="ts">
defineProps({
	title: {
		type: String,
		required: true,
	},
	value: {
		type: String,
		required: true,
	},
});
</script>

<style scoped>
/* Add any specific styles if needed */
</style>
