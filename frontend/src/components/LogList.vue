<template>
  <section>
    <div v-if="this.getLogs.length == 0">
      <span class="tag is-warning is-medium"
        >You haven't uploaded any logs yet</span
      >
    </div>
    <div v-else>
      <b-tabs>
        <b-tab-item>
          <b-table
            :data="getLogs"
            :columns="columns"
            :selected.sync="selected"
            focusable
          >
          </b-table>
        </b-tab-item>
      </b-tabs>

      <b-button
        class="is-info"
        :disabled="!selected"
        @click="isLogPreviewModalActive = true"
      >
        <b-icon class="fas fa-search"></b-icon>
        <span>Preview</span>
      </b-button>
      <b-modal
        :active.sync="isLogPreviewModalActive"
        has-modal-card
        trap-focus
        :destroy-on-hide="false"
        aria-role="dialog"
        aria-modal
      >
        <div v-if="selected">
          <LogPreviewModal
            v-bind:logSystem="selected.system"
            v-bind:logFilename="selected.filename"
          />
        </div>
      </b-modal>
      &nbsp;
      <b-button
        class="is-warning"
        :disabled="!selected"
        @click="runFetchAnomalyDetection"
      >
        <b-icon class="fas fa-cogs"></b-icon>
        <span>Detect Anomalies</span>
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
import LogPreviewModal from "@/components/LogPreviewModal.vue";

export default {
  name: "LogList",
  components: {
    LogPreviewModal
  },
  data() {
    return {
      isLogPreviewModalActive: false,
      selected: null,
      columns: [
        {
          field: "id",
          label: "#"
        },
        {
          field: "filename",
          label: "Filename"
        },
        {
          field: "system",
          label: "System"
        }
      ]
    };
  },
  computed: {
    ...mapGetters(["getUser", "getSystems", "getLogs"])
  },
  methods: {
    ...mapActions(["fetchLogs", "fetchAnomalyDetection"]),
    runFetchAnomalyDetection() {
      if (!this.selected) {
        alert("Please select a file first.");
      } else {
        this.fetchAnomalyDetection({
          user: this.getUser._id.$oid,
          system: this.selected.system,
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
