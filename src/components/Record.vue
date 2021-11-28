<template>
  <div class="record">
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
          <th scope="row">{{ records.value }}</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { reactive, onMounted } from 'vue';

export default {
  setup() {
    const url = process.env.VUE_APP_API_URL;
    let records = reactive([]);
    onMounted(async () => {
      const games = await (await fetch(url + '/games/')).json();
      records.value = games
    });
    return { records };
  },
};
</script>
