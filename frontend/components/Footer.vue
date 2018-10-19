<template>
  <v-footer :fixed="fixed" app>
    <span>&copy; 2018 All rights reserved. Henprokuror said</span>
  </v-footer>
</template>

<script>
  export default {
    name: "Footer",
    data() {
      return {
        fixed: false,
      }
    }
  }
</script>

<style scoped>

</style>
