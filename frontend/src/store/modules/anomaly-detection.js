import axios from "axios";

const state = {
  logs: null,
  events: null,
  features: null,
  anomalies: null
};

const getters = {
  getLogs: state => state.logs,
  getEvents: state => state.events,
  getFeatures: state => state.features,
  getAnomalies: state => state.anomalies
};

const mutations = {
  setLogs: (state, logs) => (state.logs = logs),
  clearLogs: state => (state.logs = null),
  setEvents: (state, events) => (state.events = events),
  clearEvents: state => (state.events = null),
  setFeatures: (state, features) => (state.features = features),
  clearFeatures: state => (state.features = null),
  setAnomalies: (state, anomalies) => (state.anomalies = anomalies),
  clearAnomalies: state => (state.anomalies = null)
};

const actions = {
  uploadFile({ commit }, { userId, formData }) {
    axios
      .post("/users/" + userId + "/files", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
      .then(res => alert(res.data.msg))
      .catch(err => alert(err.response.data.msg));
  },
  clearLogs({ commit }) {
    commit("clearLogs");
  },
  clearAnomalyDetectionData({ commit }) {
    commit("clearEvents");
    commit("clearFeatures");
    commit("clearAnomalies");
  },
  fetchLogs({ commit }, { userId }) {
    axios
      .get("/users/" + userId + "/files")
      .then(res => {
        let logs = [];
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
      .get("/users/" + userId + "/files/" + filename + "/detect")
      .then(res => {
        // Add the 'id' field to each part of the response, specifically 'events', 'features' and
        // 'anomalies' so they can be easily looped through and displayed in Buefy tables.

        let eventsWithId = [];
        res.data.events.forEach(function (item, index) {
          eventsWithId.push({
            id: index + 1,
            event: item
          });
        });

        let idx = 1;
        let featuresWithId = [];
        for (let [blk, feature] of Object.entries(res.data.features)) {
          featuresWithId.push({
            id: idx,
            blk: blk,
            feature: feature
          });

          idx++;
        }

        let idx2 = 1;
        let anomaliesWithId = [];
        for (let [blk, anomaly] of Object.entries(res.data.anomalies)) {
          anomaliesWithId.push({
            id: idx,
            blk: blk,
            anomaly: anomaly
          });

          idx2++;
        }
        commit("setEvents", eventsWithId);
        commit("setFeatures", featuresWithId);
        commit("setAnomalies", anomaliesWithId);
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
