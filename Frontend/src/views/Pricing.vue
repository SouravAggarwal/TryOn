<template>
  <div class="pt-20">
    <section class="section">
      <div class="container">
        <h1 class="heading text-center">Simple, Transparent Pricing</h1>
        <p class="subheading text-center">Choose the plan that best fits your needs</p>

        <div class="grid md:grid-cols-3 gap-8 mt-12">
          <!-- Basic Plan -->
          <div class="p-6 rounded-xl border-2 hover:border-primary transition-all">
            <h3 class="text-2xl font-bold mb-2">Basic</h3>
            <p class="text-gray-600 mb-4">Perfect for individuals</p>
            <div class="text-4xl font-bold mb-6">$9<span class="text-lg text-gray-600">/month</span></div>
            <ul class="space-y-3 mb-8">
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                50 Try-ons per month
              </li>
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                Basic analytics
              </li>
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                Email support
              </li>
            </ul>
            <button class="w-full btn btn-primary">Get Started</button>
          </div>

          <!-- Pro Plan -->
          <div class="p-6 rounded-xl border-2 border-primary bg-purple-50">
            <div class="absolute top-4 right-4 bg-primary text-white px-3 py-1 rounded-full text-sm">Popular</div>
            <h3 class="text-2xl font-bold mb-2">Pro</h3>
            <p class="text-gray-600 mb-4">For growing businesses</p>
            <div class="text-4xl font-bold mb-6">$29<span class="text-lg text-gray-600">/month</span></div>
            <ul class="space-y-3 mb-8">
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                Unlimited Try-ons
              </li>
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                Advanced analytics
              </li>
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                Priority support
              </li>
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                API access
              </li>
            </ul>
            <button class="w-full btn btn-primary">Get Started</button>
          </div>

          <!-- Enterprise Plan -->
          <div class="p-6 rounded-xl border-2 hover:border-primary transition-all">
            <h3 class="text-2xl font-bold mb-2">Enterprise</h3>
            <p class="text-gray-600 mb-4">Custom solutions</p>
            <div class="text-4xl font-bold mb-6">Custom</div>
            <ul class="space-y-3 mb-8">
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                Custom integration
              </li>
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                Dedicated support
              </li>
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                SLA guarantee
              </li>
              <li class="flex items-center">
                <span class="text-primary mr-2">✓</span>
                Custom features
              </li>
            </ul>
            <button class="w-full btn btn-secondary">Contact Sales</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>