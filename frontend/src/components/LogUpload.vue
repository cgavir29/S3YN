<template>
  <div class="container has-text-centered">
    <b-dropdown v-model="selectedSystem" aria-role="list">
      <button class="button is-primary" type="button" slot="trigger">
        <div v-if="selectedSystem === null">
          <span>Select System Type</span>
        </div>
        <div v-else>
          <span>{{ selectedSystem }}</span>
        </div>
      </button>
      <div v-for="(system, index) in this.getSystems" :key="index">
        <b-dropdown-item :value="system.name" aria-role="listitem">
          <span>{{ system.name }}</span>
        </b-dropdown-item>
      </div>
    </b-dropdown>
    <br />
    <br />
    <div class="large-12 medium-12 small-12 cell">
      <input
        type="file"
        id="file"
        ref="file"
        v-on:change="handleFileUpload()"
      />
    </div>
    <br />
    <b-button class="is-warning" @click="runUploadFile">Upload</b-button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "LogUpload",
  data() {
    return {
      selectedSystem: null,
      file: ""
    };
  },
  computed: {
    ...mapGetters(["getUser", "getSystems"])
  },
  methods: {
    ...mapActions(["uploadFile"]),
    runUploadFile() {
      if (!this.selectedSystem) {
        alert("Please select the system type of your file");
        return;
      }

      if (this.file == "") {
        alert("Please upload a file");
        return;
      }

      let formData = new FormData();
      formData.append("file", this.file);

      this.uploadFile({
        userId: this.getUser._id.$oid,
        systemName: this.selectedSystem,
        formData: formData
      });
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    deleteFile(index) {
      this.files.splice(index, 1);
    }
  }
};
</script>
