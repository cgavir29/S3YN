<template>
  <div class="container has-text-centered">
    <div class="large-12 medium-12 small-12 cell">
      <label
        >File
        <input
          type="file"
          id="file"
          ref="file"
          v-on:change="handleFileUpload()"
        />
      </label>
      <b-button class="is-warning" @click="runUploadFile">Upload</b-button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "LogUpload",
  data() {
    return {
      files: [],
      file: ""
    };
  },
  computed: {
    ...mapGetters(["getUser"])
  },
  methods: {
    ...mapActions(["uploadFile"]),
    runUploadFile() {
      if (this.file == "") {
        alert("Please upload a file first.");
        return;
      }

      let formData = new FormData();
      formData.append("file", this.file);

      this.uploadFile({ userId: this.getUser._id.$oid, formData: formData });
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
