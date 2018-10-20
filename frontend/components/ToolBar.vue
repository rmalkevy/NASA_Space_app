<template>
    <v-toolbar fixed app color="blue darken-3" dark height="50" clipped-left>

      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-btn flat :to="{name: 'index'}">Mars</v-btn>
      </v-toolbar-items>

    </v-toolbar>
</template>

<script>
  export default {
    name: "ToolBar",
    data() {
      return {
        drawer: true,
        fixed: false,
        items: [
          { icon: 'apps', title: 'Welcome', to: '/' },
        ],
      }
    },
  }
</script>

<style scoped>

</style>
