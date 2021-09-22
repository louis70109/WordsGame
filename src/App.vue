<template>
  <div id="app">
    <!-- <Barrage></Barrage> -->
    <LineLogin></LineLogin>
    <router-view />
  </div>
</template>

<script>
// import LineLogin from '../components/LineLogin.vue';
import LineLogin from '../src/components/LineLogin.vue'
export default {
  name: 'App',
  components: {
    LineLogin
  },
};
</script>
