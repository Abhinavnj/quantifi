<template>
  <div class="stats shadow">
    <div class="stat">
      <div class="stat-title">{{ title }}</div>
      <div class="stat-value">${{ value }}</div>
      <div class="stat-figure text-secondary">
        <InformationCircleIcon class="h-6 w-6 text-blue-500" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { InformationCircleIcon } from '@heroicons/vue/24/outline'

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
