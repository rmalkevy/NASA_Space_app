
const CHARTS_DATA_PENDING = 'CHARTS_DATA_PENDING';
const CHARTS_DATA_SUCCESS = 'CHARTS_DATA_SUCCESS';
const CHARTS_DATA_FAILURE = 'CHARTS_DATA_FAILURE';


export const state = () => ({
  pending: false,
  charts: null,
});

export const getters = {
  charts: state => {
    return state.charts;
  },
};


export const mutations = {
  [CHARTS_DATA_PENDING](state) {
    state.pending = true;
    state.charts = null;
  },
  [CHARTS_DATA_SUCCESS](state, value) {
    state.pending = false;
    if (value.data.hasOwnProperty('charts')) {
      state.charts = value.data.charts;
    }
  },
  [CHARTS_DATA_FAILURE](state) {
    state.pending = false;
  },
};


export const actions = {
  async loadPickedDateChart({commit}, partLink) {

    commit(CHARTS_DATA_PENDING);
    try {
      const endpoint = 'queries/getChartsInfoDaily/?date=' + partLink;
      const responseData = await this.$axios.get(endpoint);

      commit(CHARTS_DATA_SUCCESS, responseData);
      return responseData;
    } catch (e) {
      // console.error(e); // 💩
      commit(CHARTS_DATA_FAILURE, 'get charts failed');
      throw e.response.data;
    }
  },

  async loadPickedRangeDateChart({commit}, data) {

    commit(CHARTS_DATA_PENDING);
    try {
      const endpoint = 'queries/getChartsInfoRange/?startDate=' + data.startDate + '&endDate=' + data.endDate;
      const responseData = await this.$axios.get(endpoint);

      commit(CHARTS_DATA_SUCCESS, responseData);
      return responseData;
    } catch (e) {
      // console.error(e); // 💩
      commit(CHARTS_DATA_FAILURE, 'get charts failed');
      throw e.response.data;
    }
  },

  async loadCorrelations({commit}) {

    commit(CHARTS_DATA_PENDING);
    try {
      const endpoint = 'queries/getCorrelations/';
      const responseData = await this.$axios.get(endpoint);

      commit(CHARTS_DATA_SUCCESS, responseData);
      return responseData;
    } catch (e) {
      // console.error(e); // 💩
      commit(CHARTS_DATA_FAILURE, 'get charts failed');
      throw e.response.data;
    }
  },

  async loadForecasting({commit}) {

    commit(CHARTS_DATA_PENDING);
    try {
      const endpoint = 'queries/forecasting/';
      const responseData = await this.$axios.get(endpoint);

      commit(CHARTS_DATA_SUCCESS, responseData);
      return responseData;
    } catch (e) {
      // console.error(e); // 💩
      commit(CHARTS_DATA_FAILURE, 'get charts failed');
      throw e.response.data;
    }
  },
};
