<template>
  <div class="font-sans text-gray-800">

    <ImageCarouselForHome />
    <HospitalInfo />

  </div>
</template>

<script>
import HospitalInfo from './HospitalInfo.vue'
import ImageCarouselForHome from './ImageCarouselForHome.vue'

export default {
  name: 'Dashboard',
  components: {
    ImageCarouselForHome,
    HospitalInfo
  }
}
</script>
