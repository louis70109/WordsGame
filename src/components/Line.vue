<template>
  <div class="setting">
    <h2>LINE</h2>
    <button @click="checkAPI()">Check</button>
    {{user}}
  </div>
</template>

<script>
import {
  // ref,
  onMounted,
  //  onUnmounted
} from 'vue';
export default {
  setup() {
    let url = 'http://localhost:8000',
      user = '';
    onMounted(()=>{
      let urlParams = new URLSearchParams(window.location.search);
      const code = urlParams.get('code'),
        state = urlParams.get('state')

      fetch(url+`/login/?code=${code}&state=${state}`, {method: 'POST'}).then(res=>{
        res.json().then(el=>{
          console.log('Mount level...');
          console.log(el)
          user = el
        })
      })
    })
    function checkAPI(){
      fetch(url+'/').then(() => {alert('ok')})
    }
    
    function settingFormat() {
      let settings = localStorage.getItem('settings');
      if (settings) return JSON.parse(settings);
      return {};
    }
    function addSettingToStorage(uid) {
      let settings = settingFormat();
      // call api
      settings[uid] = '';
      localStorage.setItem('settings', JSON.stringify(settings));
    }
    return {
      user,
      checkAPI,
      settingFormat,
      addSettingToStorage
    };
  },
};
</script>
