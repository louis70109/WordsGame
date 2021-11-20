<template>
  <div id="app">
    <div>
    <LineLogin></LineLogin>
    <span v-if="userCheck() === true">
      <Barrage></Barrage>
    </span>
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
