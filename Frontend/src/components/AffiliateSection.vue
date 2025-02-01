<template>
  <section class="section bg-gray-50">
    <div class="container">
      <h2 class="heading text-center">Trusted by Leading Brands 1</h2>
      <p class="subheading text-center">
        Join the companies revolutionizing online shopping with TryOn
      </p>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-8 mt-12">
        <div v-for="i in 4" :key="i" class="flex items-center justify-center p-6 bg-white rounded-lg shadow-sm">
          <div class="h-12 w-32 bg-gray-200 animate-pulse rounded"></div>
        </div>
      </div>

      <div class="mt-16 text-center">
        <h3 class="text-2xl font-bold mb-4">Ready to Transform Your Business?</h3>
        <button class="btn btn-primary">Become a Partner</button>
      </div>
    </div>
  </section>
</template>