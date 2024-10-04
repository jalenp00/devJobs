<template>
    <div class="min-h-screen">
        <div class="flex flex-col items-center pt-[17vh]">
            <h1 class="mb-5 font-bold text-xl">Sign Up</h1>
            <div>
                <label class="input input-bordered rounded-lg flex items-center">
                    <input type="text" placeholder="Full Name" class="w-full"
                    v-model="userInfo.name"  />
                </label>
                <label class="input input-bordered rounded-lg flex items-center mt-2">
                    <input type="text" placeholder="Email" class="w-full"
                    v-model="userInfo.email"/>
                </label>
                <label class="input input-bordered rounded-lg flex items-center mt-2 w-[30vw]">
                    <input type="password" placeholder="Password" class="w-full"
                    v-model="userInfo.password"/>
                </label>
                <label class="input input-bordered rounded-lg flex items-center mt-2">
                    <input type="password" placeholder="Confirm Password" class="w-full"
                    v-model="confirmPw"
                    @keyup.enter="signup()"/>
                </label>
                <button class="btn btn-primary w-full rounded-lg mt-4 text-md"
                @click="signup()">Create Account</button>
            </div>
            <p class="text-center mt-3 text-[14px]">Already have an account? 
                <NuxtLink to="/Login" class="text-gray-600">Log In</NuxtLink>
            </p>
        </div>
    </div>
</template>

<script setup lang="ts">
import { authStore } from '~/store/auth';
import { useRouter } from 'vue-router';

const router = useRouter();
const authS = authStore();

const userInfo = ref<CreateUser>({
    name: '',
    email: '',
    password: ''
});

const confirmPw = ref('');

const { 
    isLoggedIn: isLoggedIn,
  } = storeToRefs(authS);

const signup = async () => {
    if (userInfo.value.password === confirmPw.value) {
        await authS.signup(userInfo.value);
        if (isLoggedIn) {
            router.push('/user/job');
        }
    }
}

</script>