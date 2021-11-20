<template>
  <span class="record">
  </span>
</template>

<script>
import { userCheck, lineLogout } from '../utils/users';
export default {
  setup() {
    let url = process.env.VUE_APP_API_URL;
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
