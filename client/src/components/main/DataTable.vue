<template>
	<div>
    <h1>Current Inventory:</h1>
    <table>
      <tr>
        <th>item</th>
        <th>Amount</th>
      </tr>
      <tr v-for="item in currentInventory">
        <td>{{ item[1] }}</td>
        <td>{{ item[2] }}</td>
      </tr>
    </table>
	</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "DataTable",
  computed: {
    ...mapGetters("data", ["currentInventory"]),
  },
  mounted() {
    this.fetchAllData();
  },
};

</script>

<style scoped>

</style>