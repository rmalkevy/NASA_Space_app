<template>
  <v-container fill-height>

    <v-flex>
      <v-card flat>
        <v-card-actions class="green lighten-4">

          <v-btn color="green lighten-1" class="white--text mr-4">Water</v-btn>
          <v-btn color="green lighten-1" class="white--text mr-4">Potassium</v-btn>
          <v-btn color="green lighten-1" class="white--text mr-4">Chlorine</v-btn>

        </v-card-actions>

        <v-card-media>
          <v-container fill-height fluid id="heatmapContainer" class="container ma-0 pa-0">

            <img src="/map_Mars.png" id="Map"/>

          </v-container>
        </v-card-media>
      </v-card>


    </v-flex>
  </v-container>
</template>

<script>

  export default {
    name: "index",
    data() {
      return {
        config: {
          container: {},
          radius: 10,
          maxOpacity: .5,
          minOpacity: 0,
          blur: .75
        }
      }
    },
    created() {
      this.config.container = document.getElementById('heatmapContainer');
      this.initMap()
    },
    methods: {
      initMap() {
        // h337.create(this.config)
      }
    }
  }
</script>

<style scoped>

  .container {
    position: relative;
  }

  #Map {
    padding: 0;
    margin: 0;
  }
</style>
