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
        {{file.name}}
        <button class="delete is-small" type="button" @click="deleteDropFile(index)"></button>
      </span>
    </div>

    <b-button type="is-warning" @click="evaluatePatterns()">Evaluate Patterns</b-button> |
    <b-button type="is-twitter">Save Results</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dropFiles: []
    }
  },
  methods: {
    evaluatePatterns() {
      if (this.dropFiles.length) {
        console.log('leyendo')
        const reader = new FileReader()
        const a = new Promise((resolve, reject) => {
          reader.onload = event => resolve(event.target.result)
          reader.onerror = error => reject(error)
          reader.readAsText(this.dropFiles[0])
        })

        a.then(res => {
          this.$buefy.dialog.alert({
            title: 'Uploaded Log',
            message: res,
            type: 'is-info',
            confirmText: 'Ok'
          })
        })
      } else {
        this.$buefy.dialog.alert({
          title: 'Error',
          message: 'Please upload a file first.',
          type: 'is-danger',
          hasIcon: true,
          icon: 'times-circle',
          iconPack: 'fa',
          ariaRole: 'alertdialog',
          ariaModal: true
        })
      }
    },
    deleteDropFile(index) {
      this.dropFiles.splice(index, 1)
    }
  }
}
</script>
