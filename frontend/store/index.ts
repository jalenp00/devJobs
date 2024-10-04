import { defineStore } from 'pinia'

export const userStore = defineStore('user', {
  state: () => ({
    userId: null,
  }),
  actions: {
    updateUserId(id: string) {
      this.userId = id;
    },
  },
});
