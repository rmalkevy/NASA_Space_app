<template>
  <v-app>

    <ToolBar></ToolBar>

    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>

    <Footer></Footer>

  </v-app>
</template>

<script>
  import ToolBar from '@/components/ToolBar.vue'
  import Footer from '@/components/Footer.vue'

  export default {
    components: {
      ToolBar,
      Footer,
    },
  }
</script>
