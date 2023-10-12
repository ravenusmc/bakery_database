<template>
  <div>
    <section>
      <div>
        <h1>Current Inventory:</h1>
        <table>
          <tr>
            <th>Item</th>
            <th>Amount</th>
          </tr>
        </table>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
// import Top from '@/components/landing/Top.vue'

// USE https://github.com/ravenusmc/work_data_entry_tool/blob/main/server/SQL/tables.sql for reference

export default {
  name: 'Main',
}
</script>

<style scoped>

th {
  font-weight: bold;
  text-transform: uppercase;
}

</style>