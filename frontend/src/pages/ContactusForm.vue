<template>
  <div class="relative">
    <!-- Loading overlay -->
    <div v-if="isLoading" class="absolute inset-0 bg-white bg-opacity-70 z-50 flex items-center justify-center">
      <div class="loader ease-linear rounded-full border-4 border-t-4 border-red-600 h-12 w-12"></div>
    </div>

    <div class="flex flex-col md:flex-row sm:p-20 p-4 gap-6">
      <!-- Contact Form -->
      <div class="md:w-1/2 space-y-4">
        <h2 class="text-2xl font-bold text-blue-900">GET IN TOUCH</h2>

        <div>
          <label class="block font-medium mb-1">First Name*</label> 
          <input type="text" v-model="firstName" class="w-full border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"/>
        </div>

        <div>
          <label class="block font-medium mb-1">Mobile No*</label>
          <input type="text" v-model="mobileNo" class="w-full border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"/>
        </div>

        <div>
          <label class="block font-medium mb-1">Your Email*</label>
          <input type="email" v-model="email" class="w-full border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"/>
        </div>

        <div>
          <label class="block font-medium mb-1">Message</label>
          <textarea rows="4" v-model="message" class="w-full border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"></textarea>
        </div>

        <button
          @click="submitContactForm"
          :disabled="isLoading"
          class="bg-red-600 text-white px-6 py-2 rounded hover:bg-red-700 transition float-right disabled:opacity-50"
        >
          {{ isLoading ? 'Submitting...' : 'SUBMIT' }}
        </button>
      </div>

      <!-- Embedded Google Map -->
      <div class="md:w-1/2">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.433318014443!2d77.54133337507593!3d13.01170168727569!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d75f0d93ca1%3A0x83a28732c8ed1d2f!2sSanjeevini%20Heart%20and%20Multi-Speciality%20Hospital!5e0!3m2!1sen!2sin!4v1716203671821!5m2!1sen!2sin"
          width="100%"
          height="100%"
          style="border:0; min-height: 450px;"
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const firstName = ref('')
const mobileNo = ref('')
const email = ref('')
const message = ref('')
const isLoading = ref(false)

const submitContactForm = async () => {
  isLoading.value = true
  try {
    const response = await fetch('/api/method/splitwise.splitwise.api.contact.submit_contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: firstName.value,
        mobile: mobileNo.value,
        email: email.value,
        message: message.value
      })
    })

    const result = await response.json()
    if (result.message?.message === 'Message submitted') {
      alert('Message sent successfully!')
        firstName.value = ''
        mobileNo.value = ''
        email.value = ''
        message.value = ''
    } else {
    alert('Failed to send message: ' + JSON.stringify(result))
    }
  } catch (err) {
    console.error(err)
    alert('Something went wrong!')
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.loader {
  border-top-color: transparent;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
