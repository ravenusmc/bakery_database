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
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}

</style>