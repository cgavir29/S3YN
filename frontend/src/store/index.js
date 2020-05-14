import Vue from "vue";
import Vuex from "vuex";

import system from "./modules/system";
import account from "./modules/account";
import anomalyDetection from "./modules/anomaly-detection";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    system,
    account,
    anomalyDetection
  }
});
