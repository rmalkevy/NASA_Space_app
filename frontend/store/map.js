
const MAPS_DATA_PENDING = 'MAPS_DATA_PENDING';
const MAPS_DATA_SUCCESS = 'MAPS_DATA_SUCCESS';
const MAPS_DATA_FAILURE = 'MAPS_DATA_FAILURE';


export const state = () => ({
  pending: false,
  mapsData: {},
  maps: [],
  image: {},
});

export const getters = {
  mapsData: state => {
    return state.mapsData;
  },
  maps: state => {
    return state.maps;
  },
};

export const mutations = {
  [MAPS_DATA_PENDING](state) {
    state.pending = true;
  },
  [MAPS_DATA_SUCCESS](state, value) {
    state.pending = false;
    state.mapsData = value.data;
    state.maps = [];
    for(let item in value.data) {
      let data = {
        name: item,
        link: value.data[item].img.url,
        size:
          {
            width: value.data[item].img.width,
            height: value.data[item].img.height
          }
      };
      state.maps.push(data);
    }
  },
  [MAPS_DATA_FAILURE](state) {
    state.pending = false;
  },
};


export const actions = {
  async mapsData({commit}) {

    commit(MAPS_DATA_PENDING);
    try {
      const endpoint = 'queries/getMaps/';
      const responseData = await this.$axios.get(endpoint);

      commit(MAPS_DATA_SUCCESS, responseData);
      return responseData;
    } catch (e) {
      // console.error(e); // 💩
      commit(MAPS_DATA_FAILURE, 'get maps failed');
      throw e.response.data;
    }
  },

};
