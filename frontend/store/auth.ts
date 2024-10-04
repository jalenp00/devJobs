import { defineStore } from 'pinia';
import userService from '../service/userService';
import Cookies from 'js-cookie';

export const authStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
  }),
  actions: {
    async signup(user: CreateUser) {
      try {
        const response = await userService.createUser(user);
        if (response.access_token) {
          Cookies.set('token', response.access_token);
          this.isLoggedIn = true;
        } else {
          console.error('Signup failed:', response.data);
        }
      } catch (error) {
        console.error('Signup failed:', error);
      }
    },
    async login(user: UserLogin) {
      try {
        const response = await userService.login(user);
        if (response.access_token) {
          Cookies.set('token', response.access_token);
          this.isLoggedIn = true;
          console.log('logged in');
        } else {
          console.error('Login failed:', response.data);
        }
      } catch (error) {
        console.error('Login failed:', error);
      }
    },
    async fetchUser() {
      try {
        const response = await userService.getUser();
        if (response.error) {
          console.error('Fetch user failed:', response.error);
        }
        this.isLoggedIn = true;
        console.log('user fetched');
      } catch (error) {
        console.error('Fetch user failed:', error);
      }
    },
    async logout() {
      try {
        const response = await userService.logout();
        console.log(JSON.stringify(response));
        if (response.success) {
          Cookies.remove('token');
          this.isLoggedIn = false;
          console.log('logged out');
          return true;
        }
        console.error('Logout failed:', response.error);
      } catch (error) {
        console.error('Logout failed:', error);
        return false;
      }
    },
  },
});