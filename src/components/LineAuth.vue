<template>
  <div class="line_auth">
  </div>
</template>

<script>
import { onMounted } from 'vue';
import {userCheck} from '../utils/users'
export default {
  setup() {
    let url = process.env.VUE_APP_API_URL;
    function userStorageFormat() {
      let settings = localStorage.getItem('user');
      if (settings) return JSON.parse(settings);
      else localStorage.setItem('user', '{}');

      return {};
    }
    function addSettingToStorage(user) {
      let settings = userStorageFormat();
      // call api
      settings['name'] = user.name;
      settings['picture'] = user.picture;
      localStorage.setItem('user', JSON.stringify(settings));
    }

    onMounted(() => {
      let urlParams = new URLSearchParams(window.location.search);
      const code = urlParams.get('code'),
        state = urlParams.get('state');

      fetch(url + `/login/?code=${code}&state=${state}`, {
        method: 'POST',
      }).then((res) => {
        res.json().then((el) => {
          console.log('Mount level...');
          addSettingToStorage(el);
          if (userCheck() === true) window.location.replace('/')
          
        });
      });
    });
    return {
      userStorageFormat,
      addSettingToStorage,
    };
  },
};
</script>
