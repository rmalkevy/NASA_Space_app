<template>
  <v-app>

    <ToolBar></ToolBar>

    <LeftSideNavigation></LeftSideNavigation>

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
  import LeftSideNavigation from '@/components/LeftSideNavigation.vue'
  import Footer from '@/components/Footer.vue'

  export default {
    name: 'mapLayout',
    components: {
      ToolBar,
      LeftSideNavigation,
      Footer,
    },
  }
</script>

