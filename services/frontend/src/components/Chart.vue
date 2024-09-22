<template>
  <div class="p-4 bg-black rounded-lg shadow-md">
    <div class="flex justify-end mb-4">
      <div class="btn-group">
        <button v-for="timeframe in timeframes" :key="timeframe" @click="selectedTimeframe = timeframe"
          :class="['btn', selectedTimeframe === timeframe ? 'btn-active' : '']">
          {{ timeframe }}
        </button>
      </div>
    </div>
    <div class="h-96 w-full">
      <LineChart :chart-data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { Line } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale, Filler,
} from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale, Filler);

export default defineComponent({
  name: 'StockChart',
  components: {
    LineChart: Line,
  },
  props: {
    aggregateData: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      timeframes: ['5D', '1M', '3M', '6M', 'YTD', '1Y', '5Y'],
      selectedTimeframe: '1Y',
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        plugins: {
          tooltip: {
            enabled: true,
            mode: 'index',
            intersect: false,
            callbacks: {
              label: function (context) {
                let label = context.dataset.label || '';
                if (label) {
                  label += ': ';
                }
                if (context.parsed.y !== null) {
                  label += '$' + context.parsed.y.toFixed(2);
                }
                return label;
              },
            },
          },
          legend: {
            display: false,
          },
        },
        scales: {
          x: {
            display: true,
            title: {
              display: false,
            },
            ticks: {
              autoSkip: true,
              maxTicksLimit: 10,
              color: '#FFFFFF', // White color for x-axis labels
            },
            grid: {
              display: false,
            },
          },
          y: {
            display: true,
            title: {
              display: false,
            },
            ticks: {
              callback: function (value) {
                return '$' + value;
              },
              color: '#FFFFFF', // White color for y-axis labels
            },
            grid: {
              display: false,
            },
          },
        },
      },
    }
  },
  computed: {
    filteredData() {
      const data = this.aggregateData.slice().sort((a, b) => a.t - b.t);
      const endDate = new Date(data[data.length - 1].t);
      let startDate;

      switch (this.selectedTimeframe) {
        case '5D':
          startDate = new Date(endDate);
          startDate.setDate(endDate.getDate() - 5);
          break;
        case '1M':
          startDate = new Date(endDate);
          startDate.setMonth(endDate.getMonth() - 1);
          break;
        case '3M':
          startDate = new Date(endDate);
          startDate.setMonth(endDate.getMonth() - 3);
          break;
        case '6M':
          startDate = new Date(endDate);
          startDate.setMonth(endDate.getMonth() - 6);
          break;
        case 'YTD':
          startDate = new Date(endDate.getFullYear(), 0, 1);
          break;
        case '1Y':
          startDate = new Date(endDate);
          startDate.setFullYear(endDate.getFullYear() - 1);
          break;
        case '5Y':
          startDate = new Date(endDate);
          startDate.setFullYear(endDate.getFullYear() - 5);
          break;
        default:
          startDate = new Date(data[0].t);
      }

      const startTime = startDate.getTime();
      const endTime = endDate.getTime();

      return data.filter(point => point.t >= startTime && point.t <= endTime);
    },
    chartData() {
      return {
        labels: this.filteredData.map(point => this.formatDate(point.t)),
        datasets: [{
          label: 'Stock Price',
          data: this.filteredData.map(point => point.c),
          borderColor: '#cd913e', // Line color
          backgroundColor: 'rgba(205, 145, 62, 0.2)', // Semi-transparent fill color
          tension: 0, // Straight lines between points
          fill: true,
        }]
      }
    },
  },
  methods: {
    formatDate(timestamp) {
      const date = new Date(timestamp);
      const options = { month: 'short', day: 'numeric', year: 'numeric' };
      return date.toLocaleDateString(undefined, options);
    },
  },
})
</script>

<style scoped>
/* Adjust the height to make the chart larger */
.h-96 {
  height: 24rem;
}
</style>
