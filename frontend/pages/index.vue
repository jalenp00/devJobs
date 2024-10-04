<template>
  <div class="min-h-screen">
    <!-- Hero Section -->
    <section class="hero min-h-[50vh] bg-base-100">
      <div class="hero-content text-center">
        <div class="max-w-lg">
          <h1 class="text-5xl font-bold">Welcome to devJobs</h1>
          <p class="py-6">Find your dream job with ease and simplicity.</p>
          <NuxtLink to="/signup" class="btn btn-primary rounded-lg">Get Started</NuxtLink>
        </div>
      </div>
    </section>
    <div class="divider"></div>
    <!-- Cards Section -->
    <section class="py-10 bg-base-100">
      <div class="container mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <!-- Card 1 -->
          <div class="card bg-base-200 shadow-xl">
            <div class="card-body">
              <h2 class="card-title">Easy to Use</h2>
              <div class="card-subtitle">
                <p>Quick, easy and all in one place.</p>
              </div>
              <div class="card-body">
                <p>• No promoted jobs to sift through</p>
                <p>• Only site dedicated to development roles</p>
              </div>
            </div>
          </div>
          <!-- Card 2 -->
          <div class="card bg-base-200 shadow-xl">
            <div class="card-body">
              <h2 class="card-title">Simple Process</h2>
              <div class="card-subtitle">
                <p>Apply for jobs with just a few clicks</p>
              </div>
              <div class="card-body">
                <p>• Submit your resume and CV once</p>
                <p>• No annoying external links to sift through</p>
              </div>
            </div>
          </div>
          <!-- Card 3 -->
          <div class="card bg-base-200 shadow-xl">
            <div class="card-body">
              <h2 class="card-title">No ghost listings</h2>
              <div class="card-subtitle">
                <p>All listings are verified and active</p>
              </div>
              <div class="card-body">
                <p>• Listings are active only for 30 days</p>
                <p>• See how many applications have been submitted</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
</style>