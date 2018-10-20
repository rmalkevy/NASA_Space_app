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
          <v-container fill-height fluid id="ContainerMap" class="container ma-0 pa-0">

            <img src="~/Mars_Viking_MDIM21_1km.png" id="Map"/>
            <div class="Dot" id="Dot" style="left: -20px"></div>

          </v-container>
        </v-card-media>
      </v-card>


    </v-flex>
  </v-container>
</template>

<script>

  export default {
    name: "map",
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
