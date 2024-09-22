<template>
  <div class="stats shadow">
    <div class="stat">
      <div class="stat-title">{{ title }}</div>
      <div class="stat-value">${{ value }}</div>
      <div class="stat-figure text-secondary relative">
        <!-- Information Icon with DaisyUI tooltip, using dynamic content -->
        <div v-if="info" class="tooltip tooltip-left" :data-tip="info">
          <InformationCircleIcon class="h-6 w-6 text-blue-500 cursor-pointer" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { InformationCircleIcon } from '@heroicons/vue/24/outline';

defineProps({
  title: {
    type: String,
    required: true,
  },
  value: {
    type: String,
    required: true,
  },
  info: {
    type: String,
    required: false, // Not all stats may have a tooltip
  },
});
</script>

<style scoped>
/* No additional styles needed */
</style>
