<template>
  <div class="record">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">成績</th>
          <th scope="col">關卡</th>
          <th scope="col">是誰</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in records.value" :key="item.id">
          <td>{{ index }}</td>
          <td>
            {{ item.score }}
          </td>
          <td>{{ item.level }}</td>
          <td>
            <img
              :src="item.picture"
              class="img-thumbnail"
              width="50"
              height="50"
            />
          </td>
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
      records.value = await (await fetch(url + '/games/')).json();

      for (let i = 0; i < records.value.length; i++) {
        const user = await (
          await fetch(url + '/users/' + records.value[i].owner_id)
        ).json();
        records.value[i]['picture'] = user.picture;
      }

      console.log(records.value);
    });
    return { records };
  },
};
</script>
