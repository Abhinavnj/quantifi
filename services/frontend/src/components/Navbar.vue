<template>
  <div class="navbar bg-black px-10" data-theme="custom-dark">
    <!-- Navbar Start (Brand Logo & Mobile Dropdown) -->
    <div class="navbar-start">
      <div class="dropdown">
        <!-- Hamburger menu for mobile -->
        <label tabindex="0" class="btn btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" />
          </svg>
        </label>
        <!-- Mobile dropdown menu items -->
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
          <li>
            <router-link to="/analysis">Analysis</router-link>
          </li>
          <li>
            <router-link to="/learn">Learn</router-link>
          </li>
          <li>
            <router-link to="/personalfinance">Personal Finance</router-link>
          </li>
        </ul>
      </div>

      <!-- Brand Logo for Desktop and Mobile -->
      <router-link to="/" class="text-2xl font-bold text-white flex items-center">
        <img src="../assets/favicon-1x1.png" alt="Quantifi Logo" class="h-8 w-8 mr-2" />
        Quantifi
      </router-link>
    </div>

    <!-- Navbar Center (Visible on larger screens) -->
    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li>
          <router-link to="/analysis">Analysis</router-link>
        </li>
        <li>
          <router-link to="/learn">Learn</router-link>
        </li>
        <li>
          <router-link to="/personalfinance">Personal Finance</router-link>
        </li>
      </ul>
    </div>

    <!-- Navbar End (Profile Dropdown) -->
    <div class="navbar-end">
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div class="w-10 rounded-full">
            <img alt="User Avatar" src="/user.png" />
          </div>
        </div>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
          <li><a>Profile</a></li>
          <li><a>Settings</a></li>
          <li><a>Logout</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// No script changes needed
</script>

<style scoped>
/* No additional styles needed */
</style>
