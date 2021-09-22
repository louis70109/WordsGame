<template>
  <div class="line_auth">
    <h2>LINE</h2>
  </div>
</template>

<script>
import { onMounted } from 'vue';
export default {
  setup() {
    let url = process.env.VUE_APP_API_URL,
      user = '';

    function settingFormat() {
      let settings = localStorage.getItem('user');
      if (settings) return JSON.parse(settings);
      return {};
    }
    function addSettingToStorage(user) {
      let settings = settingFormat();
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
          console.log(el);
          user = el;
          addSettingToStorage();
        });
      });
    });
    return {
      user,
      settingFormat,
      addSettingToStorage,
    };
  },
};
</script>
