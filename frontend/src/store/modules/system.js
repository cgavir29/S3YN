import axios from "axios";

const state = {
  systems: null
};

const getters = {
  getSystems: state => state.systems
};

const mutations = {
  setSystems: (state, systems) => (state.systems = systems),
  clearSystems: state => (state.systems = null)
};

const actions = {
  fetchSystems({ commit }) {
    axios
      .get("/systems")
      .then(res => commit("setSystems", res.data.systems))
      .catch(err => console.log(err.response.data.msg));
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};
