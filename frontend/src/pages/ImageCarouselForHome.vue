<template>
    <div class="w-full relative overflow-hidden rounded-lg shadow-lg">
        <div class="flex transition-transform duration-500 ease-in-out"
            :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
            <div v-for="(image, index) in images" :key="index" class="flex-none w-full">
                <img :src="image" alt="Carousel image" class="w-full object-cover" />
            </div>
        </div>

        <!-- Indicators -->
        <div class="absolute bottom-3 left-1/2 transform -translate-x-1/2 flex space-x-2">
            <span v-for="(image, index) in images" :key="'dot-' + index" class="w-3 h-3 rounded-full cursor-pointer"
                :class="currentIndex === index ? 'bg-white' : 'bg-gray-400'" @click="goToSlide(index)">
            </span>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

import Carousel1 from '@/assets/Images/Carousel1.jpg'
import Carousel2 from '@/assets/Images/Carousel2.jpg'
import Carousel3 from '@/assets/Images/Carousel3.jpg'

const images = [Carousel1, Carousel2, Carousel3]
const currentIndex = ref(0)
let interval = null

const nextSlide = () => {
    currentIndex.value = (currentIndex.value + 1) % images.length
}

const goToSlide = (index) => {
    currentIndex.value = index
}

// Auto slide every 3 seconds
onMounted(() => {
    interval = setInterval(nextSlide, 3000)
})

onUnmounted(() => {
    clearInterval(interval)
})
</script>
