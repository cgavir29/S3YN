<template>
  <div>
    <h1 class="title">Welcome to S3YN</h1>
    <router-link :to="{ name: 'Charts' }">
      <b-button class="is-warning" @click="runAnomalyDetection()">
        Detect Anomalies
      </b-button>
    </router-link>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import axios from "axios";

export default {
  name: "Home",
  computed: {
    ...mapGetters(["getUser"])
  },
  methods: {
    ...mapActions(["setAnomalyDetectionResults"]),
    runAnomalyDetection() {
      axios
        .get("/users/dcardonag/files/logs.log/preprocess")
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

          this.setAnomalyDetectionResults({
            events: prettyEvents,
            features: prettyFeatures
          });
        })
        .catch(err => console.log(err));
    }
  }
};
</script>
