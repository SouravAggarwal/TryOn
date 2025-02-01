<script setup lang="ts">
import { onMounted } from 'vue';
import gsap from 'gsap';

onMounted(() => {
  gsap.from('.hero-content', {
    opacity: 0,
    y: 30,
    duration: 1,
    ease: 'power2.out'
  });
});
</script>

<template>
  <section class="relative min-h-screen flex items-center bg-gradient-to-br from-purple-50 to-indigo-50">
    <div class="container mx-auto px-4 hero-content">
      <div class="text-center max-w-4xl mx-auto">
        <h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
          Virtual Clothing Try-On,<br />
          Powered by AI
        </h1>
        <p class="text-xl text-gray-600 mb-10">
          Experience clothes shopping like never before. Upload your photo and try on any garment virtually with our advanced AI technology.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <button class="btn btn-primary">Get Started</button>
          <button class="btn btn-secondary">View Samples</button>
        </div>
      </div>
    </div>
  </section>
</template>