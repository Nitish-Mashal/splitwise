<template>
    <div class="font-sans text-gray-800">

        <div class="container">
            <!-- Top Header: Logo + Call -->
            <header class="flex items-center justify-between px-4 py-2">
                <!-- Logo -->
                <img src="../assets/Images/Sanjeevini-logo.png" alt="Logo" class="h-12 w-auto" />

                <!-- Call Button -->
                <div class="flex items-center gap-1">
                    <button class="bg-green-700 text-white p-2 rounded-md">
                        <span class=" font-bold text-sm leading-tight text-right">
                            CALL<br />
                            <span class="text-xs font-normal">24/7 Helpline</span>
                        </span>
                    </button>
                </div>
            </header>
        </div>

        <!-- Blue Nav Bar -->
        <nav class="bg-[#007AB3] text-white px-4 py-4">
            <!-- Top Nav Row (Small Screens) -->
            <div class="flex items-center justify-between md:hidden">
                <!-- Key Links (short ones for mobile) -->
                <div class="flex gap-2 text-sm font-semibold whitespace-nowrap">
                    <router-link to="/" class="hover:underline">Book Appointment</router-link>
                    <span>|</span>
                    <router-link to="/" class="hover:underline">Specialities</router-link>
                </div>

                <!-- Hamburger -->
                <button @click="isMenuOpen = !isMenuOpen" class="text-2xl focus:outline-none">
                    ☰
                </button>
            </div>

            <!-- Expandable Menu for Small Screens -->
            <transition name="fade">
                <div v-if="isMenuOpen" class="flex flex-col gap-2 mt-3 text-md font-semibold md:hidden">
                    <router-link to="/dashboard" class="hover:underline">Home</router-link>
                    <router-link to="/" class="hover:underline">Our Doctors</router-link>
                    <router-link to="/" class="hover:underline">Blogs</router-link>
                    <router-link to="/contactus" class="hover:underline">Contact Us</router-link>
                </div>
            </transition>

            <!-- Full Menu for Medium and Larger Screens -->
            <div class="hidden md:flex justify-end items-center gap-6 font-semibold text-sm">
                <router-link to="/dashboard" class="hover:underline">Home</router-link>
                <router-link to="/" class="hover:underline">Our Doctors</router-link>
                <router-link to="/" class="hover:underline">Blogs</router-link>
                <router-link to="/contactus" class="hover:underline">Contact Us</router-link>
            </div>
        </nav>

    </div>
</template>

<script setup>
import { ref } from 'vue'
const isMenuOpen = ref(false)
</script>

<style scoped>
/* Optional animation */
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
