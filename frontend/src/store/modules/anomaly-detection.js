import axios from "axios";

const state = {
  logs: null,
  events: null,
  // features: null,
  anomalies: null
};

const getters = {
  getLogs: state => state.logs,
  getEvents: state => state.events,
  // getFeatures: state => state.features,
  getAnomalies: state => state.anomalies
};

const mutations = {
  setLogs: (state, logs) => (state.logs = logs),
  clearLogs: state => (state.logs = null),
  setEvents: (state, events) => (state.events = events),
  clearEvents: state => (state.events = null),
  // setFeatures: (state, features) => (state.features = features),
  // clearFeatures: state => (state.features = null),
  setAnomalies: (state, anomalies) => (state.anomalies = anomalies),
  clearAnomalies: state => (state.anomalies = null)
};

const actions = {
  uploadFile({ commit }, { userId, systemName, formData }) {
    axios
      .post(
        "/users/" + userId + "/systems/" + systemName + "/files",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      )
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
        let idx = 1;
        let logs = [];

        res.data.files.forEach(item => {
          item.logs.forEach(log => {
            logs.push({
              id: idx,
              system: item.system,
              filename: log
            });
            idx++;
          });
        });

        commit("setLogs", logs);
      })
      .catch(err => {
        console.log(err.response.data.msg);
      });
  },
  fetchAnomalyDetection({ commit }, { userId, systemName, filename }) {
    axios
      .get(
        "/users/" +
          userId +
          "/systems/" +
          systemName +
          "/files/" +
          filename +
          "/detect"
      )
      .then(res => {
        let idxEvent = 1;
        eventsWithId = [];
        res.data.events.forEach(event => {
          eventsWithId.push({
            id: idxEvent,
            event: event.name,
            status: event.status
          });
          idxEvent++;
        });

        // let idxAnomaly = 1;
        // let anomaliesWithId = [];
        // for (let [blk, anomaly] of Object.entries(res.data.anomalies)) {
        //   anomaliesWithId.push({
        //     id: idxAnomaly,
        //     blk: blk,
        //     anomaly: anomaly
        //   });

        //   idxAnomaly++;
        // }

        commit("setEvents", eventsWithId);
        // commit("setAnomalies", anomaliesWithId);
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
