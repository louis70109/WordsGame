<template>
  <div class="line_login">
    <img
      alt="Vue logo"
      src="../assets/btn_login_hover.png"
      @click="login()"
      style="cursor: pointer;"
    />
  </div>
</template>

<script>
import { onMounted } from 'vue';
export default {
  setup() {
    let url = process.env.VUE_APP_API_URL;

    onMounted(() => {});
    function login() {
      fetch(url + '/login/uri').then((res) => {
        res.json().then((el) => {
          window.location.replace(el.result);
        });
      });
    }

    return { login };
  },
};
</script>
