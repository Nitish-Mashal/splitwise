<template>
    <div>
        <div class="relative w-full h-72">
            <!-- Image -->
            <img src="../assets/Images/DocImage.png" class="w-full h-72 object-cover" alt="Doctor Image" />

            <!-- Overlay Text -->
            <div class="absolute left-20 top-1/2 transform -translate-y-1/2 text-blue-950 text-[35px] font-bold">
                CONTACT US
            </div>
        </div>

<div class="p-4">
  <div class="flex flex-wrap justify-center gap-6">

    <!-- Card 1 -->
    <div class="flex w-full sm:w-auto">
      <!-- Left Blue Icon Box -->
      <div class="bg-blue-700 w-24 h-24 flex items-center justify-center">
        <img src="../assets/Images/Emergency.png" class="w-10 h-10" alt="Emergency Icon" />
      </div>

      <!-- Right Text Box -->
      <div class="bg-gray-100 flex-1 h-24 flex flex-col justify-center px-4 min-w-[250px]">
        <p class="font-bold text-gray-700 flex justify-center">EMERGENCY</p>
        <p class="text-blue-900 text-lg flex justify-center">+91 6362977715</p>
      </div>
    </div>

    <!-- Card 2 -->
    <div class="flex w-full sm:w-auto">
      <div class="bg-red-500 w-24 h-24 flex items-center justify-center">
        <img src="../assets/Images/Appointment.png" class="w-10 h-10" alt="Appointment Icon" />
      </div>
      <div class="bg-gray-100 flex-1 h-24 flex flex-col justify-center px-4 min-w-[250px]">
        <p class="font-bold text-gray-700 flex justify-center">APPOINTMENT</p>
        <p class="text-blue-900 text-lg flex justify-center">+91 7676000676</p>
        <p class="text-blue-900 text-lg flex justify-center">+91 9015115511</p>
      </div>
    </div>

    <!-- Card 3 -->
    <div class="flex w-full sm:w-auto">
      <div class="bg-green-700 w-24 h-24 flex items-center justify-center">
        <img src="../assets/Images/Email.png" class="w-10 h-10" alt="Email Icon" />
      </div>
      <div class="bg-gray-100 flex-1 h-24 flex flex-col justify-center px-4 min-w-[250px]">
        <p class="font-bold text-gray-700 flex justify-center">EMAIL</p>
        <p class="text-blue-900 text-lg flex justify-center">pro@sanjeevinihospital.com</p>
      </div>
    </div>

  </div>
</div>

    <ContactUsForm />
</div>
</template>



<script>
import ContactUsForm from './ContactusForm.vue'

export default {
  name: 'ContactUs',
  components: {
    ContactUsForm,
  }
}
</script>
