<template>
  <div id="app">
    <LineLogin></LineLogin>
    <router-view />
  </div>
</template>

<script>
import LineLogin from '../src/components/LineLogin.vue';
export default {
  name: 'App',
  components: {
    LineLogin,
  },
};
</script>
