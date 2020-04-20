const state = {
  events: null,
  features: null
};

const getters = {
  getEvents: state => state.events,
  getFeatures: state => state.features
};

const mutations = {
  setEvents: (state, events) => (state.events = events),
  setFeatures: (state, features) => (state.features = features)
};

const actions = {
  setAnomalyDetectionResults({ commit }, { events, features }) {
    commit("setEvents", events);
    commit("setFeatures", features);
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};
