<template>
  <nav class="fixed w-full bg-white/80 backdrop-blur-sm shadow-sm z-50">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between h-16">
        <router-link to="/" class="text-2xl font-bold text-primary">TryOn</router-link>
        
        <div class="hidden md:flex items-center space-x-8">
          <router-link to="/" class="text-gray-600 hover:text-primary">Home</router-link>
          <router-link to="/pricing" class="text-gray-600 hover:text-primary">Pricing</router-link>
          <button class="btn btn-primary">Login</button>
        </div>

        <button class="md:hidden">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>
    </div>
  </nav>
</template>