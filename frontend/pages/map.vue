<template>
  <v-container fill-height>
    <v-flex>

      <notifications group="newUsers" />

      <v-card flat>
        <v-card-actions class="green lighten-4">

          <v-btn
            v-for="n in floors" :key="n"
            @click="floorMap(n)"
            color="green lighten-1"
            class="white--text mr-4"
          >Floor {{n}}</v-btn>

          <v-card-text class="glyphicon--text pa-1"><b>Floor 1</b><br/>Clients connected {{numberOfClients[0]}}</v-card-text>

          <v-card-text class="glyphicon--text pa-1"><b>Floor 2</b><br/>Clients connected {{numberOfClients[1]}}</v-card-text>

          <v-card-text class="glyphicon--text pa-1"><b>Floor 3</b><br/>Clients connected {{numberOfClients[2]}}</v-card-text>

          <v-card-text class="glyphicon--text pa-1"><b>All users</b><br/>Connected {{connectedClients}}</v-card-text>
        </v-card-actions>

        <v-card-media>
          <v-container fill-height fluid id="ContainerMap" class="container ma-0 pa-0">

            <img :src="currentMap.link" id="Map"/>
            <div class="Dot" id="Dot" style="left: -20px"></div>

          </v-container>
        </v-card-media>
      </v-card>


    </v-flex>
  </v-container>
</template>

<script>

  import ClientsMixin from '~/mixins/clientsMixin.js'
  import Vue from 'vue'

  export default {
    name: "map",
    layout: 'mapLayout',
    mixins: [
      ClientsMixin
    ],
    data() {
      return {
        active: null,
        readyNewMapSize: false,
        floors: 3,
        currentMap: {
          link: '',
          coefficient: 1,
        },
        floor: 1,
        numberOfClients: [0, 0, 0],
        realMapWidth: [1, 1, 1],
        realMapHeight: [1, 1, 1],
        redDot: null,
      }
    },
    async created() {
      this.$nuxt.$on('PUT_DOTS_ON_MAP', data => {
        this.clients = Vue.allClients[0].clients;
        this.numberOfClients = [Vue.allClients[0].count, Vue.allClients[1].count, Vue.allClients[2].count];
        this.placeDotsOnMap();
      });
      await this.$store.dispatch('map/mapsData');
      await this.realMapSize();
      await this.floorMap(this.floor);
      this.$nuxt.$on('CLIENTS_REFRESHED', async data => {

        this.clients = Vue.allClients[this.floor - 1].clients;
        this.numberOfClients = [Vue.allClients[0].count, Vue.allClients[1].count, Vue.allClients[2].count];
        this.placeDotsOnMap()
      });
      window.addEventListener('resize', this.resizeCoordinates);
      window.addEventListener('load', this.resizeCoordinates);

      this.$nuxt.$on('HIGHLIGHT_DOT', async (client) => {
        if (this.floor !== client.floor) {
          await this.floorMap(client.floor);
        }

        setTimeout(() => {
          this.highlightDot(client);
        }, 200)
      })

      this.$nuxt.$on('NEW_USERS', this.showNotifications);
    },
    destroyed() {
      this.$nuxt.$off('CLIENTS_REFRESHED');
      window.removeEventListener('resize', this.resizeCoordinates);
      window.removeEventListener('load', this.resizeCoordinates);
    },
    methods: {
      async floorMap(floor) {

        if (floor === 0 || floor == null || floor === undefined)
          floor = 1;
        this.floor = floor;

        this.currentMap.link = process.env.baseURL + this.maps[this.floor - 1].link;

        this.clients = Vue.allClients[floor - 1].clients;
        this.numberOfClients = [Vue.allClients[0].count, Vue.allClients[1].count, Vue.allClients[2].count];
        this.$nuxt.$emit('MAC_ADDRESSES_CHANGED', floor);
        this.resizeCoordinates(0);

        this.removeRedDot()
      },

      /*** Callback for Event Listener ***/
      async resizeCoordinates(ev) {
        const img = await document.getElementById('Map');
        let width = await img.clientWidth;
        if (this.realMapWidth[this.floor - 1] !== 0 || this.realMapWidth[this.floor - 1] !== undefined) {
          this.currentMap.coefficient = await (width / this.realMapWidth[this.floor - 1]);
        }
        await this.placeDotsOnMap();
      },

      async placeDotsOnMap() {
        await this.removeAllElementsOnMap();

        let dot = document.getElementById('Dot')
        for (let item in this.clients) {
          if (this.clients.hasOwnProperty(item)) {
            let cln = dot.cloneNode(true);
            cln.setAttribute('class', 'deleteDot');
            // cln.setAttribute('id', item.replace(/:/g , "_"));
            cln.id = item;
            // alert(item.replace(/:/g , "_"))
            cln.style.top = (this.clients[item].mapCoordinate.y * this.currentMap.coefficient) +'px';
            cln.style.left = (this.clients[item].mapCoordinate.x * this.currentMap.coefficient) +'px';

            document.getElementById("ContainerMap").appendChild(cln);
          }
        }

      },

      removeAllElementsOnMap() {
        let dots = document.getElementsByClassName('deleteDot');

        while(dots[0])
          dots[0].parentNode.removeChild(dots[0]);
      },

      removeRedDot() {
        if (this.redDot !== null) {
          let dot = document.getElementById(this.redDot);

          dot.parentNode.removeChild(dot);
        }
        this.redDot = null;
      },

      realMapSize() {
        let maps = this.$store.getters['map/maps'];
        this.realMapWidth = [maps[0].size.width, maps[1].size.width, maps[2].size.width];
        this.realMapHeight = [maps[0].size.height, maps[1].size.height, maps[2].size.height];
      },

      async highlightDot(client) {

        if (this.redDot !== null) {
          let dot = document.getElementById(this.redDot);
          if (dot !== null && dot !== undefined) {
            let cln = dot.cloneNode(true);
            cln.setAttribute('class', 'deleteDot');
            cln.id = this.redDot
            dot.parentNode.replaceChild(cln, dot);
          }
        }

        let dotClient = await document.getElementById(client.macAddress);
        if (dotClient !== null && dotClient !== undefined) {
          let cln = dotClient.cloneNode(true);
          cln.setAttribute('class', 'redDot');
          cln.id = client.macAddress;
          dotClient.parentNode.replaceChild(cln, dotClient);
        }

        this.redDot = client.macAddress;
      },
      showNotifications(data) {
        let len = data.length;
        for (let i = 0; i < len; i++) {
          this.$notify({
            group: 'newUsers',
            title: 'New user',
            text: 'Hi, mac: ' + data[i].macAddress + ' now is on the ' + data[i].floor + ' floor.',
            position: 'top right',
            duration: 5000,
            speed: 1000
          });
        }
      }
    },
    computed: {
      connectedClients() {
        return this.numberOfClients.reduce(function(acc, val) { return acc + val; }, 0)
      }
    }

  }
</script>

<style scoped>

  .deleteDot {
    position: absolute;
    height: 10px;
    width: 10px;
    background-color: blue;
    opacity: 0.5;
    border-radius: 50%;
  }

  .redDot {
    position: absolute;
    height: 17px;
    width: 17px;
    background-color: red;

    border-radius: 50%;
  }

  .container {
    position: relative;
  }

  #Map {
    padding: 0;
    margin: 0;
  }
</style>
