<template>
  <span class="line_login">
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand">日文仔</a>
        <form class="d-flex">
          <div v-if="userCheck() === true">
            <button class="btn btn-secondary" @click="lineLogout">
              登出
            </button>
          </div>
          <div v-else>
            <img
              alt="Vue logo"
              src="../assets/btn_login_hover.png"
              @click="login()"
              style="cursor: pointer;"
            />
          </div>
        </form>
      </div>
    </nav>
  </span>
</template>

<script>
import { userCheck, lineLogout } from '../utils/users';
export default {
  setup() {
    const url = process.env.VUE_APP_API_URL;
    function login() {
      fetch(url + '/login/uri').then((res) => {
        res.json().then((el) => {
          window.location.replace(el.result);
        });
      });
    }
    return { login, userCheck, lineLogout };
  },
};
</script>
