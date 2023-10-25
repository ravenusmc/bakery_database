<template>
  <div>
    <section>
      <div>
        <h1>Sold Amount</h1>
        <form @submit="submitAmountSold">
          <label for="item">Item name:</label><br />
          <input type="text" id="item" name="item" v-model="item" /><br />
          <label for="amount">Amount Sold:</label><br />
          <input
            type="number"
            id="amount"
            name="amount"
            v-model="amount"
          /><br /><br />
          <label for="date">Start date:</label>
          <input
            type="date"
            id="date"
            name="date"
            min="2023-01-01"
            max="204-12-31"
            v-model="date"
          /><br /><br />
          <input type="submit" value="Submit" />
        </form>
      </div>

      <div>
        <DataTable/>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
import DataTable from '@/components/main/DataTable.vue'
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Main",
  components: {
    DataTable
  },
  data() {
    return {
      item: "",
      amount: 0,
      date: null,
    };
  },
  computed: {
    ...mapGetters("data", ["currentInventory"]),
  },
  methods: {
    ...mapActions("data", ["fetchAllData", "submitDaySalesToDataBase"]),
    submitAmountSold() {
      event.preventDefault();
      const payload = {
        item: this.item,
        amount: this.amount,
        date: this.date,
      };
      this.submitDaySalesToDataBase({ payload });
    },
  },
  mounted() {
    this.fetchAllData();
  },
};
</script>

<style scoped>
th {
  font-weight: bold;
  text-transform: uppercase;
}
</style>