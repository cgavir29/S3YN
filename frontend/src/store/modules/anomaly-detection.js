import axios from "axios";

const state = {
  logs: null,
  events: null,
  features: null
};

const getters = {
  getLogs: state => state.logs,
  getEvents: state => state.events,
  getFeatures: state => state.features
};

const mutations = {
  setLogs: (state, logs) => (state.logs = logs),
  clearLogs: state => (state.logs = null),
  setEvents: (state, events) => (state.events = events),
  clearEvents: state => (state.events = null),
  setFeatures: (state, features) => (state.features = features),
  clearFeatures: state => (state.features = null)
};

const actions = {
  clearLogs({ commit }) {
    commit("clearLogs");
  },
  clearAnomalyDetectionData({ commit }) {
    commit("clearEvents");
    commit("clearFeatures");
  },
  fetchLogs({ commit }, { userId }) {
    axios
      .get("/users/" + userId + "/files")
      .then(res => {
        var logs = [];
        res.data.logs.forEach(function (item, index) {
          logs.push({
            id: index,
            filename: item
          });
        });

        commit("setLogs", logs);
      })
      .catch(err => {
        console.log(err.response.data.msg);
      });
  },
  fetchAnomalyDetection({ commit }, { userId, filename }) {
    axios
      .get("/users/" + userId + "/files/" + filename + "/preprocess")
      .then(res => {
        var prettyEvents = [];
        res.data.events.forEach(function (item, index) {
          prettyEvents.push({
            id: index + 1,
            event: item
          });
        });

        var idx = 1;
        var prettyFeatures = [];
        for (let [key, value] of Object.entries(res.data.features)) {
          prettyFeatures.push({
            id: idx,
            blk: key,
            feature: value
          });
          idx++;
        }

        commit("setEvents", prettyEvents);
        commit("setFeatures", prettyFeatures);
      })
      .catch(err => console.log(err));
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};
