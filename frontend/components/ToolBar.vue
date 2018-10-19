<template>
    <v-toolbar fixed app color="blue darken-3" dark height="50" clipped-left>

      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat :to="{name: 'forecasting'}">Forecasting</v-btn>
        <v-divider vertical></v-divider>
        <v-btn flat :to="{name: 'correlations'}">Correlations</v-btn>
        <v-divider vertical></v-divider>
        <v-btn flat :to="{name: 'chart'}">Charts</v-btn>
        <v-divider vertical></v-divider>
        <v-btn flat :to="{name: 'map'}">Maps</v-btn>
      </v-toolbar-items>

      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-btn flat :to="{name: 'index'}">CCMN Home</v-btn>
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
    methods: {
      triggerDrawer() {
        this.drawer = !this.drawer;
        this.$nuxt.$emit('CHANGE_DRAWER', this.drawer)
      }
    }
  }
</script>

<style scoped>

</style>
