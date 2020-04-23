<template>
  <div class="container has-text-centered">
    <b-field>
      <b-upload v-model="dropFiles" multiple drag-drop>
        <section class="section">
          <div class="content has-text-centered">
            <p>
              <b-icon icon="upload" size="is-large"></b-icon>
            </p>
            <p>Drop your files here or click to upload</p>
          </div>
        </section>
      </b-upload>
    </b-field>

    <div class="tags has-text-centered">
      <span v-for="(file, index) in dropFiles" :key="index" class="tag is-info">
        {{ file.name }}
        <button
          class="delete is-small"
          type="button"
          @click="deleteFile(index)"
        ></button>
      </span>
    </div>

    <!-- <b-button type="is-warning" @click="evaluatePatterns()"
      >Evaluate Patterns</b-button
    >| -->
    <b-button type="is-warning">Upload</b-button>
  </div>
</template>

<script>
export default {
  name: "LogUpload",
  data() {
    return {
      dropFiles: []
    };
  },
  methods: {
    deleteFile(index) {
      this.dropFiles.splice(index, 1);
    }
  }
};
</script>
