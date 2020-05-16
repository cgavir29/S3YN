import axios from "axios";

const state = {
  logs: null,
  events: null,
  clusters: null
};

const getters = {
  getLogs: state => state.logs,
  getEvents: state => state.events,
  getClusters: state => state.clusters
};

const mutations = {
  setLogs: (state, logs) => (state.logs = logs),
  clearLogs: state => (state.logs = null),
  setEvents: (state, events) => (state.events = events),
  clearEvents: state => (state.events = null),
  setClusters: (state, clusters) => (state.clusters = clusters),
  clearClusters: state => (state.clusters = null)
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
  clearAnomalyDetection({ commit }) {
    commit("clearEvents");
    commit("clearClusters");
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
  fetchAnomalyDetection({ commit }, { user, system, filename }) {
    axios
      .post(
        "/users/" +
          user +
          "/systems/" +
          system +
          "/files/" +
          filename +
          "/detect"
      )
      .then(res => {
        let idxEvent = 1;
        let eventsWithId = [];

        for (let [event, status] of Object.entries(res.data.events)) {
          eventsWithId.push({
            id: idxEvent,
            event: event,
            status: status
          });
          idxEvent++;
        }

        commit("setEvents", eventsWithId);
        commit("setClusters", res.data.clusters);
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
