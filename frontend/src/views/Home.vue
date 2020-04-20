<template>
  <div>
    <h1 class="title">Welcome to S3YN</h1>
    <b-button class="is-warning" @click="runAnomalyDetection()"
      >Detect Anomalies!</b-button
    >
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
          this.setAnomalyDetectionResults(res.data);
        })
        .catch(err => console.log(err));
    }
  }
};
</script>
