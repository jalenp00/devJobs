<template>
    <div class="min-h-screen">
        <div class="flex flex-col items-center pt-[17vh]">
            <h1 class="mb-5 font-bold text-xl">Login</h1>
            <div>
                <label class="input input-bordered rounded-lg flex items-center mt-2">
                    <input type="text" placeholder="Email" class="w-full"
                    v-model="userInfo.email"/>
                </label>
                <label class="input input-bordered rounded-lg flex items-center mt-2 w-[30vw]">
                    <input type="text" placeholder="Password" class="w-full"
                    v-model="userInfo.password"
                    @keyup.enter="submit()"/>
                </label>
                <button class="btn btn-primary w-full rounded-lg mt-4 text-md"
                @click="submit()">Login</button>
            </div>
            <p class="text-center mt-3 text-[14px]">New to devJobs? 
                <NuxtLink to="/signup" class="text-gray-600">Sign Up</NuxtLink>
            </p>
        </div>
    </div>
</template>

<script setup lang="ts">
import { authStore } from '~/store/auth';
import { useRouter } from 'vue-router';

const router = useRouter();
const authS = authStore();

const { 
    isLoggedIn: isLoggedIn,
  } = storeToRefs(authS);

const userInfo = ref<UserLogin>({
    email: '',
    password: ''
});

const submit = async () => {
    await authS.login(userInfo.value);
    
    if (isLoggedIn) {
        router.push('/user/job');
    }
}

</script>