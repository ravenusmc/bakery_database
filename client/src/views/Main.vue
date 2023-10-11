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