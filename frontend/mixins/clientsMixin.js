import Vue from 'vue'

Vue.allClients = [
  {clients: [], count: 0},
  {clients: [], count: 0},
  {clients: [], count: 0}
];

/**** Clients Mixin ****/
// let clientsJson = require('~/clients.json');

const ClientsMixin = {
  data() {
    return {
      // macAddresses: [],
      clients: [],
    }
  },
  async created () {
    let mapData = await this.$store.dispatch('map/mapsData');
  },
  methods: {
    async refreshClients(floor) {

      if (floor === 0 || floor == null || floor === undefined)
        floor = 1;

      // let mapData = await this.$store.dispatch('map/mapsData');
      let partLink = await this.maps[floor - 1].name;
      const result = await this.$store.dispatch('clients/clientsData', partLink);
      return result.data;
    },

    async refreshAllClients() {
      let data = await this.refreshClients(1);
      Vue.allClients[0].clients = await data.clients;
      Vue.allClients[0].count = await data.countClients;

      data = await this.refreshClients(2);
      Vue.allClients[1].clients = await data.clients;
      Vue.allClients[1].count = await data.countClients;

      data = await this.refreshClients(3);
      Vue.allClients[2].clients = await data.clients;
      Vue.allClients[2].count = await data.countClients;

      this.$nuxt.$emit('CLIENTS_REFRESHED', true);
    },
    async mapsData() {
        await this.$store.dispatch('map/mapsData');
      },
  },
  computed: {
    maps() {
      return this.$store.getters['map/maps']
    },

  }
};

export default ClientsMixin;
