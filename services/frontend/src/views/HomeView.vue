<script setup lang="ts">
import HelloWorld from '../components/HelloWorld.vue'
</script>

<template>
  <main>
    <HelloWorld />
  </main>
</template>

<!-- <template>
  <div class="home">
    <h1>Welcome to the Home Page</h1>
    <p>{{ message }}</p>
    <button @click="fetchMessage">Fetch Message</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      message: ''
    }
  },
  methods: {
    async fetchMessage() {
      try {
        const response = await axios.get('/')
        this.message = response.data.message
      } catch (error) {
        console.error('Error fetching message:', error)
      }
    }
  },
  created() {
    this.fetchMessage()
  }
}
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
}
</style> -->
