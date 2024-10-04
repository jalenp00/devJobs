<template>
    <!-- Computer NavBar -->
    <div class="navbar fixed top-0 z-50 bg-base-100 h-[8vh] lg:h-[15vh] xl:h-[8vh] flex align-top justify-center items-center w-full">
        <!-- Left section for branding or logo -->
        <div class="flex justify-start">
        <NuxtLink :to="'/user/job'" class="btn btn-primary btn-ghost sm:text-lg md:text-xl lg:text-xl">devJobs</NuxtLink>
        </div>

        <!-- Search bar -->
        <div class="hidden sm:flex justify-center absolute left-1/2 transform -translate-x-1/2">
          <label class="input input-bordered flex items-center  sm:w-[30vw] md:w-[35vw] lg:w-[25vw]">
              <input type="text" class="grow" placeholder="Search Positions" 
              v-model="userSearch"
              @keyup.enter="emitSearch(userSearch)" />
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="h-4 w-4 opacity-70 cursor-pointer"
              @click="emitSearch(userSearch)">
              <path fill-rule="evenodd"
                  d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
                  clip-rule="evenodd" />
              </svg>
          </label>
        </div>

        <!-- Theme toggle -->
        <div class="hidden sm:flex absolute lg:right-[22.5vw] 2xl:right-[11.5vw]">
          <label class="swap swap-rotate">
            <!-- this hidden checkbox controls the state -->
            <input type="checkbox" v-model="isDarkMode" @click="toggleTheme(isDarkMode)" />

            <!-- sun icon -->
            <svg
              class="swap-off h-5 fill-current"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24">
              <path
                d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z" />
            </svg>

            <!-- moon icon -->
            <svg
              class="swap-on h-5 fill-current"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24">
              <path
                d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z" />
            </svg>
          </label>
        </div>
        
        <!-- Right section -->
        <div class="flex items-center ml-auto">
            <!-- My Jobs button -->
            <NuxtLink :to="'/employee/createJob'"
            class="hidden sm:flex btn btn-primary rounded-md mr-3"
            >Create Job</NuxtLink>
            <button
            v-if="isLoggedIn"
            class="hidden sm:flex btn btn-primary rounded-md"
            >*My Jobs</button>

            <!-- User dropdown -->
            <div v-if="isLoggedIn"
            class="dropdown dropdown-end ml-3 hidden sm:flex">
                <label tabindex="0" class="btn btn-ghost btn-circle avatar">
                    <div class="w-10 rounded-full">
                    <img alt="Tailwind CSS Navbar component"
                        src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                    </div>
                </label>
                <ul tabindex="0" class="menu menu-sm dropdown-content bg-secondary text-white rounded-box z-[1] mt-14 w-24 p-2 shadow">
                    <li><a>*Profile</a></li>
                    <li><a>*Settings</a></li>
                    <li><a @click="logout()">Logout</a></li>
                </ul>
            </div>

            <!-- Guest dropdown -->
            <div v-else
            class="dropdown dropdown-end ml-3 hidden sm:flex">
                <label tabindex="0" class="btn btn-ghost btn-circle avatar">
                    <div class="w-10 rounded-full">
                    <img alt="Tailwind CSS Navbar component"
                        src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                    </div>
                </label>
                <ul tabindex="0" class="menu menu-sm dropdown-content bg-secondary text-white rounded-box z-[1] mt-14 w-24 p-2 shadow">
                    <li><NuxtLink to="/signup">Sign up</NuxtLink></li>
                    <li><NuxtLink to="/login">Log in</NuxtLink></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Mobile Navbar -->
    <div class="navbar sm:hidden fixed top-0 z-50 bg-base-100 h-[10vh] flex justify-between items-center w-full ">
        <div class="flex justify-start">
            <NuxtLink :to="'/user/job'" class="btn btn-primary btn-ghost">devJobs</NuxtLink>
        </div>
        <!-- Search bar -->
        <div class="mt-3 sm:hidden">
          <label class="input input-bordered flex items-center justify-center ">
            <input type="text" class="grow" placeholder="Search" 
            />
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="h-4 w-4 opacity-70">
              <path fill-rule="evenodd"
                d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
                clip-rule="evenodd" />
            </svg>
          </label>
        </div>
  
        <!-- Hamburger menu -->
        <div class="sm:hidden">
          <button class="btn btn-ghost btn-circle" @click="toggleMobileMenu">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-6 h-6 stroke-current">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 6h16M4 12h16m-7 6h7" />
            </svg>
          </button>
        </div>
    </div>
  
      <!-- Hamburger Menu Contents -->
      <div v-if="isMobileMenuOpen" ref="mobileMenu" class="sm:hidden fixed top-14 right-0 w-auto bg-base-100 p-4 shadow-lg z-40">
        <ul class="menu menu-compact">
          <li><a class="flex justify-end" @click="closeMobileMenu">My Jobs</a></li>
          <li><a class="flex justify-end" @click="closeMobileMenu">Profile</a></li>
          <li><a class="flex justify-end" @click="closeMobileMenu">Settings</a></li>
          <li><a class="flex justify-end" @click="closeMobileMenu">Logout</a></li>
        </ul>
      </div>
</template>
  
<script setup>
  import { ref, defineEmits } from 'vue';
  import { onClickOutside } from '@vueuse/core';
  import { authStore } from '~/store/auth';
  import { useRouter } from 'vue-router';
  import Cookies from 'js-cookie';
  import { storeToRefs } from 'pinia';

  // Data
  const emit = defineEmits(['search', 'changeTheme']);
  const authS = authStore();
  const router = useRouter();

  // Mobile menu
  const isMobileMenuOpen = ref(false);
  const mobileMenu = ref('mobileMenu');

  // Theme toggle
  const isDarkMode = ref(true);

  // User
  const { 
    isLoggedIn: isLoggedIn,
  } = storeToRefs(authS);

  const userSearch = ref('');
  
  const toggleTheme = (lightTheme) => {
    lightTheme = !lightTheme;
    console.log('emitted: ' + lightTheme);
    emit('changeTheme', lightTheme);
  };

  onClickOutside(mobileMenu, () => {
    isMobileMenuOpen.value = false;
  });

  const toggleMobileMenu = () => {
    isMobileMenuOpen.value = !isMobileMenuOpen.value;
  };

  const emitSearch = (userSearch) => {
    if (userSearch != null) {
      emit('search', userSearch);
    }
    router.push('/user/job');
  };

  const logout = async () => {
    await authS.logout();
    router.push('/');
  }
  </script>