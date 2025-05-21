<template>
  <footer class="bg-white text-blue-900 px-6 py-10">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10 text-sm p-8">
      <!-- Contact Section -->
      <div>
        <h3 class="font-bold mb-2">Contact</h3>
        <p>Sanjeevini Super Speciality Hospital<br />
          Last bus stop, Mahalakshmi Layout,<br />
          Bengaluru - 560086</p>
        <p class="mt-2">+91 9015115511</p>
        <p>pro@sanjeevinihospital.com</p>
        <p>www.sanjeevinihospital.com</p>
        <!-- <div class="flex space-x-4 mt-4">
          <a href="#"><img src="../assets/icons/facebook.svg" class="w-5 h-5" alt="Facebook" /></a>
          <a href="#"><img src="../assets/icons/instagram.svg" class="w-5 h-5" alt="Instagram" /></a>
          <a href="#"><img src="../assets/icons/twitter.svg" class="w-5 h-5" alt="Twitter" /></a>
          <a href="#"><img src="../assets/icons/youtube.svg" class="w-5 h-5" alt="YouTube" /></a>
        </div> -->
      </div>

      <!-- Specialities Section -->
      <div>
        <h3 class="font-bold mb-2">Specialities</h3>
        <ul class="space-y-1">
          <li>Cardiology and Cardiothoracic surgery</li>
          <li>Neurology</li>
          <li>Neuro Surgery</li>
          <li>Oncology</li>
          <li>Vascular Surgery</li>
          <li>NeuroInterventional Radiology</li>
          <li>More Specialities</li>
        </ul>
      </div>

      <!-- Quick Links -->
      <div>
        <h3 class="font-bold mb-2">Quick Links</h3>
        <ul class="space-y-1">
          <router-link to="/dashboard" class="hover:underline"><div>Home</div></router-link>
          <router-link to="/contactus" class="hover:underline"><div>Contact Us</div></router-link>
        </ul>
      </div>

      <!-- About & Legal -->
      <div>
        <h3 class="font-bold mb-2">About</h3>
        <ul class="space-y-1 mb-4">
          <li><a href="#">CEO Message</a></li>
          <li><a href="#">About us</a></li>
          <li><a href="#">Our Doctors</a></li>
        </ul>
        <h3 class="font-bold mb-2">Legal</h3>
        <ul class="space-y-1">
          <li><a href="#">Return and Refund Policy</a></li>
          <li><a href="#">Terms and Conditions</a></li>
          <li><a href="#">Privacy Policy</a></li>
        </ul>
      </div>
    </div>
  </footer>
</template>
