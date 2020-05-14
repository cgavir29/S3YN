<template>
  <section>
    <div v-if="!getLogs">
      <p>You haven't uploaded any logs yet.</p>
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

        <!-- <b-tab-item label="Selected">
          <pre>{{ selected }}</pre>
        </b-tab-item> -->
      </b-tabs>

      <b-button
        class="is-info"
        :disabled="!selected"
        @click="isLogPreviewModalActive = true"
      >
        Preview
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
          <LogPreview
            v-bind:logSystem="selected.system"
            v-bind:logFilename="selected.filename"
          />
        </div>
      </b-modal>
      &nbsp;
      <b-button
        class="is-warning"
        :disabled="!selected"
        @click="runFetchLogParser"
      >
        Preprocess
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
import LogPreview from "@/components/LogPreview.vue";

export default {
  name: "LogList",
  components: {
    LogPreview
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
    ...mapActions(["fetchLogs", "fetchLogParser"]),
    runFetchLogParser() {
      if (!this.selected) {
        alert("Please select a file first.");
      } else {
        this.fetchLogParser({
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
