<!-- <script setup lang="ts">
import { ref } from 'vue'

defineProps<{ msg: string }>()

const count = ref(0)
</script>

<template>
  <h1 className="text-3xl font-bold underline">{{ msg }}</h1>
  <div class="card bg-base-100 w-96 shadow-xl">
    <button class="btn btn-primary" type="button" @click="count++">count is {{ count }}</button>
  </div>
</template> -->

<!-- <template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'Ping',
	data() {
		return {
			msg: '',
		};
	},
	methods: {
		getMessage() {
			axios.get('/')
				.then((res) => {
					this.msg = res.data;
				})
				.catch((error) => {
					console.error(error);
				});
		},
	},
	created() {
		this.getMessage();
	},
};
</script> -->

<!-- <template>
  <div>{{ answer }}</div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      answer: {},
    };
  },
  methods: {
    async getBitcoinIndex() {
      const { data } = await axios.get(
        "https://api.coindesk.com/v1/bpi/historical/close.json",
        {
          params: {
            start: "2022-09-01",
            end: "2022-09-05",
          },
        }
      );
      this.answer = data;
    },
  },
  beforeMount() {
    this.getBitcoinIndex();
  },
};
</script> -->

<template>
  <div>
    <h1>Bitcoin Index</h1>
    <pre>{{ answer }}</pre>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      answer: {},
    };
  },
  methods: {
    async getBitcoinIndex() {
      try {
        const { data } = await axios.get(
          "http://localhost:5001/test"
        );
        console.log(data);  // Log the data to the console
        this.answer = data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
  },
  beforeMount() {
    this.getBitcoinIndex();
  },
};
</script>
