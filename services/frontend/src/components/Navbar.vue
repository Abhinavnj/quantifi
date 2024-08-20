<template>
	<nav class="relative z-10 bg-gray-900 shadow-lg">
		<div class="container mx-auto px-4 py-3">
			<div class="navbar bg-transparent">
				<div class="navbar-start">
					<!-- Use router-link for the brand name to link to the Home page -->
					<img
						src="../assets/favicon-1x1.png"
						alt="Quantifi Logo"
						class="h-8 w-8 mr-2"
					/>
					<router-link to="/" class="text-2xl font-bold text-white">
						Quantifi
					</router-link>
				</div>
				<div class="navbar-end">
					<ul class="menu menu-horizontal p-0">
						<li>
							<!-- Use router-link for navigation to the Home page -->
							<router-link
								to="/"
								class="text-base font-medium text-white hover:text-primary"
							>
								Home
							</router-link>
						</li>
						<li>
							<!-- Use router-link for navigation to the Contact page -->
							<router-link
								to="/contact"
								class="text-base font-medium text-white hover:text-primary"
							>
								Contact
							</router-link>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</nav>
</template>

<script setup lang="ts">
// No changes needed in the script for this specific case
</script>
