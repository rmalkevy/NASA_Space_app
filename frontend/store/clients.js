
const CLIENTS_DATA_PENDING = 'CLIENTS_DATA_PENDING';
const CLIENTS_DATA_SUCCESS = 'CLIENTS_DATA_SUCCESS';
const CLIENTS_DATA_FAILURE = 'CLIENTS_DATA_FAILURE';


export const state = () => ({
  pending: false,
  clients: null,
  numberOfClients: 0,
  macAddresses: null,
});

export const getters = {
  clients: state => {
    return state.clients;
  },
  numberOfClients: state => {
    return state.numberOfClients;
  },
};


export const mutations = {
  [CLIENTS_DATA_PENDING](state) {
    state.pending = true;
    state.clients = null;
  },
  [CLIENTS_DATA_SUCCESS](state, value) {
    state.pending = false;
    if (value.data.hasOwnProperty('clients')) {
      state.clients = value.data.clients;
    }
    if (value.data.hasOwnProperty('countClients')) {
      state.numberOfClients = value.data.countClients;
    }
  },
  [CLIENTS_DATA_FAILURE](state) {
    state.pending = false;
  },
};


export const actions = {

  async clientsData({commit}, partLink) {

    commit(CLIENTS_DATA_PENDING);
    try {
      const endpoint = 'queries/getUsersByFloor/?nameFloor=' + partLink;
      const responseData = await this.$axios.get(endpoint);

      commit(CLIENTS_DATA_SUCCESS, responseData);
      return responseData;
    } catch (e) {
      // console.error(e); // 💩
      commit(CLIENTS_DATA_FAILURE, 'get clients failed');
      throw e.response.data;
    }
  },

};
