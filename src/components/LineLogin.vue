<template>
  <div class="line_login">
    <div v-if="userCheck() === true">
      <div style="cursor: pointer;" @click="lineLogout">Logout</div>
    </div>
    <div v-else>
      <img
        alt="Vue logo"
        src="../assets/btn_login_hover.png"
        @click="login()"
        style="cursor: pointer;"
      />
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';
import { userCheck, lineLogout } from '../utils/users';
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
    // function userCheck(

    // )
    return { login, userCheck, lineLogout };
  },
};
</script>
