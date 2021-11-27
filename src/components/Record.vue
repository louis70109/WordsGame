<template>
  <span class="record">
    <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">{{ records }}</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
  </tbody>
</table>
  </span>
</template>

<script>
import {onMounted, ref} from 'vue'

export default {
  setup() {
    const url = process.env.VUE_APP_API_URL;
    let records = ref(null);
    onMounted(async ()=>{
      records = await (await fetch(url+'/games/')).json()
      console.log(records);
    })
    return { records };
  },
};
</script>
