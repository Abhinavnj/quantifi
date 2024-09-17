<template>
  <div>
    <!-- Timeframe selection -->
    <div class="mb-4">
      <label class="mr-2">Select Timeframe:</label>
      <select class="select select-bordered" v-model="selectedTimeframe">
        <option value="1M">1M</option>
        <option value="3M">3M</option>
        <option value="6M">6M</option>
        <option value="1Y">1Y</option>
        <option value="2Y">2Y</option>
        <option value="5Y">5Y</option>
      </select>
    </div>

    <!-- Chart -->
    <line-chart :chart-data="chartData" :options="chartOptions"></line-chart>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue';
import { Line } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  TimeScale,
} from 'chart.js';
import 'chartjs-adapter-date-fns';
import { format } from 'date-fns';

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  TimeScale,
);

export default defineComponent({
  name: 'Chart',
  components: {
    LineChart: Line,
  },
  props: {
    aggregateData: {
      type: Array,
      required: true,
    },
  },
  setup(props) {
    const selectedTimeframe = ref('6M');

    const filteredData = computed(() => {
      // Filter data based on selectedTimeframe
      const timeframes = {
        '1M': 30,
        '3M': 90,
        '6M': 180,
        '1Y': 365,
        '2Y': 730,
        '5Y': 1825,
      };
      const days = timeframes[selectedTimeframe.value];
      const cutoffTime = Date.now() - days * 24 * 60 * 60 * 1000;
      return props.aggregateData
        .filter((dataPoint) => dataPoint.t >= cutoffTime)
        .sort((a, b) => a.t - b.t);
    });

    const chartData = computed(() => {
      return {
        labels: filteredData.value.map((dataPoint) => new Date(dataPoint.t)), // Convert epoch to Date
        datasets: [
          {
            label: 'Closing Price',
            data: filteredData.value.map((dataPoint) => dataPoint.c),
            borderColor: '#c9882e', // Gold color for line
            backgroundColor: 'rgba(201, 136, 46, 0.2)', // Light gold fill
            fill: true, // Filled chart like the image
            pointBackgroundColor: '#c9882e', // Gold hover dot
            pointRadius: 3, // Set the radius for hover dots
            pointHoverRadius: 6, // Larger radius when hovering
            pointHoverBorderColor: '#fff', // White border on hover
            pointHoverBorderWidth: 2, // Border thickness on hover
            tension: 0.4, // Smooth curve for line
          },
        ],
      };
    });

    const chartOptions = computed(() => {
      let timeUnit = 'month';
      if (selectedTimeframe.value === '1M' || selectedTimeframe.value === '3M') {
        timeUnit = 'day';
      } else if (selectedTimeframe.value === '6M' || selectedTimeframe.value === '1Y') {
        timeUnit = 'month';
      } else {
        timeUnit = 'year';
      }

      return {
        responsive: true,
        interaction: {
          mode: 'nearest',
          intersect: false,
        },
        plugins: {
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'rgba(0, 0, 0, 0.8)', // Dark tooltip background
            titleColor: '#fff', // White tooltip title
            bodyColor: '#fff', // White tooltip body
            callbacks: {
              label: function (tooltipItem) {
                return `$${tooltipItem.formattedValue} USD`;
              },
              title: function (tooltipItems) {
                return format(new Date(tooltipItems[0].label), 'MMM dd, yyyy'); // Human-readable date
              },
            },
          },
        },
        scales: {
          x: {
            type: 'time',
            time: {
              unit: timeUnit, // Ensure this is still dynamic based on the timeframe
              displayFormats: {
                day: 'MMM dd, yyyy',  // Ensure this displays only month, day, and year
                month: 'MMM yyyy',
                year: 'yyyy',
              },
            },
            ticks: {
              color: '#aaa', // Lighter ticks
              autoSkip: true,
              maxRotation: 0,
              callback: function (value) {
                return format(new Date(value), 'MMM dd, yyyy'); // Ensure this returns only the date
              },
            },
          },
          y: {
            grid: {
              color: 'rgba(255, 255, 255, 0.1)', // Light grid lines
            },
            ticks: {
              color: '#aaa', // Lighter ticks
            },
            title: {
              display: true,
              text: 'Closing Price (USD)',
              color: '#fff',
            },
          },
        },
        elements: {
          point: {
            radius: 0, // Hide points unless hovered
          },
        },
      };
    });

    return {
      selectedTimeframe,
      chartData,
      chartOptions,
    };
  },
});
</script>

<style scoped>
/* Dark background for the chart area */
div {
  background-color: #1c1c1e;
  padding: 16px;
  border-radius: 8px;
}
</style>
