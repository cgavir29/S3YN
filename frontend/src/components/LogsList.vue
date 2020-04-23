<template>
  <section>
    <p class="subtitle has-text-weight-bold">My Logs</p>
    <div v-if="!getLogs">
      <p>You haven't uploaded any logs yet.</p>
    </div>
    <div v-else>
      <b-tabs>
        <b-tab-item label="Table">
          <b-table
            :data="getLogs"
            :columns="columns"
            :selected.sync="selected"
            focusable
          >
          </b-table>
        </b-tab-item>

        <b-tab-item label="Selected">
          <pre>{{ selected }}</pre>
        </b-tab-item>
      </b-tabs>

      <b-button class="is-warning" @click="runFetchAnomalyDetection">
        Detect Anomalies
      </b-button>
      &nbsp;
      <button
        class="button field is-danger"
        @click="selected = null"
        :disabled="!selected"
      >
        <b-icon icon="fas fa-times"></b-icon>
        <span>Clear selected</span>
      </button>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "LogsList",
  data() {
    return {
      selected: "",
      columns: [
        {
          field: "id",
          label: "#",
          width: 40
        },
        {
          field: "filename",
          label: "Filename"
        }
      ]
    };
  },
  computed: {
    ...mapGetters(["getUser", "getLogs"])
  },
  methods: {
    ...mapActions(["fetchLogs", "fetchAnomalyDetection"]),
    runFetchAnomalyDetection() {
      if (!this.selected) {
        alert("Please select a file first.");
      } else {
        this.fetchAnomalyDetection({
          userId: this.getUser._id.$oid,
          filename: this.selected.filename
        });
        this.$router.push({ name: "Charts" });
      }
    }
  },
  beforeMount() {
    this.fetchLogs({ userId: this.getUser._id.$oid });
  }
};
</script>
