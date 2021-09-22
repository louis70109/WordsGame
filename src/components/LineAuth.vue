<template>
  <div class="line_auth">
    <h2>LINE</h2>
    {{user}}
  </div>
</template>

<script>
import { onMounted } from 'vue';
export default {
  setup() {
    let url = process.env.VUE_APP_API_URL,
      user = {};

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
        let settings = settingFormat();

        settings.name = user.name;
        settings.picture = user.picture;
        localStorage.setItem('user', JSON.stringify(settings));
      }

      fetch(url + `/login/?code=${code}&state=${state}`, {
        method: 'POST',
      }).then((res) => {
        res.json().then((el) => {
          console.log('Mount level...');
          console.log(el);
          addSettingToStorage(el);
        });
      });
    });
    return {
      user,
    };
  },
};
</script>
