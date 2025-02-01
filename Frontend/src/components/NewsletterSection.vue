<script setup lang="ts">
import { ref } from 'vue';

const email = ref('');

const subscribe = () => {
  // Mock API call
  console.log('Subscribing:', email.value);
  email.value = '';
  alert('Thanks for subscribing!');
};
</script>

<template>
  <section class="section bg-primary text-white">
    <div class="container">
      <div class="max-w-2xl mx-auto text-center">
        <h2 class="text-3xl font-bold mb-4">Stay Updated</h2>
        <p class="mb-8">Get the latest updates about new features and early access to beta releases.</p>
        
        <form @submit.prevent="subscribe" class="flex flex-col sm:flex-row gap-4">
          <input
            v-model="email"
            type="email"
            placeholder="Enter your email"
            class="flex-1 px-4 py-3 rounded-lg text-gray-900"
            required
          />
          <button type="submit" class="btn bg-white text-primary hover:bg-gray-100">
            Subscribe
          </button>
        </form>
      </div>
    </div>
  </section>
</template>