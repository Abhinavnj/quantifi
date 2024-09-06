<template>
  <nav class="relative z-10 bg-gray-900 shadow-lg">
    <div class="container mx-auto px-1 py-3">
      <div class="navbar bg-transparent">
        <div class="navbar-start">
          <!-- Use router-link for the brand name to link to the Home page -->
          <img src="../assets/favicon-1x1.png" alt="Quantifi Logo" class="h-8 w-8 mr-2" />
          <router-link to="/" class="text-2xl font-bold text-white">
            Quantifi
          </router-link>
        </div>
        <div class="navbar-center hidden lg:flex">
          <ul class="menu menu-horizontal p-0">
            <li>
              <!-- Use router-link for navigation to the Home page -->
              <router-link to="/analysishome" class="text-base font-medium text-white hover:text-primary">
                Analysis
              </router-link>
            </li>
            <li>
              <!-- Use router-link for navigation to the Contact page -->
              <router-link to="/learnhome" class="text-base font-medium text-white hover:text-primary">
                Learn
              </router-link>
            </li>
            <li>
              <!-- Use router-link for navigation to the Contact page -->
              <router-link to="/personalfinance" class="text-base font-medium text-white hover:text-primary">
                Personal Finance
              </router-link>
            </li>
          </ul>
        </div>
        <div class="navbar-end">
          <ul class="menu menu-horizontal p-0">
            <div class="dropdown dropdown-end">
              <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
                <div class="w-10 rounded-full">
                  <img alt="Tailwind CSS Navbar component" src="/reetu-circle.png" />
                </div>
              </div>
              <ul tabindex="0" class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                <li>
                  <a class="justify-between">
                    Profile
                    <span class="badge">New</span>
                  </a>
                </li>
                <li><a>Settings</a></li>
                <li><a>Logout</a></li>
              </ul>
            </div>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
// No changes needed in the script for this specific case
</script>
