<template>
  <div id="app">
    <LineLogin></LineLogin>
    <div v-if="userCheck() === true">
    <Barrage></Barrage>
    </div>
    <router-view />
  </div>
</template>

<script>
import LineLogin from '../src/components/LineLogin.vue';
import Barrage from '../src/components/Barrage.vue';
import { userCheck } from './utils/users';
export default {
  name: 'App',
  components: {
    LineLogin,
    Barrage,
  },
  setup() {
    return { userCheck };
  },
};
</script>
