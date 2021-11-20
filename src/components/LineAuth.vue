<template>
  <span class="line_auth"></span>
</template>

<script>
import { onMounted } from 'vue';
import { userCheck } from '../utils/users';
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

      function settingFormat() {
        let settings = localStorage.getItem('user');
        if (settings) return JSON.parse(settings);
        return {};
      }
      function addSettingToStorage(user) {
        fetch(url + '/users/', {
          method: 'POST',
          headers: { 'content-type': 'application/json' },
          body: JSON.stringify(user),
        }).then((el) => {
          let settings = settingFormat();
          console.log('user post data');
          console.log(el);
          settings.name = user.name;
          settings.picture = user.picture;
          localStorage.setItem('user', JSON.stringify(settings));
          if (userCheck() === true) window.location.replace('/');
        });
      }

      fetch(url + `/login/?code=${code}&state=${state}`, {
        method: 'POST',
      }).then((res) => {
        res.json().then((el) => {
          console.log('Mount level...');
          addSettingToStorage(el);
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
