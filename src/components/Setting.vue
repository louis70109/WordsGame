<template>
  <div class="setting">
    <button @click="checkAPI()">Check</button>
    <button @click="login()">Login</button>
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
    let url = 'http://localhost:8000';
    onMounted(()=>{
      
    })
    function checkAPI(){
      fetch(url+'/').then(() => {alert('ok')})
    }
    function login(){
      fetch(url+'/login/uri').then(res=>{
        res.json().then(el=>{
          window.location.replace(el.result)
        })
      })
    }
    function settingFormat() {
      let settings = localStorage.getItem('settings');
      // list of dict
      // {
      //   'あ': 'class-1',
      // }
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
      checkAPI,
      login,
      settingFormat,
      addSettingToStorage
    };
  },
};
</script>
