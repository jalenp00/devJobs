<template>
  <div :data-theme="theme" class="bg-base-100">
    <header>
      <ResponsiveNavBar @search="handleSearch" @changeTheme="handleTheme"/>
    </header>
    <main>
      <NuxtPage :searchTerm="searchTerm"/>
    </main>
  </div>
</template>

<script setup lang="ts">
import ResponsiveNavBar from './components/global/ResponsiveNavBar.vue';
import { authStore } from '~/store/auth';
import Cookies from 'js-cookie';

const searchTerm = ref('');
const theme = ref('business');
const authS = authStore();

const handleSearch = (search: string) => {
  searchTerm.value = search;
};

const handleTheme = (isDarkMode: Boolean) => {
  console.log('isDarkMode: ' + isDarkMode);
  if (isDarkMode) {
    theme.value = 'business';
  } else {
    theme.value = 'lofi';
  }
  console.log('theme: ' + theme.value);
};

onMounted(() => {
  console.log(Cookies.get('token'));
  if (Cookies.get('token')) {
    authS.fetchUser();
  }
});
</script>

<style>

</style>
