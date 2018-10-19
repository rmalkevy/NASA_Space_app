<template>
  <v-navigation-drawer fixed app clipped width="320">

    <v-text-field v-model="searchValue"
                  label="Search" prepend-inner-icon="search" solo height="50"></v-text-field>

    <v-list  dense v-for="item in filteredList" :key="item.macAddress">

      <v-list-group prepend-icon="devices_other">

          <v-list-tile slot="activator" @click="highlightDot(item)" class="ml-0 pl-0">
            <v-list-tile-title class="ml-0 pl-0"><b>{{item.macAddress}}</b>  -->> {{item.floor}} FLOOR</v-list-tile-title>
          </v-list-tile>

          <div v-for="(value, k) in clients[item.macAddress]" :key="k">
            <v-list-tile v-if="clients[item.macAddress][k] && k !== 'mapCoordinate'">
              <v-list-tile-title
                v-if="value.length > 1 && (typeof value) !== 'string'">{{k + ' - ' + value[0]}}</v-list-tile-title>
              <v-list-tile-title v-else>{{k + ' - ' + value}}</v-list-tile-title>
            </v-list-tile>
          </div>
      </v-list-group>

    </v-list>

  </v-navigation-drawer>
</template>


<script>
  import ClientsMixin from '~/mixins/clientsMixin.js'
  import Vue from 'vue'

  Vue.newUsers = [];

  export default {
    name: "LeftSideNavigation",
    mixins: [
      ClientsMixin
    ],
    data() {
      return {
        searchValue: '',
        activator: true,
        allMacAddresses: [],
        floor: 1,
        idInterval: null,
      }
    },
    async created() {

      setTimeout(async () => {
        await this.refreshAllClients();
        // initialize all clients in sidebar
        this.clients = Vue.allClients[0].clients;
        this.getAllMacAddresses();
        this.$nuxt.$emit('PUT_DOTS_ON_MAP', true)
      }, 2000);

      this.idInterval = setInterval(async ()=> {
        await this.refreshAllClients();
        this.getAllMacAddresses();
      }, 20000);

      this.$nuxt.$on('MAC_ADDRESSES_CHANGED', floor => {
        this.floor = floor;
        if (floor === 1) {
          this.clients = Vue.allClients[0].clients;
        } else if (floor === 2) {
          this.clients = Vue.allClients[1].clients;
        } else if (floor === 3) {
          this.clients = Vue.allClients[2].clients;
        }
      });
    },
    destroyed() {
      this.$nuxt.$off('MAC_ADDRESSES_CHANGED');
      clearInterval(this.idInterval);
    },

    methods: {
      searchMacAddress() {
        alert("Search value " + this.searchValue);
      },
      highlightDot(client) {
        this.$nuxt.$emit('HIGHLIGHT_DOT', client)
      },
      getAllMacAddresses() {
        this.allMacAddresses = [];

        for (let item in Vue.allClients[0].clients) {
          let data = {
            macAddress: item,
            floor: 1,
          };
          if (Vue.allClients[0].clients[item].new != null)
            data['new'] = Vue.allClients[0].clients[item].new;
          else data['new'] = false;
          this.allMacAddresses.push(data);
        }
        for (let item in Vue.allClients[1].clients) {
          let data = {
            macAddress: item,
            floor: 2,
          };
          if (Vue.allClients[1].clients[item].new != null)
            data['new'] = Vue.allClients[1].clients[item].new;
          else data['new'] = false;
          this.allMacAddresses.push(data);
        }
        for (let item in Vue.allClients[2].clients) {
          let data = {
            macAddress: item,
            floor: 3,
          };
          if (Vue.allClients[2].clients[item].new != null)
            data['new'] = Vue.allClients[2].clients[item].new;
          else data['new'] = false;
          this.allMacAddresses.push(data);
        }
        this.$nuxt.$emit('NEW_USERS', this.filteredNewUsers)
      },
    },

    computed: {
      filteredList() {
        return this.allMacAddresses.filter(item => {
          return item.macAddress.toLowerCase().includes(this.searchValue.toLowerCase())
        })
      },
      filteredNewUsers() {
        return this.allMacAddresses.filter(item => {
          return item.new === true
        })
      }
    }
  }
</script>

<style scoped>

</style>
